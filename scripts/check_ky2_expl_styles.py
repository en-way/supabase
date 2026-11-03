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

print("=== CHECKING EXPLANATION STYLES & PATTERNS IN KY2 ===")

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    questions = exam.get("questions", [])
    expl_lengths = [len(q.get("explanation", "")) for q in questions]
    avg_len = sum(expl_lengths) / len(expl_lengths) if expl_lengths else 0
    min_len = min(expl_lengths) if expl_lengths else 0
    max_len = max(expl_lengths) if expl_lengths else 0
    
    # Sample Q1, Q21, Q41
    q1_expl = questions[0].get("explanation", "") if len(questions) > 0 else ""
    q21_expl = questions[20].get("explanation", "") if len(questions) > 20 else ""
    q41_expl = questions[40].get("explanation", "") if len(questions) > 40 else ""
    
    print(f"\n[{year} KY2] Questions: {len(questions)} | Expl Len: min={min_len}, avg={avg_len:.0f}, max={max_len}")
    print(f"   Q1 (Cloze) snippet: {q1_expl[:80].replace(chr(10), ' ')}...")
    print(f"   Q21 (Reading) snippet: {q21_expl[:80].replace(chr(10), ' ')}...")
    print(f"   Q41 (Part B) snippet: {q41_expl[:80].replace(chr(10), ' ')}...")
