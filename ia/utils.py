import openai
from django.conf import settings
import openpyxl
from openpyxl.utils import get_column_letter
import os
import re
from django.db.models import Q
from django.db import models

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

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": context},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1050,
    )
    print(f"Total tokens usados: {response['usage']['total_tokens']}")
    return response["choices"][0]["message"]["content"].strip()


def calculate_statistics(informacoes):
    total_respostas = informacoes.count()
    stats = {
        "Negativo": 0,
        "Neutro": 0,
        "Positivo": 0,
        "Detrator": 0,
        "Promotor": 0,
    }

    for info in informacoes:
        if (
            info.questao
            == "Em uma escala de 0 a 10, o quanto você recomendaria a escola para um amigo ou familiar?"
        ):
            if info.resposta >= 1 and info.resposta <= 6:
                stats["Negativo"] += 1
                stats["Detrator"] += 1
            elif info.resposta == 7 or info.resposta == 8:
                stats["Neutro"] += 1
            elif info.resposta == 9 or info.resposta == 10:
                stats["Positivo"] += 1
                stats["Promotor"] += 1
        else:
            if info.resposta >= 1 and info.resposta <= 2:
                stats["Negativo"] += 1
            elif info.resposta == 3:
                stats["Neutro"] += 1
            elif info.resposta >= 4 and info.resposta <= 5:
                stats["Positivo"] += 1

    return total_respostas, stats


def calculate_nps(
    informacoes, suposicao_promotores=0, suposicao_neutros=0, suposicao_detratores=0
):
    total_respostas = (
        informacoes.count()
        + suposicao_promotores
        + suposicao_neutros
        + suposicao_detratores
    )
    if total_respostas == 0:
        return None  # Evita divisão por zero se não houver respostas

    promotores = informacoes.filter(resposta__in=[9, 10]).count() + suposicao_promotores
    detratores = informacoes.filter(resposta__lte=6).count() + suposicao_detratores

    percentual_promotores = (promotores / total_respostas) * 100
    percentual_detratores = (detratores / total_respostas) * 100

    nps = percentual_promotores - percentual_detratores
    return nps


def generate_excel_report(informacoes):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Relatório de Avaliações"

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

    for col_num, column_title in enumerate(headers, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = 20

    file_name = "relatorio_avaliacoes.xlsx"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    wb.save(file_path)

    return settings.MEDIA_URL + file_name
