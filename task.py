import json
import sys
from datetime import datetime
from pathlib import Path

FILE = Path("tasks.json")
STAGES = ["coding", "deployed-dev", "dag-running", "validating", "pr-open", "done"]


def load():
    return json.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else {}


def save(tasks):
    FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8")


def show(tasks):
    for tid, t in tasks.items():
        note = t["notes"][-1] if t["notes"] else ""
        print(f'{tid:6} {t["stage"]:13} {t["repo"]:12} {t["branch"]:25} {note}')


tasks = load()
cmd = sys.argv[1] if len(sys.argv) > 1 else "list"

if cmd == "add":  # task.py add T4 gold-repo feature/t4 "aciklama"
    tid, repo, branch, desc = sys.argv[2:6]
    tasks[tid] = {"repo": repo, "branch": branch, "desc": desc,
                  "stage": "coding", "notes": [], "updated": ""}
    tasks[tid]["updated"] = datetime.now().strftime("%H:%M")
    save(tasks)
elif cmd == "set":  # task.py set T2 validating "run_id=manual__02"
    tid, stage = sys.argv[2], sys.argv[3]
    if tid not in tasks:
        raise SystemExit(f"Unknown task: {tid}")
    if stage not in STAGES:
        raise SystemExit(f"Stage must be one of: {STAGES}")
    tasks[tid]["stage"] = stage
    if len(sys.argv) > 4:
        tasks[tid]["notes"].append(sys.argv[4])
    tasks[tid]["updated"] = datetime.now().strftime("%H:%M")
    save(tasks)

show(tasks)