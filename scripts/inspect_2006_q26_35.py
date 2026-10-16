# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

f = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    if 26 <= q['sort_order'] <= 35:
        print(f"=== Q{q['sort_order']} ({q['correct_answer']}) ===")
        print("Stem:", q['stem'])
        for o in q['options']:
            print(f"  [{o['key']}] {o['text']}")
