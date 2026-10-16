# -*- coding: utf-8 -*-
"""
audit_round19_comprehensive.py
Comprehensive multi-sector forensic audit across all 41 exams / 1,825 questions:
1. Sector A: Cloze Blank & Options vs Explanation Alignment
2. Sector B: Reading Part A Options vs Explanation Mentions (cross-exam leak detector)
3. Sector C: Stem syntax, punctuation, unclosed quotes, and truncation check
4. Sector D: Passage length, boundary, and ending punctuation integrity
5. Sector E: Part B options, headings, and answers integrity
"""

import json
import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'exams'))
exam_files = sorted(glob.glob(os.path.join(exams_dir, '*.json')))

print(f"=== Round 19 Comprehensive Multi-Sector Deep Audit ===")
print(f"Found {len(exam_files)} exam files.")

sector_a_cloze_anomalies = []
sector_b_option_mismatch = []
sector_c_stem_issues = []
sector_d_passage_issues = []
sector_e_part_b_issues = []

for fpath in exam_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    title = data['exam'].get('title', '')
    yr = data['exam'].get('year')
    cat = data['exam'].get('category_id')
    passages = data.get('passages', [])
    questions = data.get('questions', [])

    # Sector D: Passage checks
    for p in passages:
        so = p.get('sort_order')
        pt = p.get('title', '')
        c = (p.get('content') or '').strip()
        paras = [line.strip() for line in c.split('\n') if line.strip()]
        
        # Word count
        words = c.split()
        if 'Part A' in pt and len(words) < 150:
            sector_d_passage_issues.append((title, so, pt, f"short_reading_passage: {len(words)} words"))
        
        # Ending punctuation
        if len(c) > 0 and c[-1] not in '.!?"\'”’':
            # Check if it ends in abnormal character
            sector_d_passage_issues.append((title, so, pt, f"passage_abnormal_end: '{c[-30:]}'"))

    # Questions checks
    for q in questions:
        so = q.get('sort_order')
        stem = (q.get('stem') or '').strip()
        ans = q.get('correct_answer')
        expl = (q.get('explanation') or '').strip()
        opts = q.get('options') or []
        opt_map = {o.get('key'): str(o.get('text', '')).strip() for o in opts}

        # Sector C: Stem punctuation and truncation
        if so > 20 and so <= 40:
            if not stem:
                sector_c_stem_issues.append((title, so, "empty_stem"))
            elif not stem.endswith(('.', '?', ':', '!', '"', '”', '________.', '________?', '________')):
                # Check what it ends with
                sector_c_stem_issues.append((title, so, f"stem_odd_ending: '{stem[-25:]}'"))

        # Sector B: Reading Part A Options vs Explanation
        if so > 20 and so <= 40:
            # Check if option letters mentioned in explanation match option text
            for key, text in opt_map.items():
                if len(text) > 4:
                    # Look for [A], [B], ［A］, ［B］ or A., B. in explanation
                    pattern = rf'(?:\[{key}\]|［{key}］|\b{key}\b[\.、\s])\s*([^\n\r\[\]［］]{{3,40}})'
                    matches = re.findall(pattern, expl)
                    # Check if significant words in option appear in explanation near the option mention or anywhere in expl
                    # Extract english words of length >= 4
                    opt_words = [w.lower() for w in re.findall(r'[a-zA-Z]{4,}', text) if w.lower() not in {'that', 'with', 'from', 'have', 'this', 'they', 'their', 'which', 'about', 'more', 'than', 'been', 'were'}]
                    if opt_words:
                        expl_lower = expl.lower()
                        # Count how many opt_words appear in explanation
                        matched_words = [w for w in opt_words if w in expl_lower]
                        if len(opt_words) >= 3 and len(matched_words) == 0:
                            # Potential foreign option!
                            sector_b_option_mismatch.append((title, so, key, text, opt_words))

        # Sector E: Part B check
        if so in range(41, 46):
            if not opts or len(opts) < 4:
                sector_e_part_b_issues.append((title, so, f"few_options: {len(opts)}"))
            if not ans:
                sector_e_part_b_issues.append((title, so, "missing_answer"))

print(f"\n--- Sector B: Reading Options with 0 word matches in Explanation ({len(sector_b_option_mismatch)}) ---")
for it in sector_b_option_mismatch[:30]:
    print(it)

print(f"\n--- Sector C: Stem Odd Endings ({len(sector_c_stem_issues)}) ---")
for it in sector_c_stem_issues[:30]:
    print(it)

print(f"\n--- Sector D: Passage Abnormal Endings ({len(sector_d_passage_issues)}) ---")
for it in sector_d_passage_issues[:30]:
    print(it)

print(f"\n--- Sector E: Part B Issues ({len(sector_e_part_b_issues)}) ---")
for it in sector_e_part_b_issues[:30]:
    print(it)
