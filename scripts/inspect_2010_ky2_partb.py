# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

fpath = 'public/data/exams/207d2963-734a-52bd-9fa3-6c341efb5974.json'
d = json.load(open(fpath, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] in range(41, 46):
        print(f"=== Q{q['sort_order']} ===")
        print(f"Stem: {q['stem']}")
        print(f"Options: {q['options']}")
        print(f"Answer: {q['correct_answer']}")
        print(f"Expl: {q['explanation'][:200]}...\n")

for p in d['passages']:
    if p['sort_order'] == 6:
        print(f"=== Passage 6 (Part B) ===")
        print(f"Title: {p['title']}")
        print(f"Content:\n{p['content']}")
