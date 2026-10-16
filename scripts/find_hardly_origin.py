import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')
for ef in glob.glob("public/data/exams/*.json"):
    with open(ef, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d.get('questions', []):
        opts = [o.get('text', '') for o in q.get('options', [])]
        if 'hardly' in opts and 'scarcely' in opts:
            e = d.get('exam', {})
            print(f"Found in {ef}: year={e.get('year')}, cat={e.get('category_id')}, Q{q.get('sort_order')}")
