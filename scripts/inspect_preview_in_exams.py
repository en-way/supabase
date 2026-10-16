import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

import glob

targets = [(2022, 'ky1'), (2022, 'ky2'), (2021, 'ky2')]
exams = {}
for f in glob.glob('public/data/exams/*.json'):
    data = json.load(open(f, encoding='utf-8'))
    y = data['exam']['year']
    c = data['exam']['category_id']
    if (y, c) in targets:
        exams[(y, c)] = data

for yr, cat in targets:
    d = exams.get((yr, cat))
    if not d: continue
    print(f"\n=================== {yr} {cat} ===================")
    for q in d['questions']:
        so = q['sort_order']
        if 21 <= so <= 40:
            expl = (q.get('explanation') or '').strip()
            first_line = expl.split('\n')[0]
            is_preview = ("事实细节" in expl or "段落主旨" in expl or "写作目的" in expl or "因果细节" in expl or "人物观点" in expl) and len(expl) < 200
            print(f"Q{so}: len={len(expl)} | preview={is_preview} | {first_line[:50]}")
