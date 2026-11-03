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

print("=== INSPECTING SYMBOLS IN KY2 ===")
for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam_data = json.load(f)
    
    # Check passages
    for p in exam_data.get("passages", []):
        content = p.get("content", "")
        for m in re.finditer(r"[£§¤¥©®±×÷µ¶·•\^~_|\\]", content):
            start = max(0, m.start() - 25)
            end = min(len(content), m.end() + 25)
            snippet = content[start:end].replace("\n", " ")
            print(f"[Passage {year} {p.get('title')[:30]}] char '{m.group()}': ...{snippet}...")
            
    # Check questions
    for q in exam_data.get("questions", []):
        stem = q.get("stem", "")
        opts = " ".join(o.get("text", "") for o in q.get("options", []) if isinstance(o, dict))
        expl = q.get("explanation", "")
        
        # Check stem
        for m in re.finditer(r"[£§¤¥©®±×÷µ¶·•\^|\\]", stem):
            start = max(0, m.start() - 25)
            end = min(len(stem), m.end() + 25)
            snippet = stem[start:end].replace("\n", " ")
            print(f"[Q Stem {year} Q{q.get('question_number')}] char '{m.group()}': ...{snippet}...")
            
        # Check options
        for m in re.finditer(r"[£§¤¥©®±×÷µ¶·•\^|\\]", opts):
            start = max(0, m.start() - 25)
            end = min(len(opts), m.end() + 25)
            snippet = opts[start:end].replace("\n", " ")
            print(f"[Option {year} Q{q.get('question_number')}] char '{m.group()}': ...{snippet}...")

        # Check expl
        for m in re.finditer(r"[£§¤¥©®±×÷µ¶\^|\\]", expl):
            start = max(0, m.start() - 25)
            end = min(len(expl), m.end() + 25)
            snippet = expl[start:end].replace("\n", " ")
            print(f"[Expl {year} Q{q.get('question_number')}] char '{m.group()}': ...{snippet}...")
