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

print("=== SCANNING STEMS & OPTIONS FOR UNUSUAL PATTERNS IN KY2 ===")

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        stem = q.get("stem", "")
        opts = q.get("options", [])
        
        # Check stem
        weird_case = re.findall(r"\b[a-z]+[A-Z]+[a-z]*\b", stem)
        if weird_case:
            filtered = [w for w in weird_case if w not in ("iPad", "iPhone", "eBay", "iMac", "MacBook", "iPod", "TikTok", "YouTube", "PayPal", "LinkedIn", "Parkrun", "WhatsApp", "GitHub", "GenZ")]
            if filtered:
                print(f"[{year} Q{qnum} stem] Weird case words: {filtered}")
                
        # Check spaced punctuation in stem
        spaced_punct = re.findall(r"\b\w+\s+[,.?!;:]\s+", stem)
        if spaced_punct:
            print(f"[{year} Q{qnum} stem] Spaced punctuation: {spaced_punct}")
            
        # Check options
        for opt in opts:
            otext = opt.get("text", "")
            weird_case_opt = re.findall(r"\b[a-z]+[A-Z]+[a-z]*\b", otext)
            if weird_case_opt:
                filtered_opt = [w for w in weird_case_opt if w not in ("iPad", "iPhone", "eBay", "iMac", "MacBook", "iPod", "TikTok", "YouTube", "PayPal", "LinkedIn", "Parkrun", "WhatsApp", "GitHub", "GenZ")]
                if filtered_opt:
                    print(f"[{year} Q{qnum} opt {opt.get('key')}] Weird case words: {filtered_opt}")
            spaced_punct_opt = re.findall(r"\b\w+\s+[,.?!;:]\s+", otext)
            if spaced_punct_opt:
                print(f"[{year} Q{qnum} opt {opt.get('key')}] Spaced punctuation: {spaced_punct_opt}")
