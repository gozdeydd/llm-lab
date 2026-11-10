import ollama

r = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "Say hello in English."}],
)
print(repr(r["message"]["content"]))