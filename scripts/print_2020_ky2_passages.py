import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('public/data/exams/ee996af1-3aaa-5380-9465-08125c4db713.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for i, p in enumerate(d.get('passages', [])):
    print(f"=== PASSAGE {i}: {p.get('title')} ===")
    print(p.get('content', ''))
    print('\n' + '='*50 + '\n')
