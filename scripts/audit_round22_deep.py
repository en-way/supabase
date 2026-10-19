import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Deep Forensic Audit for Round 22 ===")

exam_files = sorted(glob.glob('public/data/exams/*.json'))

# 1. Check for suspicious apostrophe OCR corruptions in options and stems
# e.g., '5' used as apostrophe (like 'patients5', 'one5s'), '*' used as apostrophe (like 'one*s', 'researchers*')
ocr_quote_anomalies = []

# 2. Check for abnormal explanation lengths (either extremely bloated > 2000 chars or extremely short < 120 chars)
bloated_explanations = []
short_explanations = []

# 3. Check for leaked chapter markers or stray question stems inside explanations
explanation_leaks = []

# 4. Check for unclosed brackets or mismatched option keys in options
option_formatting_issues = []

for fpath in exam_files:
    data = json.load(open(fpath, encoding='utf-8'))
    t = data['exam'].get('title', '')
    yr = data['exam'].get('year')
    cat = data['exam'].get('category_id')
    
    for q in data.get('questions', []):
        so = q.get('sort_order')
        stem = q.get('stem', '')
        expl = q.get('explanation', '')
        opts = q.get('options', [])
        
        # 1. Option texts
        for o in opts:
            ot = o.get('text', '')
            k = o.get('key', '')
            
            # Check for digit '5' or '*' used instead of apostrophe
            m_quote = re.findall(r'\b[a-zA-Z]+[5\*][a-zA-Z]*\b', ot)
            if m_quote:
                ocr_quote_anomalies.append((yr, cat, so, k, m_quote, ot))
                
            # Check for space before 's (e.g. "word s ")
            if re.search(r'\b[a-zA-Z]+\s+s\b', ot):
                ocr_quote_anomalies.append((yr, cat, so, k, "space_s", ot))
                
        # 2. Stem texts
        m_stem_quote = re.findall(r'\b[a-zA-Z]+[5\*][a-zA-Z]*\b', stem)
        if m_stem_quote:
            ocr_quote_anomalies.append((yr, cat, so, 'STEM', m_stem_quote, stem))
            
        # 3. Explanation length
        l_exp = len(expl)
        if l_exp > 2200:
            bloated_explanations.append((yr, cat, so, l_exp, expl[:80]))
        elif l_exp < 100:
            short_explanations.append((yr, cat, so, l_exp, expl))
            
        # 4. Leaks inside explanation (e.g., another question number at beginning of line)
        lines = expl.splitlines()
        for idx, line in enumerate(lines):
            line_s = line.strip()
            # check for next question marker like "32. " inside Q31
            m_q = re.match(r'^([1-4]\d)\.\s+[A-Za-z\u4e00-\u9fa5]', line_s)
            if m_q and int(m_q.group(1)) != so:
                explanation_leaks.append((yr, cat, so, m_q.group(1), line_s[:60]))

print(f"\n1. OCR Quote Corruptions Found ({len(ocr_quote_anomalies)}):")
for item in ocr_quote_anomalies:
    print(f"  - {item[0]} {item[1]} Q{item[2]} [{item[3]}]: pattern {item[4]} in: {repr(item[5])}")

print(f"\n2. Bloated Explanations > 2200 chars ({len(bloated_explanations)}):")
for item in bloated_explanations:
    print(f"  - {item[0]} {item[1]} Q{item[2]}: length {item[3]} chars | Preview: {item[4]}...")

print(f"\n3. Short Explanations < 100 chars ({len(short_explanations)}):")
for item in short_explanations:
    print(f"  - {item[0]} {item[1]} Q{item[2]}: length {item[3]} chars | Content: {repr(item[4])}")

print(f"\n4. Explanation Bleedings / Leaked Question Numbers ({len(explanation_leaks)}):")
for item in explanation_leaks:
    print(f"  - {item[0]} {item[1]} Q{item[2]}: leaked Q{item[3]} -> {item[4]}")
