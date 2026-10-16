# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

f = 'public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json'
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    so = q['sort_order']
    if 21 <= so <= 40:
        opts_str = " | ".join([f"[{o['key']}] {o['text']}" for o in q['options']])
        print(f"=== Q{so} ({q['correct_answer']}) ===")
        print("Stem:", q['stem'])
        print("Opts:", opts_str)
        print("Expl head:", q['explanation'][:150].replace('\n', ' '))
        print()
