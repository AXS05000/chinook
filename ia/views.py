import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import (
    Informacao,
    Beneficio,
    FolhaPonto,
    Salario,
    Ferias,
    CRM_FUI,
    Respostas_NPS,
)
from .utils import (
    get_chat_response,
    generate_excel_report,
    calcular_nps,
    config_chat_central,
    obter_distribuicao_nps,
    resumo_por_pergunta,
    config_chat_rh,
    classify_question,
)
import openpyxl
import pandas as pd
from openpyxl.utils import get_column_letter
from django.views import View


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").lower()
            context = ""

            # Escalas de avaliação
            escalas = {
                "Metodologia de ensino": "1 - Péssimo, 2 - Ruim, 3 - Mediano, 4 - Bom, 5 - Excelente",
                "Infraestrutura": "1 - Péssimo, 2 - Ruim, 3 - Mediano, 4 - Bom, 5 - Excelente",
                "Atendimento pedagógico": "1 - Péssimo, 2 - Ruim, 3 - Mediano, 4 - Bom, 5 - Excelente",
                "Atendimento administrativo/financeiro": "1 - Péssimo, 2 - Ruim, 3 - Mediano, 4 - Bom, 5 - Excelente",
                "Em uma escala de 0 a 10, o quanto você recomendaria a escola para um amigo ou familiar?": "0 - Horrível a 10 - Perfeito",
            }

            # Consultar o banco de dados para obter informações relevantes
            informacoes = Informacao.objects.all()
            total_respostas = informacoes.count()
            if total_respostas > 0:
                soma_respostas = sum(info.resposta for info in informacoes)
                media_respostas = soma_respostas / total_respostas
                context_list = []
                for info in informacoes:
                    escala = escalas.get(info.questao, "")
                    context_list.append(
                        f"Nome: {info.nome}, Persona: {info.persona}, Data da Resposta: {info.data_resposta}, Unidade: {info.unidade}, Questão: {info.questao} (Escala: {escala}), Resposta: {info.resposta}, Comentário: {info.comentario}"
                    )
                context = "\n".join(context_list)
                context += (
                    f"\n\nA média das respostas para a escola é: {media_respostas:.2f}"
                )
            else:
                context = "No relevant information found in the database."

            # Checar se a pergunta é sobre a distribuição de NPS
            if "quantos" in user_message and (
                "promotores" in user_message
                or "detratores" in user_message
                or "neutros" in user_message
            ):
                promotores, neutros, detratores = obter_distribuicao_nps(informacoes)
                response = f"No NPS, houve {promotores} promotores, {neutros} neutros e {detratores} detratores."
            # Checar se a pergunta é sobre o valor do NPS
            elif any(
                term in user_message
                for term in ["nps", "promotores", "detratores", "passivas", "neutras"]
            ):
                nps_score = calcular_nps(informacoes)
                response = f"O Net Promoter Score (NPS) da escola é: {nps_score:.2f}"
            else:
                # Obter resposta do ChatGPT
                response = get_chat_response(user_message, context)

            return JsonResponse({"response": response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return render(request, "chatapp/chat.html")


####################################################################################################################


@csrf_exempt
def hr_assistant_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").lower()
            context = ""

            # Classificar a pergunta do usuário
            tipo_informacao = classify_question(user_message)

            # Definir os modelos a serem verificados
            modelos = {
                "benefício": Beneficio,
                "folha de ponto": FolhaPonto,
                "salário": Salario,
                "férias": Ferias,
            }

            # Buscar a informação correta baseada no tipo de informação identificado
            if tipo_informacao in modelos:
                modelo = modelos[tipo_informacao]
                informacoes = modelo.objects.all()
                if informacoes.exists():
                    context = informacoes.first().descricao
                    response = config_chat_rh(user_message, context)
                else:
                    context = f"No relevant information found for {tipo_informacao} in the database."
                    response = config_chat_rh(user_message, context)
            else:
                context = f"No relevant information found for {tipo_informacao} in the database."
                response = config_chat_rh(user_message, context)

            # Se a resposta não for satisfatória ou não houver informações, buscar em todas as categorias
            if "No relevant information found" in context or not context:
                context_list = []
                for key, model in modelos.items():
                    informacoes = model.objects.all()
                    if informacoes.exists():
                        context_list.append(informacoes.first().descricao)
                if context_list:
                    context = "\n".join(context_list)
                    response = config_chat_rh(user_message, context)

            return JsonResponse({"response": response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return render(request, "chatapp/hr_chat.html")


############################################# CHAT CENTRAL###########################################################


def filtered_chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        school_id = data.get("school_id")
        message = data.get("message")

        if not school_id:
            return JsonResponse({"error": "School ID not provided"}, status=400)

        try:
            school = CRM_FUI.objects.get(id_escola=school_id)
        except CRM_FUI.DoesNotExist:
            return JsonResponse({"error": "School not found"}, status=404)

        context = (
            f"Nome da Escola: {school.nome_da_escola}\n"
            f"CNPJ: {school.CNPJ}\n"
            f"Status: {school.status_da_escola}\n"
            f"SLMs Vendidos: {school.slms_vendidos}\n"
            f"Meta: {school.meta}\n"
            f"Cluster: {school.cluster}\n"
            f"Endereço: {school.endereco}\n"
            f"CEP: {school.cep_escola}\n"
            f"Bairro: {school.bairro_escola}\n"
            f"Cidade: {school.cidade_da_escola}\n"
            f"Estado: {school.estado_da_escola}\n"
            f"Região: {school.regiao_da_escola}\n"
            f"Telefone: {school.telefone_de_contato_da_escola}\n"
            f"Email: {school.email_da_escola}\n"
            f"Segmento: {school.segmento_da_escola}\n"
            f"Atual Série: {school.atual_serie}\n"
            f"Avanço Segmento: {school.avanco_segmento}\n"
            f"NPS Pais 2024 - 1° Onda: {school.nps_pais_2024_1_onda} - "
            f"Este campo indica a pontuação referente ao NPS(Net Promoter Score) dos pais dos alunos que estudam na escola, que foi realizado no 1° semestre no ano(1° Onda).\n"
            f"Cliente Oculto 2024: {school.cliente_oculto_2024} - "
            f"Este campo indica a pontuação referente ao Cliente Oculto, que uma avaliação realizada por uma empresa terceirizada onde consiste em um falso cliente ir até a escola para avaliar ela.\n"
            f"Quality Assurance 2024: {school.quality_assurance_2024} - "
            f"Este campo indica a pontuação referente Quality Assurance uma avaliação realizada para ver a qualidade da escola.\n"
            f"Status de Adimplência/Inadimplência: {school.status_de_adimplencia} - "
            f"Este campo indica se a escola está Adimplente ou Inadimplente referente aos seus pagamentos que devem ser feitos à franqueada Maple Bear.\n"
            f"Ticket Médio: {school.ticket_medio} - Este é o valor médio de mensalidade cobrada pela escola.\n"
        )

        if school.status_de_adimplencia == "Inadimplente":
            context += f"Inadimplência: {school.inadimplencia} - Este é o valor que a escola está devendo para a Maple Bear.\n"

        context += (
            f"Consultor Comercial: {school.consultor_comercial}\n"
            f"Consultor Gestão Escolar: {school.consultor_gestao_escolar}\n"
        )

        response = config_chat_central(message, context)

        return JsonResponse({"response": response})
    else:
        schools = CRM_FUI.objects.all()
        return render(request, "chatapp/filtered_chat.html", {"schools": schools})


################################################# IMPORTAR FUI######################################################


def import_crm_fui(request):
    if request.method == "POST":
        file = request.FILES["file"]
        if not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_crm_fui")

        df = pd.read_excel(file)
        for _, row in df.iterrows():
            CRM_FUI.objects.update_or_create(
                id_escola=row["id_escola"],
                defaults={
                    "nome_da_escola": row["nome_da_escola"],
                    "CNPJ": row["CNPJ"],
                    "status_da_escola": row["status_da_escola"],
                    "slms_vendidos": row["slms_vendidos"],
                    "alunos": row["alunos"],
                    "meta": row["meta"],
                    "cluster": row["cluster"],
                    "endereco": row["endereco"],
                    "cep_escola": row["cep_escola"],
                    "bairro_escola": row["bairro_escola"],
                    "cidade_da_escola": row["cidade_da_escola"],
                    "estado_da_escola": row["estado_da_escola"],
                    "regiao_da_escola": row["regiao_da_escola"],
                    "telefone_de_contato_da_escola": row[
                        "telefone_de_contato_da_escola"
                    ],
                    "email_da_escola": row["email_da_escola"],
                    "segmento_da_escola": row["segmento_da_escola"],
                    "atual_serie": row["atual_serie"],
                    "avanco_segmento": row["avanco_segmento"],
                    "status_de_adimplencia": row["status_de_adimplencia"],
                    "ticket_medio": row["ticket_medio"],
                    "inadimplencia": row["inadimplencia"],
                    "nps_pais_2024_1_onda": row["nps_pais_2024_1_onda"],
                    "cliente_oculto_2024": row["cliente_oculto_2024"],
                    "quality_assurance_2024": row["quality_assurance_2024"],
                    "consultor_comercial": row["consultor_comercial"],
                    "consultor_gestao_escolar": row["consultor_gestao_escolar"],
                },
            )
        messages.success(request, "Dados importados com sucesso!")
        return redirect("import_crm_fui")
    return render(request, "chatapp/import/import_crm_fui.html")


################################################# IMPORTAR RESPOSTA######################################################


def import_resposta(request):
    if request.method == "POST":
        file = request.FILES["file"]
        if not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_respostas_nps")

        df = pd.read_excel(file)
        for _, row in df.iterrows():
            try:
                escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                Respostas_NPS.objects.update_or_create(
                    escola=escola,
                    nome=row["nome"],
                    data_da_resposta=row["data_da_resposta"],
                    defaults={
                        "questao": row["questao"],
                        "nota": row["nota"],
                        "comentario": row["comentario"],
                    },
                )
            except CRM_FUI.DoesNotExist:
                messages.error(
                    request, f"Escola com id_escola {row['id_escola']} não encontrada."
                )
                continue
        messages.success(request, "Dados importados com sucesso!")
        return redirect("import_respostas_nps")
    return render(request, "chatapp/import/import_resposta.html")
