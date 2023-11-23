from openai import OpenAI

openai = OpenAI(api_key="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")

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are professional joke writer."},
        {"role": "user", "content": "Writa a joke about my teacher."},
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)
