import ollama

try:
    ollama.chat(model="yanlis-model", messages=[{"role": "user", "content": "hi"}])
except ollama.ResponseError as e:
    print(f"Model problem: {e}")
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")
