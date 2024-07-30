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
    Vendas_SLM_2024,
    Base_de_Conhecimento,
)
from .utils import (
    get_chat_response,
    generate_excel_report,
    classify_question_chat_central,
    calcular_nps,
    config_chat_central,
    obter_distribuicao_nps,
    resumo_por_pergunta,
    config_chat_rh,
    classify_question,
    config_simple_chat,
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
                    questao=row["questao"],
                    nota=row["nota"],
                    defaults={
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


################################################# IMPORTAR VENDAS 2024######################################################


def import_vendas_slm_2024(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if not file or not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_vendas_slm_2024")

        try:
            df = pd.read_excel(file)
        except Exception as e:
            messages.error(request, f"Erro ao ler o arquivo Excel: {e}")
            return redirect("import_vendas_slm_2024")

        for _, row in df.iterrows():
            try:
                escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                Vendas_SLM_2024.objects.update_or_create(
                    escola=escola,
                    numero_do_pedido=row["numero_do_pedido"],
                    nome_pais=row["nome_pais"],
                    nome_do_aluno=row["nome_do_aluno"],
                    defaults={
                        "data_do_pedido": row["data_do_pedido"],
                        "quantidade": row["quantidade"],
                    },
                )
            except CRM_FUI.DoesNotExist:
                messages.error(
                    request, f"Escola com id_escola {row['id_escola']} não encontrada."
                )
                continue
            except Exception as e:
                messages.error(
                    request,
                    f"Erro ao importar a linha com id_escola {row['id_escola']}: {e}",
                )
                continue

        messages.success(request, "Dados importados com sucesso!")
        return redirect("import_vendas_slm_2024")
    return render(request, "chatapp/import/import_vendas_slm_2024.html")


############################################# CHAT SAF###########################################################


def generate_excel_report(vendas):
    df = pd.DataFrame(list(vendas.values()))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="vendas_slm_2024.xlsx"'
    df.to_excel(response, index=False)
    return response


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

        question_type = classify_question_chat_central(message)

        if question_type == "nps":
            nps_responses = (
                Respostas_NPS.objects.filter(escola__id_escola=school_id)
                .exclude(comentario__isnull=True)
                .exclude(comentario__exact="")
                .exclude(comentario__exact="nan")
            )
            context = ""
            for response in nps_responses:
                context += (
                    f"Nome do respondente: {response.nome}\n"
                    f"Questão perguntada no NPS: {response.questao}\n"
                    f"Nota: {response.nota} - "
                    f"As notas variam de 1 a 5, exceto para a pergunta de recomendação, que varia de 0 a 10.\n"
                    f"Comentário: {response.comentario}\n\n"
                )
        elif question_type in ["vendas", "relatório de vendas"]:
            vendas_responses = Vendas_SLM_2024.objects.filter(
                escola__id_escola=school_id
            )
            total_vendas = vendas_responses.count()
            context = f"O total de vendas da escola foi {total_vendas}. Para outras informações, você pode ver o relatório completo em Excel clicando [aqui](/download_excel_report/?school_id={school_id})."
        else:
            # Adicionar lógica para base de conhecimento
            knowledge_base_entries = Base_de_Conhecimento.objects.filter(
                assunto__icontains=message
            )
            if knowledge_base_entries.exists():
                context = ""
                for entry in knowledge_base_entries:
                    context += (
                        f"Título: {entry.titulo}\n"
                        f"Assunto: {entry.assunto}\n"
                        f"Sub Assunto: {entry.sub_assunto}\n"
                        f"Texto: {entry.texto}\n\n"
                    )
            else:
                context = (
                    f"Nome da Escola: {school.nome_da_escola}\n"
                    f"CNPJ: {school.CNPJ}\n"
                    f"Status: {school.status_da_escola}\n"
                    f"SLMs Vendidos: {school.slms_vendidos} - SLM ou SLMs no plural são os materiais vendidos.\n"
                    f"Meta: {school.meta} - Esse campo é a meta de Vendas de SLM vendidos.\n"
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
        schools = CRM_FUI.objects.all().order_by(
            "nome_da_escola"
        )  # Ordenar alfabeticamente
        return render(request, "chatapp/filtered_chat.html", {"schools": schools})


def download_excel_report_slm_2024(request):
    school_id = request.GET.get("school_id")
    vendas_responses = Vendas_SLM_2024.objects.filter(escola__id_escola=school_id)
    df = pd.DataFrame(list(vendas_responses.values()))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = (
        f'attachment; filename="vendas_slm_2024_{school_id}.xlsx"'
    )
    df.to_excel(response, index=False)
    return response


############################################# CHAT CENTRAL###########################################################


def simple_chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        if not message:
            return JsonResponse({"error": "Message not provided"}, status=400)

        context = ""
        schools = CRM_FUI.objects.all()
        for school in schools:
            context += (
                f"Nome da Escola: {school.nome_da_escola}\n"
                f"CNPJ: {school.CNPJ}\n"
                f"Status: {school.status_da_escola} - Esse é o status da escola se ela está operando normalmente ou se está em fase de implantação.\n"
                f"SLMs Vendidos: {school.slms_vendidos} - SLM ou SLMs no plural são os materiais vendidos.\n"
                f"Meta: {school.meta} - Esse campo é a meta de Vendas de SLM vendidos.\n"
                f"Cluster: {school.cluster}\n"
                f"Endereço da escola: {school.endereco}\n"
                f"CEP da escola: {school.cep_escola}\n"
                f"Bairro da escola: {school.bairro_escola}\n"
                f"Cidade da escola: {school.cidade_da_escola}\n"
                f"Estado da escola: {school.estado_da_escola}\n"
                f"Região da escola: {school.regiao_da_escola}\n"
                f"Telefone  da escola: {school.telefone_de_contato_da_escola}\n"
                f"Email da escola: {school.email_da_escola}\n"
                f"Segmento da escola: {school.segmento_da_escola}\n"
                f"Atual Série da escola: {school.atual_serie}\n"
                f"Avanço Segmento  da escola: {school.avanco_segmento}\n"
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
                f"Consultor Gestão Escolar: {school.consultor_gestao_escolar}\n\n"
            )

        response = config_simple_chat(message, context)

        return JsonResponse({"response": response})
    else:
        schools = CRM_FUI.objects.all().order_by(
            "nome_da_escola"
        )  # Ordenar alfabeticamente
        return render(request, "chatapp/simple_chat.html", {"schools": schools})
