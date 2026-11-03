import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

fpath = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json"
with open(fpath, "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d["questions"]:
    expl = q.get("explanation", "")
    if "词汇注释" in expl:
        print(f"=== 2020 Q{q.get('question_number')} VOCAB ===")
        idx = expl.find("词汇注释")
        print(expl[idx:idx+400])
