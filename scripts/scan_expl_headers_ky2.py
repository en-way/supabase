import json
import glob
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams.json"
exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

with open(exams_file, "r", encoding="utf-8") as f:
    all_exams_meta = json.load(f)

ky2_exams = [e for e in all_exams_meta if e.get("category_id") == "ky2"]
ky2_exams.sort(key=lambda x: x.get("year", 0))

print("=== SCANNING EXPLANATION STARTS & HEADERS IN KY2 ===")

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        expl = q.get("explanation", "").strip()
        first_line = expl.split("\n")[0] if expl else ""
        
        # Check for weird headers like "1&", "41. [答案]", or strange numbers
        if re.search(r"^\d+[\&§\*\@\^]", first_line):
            print(f"[{year} Q{qnum}] Suspicious start: {first_line[:60]}")
        elif re.search(r"^\d+\.\s*\[[A-Ga-g]\]", first_line) and not first_line.startswith(f"{qnum}."):
            print(f"[{year} Q{qnum}] Number mismatch in start: {first_line[:60]}")
