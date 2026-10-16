# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

fpath = 'public/data/exams/5bcba462-0a1e-59b2-9fcb-c171d242db3b.json'
d = json.load(open(fpath, encoding='utf-8'))

for p in d['passages']:
    if p['sort_order'] in [2, 5]:
        print(f"=== Passage {p['sort_order']}: {p['title']} ===")
        print(f"Length: {len(p['content'])} chars")
        print("--- First 200 chars ---")
        print(p['content'][:200])
        print("--- Last 300 chars ---")
        print(p['content'][-300:])
        print("\n" + "="*50 + "\n")

for q in d['questions']:
    if q['sort_order'] in range(21, 26):
        print(f"Q{q['sort_order']}: {q['stem']}")
