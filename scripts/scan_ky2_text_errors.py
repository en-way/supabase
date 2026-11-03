import json
import glob
import os
import re
import sys
import io

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"
all_exam_files = glob.glob(os.path.join(exams_dir, "*.json"))

ky2_files = []
for fpath in all_exam_files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            title = data.get("title", "")
            if "英语二" in title or "英语（二）" in title or "英语2" in title:
                ky2_files.append((data.get("year", 0), title, fpath, data))
    except Exception as e:
        pass

ky2_files.sort(key=lambda x: x[0])
print(f"Total English 2 exams found: {len(ky2_files)}")
for year, title, fpath, data in ky2_files:
    questions = data.get("questions", [])
    passages = data.get("passages", [])
    print(f"{year} | {title} | Passages: {len(passages)} | Questions: {len(questions)}")
