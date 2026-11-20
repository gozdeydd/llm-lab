import json
from pathlib import Path

import ollama

MODEL = "qwen2.5:7b"


def get_tasks(stage: str = "") -> str:
    """Return tasks as JSON, optionally filtered by stage."""
    tasks = json.loads(Path("tasks.json").read_text(encoding="utf-8"))
    if stage:
        tasks = {k: v for k, v in tasks.items() if v["stage"] == stage}
    return json.dumps(tasks, ensure_ascii=False)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_tasks",
            "description": "List the user's tasks. Stages: coding, deployed-dev, dag-running, validating, pr-open, done.",
            "parameters": {
                "type": "object",
                "properties": {
                    "stage": {
                        "type": "string",
                        "description": "Optional stage filter. Empty means all tasks.",
                    }
                },
            },
        },
    }
]

AVAILABLE = {"get_tasks": get_tasks}

messages = [
    {
        "role": "system",
        "content": "You are an assistant for a data engineer. Use tools to answer questions about tasks. Never invent tasks.",
    },
    {"role": "user", "content": input("Question: ")},
]

for _ in range(5):  # sonsuz döngüye karşı koruma
    response = ollama.chat(model=MODEL, messages=messages, tools=TOOLS)
    msg = response["message"]
    messages.append(msg)

    if not msg.get("tool_calls"):
        print("\nAnswer:", msg["content"])
        break

    for call in msg["tool_calls"]:
        name = call["function"]["name"]
        args = call["function"]["arguments"]
        print(f"[tool call] {name}({args})")
        result = AVAILABLE[name](**args)
        messages.append({"role": "tool", "content": result, "name": name})