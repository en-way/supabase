# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

f = 'public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json'
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] <= 20:
        opts_str = " | ".join([f"[{o['key']}] {o['text']}" for o in q['options']])
        expl_snippet = (q.get('explanation') or '')[:50].replace('\n', ' ')
        print(f"Q{q['sort_order']:02d} ({q['correct_answer']}): {opts_str}")
        print(f"     Expl: {expl_snippet}")
