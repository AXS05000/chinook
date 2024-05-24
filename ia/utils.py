import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def get_chat_response(prompt, context=""):
    if not context:
        context = "No relevant information found in the database."
    if not prompt:
        prompt = "No question provided."

    # Verifica se o usuário pediu uma tabela ou um relatório
    if "tabela" in prompt.lower() or "relatório" in prompt.lower():
        return "Você pode baixar o relatório em Excel clicando no botão 'Download Relatório Excel'."

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
