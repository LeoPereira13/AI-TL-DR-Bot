from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

def summarize(text):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Resuma o texto abaixo de forma objetiva:"},
            {"role": "user", "content": text}
        ],
        temperature=0.5,
        max_tokens=200
    )
    return response.choices[0].message.content

import sys
texto = sys.argv[1]
print(summarize(texto))
