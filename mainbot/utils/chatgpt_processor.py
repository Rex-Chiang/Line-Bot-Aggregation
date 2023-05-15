import openai
from django.conf import settings

def generate_response(prompt):
    messages = [
        {
            "role": "system",
            "content": prompt
        }
    ]

    response = openai.ChatCompletion.create(
        model=settings.CHATGPT_MODEL,
        messages=messages,
        max_tokens=200
    )

    return response["choices"][0]["message"]["content"]