import openai

def generate_response(prompt):
    messages = [
        {
            "role": "system",
            "content": prompt
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200
    )

    return response["choices"][0]["message"]["content"]