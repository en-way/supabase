import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Scanning All Questions for OCR Typos and Irregular Characters in Stems ===")

exam_files = sorted(glob.glob("public/data/exams/*.json"))

suspicious_stems = []

for fpath in exam_files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    title = data["exam"]["title"]
    year = data["exam"]["year"]
    cat = data["exam"]["category_id"]

    for q in data["questions"]:
        so = q.get("sort_order")
        stem = q.get("stem", "")

        # Look for OCR anomalies like single stray letters or odd punctuation inside quotes
        if re.search(r'\b[uU]\s+[a-z]{4,}"', stem): # e.g. u behavioural"
            suspicious_stems.append((year, cat, so, "stray_u_quote", stem))
        if re.search(r'[a-z]+rmarket', stem): # e.g. masrmarket
            suspicious_stems.append((year, cat, so, "typo_market", stem))
        if re.search(r'[a-zA-Z]+[0-9]+[a-zA-Z]+', stem): # e.g. word12word
            suspicious_stems.append((year, cat, so, "digit_in_word", stem))
        if re.search(r'M[a-zA-Z\-]+H', stem): # e.g. Mhigh-income thresholdH
            suspicious_stems.append((year, cat, so, "OCR_quote_MH", stem))
        if "”" in stem and "“" not in stem and '"' not in stem:
            suspicious_stems.append((year, cat, so, "unmatched_right_curly_quote", stem))
        if "“" in stem and "”" not in stem and '"' not in stem:
            suspicious_stems.append((year, cat, so, "unmatched_left_curly_quote", stem))
        if "" in stem:
            suspicious_stems.append((year, cat, so, "replacement_char_in_stem", stem))

print(f"Total suspicious stems: {len(suspicious_stems)}")
for s in suspicious_stems:
    print(f"[{s[0]} {s[1]} Q{s[2]}] {s[3]}: {repr(s[4])}")
