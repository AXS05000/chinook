import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def get_chat_response(prompt, context=""):
    if not context:
        context = "No relevant information found in the database."
    if not prompt:
        prompt = "No question provided."

    # Verifica se o usuário pediu para montar uma tabela
    if "montar uma tabela" in prompt.lower():
        return generate_table(context)

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": context},
            {"role": "user", "content": prompt},
        ],
        max_tokens=550,
    )
    return response["choices"][0]["message"]["content"].strip()


def generate_table(context):
    # Converte o contexto em uma tabela HTML
    rows = context.strip().split("\n")
    headers = [
        "Nome",
        "Persona",
        "Data da Resposta",
        "Unidade",
        "Questão",
        "Resposta",
        "Comentário",
    ]
    table_html = "<table border='1'><tr>"
    table_html += "".join([f"<th>{header}</th>" for header in headers])
    table_html += "</tr>"

    for row in rows:
        if row.strip():
            cols = row.split(",")
            table_html += "<tr>"
            for col in cols:
                table_html += f"<td>{col.strip()}</td>"
            table_html += "</tr>"
    table_html += "</table>"
    return table_html
