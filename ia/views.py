import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Informacao
from .utils import get_chat_response
import json
import openpyxl
from openpyxl.utils import get_column_letter
from django.conf import settings


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
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
                for info in informacoes:
                    escala = escalas.get(info.questao, "")
                    context += f"{info.nome},{info.persona},{info.data_resposta},{info.unidade},{info.questao} (Escala: {escala}),{info.resposta},{info.comentario}\n"
                context += (
                    f"\nA média das respostas para a escola é: {media_respostas:.2f}\n"
                )
            else:
                context = "No relevant information found in the database."

            # Obter resposta do ChatGPT
            response = get_chat_response(user_message, context)

            # Verifica se o usuário pediu um relatório ou uma tabela
            if "tabela" in user_message.lower() or "relatório" in user_message.lower():
                file_path = generate_excel_report(informacoes)
                file_url = request.build_absolute_uri(file_path)
                response += f"\n\n<a href='{file_url}' target='_blank'>Baixar Relatório Excel</a>"

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
