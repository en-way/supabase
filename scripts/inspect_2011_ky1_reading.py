# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

f = 'public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json'
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    if 21 <= q['sort_order'] <= 25:
        print(f"=== Q{q['sort_order']} (Ans: {q['correct_answer']}) ===")
        print("Stem:", q['stem'])
        print("Opts:", [f"[{o['key']}] {o['text']}" for o in q['options']])
        print("Expl head:", q['explanation'][:300])
        print()
