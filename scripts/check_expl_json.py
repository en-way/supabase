import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scripts/expl_2004.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for q in ["1", "2", "6", "10", "20"]:
    print(f"=== Q{q} ===")
    print(d[q][:350])
