import json
import random
import markdown
import time
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .forms import PlanificadorForm
from datetime import datetime
from datetime import timedelta
from django.db.models import Count
from django.db.models import Q
from .models import (
    Informacao,
    Beneficio,
    Ticket_Sprinklr,
    FolhaPonto,
    Resumo_Respostas_NPS,
    Salario,
    Ferias,
    CRM_FUI,
    Respostas_NPS,
    Vendas_SLM_2024,
    Vendas_SLM_2025,
    Base_de_Conhecimento,
    Planificador_2024,
    Avaliacao_Cliente_Oculto_24,
    Resumo_Respostas_ClienteOculto24,
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
    config_resumo_cliente_oculto,
    config_resumo_nps,
    config_chat_central,
    classify_question_chat_central,
)
import openpyxl
from openpyxl.utils import get_column_letter
from django.views import View
from django.views.generic import ListView


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
                        id_linha=row["id_linha"],
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
                        id_linha=row["id_linha"],
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

################################################# IMPORTAR CLIENTE OCULTO 2024######################################################


@login_required(login_url='/login/')
def import_cliente_oculto_2024(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if not file or not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_cliente_oculto_2024")

        try:
            df = pd.read_excel(file)
        except Exception as e:
            messages.error(request, f"Erro ao ler o arquivo Excel: {e}")
            return redirect("import_cliente_oculto_2024")

        with transaction.atomic():
            Avaliacao_Cliente_Oculto_24.objects.all().delete()  # Limpar a tabela antes de importar novos dados

            for _, row in df.iterrows():
                try:
                    escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                    Avaliacao_Cliente_Oculto_24.objects.create(
                        escola=escola,
                        categoria=row["categoria"],
                        pergunta=row["pergunta"],
                        resposta=row["resposta"],
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
        return redirect("import_cliente_oculto_2024")
    return render(request, "chatapp/import/import_cliente_oculto_2024.html")




################################################# IMPORTAR TICKET SPRINKLR######################################################
@login_required(login_url='/login/')
def import_ticket_sprinklr(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if not file or not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_ticket_sprinklr")

        try:
            df = pd.read_excel(file)
        except Exception as e:
            messages.error(request, f"Erro ao ler o arquivo Excel: {e}")
            return redirect("import_ticket_sprinklr")

        with transaction.atomic():
            Ticket_Sprinklr.objects.all().delete()  # Limpar a tabela antes de importar novos dados

            for _, row in df.iterrows():
                try:
                    escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                    
                    # Ajuste para usar os nomes corretos das colunas
                    tempo_medio_de_resposta_total = row["tempo_medio_de_resposta"]
                    tempo_medio_de_primeira_resposta_do_agente_total = row["tempo_medio_de_primeira_resposta_do_agente"]

                    Ticket_Sprinklr.objects.create(
                        escola=escola,
                        id_ticket=row["id_ticket"],
                        cliente=row["cliente"],
                        area=row["area"],
                        assunto=row["assunto"],
                        tempo_medio_de_resposta_total=tempo_medio_de_resposta_total,
                        tempo_medio_de_primeira_resposta_do_agente_total=tempo_medio_de_primeira_resposta_do_agente_total,
                        data_ticket=row["data_ticket"],
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
        return redirect("import_ticket_sprinklr")
    return render(request, "chatapp/import/import_ticket_sprinklr.html")
############################################# CHAT SAF###########################################################


def generate_excel_report(vendas):
    df = pd.DataFrame(list(vendas.values()))
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="vendas_slm_2024.xlsx"'
    df.to_excel(response, index=False)


    return response


def escolher_frase_inicial(school):
    frases_iniciais = [
        "Olá, seja bem-vindo ao meu cantinho! Sou o Chinook, o ursinho guia da Maple Bear e vou te mostrar tudo sobre a escola {school.nome_da_escola}.",
        "Bem-vindo! Sou o Chinook, o urso que adora ajudar! Vamos dar uma espiadinha na escola {school.nome_da_escola} da Maple Bear?",
        "E aí! Eu sou o Chinook, o ursinho mais curioso da Maple Bear. Vamos explorar a escola {school.nome_da_escola} juntos?",
        "Oi, eu sou o Chinook, o ursinho que adora compartilhar. Vem comigo conhecer a escola {school.nome_da_escola} da Maple Bear!",
        "Bem-vindo ao meu mundo! Eu sou o Chinook, seu urso guia na Maple Bear e vou te apresentar a escola {school.nome_da_escola} com muito carinho.",
        "Oi, oi! Sou o Chinook, seu amigo de confiança na Maple Bear. Preparado para descobrir tudo sobre a escola {school.nome_da_escola}?",
        "Olá! Eu sou o Chinook, o urso que adora novas aventuras na Maple Bear e hoje vou te levar para conhecer a escola {school.nome_da_escola}.",
        "Oiii, eu sou o Chinook, seu companheiro de pelúcia da Maple Bear, estou animado para te mostrar a escola {school.nome_da_escola}!",
        "Bem-vindo! Eu sou o Chinook, o ursinho mais fofo da Maple Bear, estou aqui para te contar tudo sobre a escola {school.nome_da_escola}.",
        "Olá! Eu sou o Chinook, seu urso amigo na Maple Bear, estou aqui para te guiar pelo universo da escola {school.nome_da_escola}.",
        "Oi! Eu sou o Chinook, seu urso guia na Maple Bear e mal posso esperar para te mostrar tudo sobre a escola {school.nome_da_escola}!",
        "Bem-vindo! Eu sou o Chinook, o urso que adora aventuras e estou aqui para te guiar pela escola {school.nome_da_escola} da Maple Bear.",
        "Oi, oi! Eu sou o Chinook, o ursinho que está sempre por perto na Maple Bear. Vamos juntos conhecer a escola {school.nome_da_escola}?",
        "Oi! Eu sou o Chinook, o ursinho que adora conhecer novos lugares. Vem comigo explorar a escola {school.nome_da_escola}!",
        "Oi, oi! Sou o Chinook, seu amiguinho de aventuras na Maple Bear. Preparado para explorar a escola {school.nome_da_escola}?",
        "Oi! Eu sou o Chinook, seu urso de confiança na Maple Bear. Juntos, vamos conhecer a escola {school.nome_da_escola}!",
        "Oi! Eu sou o Chinook, seu companheiro de todas as horas na Maple Bear. Vamos conhecer juntos a escola {school.nome_da_escola}?",
        "Bem-vindo! Sou o Chinook, o ursinho que adora fazer novos amigos. Hoje, vou te guiar pela escola {school.nome_da_escola} da Maple Bear.",
        "Olá! Eu sou o Chinook, o ursinho sempre pronto para te ajudar. Vamos descobrir juntos tudo sobre a escola {school.nome_da_escola} da Maple Bear!",
        "Oi, oi! Eu sou o Chinook, o urso que adora fazer parte das suas aventuras. Vem comigo conhecer a escola {school.nome_da_escola}!",
        "Bem-vindo! Eu sou o Chinook, o ursinho que sempre tem uma novidade para compartilhar. Hoje, vou te mostrar a escola {school.nome_da_escola}.",
        "Olá! Eu sou o Chinook, seu ursinho guia na Maple Bear. Pronto para explorar a escola {school.nome_da_escola} comigo?",
        "Oi! Eu sou o Chinook, o ursinho que ama ajudar os amigos. Vem comigo descobrir a escola {school.nome_da_escola} da Maple Bear!",
        "Oi, oi! Eu sou o Chinook, o ursinho que adora novas descobertas. Vamos juntos conhecer a escola {school.nome_da_escola}?",
        "Olá! Eu sou o Chinook, o ursinho que adora guiar novas aventuras. Vamos conhecer a escola {school.nome_da_escola} da Maple Bear?",
        "Oi! Eu sou o Chinook, o ursinho sempre animado para novas aventuras. Vamos explorar a escola {school.nome_da_escola} juntos?",
        "Oi, oi! Eu sou o Chinook, seu amiguinho de todas as horas. Preparado para descobrir tudo sobre a escola {school.nome_da_escola} da Maple Bear?",
        "Bem-vindo! Eu sou o Chinook, o ursinho que adora estar por perto. Vem comigo conhecer a escola {school.nome_da_escola}!",
        "Oi, oi! Eu sou o Chinook, o ursinho que ama conhecer novos amigos. Vamos juntos explorar a escola {school.nome_da_escola}?",
        "Bem-vindo! Eu sou o Chinook, o urso que adora guiar aventuras. Hoje, vou te mostrar tudo sobre a escola {school.nome_da_escola}!",
        "Olá! Eu sou o Chinook, o ursinho que está sempre pronto para te ajudar. Vamos conhecer a escola {school.nome_da_escola}?",
        "Oi! Eu sou o Chinook, o urso que adora conhecer novos lugares. Hoje, vou te mostrar tudo sobre a escola {school.nome_da_escola}!",
        "Bem-vindo! Eu sou o Chinook, o ursinho que adora estar ao seu lado. Vamos juntos explorar a escola {school.nome_da_escola}!",

    ]

    return random.choice(frases_iniciais).format(school=school)


def escolher_frase_final(school):
    frases_finais = [
        "Espero ter ajudado! Se precisar de mais alguma coisa, é só me chamar!",
        "Estou sempre por aqui para te ajudar. Qualquer dúvida, conte comigo!",
        "Se precisar de mais informações, estou só a um enter de distância!",
        "Se precisar de mais alguma informação, estarei sempre aqui para te ajudar!",
        "Foi ótimo estar com você! Se precisar de mim, é só chamar.",
        "Se precisar de mais alguma coisa, estou aqui para te ajudar!",
        "Espero que tenha sido útil! Estou por aqui se precisar de mais informações.",
        "Conte comigo sempre que precisar! Estou aqui para ajudar.",
        "Se precisar de mais alguma coisa, estou sempre por aqui!",
        "Estou sempre à disposição! Se precisar, é só me chamar!",
    ]

    return random.choice(frases_finais).format(school=school)

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

        # Tenta obter a escola, independentemente do tipo de mensagem
        try:
            school = CRM_FUI.objects.get(id_escola=school_id)
            print(f"Escola encontrada: {school.nome_da_escola}")
        except CRM_FUI.DoesNotExist:
            print("Erro: Escola não encontrada")
            return JsonResponse({"error": "School not found"}, status=404)

        # Busca o resumo do NPS, se existir
        resumo_nps = Resumo_Respostas_NPS.objects.filter(escola=school).first()
        resumo_nps_text = resumo_nps.resumo if resumo_nps else None

        # Converte o texto markdown para HTML se existir
        if resumo_nps_text:
            resumo_nps_text = markdown.markdown(resumo_nps_text, extensions=['nl2br', 'extra'])

            # Substitui <strong> por <span style='font-weight: bold;'>
            resumo_nps_text = resumo_nps_text.replace("<strong>", "<span style='font-weight: bold;'>").replace("</strong>", "</span>")

        # Busca o resumo do NPS, se existir
        resumo_co24 = Resumo_Respostas_ClienteOculto24.objects.filter(escola=school).first()
        resumo_resumo_co24_text = resumo_co24.resumo if resumo_co24 else None

        # Converte o texto markdown para HTML se existir
        if resumo_resumo_co24_text:
            resumo_resumo_co24_text = markdown.markdown(resumo_resumo_co24_text, extensions=['nl2br', 'extra'])

            # Substitui <strong> por <span style='font-weight: bold;'>
            resumo_resumo_co24_text = resumo_resumo_co24_text.replace("<strong>", "<span style='font-weight: bold;'>").replace("</strong>", "</span>")




        if message == 'auto':
            complemento = ""
            if school.complemento_escola and school.complemento_escola.lower() not in ["", "null", "nan", "0", "-"]:
                complemento = f" {school.complemento_escola}"
            segmento_info = ""
            if school.segmento_da_escola and school.segmento_da_escola.lower() not in ["", "null", "nan", "em implantação"] \
                    and school.atual_serie and school.atual_serie.lower() not in ["", "null", "nan", "em implantação"]:
                segmento_info = (
                    f"<span style='font-weight: bold;'>Segmento:</span> {school.segmento_da_escola} - "
                    f"<span style='font-weight: bold;'>Atual Série:</span> {school.atual_serie} - "
                    f"<span style='font-weight: bold;'>Avanço de Segmento:</span> {school.avanco_segmento}.<br>"
                )

            inadimplencia_info = ""
            if school.status_de_adimplencia.lower() != "adimplente":
                inadimplencia_info = f" - <span style='font-weight: bold;'>Inadimplência:</span> R$ {school.inadimplencia}"

            # URLs de download
            url_slm_2024 = f"/download_excel_report/?school_id={school_id}"
            url_slm_2025 = f"/download_excel_report_25/?school_id={school_id}"

            download_icon = '<i class="ri-file-excel-line"  style="font-size: 18px"></i>'

            frase_inicial = escolher_frase_inicial(school)
            frase_final = escolher_frase_final(school)

            response = (
                f"{frase_inicial}<br><br>"
                
                f"<span style='font-weight: bold;'>Informações Básicas:</span><br>"
                f"<span style='font-weight: bold;'>Id da Escola:</span> {school.id_escola} - <span style='font-weight: bold;'>CNPJ:</span> {school.CNPJ} - <span style='font-weight: bold;'>Cluster:</span> {school.cluster} - <span style='font-weight: bold;'>Status:</span> {school.status_da_escola}.<br>"
                f"<span style='font-weight: bold;'>Endereço:</span> {school.endereco}{complemento}, {school.bairro_escola}, {school.cidade_da_escola}, {school.estado_da_escola}, CEP {school.cep_escola}, na região {school.regiao_da_escola} do Brasil."
                f" - <span style='font-weight: bold;'>Telefone:</span> {school.telefone_de_contato_da_escola} - <span style='font-weight: bold;'>Email:</span> {school.email_da_escola}.<br>"
                f"{segmento_info}"
                
                f"<br><span style='font-weight: bold;'>Vendas e Metas de SLM:</span><br>"
                f"<span style='font-weight: bold;'>SLMs Vendidos 2024:</span> {school.slms_vendidos} - "
                f"<a href='{url_slm_2024}'>{download_icon}</a> - "
                f"<span style='font-weight: bold;'>Meta de SLMs 2024:</span> {school.meta} - "
                f"<span style='font-weight: bold;'>SLMs Vendidos 2025:</span> {school.slms_vendidos_25} - "
                f"<a href='{url_slm_2025}'>{download_icon}</a> - "
                f"<span style='font-weight: bold;'>Meta de SLMs 2025:</span> Ainda não foi definido - "
                f"<span style='font-weight: bold;'>Dias Úteis para Entrega do SLM:</span> {school.dias_uteis_entrega_slm}.<br>"
                
                f"<br><span style='font-weight: bold;'>Avaliações:</span><br>"
                f"<span style='font-weight: bold;'>NPS Pais 2024 - 1ª Onda:</span> {school.nps_pais_2024_1_onda} - "
                f"<span style='font-weight: bold;'>Cliente Oculto 2024:</span> {school.cliente_oculto_2024} - "
                f"<span style='font-weight: bold;'>Quality Assurance 2024: </span> {school.quality_assurance_2024}.<br>"

                f"<br><span style='font-weight: bold;'>Financeiro:</span><br>"
                f"<span style='font-weight: bold;'>Ticket Médio:</span> R$ {school.ticket_medio} - "
                f"<span style='font-weight: bold;'>Valor Royalties:</span> R$ {school.valor_royalties} - "
                f"<span style='font-weight: bold;'>Valor de FDMP:</span> R$ {school.valor_fdmp} - "
                f"<span style='font-weight: bold;'>Status de Adimplência/Inadimplência:</span> {school.status_de_adimplencia}{inadimplencia_info}.<br>"

                f"<br><span style='font-weight: bold;'>Consultores:</span><br>"
                f"<span style='font-weight: bold;'>Consultor Comercial:</span> {school.consultor_comercial} - "
                f"<span style='font-weight: bold;'>Consultor de Gestão Escolar:</span> {school.consultor_gestao_escolar} - "
                f"<span style='font-weight: bold;'>Consultor Acadêmico:</span> {school.consultor_academico} - "
                f"<span style='font-weight: bold;'>Consultor SAF:</span> {school.consultor_saf}.<br>"
            )

            # Adiciona o resumo do NPS se estiver disponível
            if resumo_nps_text:
                response += (
                    f"<br><span style='font-weight: bold;'>Resumo das Respostas Negativas do NPS:</span><br>"
                    f"{resumo_nps_text}<br>"
                )
            # Adiciona o resumo do NPS se estiver disponível
            if resumo_resumo_co24_text:
                response += (
                    f"<br><span style='font-weight: bold;'>Resumo dos Comentários Negativos do Cliente Oculto:</span><br>"
                    f"{resumo_resumo_co24_text}<br>"
                )

            # Adiciona a frase final
            response += f"<br>{frase_final}"

            return JsonResponse({"response": response})


        # Apenas chama a função de classificação se a mensagem não for automática
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
                    f"NPS: {school.nps_pais_2024_1_onda} - Pontuação Geral dessa Escola.\n"
                    f"Nome do respondente: {response.nome}\n"
                    f"Questão perguntada no NPS: {response.questao}\n"
                    f"Nota: {response.nota} - "
                    f"As notas variam de 1 a 5, exceto para a pergunta de recomendação, que varia de 0 a 10.\n"
                    f"Comentário: {response.comentario}\n\n"
                )
            print("Contexto NPS gerado")


        if question_type == "cliente_oculto":
            print("Lidando com categoria Cliente Oculto")
            co24_responses = (
                Avaliacao_Cliente_Oculto_24.objects.filter(escola__id_escola=school_id)
            )
            context = ""
            context += (
                f"Cliente Oculto é uma avaliação realizada por cliente secreto enviado pela franqueada Maple Bear onde o objetivo é avaliar a escola do ponte de vista de um cliente:\n"
            )
            for response in co24_responses:
                context += (
                    f"Categoria: {response.categoria}\n"
                    f"Questão perguntada no Cliente Oculto 2024: {response.pergunta}\n"
                    f"Resposta: {response.resposta}\n\n"
                )
            print("Contexto Cliente Oculto")



        elif question_type == "analise completa da escola":
            print("Lidando com análise completa da escola")
            knowledge_base_entries = Base_de_Conhecimento.objects.all()
            nps_responses = (
                Respostas_NPS.objects.filter(escola__id_escola=school_id)
                .exclude(comentario__isnull=True)
                .exclude(comentario__exact="")
                .exclude(comentario__exact="nan")
            )
            context = (
                f"Informações Básicas da Escola:\n"
                f"Nome da Escola: {school.nome_da_escola}\n"
                f"Status: {school.status_da_escola}\n"
                f"Cluster: {school.cluster}\n"
                f"CEP: {school.cep_escola}\n"
                f"Endereço: {school.endereco}\n"
                f"Complemento: {school.complemento_escola}\n"
                f"Bairro: {school.bairro_escola}\n"
                f"Cidade: {school.cidade_da_escola}\n"
                f"Estado: {school.estado_da_escola}\n"
                f"Região: {school.regiao_da_escola}\n"
                f"Segmento: {school.segmento_da_escola}\n"
                f"Atual Série: {school.atual_serie}\n"
                f"Avanço Segmento: {school.avanco_segmento}\n"
                f"Vendas e Metas de SLM:\n"
                f"SLMs Vendidos 2024: {school.slms_vendidos} - SLM ou SLMs no plural são os materiais vendidos, esses aqui são referente a 2024.\n"
                f"SLMs Vendidos 2025: {school.slms_vendidos_25} - SLM ou SLMs no plural são os materiais vendidos, esses aqui são referente a 2025.\n"
                f"Meta de SLMs 2024: {school.meta} - Esse campo é a meta de Vendas de SLM vendidos.\n"
                f"Meta de SLMs 2025: Ainda não foi definido a meta por escola.\n"
                f"Avaliações:\n"
                f"NPS Pais 2024 - 1° Onda: {school.nps_pais_2024_1_onda} - Este campo indica a pontuação referente ao NPS(Net Promoter Score) dos pais dos alunos que estudam na escola, que foi realizado no 1° semestre no ano(1° Onda).\n"
                f"Cliente Oculto 2024: {school.cliente_oculto_2024} - Este campo indica a pontuação referente ao Cliente Oculto, que uma avaliação realizada por uma empresa terceirizada onde consiste em um falso cliente ir até a escola para avaliar ela.\n"
                f"Quality Assurance 2024: {school.quality_assurance_2024} - Este campo indica a pontuação referente Quality Assurance uma avaliação realizada para ver a qualidade da escola.\n"
                f"Financeiro:\n"
                f"Ticket Médio: {school.ticket_medio} - Este é o valor médio de mensalidade cobrada pela escola.\n"
                f"Valor Royalties: {school.valor_royalties} - Este é o valor de royalties que a escola deve pagar por mês à franqueada Maple Bear.\n"
                f"Valor de FDMP(Fundo de Marketing): {school.valor_fdmp} - Este é o valor de FDMP(Fundo de Marketing) que a escola deve pagar por mês à franqueada Maple Bear.\n"
                f"Status de Adimplência/Inadimplência: {school.status_de_adimplencia} - Este campo indica se a escola está Adimplente ou Inadimplente referente aos seus pagamentos(Royalties e FDMP) que devem ser feitos à franqueada Maple Bear.\n"
            )
            if school.status_de_adimplencia == "Inadimplente":
                context += f"Inadimplência: {school.inadimplencia} - Este é o valor que a escola está devendo para a Maple Bear.\n"

            for response in nps_responses:
                context += (
                    f"Respostas do NPS dessa escola:\n"
                    f"Questão perguntada no NPS: {response.questao}\n"
                    f"Comentário: {response.comentario}\n\n"
                )
            
            context += (
                f"Base de Conhecimento, com ela você busca todas informações referentes a Maple Bear para conseguir responder o usuário:\n"
            )
            for entry in knowledge_base_entries:
                context += f"Título: {entry.titulo}\nSub Assunto: {entry.sub_assunto}\nTexto: {entry.texto}\n\n"

            print("Contexto de análise completa da escola gerado")
        elif question_type == "base de conhecimento":
            print("Lidando com categoria conhecimento")
            knowledge_base_entries = Base_de_Conhecimento.objects.all()
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
                f"NPS Pais 2024 - 1° Onda: {school.nps_pais_2024_1_onda} - Este campo indica a pontuação referente ao NPS(Net Promoter Score) dos pais dos alunos que estudam na escola, que foi realizado no 1° semestre no ano(1° Onda).\n"
                f"Cliente Oculto 2024: {school.cliente_oculto_2024} - Este campo indica a pontuação referente ao Cliente Oculto, que uma avaliação realizada por uma empresa terceirizada onde consiste em um falso cliente ir até a escola para avaliar ela.\n"
                f"Quality Assurance 2024: {school.quality_assurance_2024} - Este campo indica a pontuação referente Quality Assurance uma avaliação realizada para ver a qualidade da escola.\n"
                f"Financeiro:\n"
                f"Ticket Médio: {school.ticket_medio} - Este é o valor médio de mensalidade cobrada pela escola.\n"
                f"Valor Royalties: {school.valor_royalties} - Este é o valor de royalties que a escola deve pagar por mês à franqueada Maple Bear.\n"
                f"Valor de FDMP(Fundo de Marketing): {school.valor_fdmp} - Este é o valor de FDMP(Fundo de Marketing) que a escola deve pagar por mês à franqueada Maple Bear.\n"
                f"Status de Adimplência/Inadimplência: {school.status_de_adimplencia} - Este campo indica se a escola está Adimplente ou Inadimplente referente aos seus pagamentos(Royalties e FDMP) que devem ser feitos à franqueada Maple Bear.\n"
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

            for entry in knowledge_base_entries:
                context += f"Titulo: {entry.titulo}\n Assunto: {entry.assunto}\nSub Assunto: {entry.sub_assunto}\nTexto: {entry.texto}\n\n"
            print("Contexto de conhecimento gerado")
        
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
                f"Dias Úteis para Entrega do SLM nessa escola: {school.dias_uteis_entrega_slm} - Basicamente o prazo de entrega do material nessa escola.\n"
                
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


################################### Controle Escolas #####################################################


class ControleEscolasSearchView(ListView):
    model = CRM_FUI
    template_name = "chatapp/controle_escolas.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        context["order_by"] = self.request.GET.get("order_by", "nome_da_escola")
        page_obj = context["page_obj"]

        # Obtém o número da página atual
        current_page = page_obj.number

        # Se há mais de 5 páginas
        if page_obj.paginator.num_pages > 5:
            if current_page - 2 < 1:
                start_page = 1
                end_page = 5
            elif current_page + 2 > page_obj.paginator.num_pages:
                start_page = page_obj.paginator.num_pages - 4
                end_page = page_obj.paginator.num_pages
            else:
                start_page = current_page - 2
                end_page = current_page + 2
        else:
            start_page = 1
            end_page = page_obj.paginator.num_pages

        context["page_range"] = range(start_page, end_page + 1)

        # Adiciona porcentagem_planificador ao contexto
        for escola in context['object_list']:
            planificador = Planificador_2024.objects.filter(escola=escola).first()
            if planificador:
                escola.planificador = planificador
                escola.porcentagem_planificador = calcular_porcentagem_sim(planificador)
            else:
                escola.planificador = None
                escola.porcentagem_planificador = 0

        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        order_by = self.request.GET.get("order_by", "nome_da_escola")
        if query:
            return CRM_FUI.objects.filter(Q(nome_da_escola__icontains=query)).order_by(order_by)
        return CRM_FUI.objects.all().order_by(order_by)
    


################################### Gerar Resumo NPS#####################################################

def gerar_resumo_nps(request, school_id):
    print("Iniciando a geração do resumo NPS...")

    # Busca a escola pelo ID
    escola = get_object_or_404(CRM_FUI, id_escola=school_id)
    print(f"Escola encontrada: {escola.nome_da_escola}")

    # Filtra as respostas NPS para a escola, excluindo comentários vazios, null ou nan
    respostas = Respostas_NPS.objects.filter(
        escola=escola
    ).exclude(
        comentario__isnull=True
    ).exclude(
        comentario__exact=""
    ).exclude(
        comentario__iexact="nan"
    )
    print(f"Número de respostas encontradas: {respostas.count()}")

    # Cria um contexto categorizado com as questões e comentários para passar para o prompt
    comentarios_categorizados = "\n".join(
        [f"Categoria: {resposta.questao}\nComentário: {resposta.comentario}\n" for resposta in respostas]
    )

    if comentarios_categorizados:
        prompt = (
            "Faça um resumo bem resumido dos comentários negativos, monte um paragrafo unico resumindo:\n"
            f"{comentarios_categorizados}"
        )
        print(f"Prompt gerado: {prompt[:100]}...")  # Exibe apenas os primeiros 100 caracteres do prompt

        api_key = request.user.api_key  # Assume que o usuário logado tem uma chave API
        resumo = config_resumo_nps(prompt, api_key)
        print(f"Resumo gerado: {resumo[:100]}...")  # Exibe apenas os primeiros 100 caracteres do resumo

        # Salva o resumo na model Resumo_Respostas_NPS
        resumo_nps, created = Resumo_Respostas_NPS.objects.get_or_create(escola=escola)
        resumo_nps.resumo = resumo
        resumo_nps.save()
        print("Resumo salvo com sucesso!")

        return redirect('controle_escolas')  # Redireciona de volta para a lista de escolas

    print("Não há comentários válidos para resumir.")
    return redirect('controle_escolas')


def gerar_resumos_todas_escolas(request):
    escolas = CRM_FUI.objects.all()
    resultados = []
    
    for escola in escolas:
        # Verifica se já existe um resumo para a escola e se está em branco
        resumo_nps, created = Resumo_Respostas_NPS.objects.get_or_create(escola=escola)
        if resumo_nps.resumo is None or resumo_nps.resumo.strip() == "":
            # Filtra as respostas NPS para a escola, excluindo comentários vazios, null ou nan
            respostas = Respostas_NPS.objects.filter(
                escola=escola
            ).exclude(
                comentario__isnull=True
            ).exclude(
                comentario__exact=""
            ).exclude(
                comentario__iexact="nan"
            )

            comentarios_categorizados = "\n".join(
                [f"Categoria: {resposta.questao}\nComentário: {resposta.comentario}\n" for resposta in respostas]
            )

            if comentarios_categorizados:
                prompt = (
                    "Faça um resumo bem resumido dos comentários negativos, monte um paragrafo unico resumindo:\n"
                    f"{comentarios_categorizados}"
                )
                api_key = request.user.api_key  # Assume que o usuário logado tem uma chave API
                resumo = config_resumo_nps(prompt, api_key)

                # Salva o resumo na model Resumo_Respostas_NPS
                resumo_nps.resumo = resumo
                resumo_nps.save()

                resultados.append(f"Resumo gerado para {escola.nome_da_escola} com sucesso!")
            else:
                resultados.append(f"Não há comentários válidos para {escola.nome_da_escola}.")
        else:
            resultados.append(f"O resumo para {escola.nome_da_escola} já existe e não está em branco.")

        time.sleep(5)

    return JsonResponse({"resultados": resultados})


################################### Gerar Resumo Cliente Oculto 2024#####################################################


def gerar_resumo_cliente_oculto(request, school_id):
    print("Iniciando a geração do resumo do Cliente Oculto 2024...")

    # Busca a escola pelo ID
    escola = get_object_or_404(CRM_FUI, id_escola=school_id)
    print(f"Escola encontrada: {escola.nome_da_escola}")

    # Filtra as respostas do Cliente Oculto para a escola, excluindo respostas vazias, null ou nan
    respostas = Avaliacao_Cliente_Oculto_24.objects.filter(
        escola=escola
    ).exclude(
        resposta__isnull=True
    ).exclude(
        resposta__exact=""
    ).exclude(
        resposta__iexact="nan"
    )
    print(f"Número de respostas encontradas: {respostas.count()}")

    # Cria um contexto categorizado com as questões e respostas para passar para o prompt
    respostas_categorizadas = "\n".join(
        [f"Categoria: {resposta.categoria}\nPergunta: {resposta.pergunta}\nResposta: {resposta.resposta}\n" for resposta in respostas]
    )

    if respostas_categorizadas:
        prompt = (
            "Faça um resumo bem resumido das respostas, monte um paragrafo único resumindo:\n"
            f"{respostas_categorizadas}"
        )
        print(f"Prompt gerado: {prompt[:100]}...")  # Exibe apenas os primeiros 100 caracteres do prompt

        api_key = request.user.api_key  # Assume que o usuário logado tem uma chave API
        resumo = config_resumo_cliente_oculto(prompt, api_key)
        print(f"Resumo gerado: {resumo[:100]}...")  # Exibe apenas os primeiros 100 caracteres do resumo

        # Salva o resumo na model Resumo_Respostas_ClienteOculto24
        resumo_co24, created = Resumo_Respostas_ClienteOculto24.objects.get_or_create(escola=escola)
        resumo_co24.resumo = resumo
        resumo_co24.save()
        print("Resumo salvo com sucesso!")

        return redirect('controle_escolas')  # Redireciona de volta para a lista de escolas

    print("Não há respostas válidas para resumir.")
    return redirect('controle_escolas')


def gerar_resumos_cliente_oculto_todas_escolas(request):
    escolas = CRM_FUI.objects.all()
    resultados = []
    
    for escola in escolas:
        # Verifica se já existe um resumo para a escola e se está em branco
        resumo_co24, created = Resumo_Respostas_ClienteOculto24.objects.get_or_create(escola=escola)
        if resumo_co24.resumo is None or resumo_co24.resumo.strip() == "":
            # Filtra as respostas do Cliente Oculto para a escola, excluindo respostas vazias, null ou nan
            respostas = Avaliacao_Cliente_Oculto_24.objects.filter(
                escola=escola
            ).exclude(
                resposta__isnull=True
            ).exclude(
                resposta__exact=""
            ).exclude(
                resposta__iexact="nan"
            )

            respostas_categorizadas = "\n".join(
                [f"Categoria: {resposta.categoria}\nPergunta: {resposta.pergunta}\nResposta: {resposta.resposta}\n" for resposta in respostas]
            )

            if respostas_categorizadas:
                prompt = (
                    "Faça um resumo bem resumido das respostas, monte um paragrafo único resumindo:\n"
                    f"{respostas_categorizadas}"
                )
                api_key = request.user.api_key  # Assume que o usuário logado tem uma chave API
                resumo = config_resumo_cliente_oculto(prompt, api_key)

                # Salva o resumo na model Resumo_Respostas_ClienteOculto24
                resumo_co24.resumo = resumo
                resumo_co24.save()

                resultados.append(f"Resumo gerado para {escola.nome_da_escola} com sucesso!")
            else:
                resultados.append(f"Não há respostas válidas para {escola.nome_da_escola}.")
        else:
            resultados.append(f"O resumo para {escola.nome_da_escola} já existe e não está em branco.")

        time.sleep(5)  # Pausa de 5 segundos entre as escolas

    return JsonResponse({"resultados": resultados})


################################### PLANIFICADOR #####################################################

class ImportPlanificadorView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "chatapp/import/import_planificador.html")

    def post(self, request):
        file = request.FILES["file"]
        if not file.name.endswith(".xlsx"):
            messages.error(request, "Por favor, envie um arquivo Excel.")
            return redirect("import_planificador")

        df = pd.read_excel(file)
        for _, row in df.iterrows():
            try:
                escola = CRM_FUI.objects.get(id_escola=row["id_escola"])
                Planificador_2024.objects.update_or_create(
                    escola=escola,
                    defaults={
                        "ultima_data_atualizacao_bloc_drivers_comerciais_estrategicos": self.parse_date(row["ultima_data_atualizacao_bloc_drivers_comerciais_estrategicos"]),
                        "crm_b2c": self.parse_text(row["crm_b2c"]),
                        "data_abertura_matricula_2025": self.parse_date(row["data_abertura_matricula_2025"]),
                        "circular_oferta_2025_publicado": self.parse_text(row["circular_oferta_2025_publicado"]),
                        "data_de_abertura_da_circular_2025": self.parse_date(row["data_de_abertura_da_circular_2025"]),
                        "toddle": self.parse_text(row["toddle"]),
                        "toddle_planejamento": self.parse_text(row["toddle_planejamento"]),
                        "toddle_portfolio": self.parse_text(row["toddle_portfolio"]),
                        "arvore": self.parse_text(row["arvore"]),
                        "data_implementacao_arvore": self.parse_date(row["data_implementacao_arvore"]),
                        "ultima_data_atualizacao_bloc_funil_comercial": self.parse_date(row["ultima_data_atualizacao_bloc_funil_comercial"]),
                        "leads_central_ago_24": self.parse_number(row["leads_central_ago_24"]),
                        "leads_escolas_ago_24": self.parse_number(row["leads_escolas_ago_24"]),
                        "visitas_ago_24": self.parse_number(row["visitas_ago_24"]),
                        "taxa_conversao_atual_leads_visitas": self.parse_number(row["taxa_conversao_atual_leads_visitas"]),
                        "matriculas_ago_24": self.parse_number(row["matriculas_ago_24"]),
                        "taxa_conversao_atual_visitas_matriculas": self.parse_number(row["taxa_conversao_atual_visitas_matriculas"]),
                        "taxa_conversao_leads_matriculas": self.parse_number(row["taxa_conversao_leads_matriculas"]),
                        "ultima_data_atualizacao_bloc_drivers_comerciais_meio": self.parse_date(row["ultima_data_atualizacao_bloc_drivers_comerciais_meio"]),
                        "meta_alunos_5k_2024": self.parse_number(row["meta_alunos_5k_2024"]),
                        "setup_plano_comercial_segundo_semestre": self.parse_text(row["setup_plano_comercial_segundo_semestre"]),
                        "acao_1_elegivel_trade_marketing": self.parse_text(row["acao_1_elegivel_trade_marketing"]),
                        "acao_1_trade_valor": self.parse_number(row["acao_1_trade_valor"]),
                        "acao_1_trade_marketing_acoes_alinhadas": self.parse_text(row["acao_1_trade_marketing_acoes_alinhadas"]),
                        "acao_2_experience_day_10_08_24": self.parse_text(row["acao_2_experience_day_10_08_24"]),
                        "acao_2_experience_day_24_08_24": self.parse_text(row["acao_2_experience_day_24_08_24"]),
                        "acao_2_experience_day_21_09_24": self.parse_text(row["acao_2_experience_day_21_09_24"]),
                        "acao_2_experience_day_26_10_24": self.parse_text(row["acao_2_experience_day_26_10_24"]),
                        "acao_2_experience_day_09_11_24": self.parse_text(row["acao_2_experience_day_09_11_24"]),
                        "acao_3_friend_get_friend": self.parse_text(row["acao_3_friend_get_friend"]),
                        "acao_4_webinars_com_autoridades_pre": self.parse_text(row["acao_4_webinars_com_autoridades_pre"]),
                        "acao_4_webinars_com_autoridades_pos": self.parse_text(row["acao_4_webinars_com_autoridades_pos"]),
                        "piloto_welcome_baby_bear": self.parse_text(row["piloto_welcome_baby_bear"]),
                        "acao_5_sdr_taxa_conversao_validacao_lead": self.parse_number(row["acao_5_sdr_taxa_conversao_validacao_lead"]),
                        "acao_5_sdr_taxa_conversao_visitas": self.parse_number(row["acao_5_sdr_taxa_conversao_visitas"]),
                        "acao_6_alinhado_resgate_leads": self.parse_text(row["acao_6_alinhado_resgate_leads"]),
                        "acao_6_quantidade_leads_resgatados": self.parse_number(row["acao_6_quantidade_leads_resgatados"]),
                        "acao_6_todos_leads_resgatados_contatados": self.parse_text(row["acao_6_todos_leads_resgatados_contatados"]),
                        "data_atualizacao_resultados": self.parse_date(row["data_atualizacao_resultados"]),
                        "slm_2022": self.parse_number(row["slm_2022"]),
                        "slm_2023": self.parse_number(row["slm_2023"]),
                        "meta_orcamentaria_2024": self.parse_number(row["meta_orcamentaria_2024"]),
                        "base_rematriculaveis_2025": self.parse_number(row["base_rematriculaveis_2025"]),
                        "meta_rematricula_2025": self.parse_number(row["meta_rematricula_2025"]),
                        "real_rematriculas_2025": self.parse_number(row["real_rematriculas_2025"]),
                        "atingimento_rematriculas_2025": self.parse_number(row["atingimento_rematriculas_2025"]),
                        "meta_matricula_2025": self.parse_number(row["meta_matricula_2025"]),
                        "real_matricula_2025": self.parse_number(row["real_matricula_2025"]),
                        "atingimento_matriculas_2025": self.parse_number(row["atingimento_matriculas_2025"]),
                        "total_meta_alunos_2025": self.parse_number(row["total_meta_alunos_2025"]),
                        "total_real_alunos_2025": self.parse_number(row["total_real_alunos_2025"]),
                        "atingimento_real_alunos_2025": self.parse_number(row["atingimento_real_alunos_2025"]),
                        "correlacao_alunos_slms_2025": self.parse_number(row["correlacao_alunos_slms_2025"]),
                        "mc_2025": self.parse_number(row["mc_2025"]),
                        "slms_2025_m": self.parse_number(row["slms_2025_m"]),
                        "pedidos_represados_logistica_2025": self.parse_number(row["pedidos_represados_logistica_2025"]),
                        "pedidos_faturados": self.parse_number(row["pedidos_faturados"]),
                        "pedidos_entregues": self.parse_number(row["pedidos_entregues"]),
                    }
                )
            except CRM_FUI.DoesNotExist:
                messages.error(request, f"Escola com id_escola {row['id_escola']} não encontrada.")
        messages.success(request, "Dados importados com sucesso!")
        return redirect("import_planificador")

    def parse_date(self, date):
        if pd.isna(date):
            return None
        if isinstance(date, str):
            return datetime.fromisoformat(date).date()
        if isinstance(date, pd.Timestamp):
            return date.to_pydatetime().date()
        if isinstance(date, datetime):
            return date.date()
        return date

    def parse_number(self, value):
        if pd.isna(value):
            return None
        return value

    def parse_text(self, value):
        if pd.isna(value):
            return ''
        return value

class PlanificadorCreateView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = PlanificadorForm()
        return render(request, "chatapp/planificador/planificador_form.html", {"form": form})

    def post(self, request):
        form = PlanificadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados criados com sucesso!")
            return redirect("planificador_list")
        return render(request, "chatapp/planificador/planificador_form.html", {"form": form})



def calcular_porcentagem_sim(planificador):
    sim_nao_fields = [
        planificador.crm_b2c,
        planificador.circular_oferta_2025_publicado,
        planificador.toddle,
        planificador.arvore,
        planificador.setup_plano_comercial_segundo_semestre,
        planificador.acao_2_experience_day_10_08_24,
        planificador.acao_2_experience_day_24_08_24,
        planificador.acao_2_experience_day_21_09_24,
        planificador.acao_2_experience_day_26_10_24,
        planificador.acao_2_experience_day_09_11_24,
        planificador.acao_3_friend_get_friend,
        planificador.acao_4_webinars_com_autoridades_pre,
        planificador.acao_4_webinars_com_autoridades_pos,
        planificador.piloto_welcome_baby_bear,
        planificador.acao_6_alinhado_resgate_leads,
        planificador.acao_6_todos_leads_resgatados_contatados
    ]

    total_fields = len(sim_nao_fields)
    sim_count = sum(1 for field in sim_nao_fields if field == 'SIM')
    porcentagem_sim = (sim_count / total_fields) * 100
    return f"{porcentagem_sim:.2f}"

class PlanificadorUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, pk):
        planificador = get_object_or_404(Planificador_2024, pk=pk)
        form = PlanificadorForm(instance=planificador)

        # Definindo os campos como readonly
        form.fields['slm_2022'].widget.attrs['readonly'] = True
        form.fields['slm_2023'].widget.attrs['readonly'] = True

        porcentagem_planificador = calcular_porcentagem_sim(planificador)

        escola = planificador.escola
        context = {
            "form": form,
            "planificador": planificador,
            "crm_fui_meta": escola.meta,
            "crm_fui_slms_vendidos": escola.slms_vendidos,
            "crm_fui_slms_vendidos_25": escola.slms_vendidos_25,
            "crm_fui_id_escola": escola.id_escola,
            "crm_fui_nome_da_escola": escola.nome_da_escola,
            "crm_fui_cluster": escola.cluster,
            "crm_fui_atual_serie": escola.atual_serie,
            "crm_fui_segmento_da_escola": escola.segmento_da_escola,
            "crm_fui_consultor_comercial": escola.consultor_comercial,
            "crm_fui_consultor_gestao_escolar": escola.consultor_gestao_escolar,
            "crm_fui_consultor_saf": escola.consultor_saf,
            "crm_fui_consultor_academico": escola.consultor_academico,
            "porcentagem_planificador": porcentagem_planificador
        }
        return render(request, "chatapp/planificador/planificador_form_edit.html", context)

    def post(self, request, pk):
        planificador = get_object_or_404(Planificador_2024, pk=pk)
        data = request.POST.copy()
        data['escola'] = planificador.escola.pk  # Inclua o campo escola nos dados do formulário
        form = PlanificadorForm(data, instance=planificador)

        # Definindo os campos como readonly na postagem também
        form.fields['slm_2022'].widget.attrs['readonly'] = True
        form.fields['slm_2023'].widget.attrs['readonly'] = True

        if form.is_valid():
            try:
                # Atualizando o campo 'usuario_modificacao' antes de salvar
                planificador = form.save(commit=False)
                planificador.usuario_modificacao = request.user
                planificador.save()

                messages.success(request, "Dados atualizados com sucesso!")
                return redirect("buscar_escolas")
            except Exception as e:
                messages.error(request, "Erro ao atualizar os dados.")
        else:
            messages.error(request, "Erro ao atualizar os dados: %s" % form.errors)

        porcentagem_planificador = calcular_porcentagem_sim(planificador)

        escola = planificador.escola
        context = {
            "form": form,
            "planificador": planificador,
            "crm_fui_meta": escola.meta,
            "crm_fui_slms_vendidos": escola.slms_vendidos,
            "crm_fui_slms_vendidos_25": escola.slms_vendidos_25,
            "crm_fui_id_escola": escola.id_escola,
            "crm_fui_nome_da_escola": escola.nome_da_escola,
            "crm_fui_cluster": escola.cluster,
            "crm_fui_atual_serie": escola.atual_serie,
            "crm_fui_segmento_da_escola": escola.segmento_da_escola,
            "crm_fui_consultor_comercial": escola.consultor_comercial,
            "crm_fui_consultor_gestao_escolar": escola.consultor_gestao_escolar,
            "crm_fui_consultor_saf": escola.consultor_saf,
            "crm_fui_consultor_academico": escola.consultor_academico,
            "porcentagem_planificador": porcentagem_planificador
        }
        return render(request, "chatapp/planificador/planificador_form_edit.html", context)
######################## BUSCA ESCOLAS PLANIFICADOR #################################################
class EscolaSearchView(ListView):
    model = CRM_FUI
    template_name = "chatapp/planificador/busca_escolas.html"  # Altere para o caminho correto do seu template
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        context["order_by"] = self.request.GET.get("order_by", "nome_da_escola")
        page_obj = context["page_obj"]

        # Obtém o número da página atual
        current_page = page_obj.number

        # Se há mais de 5 páginas
        if page_obj.paginator.num_pages > 5:
            if current_page - 2 < 1:
                start_page = 1
                end_page = 5
            elif current_page + 2 > page_obj.paginator.num_pages:
                start_page = page_obj.paginator.num_pages - 4
                end_page = page_obj.paginator.num_pages
            else:
                start_page = current_page - 2
                end_page = current_page + 2
        else:
            start_page = 1
            end_page = page_obj.paginator.num_pages

        context["page_range"] = range(start_page, end_page + 1)

        # Adiciona porcentagem_planificador ao contexto
        for escola in context['object_list']:
            planificador = Planificador_2024.objects.filter(escola=escola).first()
            if planificador:
                escola.planificador = planificador
                escola.porcentagem_planificador = calcular_porcentagem_sim(planificador)
            else:
                escola.planificador = None
                escola.porcentagem_planificador = 0

        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        order_by = self.request.GET.get("order_by", "nome_da_escola")
        if query:
            return CRM_FUI.objects.filter(Q(nome_da_escola__icontains=query)).order_by(order_by)
        return CRM_FUI.objects.all().order_by(order_by)
    


################################################# ATUALIZAÇÃO JSON ######################################################


@csrf_exempt
def import_vendas_slm_2025_json(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'erro', 'mensagem': f"Erro ao parsear o JSON: {e}"}, status=400)

        with transaction.atomic():
            for result in dados.get('results', []):
                for table in result.get('tables', []):
                    for row in table.get('rows', []):
                        try:
                            escola = CRM_FUI.objects.get(id_escola=row.get('fui_slm_2025[id_escola]'))

                            # Converte o campo data_do_pedido para um objeto datetime
                            data_do_pedido = datetime.strptime(row.get('fui_slm_2025[data_do_pedido]', ''), "%Y-%m-%dT%H:%M:%S")

                            # Cria o novo registro com o novo campo id_linha
                            Vendas_SLM_2025.objects.create(
                                escola=escola,
                                numero_do_pedido=row.get('fui_slm_2025[numero_do_pedido]', ''),
                                nome_pais=row.get('fui_slm_2025[nome_pais]', ''),
                                nome_do_aluno=row.get('fui_slm_2025[nome_do_aluno]', ''),
                                data_do_pedido=data_do_pedido,
                                quantidade=row.get('[Sumquantidade]', 0),
                                id_linha=row.get('fui_slm_2025[id_linha]', 0)  # Novo campo adicionado
                            )
                        except CRM_FUI.DoesNotExist:
                            return JsonResponse(
                                {'status': 'erro', 'mensagem': f"Escola com id_escola {row.get('fui_slm_2025[id_escola]')} não encontrada."},
                                status=400
                            )
                        except Exception as e:
                            return JsonResponse(
                                {'status': 'erro', 'mensagem': f"Erro ao importar o pedido {row.get('fui_slm_2025[numero_do_pedido]')}: {e}"},
                                status=500
                            )

        return JsonResponse({'status': 'sucesso', 'mensagem': 'Dados importados com sucesso!'}, status=200)

    return JsonResponse({'status': 'falha', 'mensagem': 'Método não permitido'}, status=405)



@csrf_exempt
def import_vendas_slm_2024_json(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'erro', 'mensagem': f"Erro ao parsear o JSON: {e}"}, status=400)

        with transaction.atomic():
            for result in dados.get('results', []):
                for table in result.get('tables', []):
                    for row in table.get('rows', []):
                        try:
                            escola = CRM_FUI.objects.get(id_escola=row.get('slm_2024[id_escola]'))
                            data_do_pedido = datetime.strptime(row.get('slm_2024[data_do_pedido]', ''), "%Y-%m-%dT%H:%M:%S")

                            # Atualiza ou cria a venda com base no numero_do_pedido e escola
                            Vendas_SLM_2024.objects.update_or_create(
                                numero_do_pedido=row.get('slm_2024[numero_do_pedido]', ''),
                                escola=escola,
                                defaults={
                                    "nome_pais": row.get('slm_2024[nome_pais]', ''),
                                    "nome_do_aluno": row.get('slm_2024[nome_do_aluno]', ''),
                                    "data_do_pedido": data_do_pedido,
                                    "quantidade": row.get('[Sumquantidade]', 0),
                                    "id_linha": row.get('slm_2024[id_linha]', None)
                                }
                            )
                        except CRM_FUI.DoesNotExist:
                            return JsonResponse(
                                {'status': 'erro', 'mensagem': f"Escola com id_escola {row.get('slm_2024[id_escola]')} não encontrada."},
                                status=400
                            )
                        except Exception as e:
                            return JsonResponse(
                                {'status': 'erro', 'mensagem': f"Erro ao importar o pedido {row.get('slm_2024[numero_do_pedido]')}: {e}"},
                                status=500
                            )

        return JsonResponse({'status': 'sucesso', 'mensagem': 'Dados importados e atualizados com sucesso!'}, status=200)

    return JsonResponse({'status': 'falha', 'mensagem': 'Método não permitido'}, status=405)


@csrf_exempt
def import_crm_fui_json(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'erro', 'mensagem': f"Erro ao parsear o JSON: {e}"}, status=400)

        with transaction.atomic():
            for result in dados.get('results', []):
                for table in result.get('tables', []):
                    for row in table.get('rows', []):
                        try:
                            CRM_FUI.objects.update_or_create(
                                id_escola=row.get('CRM_B2B[id_escola]'),
                                defaults={
                                    "nome_da_escola": row.get('CRM_B2B[nome_da_escola]', ''),
                                    "CNPJ": row.get('CRM_B2B[CNPJ]', ''),
                                    "status_da_escola": row.get('CRM_B2B[status_da_escola]', ''),
                                    "slms_vendidos": row.get('CRM_B2B[slms_vendidos]', 0),
                                    "slms_vendidos_25": row.get('CRM_B2B[slms_vendidos_25]', 0),
                                    "meta": row.get('CRM_B2B[meta]', 0),
                                    "cluster": row.get('CRM_B2B[cluster]', ''),
                                    "cep_escola": row.get('CRM_B2B[cep_escola]', ''),
                                    "endereco": row.get('CRM_B2B[endereco]', ''),
                                    "complemento_escola": row.get('CRM_B2B[complemento_escola]', ''),
                                    "bairro_escola": row.get('CRM_B2B[bairro_escola]', ''),
                                    "cidade_da_escola": row.get('CRM_B2B[cidade_da_escola]', ''),
                                    "estado_da_escola": row.get('CRM_B2B[estado_da_escola]', ''),
                                    "regiao_da_escola": row.get('CRM_B2B[regiao_da_escola]', ''),
                                    "status_de_adimplencia": row.get('CRM_B2B[status_de_adimplencia]', ''),
                                    "inadimplencia": row.get('CRM_B2B[inadimplencia]', 0),
                                    "ticket_medio": row.get('CRM_B2B[ticket_medio]', 0),
                                    "valor_royalties": row.get('CRM_B2B[valor_royalties]', 0),
                                    "valor_fdmp": row.get('CRM_B2B[valor_fdmp]', 0),
                                    "segmento_da_escola": row.get('CRM_B2B[segmento_da_escola]', ''),
                                    "atual_serie": row.get('CRM_B2B[atual_serie]', ''),
                                    "avanco_segmento": row.get('CRM_B2B[avanco_segmento]', ''),
                                    "telefone_de_contato_da_escola": row.get('CRM_B2B[telefone_de_contato_da_escola]', ''),
                                    "email_da_escola": row.get('CRM_B2B[email_da_escola]', ''),
                                    "nps_pais_2024_1_onda": row.get('CRM_B2B[nps_pais_2024_1_onda]', 0),
                                    "quality_assurance_2024": row.get('CRM_B2B[quality_assurance_2024]', 0),
                                    "cliente_oculto_2024": row.get('CRM_B2B[cliente_oculto_2024]', 0),
                                    "consultor_saf": row.get('CRM_B2B[consultor_saf]', ''),
                                    "consultor_academico": row.get('CRM_B2B[consultor_academico]', ''),
                                    "consultor_comercial": row.get('CRM_B2B[consultor_comercial]', ''),
                                    "consultor_gestao_escolar": row.get('CRM_B2B[consultor_gestao_escolar]', ''),
                                    "dias_uteis_entrega_slm": row.get('CRM_B2B[dias_uteis_entrega_slm]', ''),
                                }
                            )
                        except Exception as e:
                            return JsonResponse(
                                {'status': 'erro', 'mensagem': f"Erro ao importar o registro com id_escola {row.get('CRM_B2B[id_escola]')}: {e}"},
                                status=500
                            )

        return JsonResponse({'status': 'sucesso', 'mensagem': 'Dados importados com sucesso!'}, status=200)

    return JsonResponse({'status': 'falha', 'mensagem': 'Método não permitido'}, status=405)