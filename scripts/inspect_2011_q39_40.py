import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d.get("questions", []):
    if q.get("sort_order") in [39, 40]:
        print(f"=== Q{q.get('sort_order')} ===")
        print("Stem:", q.get('stem'))
        print("Options:", q.get('options'))
        print("Ans:", q.get('correct_answer'))
        print("Expl:", str(q.get('explanation'))[:300])
        print()
