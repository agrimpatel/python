from openai import OpenAI
#pip install openai
#if you saved the key under a different environment variable name,you can do something like:
client = OpenAI(
    api_key="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"
)

completion = client.chat.completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role":"user","content":"compose a poem that explain the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)