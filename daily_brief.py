import json
from pathlib import Path

import ollama

tasks = json.loads(Path("tasks.json").read_text(encoding="utf-8"))
open_tasks = {k: v for k, v in tasks.items() if v["stage"] != "done"}

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[
        {"role": "system", "content": "You are a brief assistant for a data engineer. Summarize open tasks in at most 6 lines. Highlight tasks that wait on the engineer (validating, pr-open). Do not invent anything."},
        {"role": "user", "content": json.dumps(open_tasks, ensure_ascii=False)},
    ],
    options={"temperature": 0.2},
)

summary = response["message"]["content"]
Path("brief.md").write_text(summary, encoding="utf-8")
print(summary)