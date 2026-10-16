import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("public/data/exams/4ebd819e-c832-5890-9048-ba16040a5607.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d.get("questions", []):
    so = q.get("sort_order")
    if 21 <= so <= 25:
        print(f"=== 2021 ky2 Q{so} ===")
        print(q.get("explanation"))
