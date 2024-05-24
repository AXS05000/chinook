import openai
from django.conf import settings
import openpyxl
from openpyxl.utils import get_column_letter
import os
import re

openai.api_key = settings.OPENAI_API_KEY


## model="gpt-4o" - Modelo mais rapido e inteligente - 30 000 TPM
## model="gpt-4-turbo" - 2 Modelo mais rapido e inteligente - 30 000 TPM
## model="gpt-4" - 2 Modelo mais rapido e inteligente - 10 000 TPM
## model="gpt-3.5-turbo" - Modelo menos inteligente - 60 000 TPM


def get_chat_response(prompt, context=""):
    if not context:
        context = "No relevant information found in the database."
    if not prompt:
        prompt = "No question provided."

    # Dividir contexto em mensagens
    context_messages = context.split("\n")

    # Limitar o número de mensagens no contexto
    max_context_messages = 50  # Limitar a quantidade de mensagens no contexto
    if len(context_messages) > max_context_messages:
        context_messages = context_messages[-max_context_messages:]
    context = "\n".join(context_messages)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": context},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1050,
    )

    formatted_response = response["choices"][0]["message"]["content"].strip()

    # Adicionar quebra de linha antes de números seguidos por um ponto
    formatted_response = re.sub(r"(\d+\.)", r"<br><br>\1", formatted_response)

    # Substituir ":" por ":<br>"
    formatted_response = formatted_response.replace(":", ":<br>")

    # Substituir "###" por "<br>"
    formatted_response = formatted_response.replace("###", "<br>")

    # Envolver palavras entre ** com uma tag <span> com a classe 'highlight'
    formatted_response = re.sub(
        r"\*\*(.*?)\*\*",
        r"<span style='font-weight: bold;'>\1</span>",
        formatted_response,
    )

    # Envolver palavras entre * com uma tag <span> com a classe 'highlight'
    formatted_response = re.sub(
        r"\*(.*?)\*",
        r"<span style='font-weight: bold;'>\1</span>",
        formatted_response,
    )

    # Adicionar quebra de linha antes de ". - Texto:"
    formatted_response = re.sub(
        r"\.\s-\s(.*?):",
        r".<br> - \1:",
        formatted_response,
    )

    # Adicionar quebra de linha antes de ". Texto:"
    formatted_response = re.sub(
        r"\.\s(.*?):",
        r".<br> \1:",
        formatted_response,
    )

    return formatted_response


def generate_excel_report(informacoes):
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
