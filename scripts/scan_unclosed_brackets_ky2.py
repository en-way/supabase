import json
import glob
import os
import re
import sys
import io

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams.json"
exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

with open(exams_file, "r", encoding="utf-8") as f:
    all_exams_meta = json.load(f)

ky2_exams = [e for e in all_exams_meta if e.get("category_id") == "ky2"]
ky2_exams.sort(key=lambda x: x.get("year", 0))

print("=== SCANNING UNCLOSED [A-G] BRACKETS IN KY2 (2010-2025) ===")

unclosed_brackets = []

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        expl = q.get("explanation", "")
        # Pattern: [A-G or ［A-G followed immediately by Chinese char or quote without closing bracket
        for m in re.finditer(r"[\[［]([A-Ga-g])([\u4e00-\u9fa5“‘\"\'\s]{1,4})", expl):
            # check if there's a closing bracket within 2 chars
            full_match = expl[m.start():m.start()+10]
            if not re.match(r"^[\[［][A-Ga-g][\]］]", full_match):
                ctx = expl[max(0, m.start()-15):min(len(expl), m.start()+35)].replace("\n", " ")
                unclosed_brackets.append((year, qnum, m.group(0), ctx))

print(f"Total unclosed [A-G] brackets found: {len(unclosed_brackets)}")
for item in unclosed_brackets:
    print(f"[{item[0]} Q{item[1]}] '{item[2]}' in: ...{item[3]}...")
