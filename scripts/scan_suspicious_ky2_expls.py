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

ky2_exams = {e.get("year"): e.get("id") for e in all_exams_meta if e.get("category_id") == "ky2"}

# Let's inspect 2020, 2021, 2022 explanations
for year in [2020, 2021, 2022]:
    eid = ky2_exams.get(year)
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n{'='*30} YEAR {year} EXPLANATION SAMPLES {'='*30}")
    for q in data["questions"]:
        qnum = q["question_number"]
        expl = q.get("explanation", "")
        # look for vocabulary notes block
        if "词汇注释" in expl or "分析" in expl or "［" in expl or "[" in expl:
            # print any suspicious substrings
            suspicious = re.findall(r"(?:\[[^\]]{10,}\]|［[^］]{10,}］|[^\u4e00-\u9fa5a-zA-Z0-9\s，。、！？；：“”‘’（）《》〈〉—…\-·•\.\,\?\!\;\'\"\:\(\)\[\]［］]{1,})", expl)
            if suspicious:
                print(f"[Q{qnum}] Suspicious: {suspicious[:5]}")
