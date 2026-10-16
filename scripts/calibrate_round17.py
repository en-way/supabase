# -*- coding: utf-8 -*-
"""
calibrate_round17.py
Round 17 Calibration:
1. Calibrate all 20 Cloze questions for 2005 ky1 (options, correct answers, explanations from Yellow Book)
2. Calibrate 2005 ky1 Q22: restore complete authentic stem and fix OCR in options
3. Calibrate 2003 ky1 Q23: restore complete authentic stem
4. Calibrate 2006 ky1 Q28: restore complete authentic stem and restore Option A from truncation ('Stratford can' -> 'Stratford cannot afford the expansion projects')
5. Calibrate 2006 ky1 Q33: restore complete authentic stem and fix OCR in options ('out of elate' -> 'out of date', 'fi shing' -> 'fishing', etc.)
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import authentic 2005 cloze data
from parse_2005_cloze import AUTHENTIC_2005_CLOZE

# 1. Calibrate 2005 ky1
f_2005 = 'public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json'
d_2005 = json.load(open(f_2005, encoding='utf-8'))
for q in d_2005['questions']:
    so = q['sort_order']
    if 1 <= so <= 20:
        data = AUTHENTIC_2005_CLOZE.get(so)
        if data:
            q['options'] = data['options']
            q['correct_answer'] = data['answer']
            q['answer'] = data['answer']
            q['explanation'] = data['explanation']
            print(f"Calibrated 2005 ky1 Cloze Q{so:02d} (Ans: {data['answer']})")
    elif so == 22:
        q['stem'] = 'The statement "it is all too monkey" (Last line, Paragraph 1) implies that ________.'
        q['options'] = [
            {"key": "A", "text": "monkeys are also outraged by slack rivals", "value": "A"},
            {"key": "B", "text": "resenting unfairness is also monkeys' nature", "value": "B"},
            {"key": "C", "text": "monkeys, like humans, tend to be jealous of each other", "value": "C"},
            {"key": "D", "text": "no animals other than monkeys can develop such emotions", "value": "D"}
        ]
        q['correct_answer'] = "B"
        q['answer'] = "B"
        print("Calibrated 2005 ky1 Q22 stem and options")

json.dump(d_2005, open(f_2005, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2. Calibrate 2003 ky1 Q23
f_2003 = 'public/data/exams/91ff038a-e3f9-5b6d-82c5-1328735be1d1.json'
d_2003 = json.load(open(f_2003, encoding='utf-8'))
for q in d_2003['questions']:
    if q['sort_order'] == 23:
        q['stem'] = 'The phrase "making the biggest splash" (Line 1, Paragraph 3) most probably means ________.'
        print("Calibrated 2003 ky1 Q23 stem")
json.dump(d_2003, open(f_2003, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 3. Calibrate 2006 ky1 Q28 and Q33
f_2006 = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'
d_2006 = json.load(open(f_2006, encoding='utf-8'))
for q in d_2006['questions']:
    so = q['sort_order']
    if so == 28:
        q['stem'] = 'By saying "Stratford cries poor traditionally" (Line 2, Paragraph 4), the author implies that ________.'
        q['options'] = [
            {"key": "A", "text": "Stratford cannot afford the expansion projects", "value": "A"},
            {"key": "B", "text": "Stratford has long been in financial difficulties", "value": "B"},
            {"key": "C", "text": "the town is not really short of money", "value": "C"},
            {"key": "D", "text": "the townsfolk used to be poorly paid", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        print("Calibrated 2006 ky1 Q28 stem and options (restored Option A)")
    elif so == 33:
        q['stem'] = 'By saying "these figures are conservative" (Line 1, Paragraph 3), Dr. Worm means that ________.'
        q['options'] = [
            {"key": "A", "text": "fishing technology has improved rapidly", "value": "A"},
            {"key": "B", "text": "the catch-sizes are actually smaller than recorded", "value": "B"},
            {"key": "C", "text": "the marine biomass has suffered a greater loss", "value": "C"},
            {"key": "D", "text": "the data collected so far are out of date", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        print("Calibrated 2006 ky1 Q33 stem and options (fixed out of date)")

json.dump(d_2006, open(f_2006, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("\n=== Round 17 Calibrations Successfully Applied to Local JSON! ===")
