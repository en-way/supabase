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

print("=== CHECKING [E] / [E］IN Q1-Q40 OF KY2 (WHERE ONLY A-D EXIST) ===")

e_in_cloze_or_reading = []

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        if 1 <= qnum <= 40:
            expl = q.get("explanation", "")
            # Look for [E] or ［E］ or [E / ［E where it's introducing an option (not e.g., or [English])
            matches = re.findall(r"(?:[\[［]E[\]］]\s*[a-zA-Z\u4e00-\u9fa5]+|[\[［]E[\]］]|正确答案为\s*E|选\s*E\b)", expl)
            if matches:
                # print context
                for m in matches:
                    idx = expl.find(m)
                    ctx = expl[max(0, idx-20):min(len(expl), idx+40)].replace("\n", " ")
                    e_in_cloze_or_reading.append((year, qnum, m, ctx))

print(f"Total [E] anomalies found in Q1-Q40: {len(e_in_cloze_or_reading)}")
for it in e_in_cloze_or_reading:
    print(f"[{it[0]} Q{it[1]}] {it[2]} in: ...{it[3]}...")
