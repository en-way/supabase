import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Checking 2009 ky1 & 2012 ky1 all questions ===")

d09 = json.load(open('public/data/exams/9369aa41-c91e-548c-bf99-1ad46a07ac25.json', encoding='utf-8'))
d12 = json.load(open('public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json', encoding='utf-8'))

for q in d09['questions']:
    so = q['sort_order']
    expl = q.get('explanation', '')
    if len(expl) < 250:
        print(f"2009 ky1 Q{so}: len={len(expl)} -> {repr(expl[:60])}")

for q in d12['questions']:
    so = q['sort_order']
    expl = q.get('explanation', '')
    if len(expl) < 250:
        print(f"2012 ky1 Q{so}: len={len(expl)} -> {repr(expl[:60])}")
