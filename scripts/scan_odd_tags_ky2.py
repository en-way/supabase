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

print("=== DEEP SCAN OF OPTION KEYS IN EXPLANATIONS OF Q1-Q40 (KY2) ===")

odd_option_tags = []

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
            # Find bracketed letters other than A, B, C, D
            found_tags = re.findall(r"[\[［]([A-Za-z0-9_]{1,3})[\]］]", expl)
            for tag in found_tags:
                if tag not in ("A", "B", "C", "D", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                               "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                               "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                               "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                               "考点提炼", "解题思路", "精准定位", "命题解密", "考点精析", "错项排除", "答案", "精解"):
                    idx = expl.find(f"[{tag}]") if f"[{tag}]" in expl else expl.find(f"［{tag}］")
                    ctx = expl[max(0, idx-20):min(len(expl), idx+40)].replace("\n", " ")
                    odd_option_tags.append((year, qnum, tag, ctx))

print(f"Total odd tags in Q1-Q40: {len(odd_option_tags)}")
for it in odd_option_tags:
    print(f"[{it[0]} Q{it[1]}] tag: '{it[2]}' in: ...{it[3]}...")
