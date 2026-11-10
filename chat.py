import json
from pathlib import Path

import ollama

MODEL = "llama3.2:3b"
HISTORY_FILE = Path("history.json")

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a Python teacher. Only answer the user's question. "
        "Reply in English, in at most 5 sentences, with one short code example. "
        "Do not ask follow-up questions."
    ),
}

OPTIONS = {"temperature": 0.3, "repeat_penalty": 1.15, "num_predict": 400}


def save_history(messages):
    HISTORY_FILE.write_text(
        json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if HISTORY_FILE.exists():
    messages = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
else:
    messages = [SYSTEM_MESSAGE]

print(f"Chatbot ready ({MODEL}). Type 'exit' to quit, '/reset' to clear history.\n")


def save_history(messages):
    HISTORY_FILE.write_text(
        json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if HISTORY_FILE.exists():
    messages = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
else:
    messages = [SYSTEM_MESSAGE]

print(f"Chatbot ready ({MODEL}). Type 'exit' to quit, '/reset' to clear history.\n")

try:
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Bye!")
            break
        if user_input == "/reset":
            messages = [SYSTEM_MESSAGE]
            save_history(messages)
            print("History cleared.\n")
            continue

        messages.append({"role": "user", "content": user_input})

        print("Bot: ", end="", flush=True)
        reply = ""
        stream = ollama.chat(
            model=MODEL, 
            messages=messages, 
            stream=True
            )
        
        for chunk in stream:
            piece = chunk["message"]["content"]
            print(piece, end="", flush=True)
            reply += piece
        print("\n")

        messages.append({"role": "assistant", "content": reply})
        save_history(messages)
except (KeyboardInterrupt, EOFError):
    print("\nBye!")