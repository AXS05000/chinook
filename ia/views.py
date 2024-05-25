import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Informacao
from .utils import (
    get_chat_response,
    generate_excel_report,
    calcular_nps,
    obter_distribuicao_nps,
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
