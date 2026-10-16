import os
import json

data_dir = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams'

def load_exam(cat, yr):
    for f in os.listdir(data_dir):
        if not f.endswith('.json'):
            continue
        fp = os.path.join(data_dir, f)
        with open(fp, 'r', encoding='utf-8') as fp_in:
            d = json.load(fp_in)
        exam = d.get('exam', d)
        if exam.get('category_id') == cat and exam.get('year') == yr:
            return f, d
    return None, None

print("=== CHECKING 2021 ky2 ===")
f21, d21 = load_exam('ky2', 2021)
if d21:
    print(f"File: {f21}")
    for q in d21['questions']:
        if q['sort_order'] in [9, 21, 23, 24, 25, 26, 27, 29, 30, 32, 35]:
            print(f"Q{q['sort_order']}: stem={repr(q['stem'][:60])}, ans={q['correct_answer']}")
            print(f"   opts={q['options']}")

print("\n=== CHECKING 2022 ky2 ===")
f22, d22 = load_exam('ky2', 2022)
if d22:
    print(f"File: {f22}")
    for q in d22['questions']:
        if q['sort_order'] in [3, 5, 8, 9, 12, 21, 25, 29]:
            print(f"Q{q['sort_order']}: stem={repr(q['stem'][:60])}, ans={q['correct_answer']}")
            print(f"   opts={q['options']}")

print("\n=== CHECKING 2013 ky2 Part B & Passage 6 ===")
f13_2, d13_2 = load_exam('ky2', 2013)
if d13_2:
    print(f"File: {f13_2}")
    for q in d13_2['questions']:
        if q['sort_order'] in range(41, 46):
            print(f"Q{q['sort_order']}: stem={repr(q['stem'])}, ans={q['correct_answer']}")
    for p in d13_2.get('passages', []):
        if p.get('sort_order') == 6 or p.get('passage_type') == 'reading_part_b':
            print(f"Passage 6 preview: {repr(p.get('content', '')[:120])}")
            print(f"Contains 's e n no os': {'s e n no os' in p.get('content', '')}")

print("\n=== CHECKING 2013 ky1 Part B ===")
f13_1, d13_1 = load_exam('ky1', 2013)
if d13_1:
    print(f"File: {f13_1}")
    for q in d13_1['questions']:
        if q['sort_order'] in range(41, 46):
            print(f"Q{q['sort_order']}: ans={q['correct_answer']}, stem={repr(q['stem'][:60])}")

print("\n=== CHECKING 2014 ky1 Part B ===")
f14_1, d14_1 = load_exam('ky1', 2014)
if d14_1:
    print(f"File: {f14_1}")
    for q in d14_1['questions']:
        if q['sort_order'] in range(41, 46):
            print(f"Q{q['sort_order']}: ans={q['correct_answer']}, stem={repr(q['stem'][:60])}")

print("\n=== CHECKING 2010 ky1 Q26 & Special Symbols (o£, th&r) ===")
f10_1, d10_1 = load_exam('ky1', 2010)
if d10_1:
    for q in d10_1['questions']:
        if q['sort_order'] in [26, 33]:
            print(f"2010 Q{q['sort_order']}: opts={q['options']}")
