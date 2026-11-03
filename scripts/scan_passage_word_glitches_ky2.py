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

print("=== SCANNING WORDS IN KY2 PASSAGES FOR UNUSUAL PATTERNS ===")

# Look for patterns that are likely OCR errors:
# - words with digits inside: e.g. "th1s", "0f"
# - words with weird mixed case: e.g. "tHe", "wOrld", "THis" (not acronyms)
# - words ending with hyphen that should be joined or separated
# - non-ASCII characters in English text (curly quotes are fine, but check for weird ones)
# - doubled punctuation or missing space after period

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
    
    for p in exam.get("passages", []):
        p_title = p.get("title", "")
        content = p.get("content", "")
        
        # Mixed case inside lowercase word like "tHis" or "exAmple"
        weird_case = re.findall(r"\b[a-z]+[A-Z]+[a-z]*\b", content)
        if weird_case:
            # ignore known names or brands like iPad, iPhone, eBay, etc.
            filtered_case = [w for w in weird_case if w not in ("iPad", "iPhone", "eBay", "iMac", "MacBook", "iPod", "TikTok", "YouTube", "PayPal", "LinkedIn", "MySpace", "BioMed", "Parkrun", "WhatsApp", "GitHub", "GenZ")]
            if filtered_case:
                print(f"[{year} {p_title[:25]}] Weird case words: {filtered_case}")
                
        # Word with digits
        digit_words = re.findall(r"\b[a-zA-Z]+\d+[a-zA-Z]+\b", content)
        if digit_words:
            print(f"[{year} {p_title[:25]}] Digit-mixed words: {digit_words}")
            
        # Punctuation spacing anomalies: comma or period preceded by space e.g. "word ," or "word ."
        spaced_punct = re.findall(r"\b\w+\s+[,.?!;:]\s+", content)
        if spaced_punct:
            print(f"[{year} {p_title[:25]}] Spaced punctuation: {spaced_punct}")
