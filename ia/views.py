import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import (
    Informacao,
    Beneficio,
    FolhaPonto,
    Salario,
    Ferias,
    CRM_FUI,
    Respostas_NPS,
    Vendas_SLM_2024,
    Vendas_SLM_2025,
    Base_de_Conhecimento,
)
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
from .utils import (
    get_chat_response,
    calcular_nps,
    obter_distribuicao_nps,
    config_chat_rh,
    classify_question,
    config_simple_chat,
    config_chat_central,
    classify_question_chat_central,
)
import openpyxl
from openpyxl.utils import get_column_letter
from django.conf import settings
from django.views import View


class ExcelImportView(View):
    def get(self, request):
        # Retorna o template de upload de arquivo
        return render(request, "chatapp/importar_nps.html")

    def post(self, request):
        excel_file = request.FILES["excel_file"]

        # Carrega o arquivo Excel na memória
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        # Itera sobre as linhas do arquivo Excel
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Ignora o cabeçalho
            nome = row[0]
            persona = row[1]
            data_resposta = row[2]
            unidade = row[3]
            questao = row[4]
            resposta = row[5]
            comentario = row[6]

            if (
                nome
                and persona
                and data_resposta
                and unidade
                and questao
                and resposta is not None
            ):
                # Cria um novo objeto Informacao
                Informacao.objects.create(
                    nome=nome,
                    persona=persona,
                    data_resposta=data_resposta,
                    unidade=unidade,
                    questao=questao,
                    resposta=resposta,
                    comentario=comentario,
                )

        return HttpResponse("Importação realizada com sucesso!")


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
@login_required(login_url='/login/')
def hr_assistant_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").lower()
            user = request.user

            if not user.api_key:
                return JsonResponse({"error": "Usuário não possui chave API válida"}, status=403)

            api_key = user.api_key
            context = ""

            # Classificar a pergunta do usuário
            tipo_informacao = classify_question(user_message, api_key)

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
                    response = config_chat_rh(user_message, api_key, context)
                else:
                    context = f"No relevant information found for {tipo_informacao} in the database."
                    response = config_chat_rh(user_message, api_key, context)
            else:
                context = f"No relevant information found for {tipo_informacao} in the database."
                response = config_chat_rh(user_message, api_key, context)

            # Se a resposta não for satisfatória ou não houver informações, buscar em todas as categorias
            if "No relevant information found" in context or not context:
                context_list = []
                for key, model in modelos.items():
                    informacoes = model.objects.all()
                    if informacoes.exists():
                        context_list.append(informacoes.first().descricao)
                if context_list:
                    context = "\n".join(context_list)
                    response = config_chat_rh(user_message, api_key, context)

            return JsonResponse({"response": response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return render(request, "chatapp/hr_chat.html")

################################################# IMPORTAR FUI######################################################

@login_required(login_url='/login/')
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
                    "slms_vendidos_25": row["slms_vendidos_25"],
                    "meta": row["meta"],
                    "cluster": row["cluster"],
                    "cep_escola": row["cep_escola"],
                    "endereco": row["endereco"],
                    "complemento_escola": row["complemento_escola"],
                    "bairro_escola": row["bairro_escola"],
                    "cidade_da_escola": row["cidade_da_escola"],
                    "estado_da_escola": row["estado_da_escola"],
                    "regiao_da_escola": row["regiao_da_escola"],
                    "status_de_adimplencia": row["status_de_adimplencia"],
                    "inadimplencia": row["inadimplencia"],
                    "ticket_medio": row["ticket_medio"],
                    "valor_royalties": row["valor_royalties"],
                    "valor_fdmp": row["valor_fdmp"],
                    "segmento_da_escola": row["segmento_da_escola"],
                    "atual_serie": row["atual_serie"],
                    "avanco_segmento": row["avanco_segmento"],
                    "telefone_de_contato_da_escola": row[
                        "telefone_de_contato_da_escola"
                    ],
                    "email_da_escola": row["email_da_escola"],
                    "nps_pais_2024_1_onda": row["nps_pais_2024_1_onda"],
                    "quality_assurance_2024": row["quality_assurance_2024"],
                    "cliente_oculto_2024": row["cliente_oculto_2024"],
                    "consultor_saf": row["consultor_saf"],
                    "consultor_academico": row["consultor_academico"],
                    "consultor_comercial": row["consultor_comercial"],
                    "consultor_gestao_escolar": row["consultor_gestao_escolar"],
                    "dias_uteis_entrega_slm": row["dias_uteis_entrega_slm"],
                },
            )
        messages.success(request, "Dados importados com sucesso!")
        return redirect("import_crm_fui")
    return render(request, "chatapp/import/import_crm_fui.html")


################################################# IMPORTAR RESPOSTA######################################################


@login_required(login_url='/login/')
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
                Respostas_NPS.objects.create(
                    escola=escola,
                    nome=row["nome"],
                    data_da_resposta=row["data_da_resposta"],
                    questao=row["questao"],
                    nota=row["nota"],
                    comentario=row["comentario"]
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

@login_required(login_url='/login/')
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

        with transaction.atomic():
            Vendas_SLM_2024.objects.all().delete()  # Limpar a tabela antes de importar novos dados

            for _, row in df.iterrows():
                try:
                    escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                    Vendas_SLM_2024.objects.create(
                        escola=escola,
                        numero_do_pedido=row["numero_do_pedido"],
                        nome_pais=row["nome_pais"],
                        nome_do_aluno=row["nome_do_aluno"],
                        data_do_pedido=row["data_do_pedido"],
                        quantidade=row["quantidade"],
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


################################################# IMPORTAR VENDAS 2025######################################################


@login_required(login_url='/login/')
def import_vendas_slm_2025(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if not file or not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_vendas_slm_2025")

        try:
            df = pd.read_excel(file)
        except Exception as e:
            messages.error(request, f"Erro ao ler o arquivo Excel: {e}")
            return redirect("import_vendas_slm_2025")

        with transaction.atomic():
            Vendas_SLM_2025.objects.all().delete()  # Limpar a tabela antes de importar novos dados

            for _, row in df.iterrows():
                try:
                    escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                    Vendas_SLM_2025.objects.create(
                        escola=escola,
                        numero_do_pedido=row["numero_do_pedido"],
                        nome_pais=row["nome_pais"],
                        nome_do_aluno=row["nome_do_aluno"],
                        data_do_pedido=row["data_do_pedido"],
                        quantidade=row["quantidade"],
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
        return redirect("import_vendas_slm_2025")
    return render(request, "chatapp/import/import_vendas_slm_2025.html")

############################################# CHAT SAF###########################################################


def generate_excel_report(vendas):
    df = pd.DataFrame(list(vendas.values()))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="vendas_slm_2024.xlsx"'
    df.to_excel(response, index=False)


    return response

@login_required(login_url='/login/')
def filtered_chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        school_id = data.get("school_id")
        message = data.get("message")

        user = request.user

        if not user.api_key:
            return JsonResponse({"error": "Usuário não possui chave API válida"}, status=403)

        api_key = user.api_key

        print("Recebido POST request")
        print(f"ID da escola: {school_id}")
        print(f"Mensagem: {message}")

        if not school_id:
            print("Erro: ID da escola não fornecido")
            return JsonResponse({"error": "School ID not provided"}, status=400)

        try:
            school = CRM_FUI.objects.get(id_escola=school_id)
            print(f"Escola encontrada: {school.nome_da_escola}")
        except CRM_FUI.DoesNotExist:
            print("Erro: Escola não encontrada")
            return JsonResponse({"error": "School not found"}, status=404)

        question_type = classify_question_chat_central(message, api_key)
        print(f"Tipo de pergunta: {question_type}")

        if question_type == "nps":
            print("Lidando com categoria NPS")
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
            print("Contexto NPS gerado")
        elif question_type == "base de conhecimento":
            print("Lidando com categoria conhecimento")
            knowledge_base_entries = Base_de_Conhecimento.objects.all()
            if knowledge_base_entries.exists():
                context = ""
                for entry in knowledge_base_entries:
                    context += f"Sub Assunto: {entry.sub_assunto}\nTexto: {entry.texto}\n\n"
                print("Contexto de conhecimento gerado")
            else:
                context = "Nenhuma informação relevante encontrada na base de conhecimento."
                print("Nenhuma entrada relevante encontrada na base de conhecimento")
        
        elif question_type in ["vendas", "relatório de vendas"]:
            vendas_responses_2024 = Vendas_SLM_2024.objects.filter(
                escola__id_escola=school_id
            )
            total_quantidade_2024 = vendas_responses_2024.aggregate(total=Sum('quantidade'))['total']

            vendas_responses_2025 = Vendas_SLM_2025.objects.filter(
                escola__id_escola=school_id
            )
            total_quantidade_2025 = vendas_responses_2025.aggregate(total=Sum('quantidade'))['total']

            context = (
                f"O total de vendas da escola no ciclo de 2024 foi {total_quantidade_2024} e no ciclo de 2025 foi {total_quantidade_2025}. "
                f"Para outras informações, você pode ver o relatório completo em Excel das vendas do ciclo de 2024 clicando "
                f"[aqui](/download_excel_report/?school_id={school_id}) e para as vendas do ciclo de 2025 clicando "
                f"[aqui](/download_excel_report_25/?school_id={school_id})."
            )
            print("Contexto de relatório de vendas gerado")
            
        else:
                context = (
                    f"Informações Básicas da Escola:\n"
                    f"Nome da Escola: {school.nome_da_escola}\n"
                    f"CNPJ: {school.CNPJ}\n"
                    f"Status: {school.status_da_escola}\n"
                    f"Cluster: {school.cluster}\n"
                    f"CEP: {school.cep_escola}\n"
                    f"Endereço: {school.endereco}\n"
                    f"Complemento: {school.complemento_escola}\n"
                    f"Bairro: {school.bairro_escola}\n"
                    f"Cidade: {school.cidade_da_escola}\n"
                    f"Estado: {school.estado_da_escola}\n"
                    f"Região: {school.regiao_da_escola}\n"
                    f"Telefone: {school.telefone_de_contato_da_escola}\n"
                    f"Email: {school.email_da_escola}\n"
                    f"Segmento: {school.segmento_da_escola}\n"
                    f"Atual Série: {school.atual_serie}\n"
                    f"Avanço Segmento: {school.avanco_segmento}\n"
                    
                    f"Vendas e Metas de SLM:\n"
                    f"SLMs Vendidos 2024: {school.slms_vendidos} - SLM ou SLMs no plural são os materiais vendidos, esses aqui são referente a 2024.\n"
                    f"SLMs Vendidos 2025: {school.slms_vendidos_25} - SLM ou SLMs no plural são os materiais vendidos, esses aqui são referente a 2025.\n"
                    f"Meta de SLMs 2024: {school.meta} - Esse campo é a meta de Vendas de SLM vendidos.\n"
                    f"Meta de SLMs 2025: Ainda não foi definido a meta por escola.\n"
                    f"Dias Úteis para Entrega do SLM nessa escola: {school.dias_uteis_entrega_slm}\n"
                    
                    f"Avaliações:\n"
                    f"NPS Pais 2024 - 1° Onda: {school.nps_pais_2024_1_onda} - "
                    f"Este campo indica a pontuação referente ao NPS(Net Promoter Score) dos pais dos alunos que estudam na escola, que foi realizado no 1° semestre no ano(1° Onda).\n"
                    f"Cliente Oculto 2024: {school.cliente_oculto_2024} - "
                    f"Este campo indica a pontuação referente ao Cliente Oculto, que uma avaliação realizada por uma empresa terceirizada onde consiste em um falso cliente ir até a escola para avaliar ela.\n"
                    f"Quality Assurance 2024: {school.quality_assurance_2024} - "
                    f"Este campo indica a pontuação referente Quality Assurance uma avaliação realizada para ver a qualidade da escola.\n"
                    
                    f"Financeiro:\n"
                    f"Ticket Médio: {school.ticket_medio} - Este é o valor médio de mensalidade cobrada pela escola.\n"
                    f"Valor Royalties: {school.valor_royalties} - Este é o valor de royalties que a escola deve pagar por mês à franqueada Maple Bear.\n"
                    f"Valor de FDMP(Fundo de Marketing): {school.valor_fdmp} - Este é o valor de FDMP(Fundo de Marketing) que a escola deve pagar por mês à franqueada Maple Bear.\n"
                    f"Status de Adimplência/Inadimplência: {school.status_de_adimplencia} - "
                    f"Este campo indica se a escola está Adimplente ou Inadimplente referente aos seus pagamentos(Royalties e FDMP) que devem ser feitos à franqueada Maple Bear.\n"
                    )

                if school.status_de_adimplencia == "Inadimplente":
                    context += f"Inadimplência: {school.inadimplencia} - Este é o valor que a escola está devendo para a Maple Bear.\n"

                context += (
                    f"Consultores:\n"
                    f"Consultor Comercial: {school.consultor_comercial}\n"
                    f"Consultor Gestão Escolar: {school.consultor_gestao_escolar}\n"
                    f"Consultor Acadêmico: {school.consultor_academico}\n"
                    f"Consultor SAF(Serviço de Atendimento ao Franqueado): {school.consultor_saf}\n"
                )

        response = config_chat_central(message, api_key, context)

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



def download_excel_report_slm_2025(request):
    school_id = request.GET.get("school_id")
    vendas_responses = Vendas_SLM_2025.objects.filter(escola__id_escola=school_id)
    df = pd.DataFrame(list(vendas_responses.values()))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = (
        f'attachment; filename="vendas_slm_2025_{school_id}.xlsx"'
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
