import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

targets = []

# Examine English I (2001-2022) and English II (2021-2022)
for ef in sorted(glob.glob('public/data/exams/*.json')):
    d = json.load(open(ef, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    
    # Only check vector text years
    if (cat == 'ky1' and 2001 <= yr <= 2022) or (cat == 'ky2' and yr in [2021, 2022]):
        for q in d['questions']:
            so = q['sort_order']
            expl = (q.get('explanation') or '').strip()
            # If length < 200
            if len(expl) < 200:
                targets.append((yr, cat, so, len(expl), expl[:70].replace('\n', ' ')))

print(f"Total questions with expl < 200 chars in 24 vector-text exams: {len(targets)}")
for t in targets:
    print(f"[{t[0]} {t[1]} Q{t[2]}] len={t[3]}: {t[4]}")
