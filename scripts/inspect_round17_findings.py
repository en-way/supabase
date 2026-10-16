# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. 2005 ky1 Q11 and Q12
f_2005 = 'public/data/exams/e1b9d134-9546-55ab-9a60-c7e5b04046a3.json'
d_2005 = json.load(open(f_2005, encoding='utf-8'))
for q in d_2005['questions']:
    if q['sort_order'] in [10, 11, 12, 13]:
        print(f"=== 2005 ky1 Q{q['sort_order']} (Ans: {q['correct_answer']}) ===")
        print("Stem:", q['stem'])
        print("Opts:", [f"[{o['key']}] {o['text']}" for o in q['options']])
        print("Expl:", q['explanation'][:150])
        print()

# 2. 2003 ky1 Q23
f_2003 = 'public/data/exams/91ff038a-e3f9-5b6d-82c5-1328735be1d1.json'
d_2003 = json.load(open(f_2003, encoding='utf-8'))
for q in d_2003['questions']:
    if q['sort_order'] == 23:
        print("=== 2003 ky1 Q23 ===")
        print("Stem:", q['stem'])
        print("Expl:", q['explanation'][:150])

# 3. 2006 ky1 Q28 and Q33
f_2006 = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'
d_2006 = json.load(open(f_2006, encoding='utf-8'))
for q in d_2006['questions']:
    if q['sort_order'] in [28, 33]:
        print(f"=== 2006 ky1 Q{q['sort_order']} ===")
        print("Stem:", q['stem'])
        print("Expl:", q['explanation'][:150])

# 4. 2005 ky1 Q22
for q in d_2005['questions']:
    if q['sort_order'] == 22:
        print("=== 2005 ky1 Q22 ===")
        print("Stem:", q['stem'])
        print("Expl:", q['explanation'][:150])

# 5. 2010 ky2 Q41-45
f_2010_ky2 = 'public/data/exams/e5abf09b-e94d-5994-b944-7c5711cd4e4d.json'
d_2010_ky2 = json.load(open(f_2010_ky2, encoding='utf-8'))
for q in d_2010_ky2['questions']:
    if q['sort_order'] in range(41, 46):
        print(f"=== 2010 ky2 Q{q['sort_order']} ===")
        print("Stem:", q['stem'])
        print("Opts:", q['options'])
