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

print("=== SCANNING MIXED BRACKETS IN KY2 (2010-2025) ===")

mixed_brackets = []

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    # Passages
    for p in exam.get("passages", []):
        content = p.get("content", "")
        for m in re.finditer(r"\[[^\]\n]{1,20}］|［[^］\n]{1,20}\]", content):
            mixed_brackets.append((year, p.get("title")[:20], "passage", m.group(0)))
            
    # Questions
    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        stem = q.get("stem", "")
        expl = q.get("explanation", "")
        opts = [o.get("text", "") for o in q.get("options", []) if isinstance(o, dict)]
        
        for m in re.finditer(r"\[[^\]\n]{1,20}］|［[^］\n]{1,20}\]", stem):
            mixed_brackets.append((year, f"Q{qnum}", "stem", m.group(0)))
            
        for opt in opts:
            for m in re.finditer(r"\[[^\]\n]{1,20}］|［[^］\n]{1,20}\]", opt):
                mixed_brackets.append((year, f"Q{qnum}", "option", m.group(0)))
                
        for m in re.finditer(r"\[[^\]\n]{1,20}］|［[^］\n]{1,20}\]", expl):
            mixed_brackets.append((year, f"Q{qnum}", "expl", m.group(0)))

print(f"Total mixed brackets found: {len(mixed_brackets)}")
for it in mixed_brackets[:30]:
    print(f"[{it[0]} {it[1]}] {it[2]}: {it[3]}")
if len(mixed_brackets) > 30:
    print(f"... and {len(mixed_brackets)-30} more")
