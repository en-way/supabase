import json, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('public/data/exams/207d2963-734a-52bd-9fa3-6c341efb5974.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for i, p in enumerate(d['passages']):
    title = p.get('title')
    print(f"\n==================== PASSAGE {i} ({title}) ====================")
    print(p.get('content'))
