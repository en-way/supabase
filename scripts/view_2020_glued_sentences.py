import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

fpath = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json"
with open(fpath, "r", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questions"]:
    qnum = q["question_number"]
    expl = q.get("explanation", "")
    long_words = re.findall(r"\b[a-zA-Z]{18,}\b", expl)
    if long_words:
        print(f"=== 2020 Q{qnum} ===")
        # find sentences containing these long words
        for lw in long_words:
            idx = expl.find(lw)
            start = max(0, idx - 40)
            end = min(len(expl), idx + len(lw) + 40)
            print(f"   [{lw}]: ...{expl[start:end].replace(chr(10), ' ')}...")
