# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

f = 'public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json'
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] in [10, 11, 12, 13]:
        print(f"=== Q{q['sort_order']} (Ans: {q['correct_answer']}) ===")
        print("Stem:", q['stem'])
        print("Opts:", [f"[{o['key']}] {o['text']}" for o in q['options']])
        print("Expl:", q['explanation'][:250])
        print()
