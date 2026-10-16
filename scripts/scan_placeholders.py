# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

found = []
for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d['questions']:
        so = q['sort_order']
        for o in q.get('options', []):
            t = o.get('text', '')
            if any(k in t for k in ['Verified standard', 'Alternative comparative', 'Essential contextual', 'Contrasting rhetorical', 'Secondary grammatical']):
                found.append((yr, cat, so, o['key'], t))

print(f"Total placeholder options found: {len(found)}")
for x in found:
    print(x)
