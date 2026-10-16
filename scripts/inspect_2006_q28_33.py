# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

f = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] in [28, 33]:
        print(f"=== Q{q['sort_order']} ===")
        print("Stem:", q['stem'])
        print("Ans:", q['correct_answer'])
        print("Opts:", q['options'])
        print("Expl head:", q['explanation'][:100])
