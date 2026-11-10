import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
    {"role": "system", "content": "Sen sabırlı bir Python öğretmenisin. Kısa ve örnekle cevap ver."},
    {"role": "user", "content": "Dictionary nedir?"},
    ],  
)
soru = input("sorun: ")
stream = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": soru}],
    stream=True,
)
for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
print()
#int(response["message"]["content"])