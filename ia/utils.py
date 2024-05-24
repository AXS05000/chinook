import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


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
        max_tokens=150,
    )
    return response["choices"][0]["message"]["content"].strip()
