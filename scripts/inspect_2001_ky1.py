# -*- coding: utf-8 -*-
import glob, json, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2001 and d['exam']['category_id'] == 'ky1':
        print(f, d['exam']['title'])
        for q in d['questions']:
            if 31 <= q['sort_order'] <= 40:
                print(f"=== Q{q['sort_order']} ({q['correct_answer']}) ===")
                print("Stem:", q['stem'])
                print("Opts:", [f"[{o['key']}] {o['text']}" for o in q['options']])
                print("Expl head:", q['explanation'][:200].replace('\n', ' '))
                print()
