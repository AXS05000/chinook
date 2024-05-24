import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Informacao
from .utils import (
    get_chat_response,
    generate_excel_report,
    calculate_statistics,
    calculate_nps,
    respostas_por_dia,
    resumo_por_pergunta,
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
            user_message = data.get("message", "")
            context = ""

            informacoes = Informacao.objects.all()
            total_respostas, stats = calculate_statistics(informacoes)

            if total_respostas > 0:
                context += f"Total de respostas: {total_respostas}\n"
                context += f"Respostas negativas: {stats['Negativo']}\n"
                context += f"Respostas neutras: {stats['Neutro']}\n"
                context += f"Respostas positivas: {stats['Positivo']}\n"
                context += f"Detratores: {stats['Detrator']}\n"
                context += f"Promotores: {stats['Promotor']}\n"

                if "respostas por dia" in user_message.lower():
                    contagem_dias = respostas_por_dia(informacoes)
                    for dia, contagem in contagem_dias.items():
                        context += f"{dia}: {contagem} respostas\n"

                if (
                    "resumo por pergunta" in user_message.lower()
                    or "resumo dos comentários" in user_message.lower()
                ):
                    resumo = resumo_por_pergunta(informacoes)
                    for pergunta, dados in resumo.items():
                        context += f"\nPergunta: {pergunta}\n"
                        context += f"Total de Respostas: {dados['total']}\n"
                        context += f"Respostas Negativas: {dados['negativo']}\n"
                        context += f"Respostas Neutras: {dados['neutro']}\n"
                        context += f"Respostas Positivas: {dados['positivo']}\n"
                        context += "Comentários:\n"
                        for comentario in dados["comentarios"]:
                            context += f"- {comentario}\n"

            if "nps" in user_message.lower():
                informacoes_nps = informacoes.filter(
                    questao="Em uma escala de 0 a 10, o quanto você recomendaria a escola para um amigo ou familiar?"
                )

                # Verificar se há suposições
                suposicao_promotores = 0
                suposicao_neutros = 0
                suposicao_detratores = 0
                if "mais" in user_message.lower():
                    suposicao_str = user_message.lower().split("mais")[1].strip()
                    try:
                        if (
                            "respostas positivas" in suposicao_str
                            or "promotores" in suposicao_str
                        ):
                            suposicao_promotores = int(suposicao_str.split()[0].strip())
                        elif (
                            "respostas neutras" in suposicao_str
                            or "neutros" in suposicao_str
                        ):
                            suposicao_neutros = int(suposicao_str.split()[0].strip())
                        elif (
                            "respostas negativas" in suposicao_str
                            or "detratores" in suposicao_str
                        ):
                            suposicao_detratores = int(suposicao_str.split()[0].strip())
                    except ValueError:
                        pass

                nps = calculate_nps(
                    informacoes_nps,
                    suposicao_promotores,
                    suposicao_neutros,
                    suposicao_detratores,
                )
                if nps is not None:
                    if (
                        suposicao_promotores > 0
                        or suposicao_neutros > 0
                        or suposicao_detratores > 0
                    ):
                        response = f"O NPS da sua escola, considerando as suposições, seria {nps:.0f}."
                    else:
                        response = f"O NPS da sua escola é {nps:.0f}."
                else:
                    response = "Não há dados suficientes para calcular o NPS."
            else:
                response = get_chat_response(user_message, context)

            if "tabela" in user_message.lower() or "relatório" in user_message.lower():
                file_path = generate_excel_report(informacoes)
                file_url = request.build_absolute_uri(file_path)
                response += f"Você pode baixar o relatório em Excel clicando no link fornecido.\n\n<a href='{file_url}' target='_blank'>Baixar Relatório Excel</a>"

            return JsonResponse({"response": response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return render(request, "chatapp/chat.html")
