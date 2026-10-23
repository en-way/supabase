# -*- coding: utf-8 -*-
"""
apply_final_2013_ky1_golden_calibration.py
Integrates all historical high-precision calibrated explanations (Round 27, 28, 36, 37)
and fixes o£/th&r into 2013 ky1 exam JSON.
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Applying Final Golden Alignment for 2013 ky1 ===")

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Load explanations from calibrate_round37.py (Q21-Q25)
c37_path = r'd:\A16pro\Aing\antigravity\supabase\scripts\calibrate_round37.py'
import importlib.util
spec37 = importlib.util.spec_from_file_location("c37", c37_path)
mod37 = importlib.util.module_from_spec(spec37)
spec37.loader.exec_module(mod37)

q21_expl = mod37.text_2013_q21
q22_expl = mod37.text_2013_q22
q23_expl = mod37.text_2013_q23
q24_expl = mod37.text_2013_q24
q25_expl = mod37.text_2013_q25

# 2. Extract Q26-Q35 from calibrate_round27.py
with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\calibrate_round27.py', 'r', encoding='utf-8') as f:
    c27_text = f.read()

r27_expls = {}
for qn in range(26, 36):
    m = re.search(rf'if so == {qn}:.*?q\["explanation"\] = \((.*?)\)\n', c27_text, re.DOTALL)
    if m:
        raw_code = m.group(1)
        # eval the string concatenation
        val = eval(raw_code)
        r27_expls[qn] = val

# 3. Extract Q20 from calibrate_round28.py
with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\calibrate_round28.py', 'r', encoding='utf-8') as f:
    c28_text = f.read()

m20 = re.search(r'so == 20:.*?q\["explanation"\] = \((.*?)\)\n', c28_text, re.DOTALL)
q20_expl = eval(m20.group(1)) if m20 else None

# 4. Extract Q7 from calibrate_round36.py
with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\calibrate_round36.py', 'r', encoding='utf-8') as f:
    c36_text = f.read()

m7 = re.search(r'so == 7:.*?q\["explanation"\] = \((.*?)\)\n', c36_text, re.DOTALL)
q7_expl = eval(m7.group(1)) if m7 else None

# 5. Apply to questions
for q in exam_data["questions"]:
    so = q.get("sort_order")
    if so == 7 and q7_expl:
        q["explanation"] = q7_expl
    elif so == 20 and q20_expl:
        q["explanation"] = q20_expl
    elif so == 21:
        q["explanation"] = q21_expl
    elif so == 22:
        q["explanation"] = q22_expl
    elif so == 23:
        q["explanation"] = q23_expl
    elif so == 24:
        q["explanation"] = q24_expl
    elif so == 25:
        q["explanation"] = q25_expl
    elif so in r27_expls:
        q["explanation"] = r27_expls[so]
    
    # Fix option characters like o£ -> of, th&r -> their
    for opt in q.get("options", []):
        opt["text"] = opt["text"].replace("o£", "of").replace("th&r", "their")

# Also check passage content for o£ and th&r
for p in exam_data.get("passages", []):
    p["content"] = p["content"].replace("o£", "of").replace("th&r", "their")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Saved updated JSON successfully!")
