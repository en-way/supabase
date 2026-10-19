import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_files = sorted(glob.glob('public/data/exams/*.json'))

suspicious = []
special_glyphs = ['・', '■', '▲', '★', '※', '*']

for f in exam_files:
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    
    for q in d.get('questions', []):
        so = q['sort_order']
        stem = q.get('stem', '').strip()
        ans = q.get('correct_answer', '').strip()
        expl = q.get('explanation', '').strip()
        opts = q.get('options', [])
        
        # 1. Option count
        if len(opts) != 4 and so <= 40:
            suspicious.append((yr, cat, so, f'Options count != 4 ({len(opts)})'))
            
        # 2. Options text
        for opt in opts:
            k = opt.get('key')
            v = opt.get('text', '').strip()
            if len(v) < 2 and so <= 40:
                suspicious.append((yr, cat, so, f'Option [{k}] too short: {repr(v)}'))
            if re.search(r'[a-zA-Z]5\b', v): # e.g. patients5
                suspicious.append((yr, cat, so, f'Option [{k}] has 5-apostrophe typo: {repr(v)}'))
            for g in special_glyphs:
                if g in v:
                    suspicious.append((yr, cat, so, f'Option [{k}] has glyph {g}: {repr(v)}'))
                
        # 3. Stem issues
        if re.search(r'[a-zA-Z]5\b', stem):
            suspicious.append((yr, cat, so, f'Stem has 5-apostrophe typo: {repr(stem[:50])}'))
        for g in special_glyphs:
            if g in stem:
                suspicious.append((yr, cat, so, f'Stem has glyph {g}: {repr(stem[:50])}'))

print(f'Total suspicious items found: {len(suspicious)}')
for item in suspicious:
    print(item)
