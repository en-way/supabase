import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Scanning All 1,825 Question Stems for Truncation or Incomplete Text ===")

exam_files = sorted(glob.glob("public/data/exams/*.json"))

truncated_stems = []

for fpath in exam_files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    title = data["exam"]["title"]
    for q in data["questions"]:
        so = q.get("sort_order")
        stem = (q.get("stem") or "").strip()
        
        # Cloze questions (1-20) standard stem
        if so <= 20:
            continue
            
        # Check if stem ends with hyphen, slash, or dangling word
        if stem.endswith("-") or stem.endswith("—") or stem.endswith("/"):
            truncated_stems.append((title, so, "ends_with_hyphen", stem))
        elif len(stem) < 25 and not stem.startswith("Choose"):
            truncated_stems.append((title, so, "abnormally_short", stem))
        elif re.search(r'\b(?:in|on|at|by|with|for|to|of|about|that|which|who|whom|whose|from|as|than|into|through|between|among|against|during|without|before|after|under|within|along|across|behind|beyond|up|down|off|over)\s*$', stem, re.IGNORECASE):
            # Check if it has an underline like _____
            if "_" not in stem and "..." not in stem and "…" not in stem:
                truncated_stems.append((title, so, "dangling_preposition_no_blank", stem))

print(f"Total potentially truncated stems found: {len(truncated_stems)}")
for t in truncated_stems:
    print(f"[{t[0]} Q{t[1]}] Issue: {t[2]}")
    print(f"   Stem: {repr(t[3])}")
