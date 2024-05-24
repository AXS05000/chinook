import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Informacao
from .utils import (
    get_chat_response,
    generate_excel_report,
    calculate_statistics,
    calculate_nps,
)
import json
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
            user_message = data.get("message", "")
            context = ""

            # Consultar o banco de dados para obter informações relevantes
            informacoes = Informacao.objects.all()
            total_respostas, stats = calculate_statistics(informacoes)

            if total_respostas > 0:
                context += f"Total de respostas: {total_respostas}\n"
                context += f"Respostas negativas: {stats['Negativo']}\n"
                context += f"Respostas neutras: {stats['Neutro']}\n"
                context += f"Respostas positivas: {stats['Positivo']}\n"
                context += f"Detratores: {stats['Detrator']}\n"
                context += f"Promotores: {stats['Promotor']}\n"

            # Verificar se o usuário pediu o NPS
            if "nps" in user_message.lower():
                informacoes_nps = informacoes.filter(
                    questao="Em uma escala de 0 a 10, o quanto você recomendaria a escola para um amigo ou familiar?"
                )
                nps = calculate_nps(informacoes_nps)
                if nps is not None:
                    response = f"O NPS da sua escola é {nps:.2f}."
                else:
                    response = "Não há dados suficientes para calcular o NPS."
            else:
                # Obter resposta do ChatGPT
                response = get_chat_response(user_message, context)

            # Verificar se o usuário pediu um relatório ou uma tabela
            if "tabela" in user_message.lower() or "relatório" in user_message.lower():
                # Aplicar filtros com base no pedido do usuário
                if "nota" in user_message.lower():
                    try:
                        nota_filter = int(user_message.split("nota")[-1].strip())
                        informacoes = informacoes.filter(resposta=nota_filter)
                    except ValueError:
                        pass
                file_path = generate_excel_report(informacoes)
                file_url = request.build_absolute_uri(file_path)
                response = f"Você pode baixar o relatório em Excel clicando no link fornecido.\n\n<a href='{file_url}' target='_blank'>Baixar Relatório Excel</a>"

            return JsonResponse({"response": response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return render(request, "chatapp/chat.html")


def generate_excel_report(informacoes):
    # Cria a pasta 'media' se não existir
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    # Cria uma planilha
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Relatório de Avaliações"

    # Adiciona o cabeçalho
    headers = [
        "Nome",
        "Persona",
        "Data da Resposta",
        "Unidade",
        "Questão",
        "Resposta",
        "Comentário",
    ]
    ws.append(headers)

    # Adiciona os dados
    for info in informacoes:
        row = [
            info.nome,
            info.persona,
            info.data_resposta,
            info.unidade,
            info.questao,
            info.resposta,
            info.comentario,
        ]
        ws.append(row)

    # Ajusta a largura das colunas
    for col_num, column_title in enumerate(headers, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = 20

    # Salva o arquivo no sistema de arquivos do servidor
    file_name = "relatorio_avaliacoes.xlsx"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    wb.save(file_path)

    return settings.MEDIA_URL + file_name
