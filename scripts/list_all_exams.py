import json
import glob

files = glob.glob("public/data/exams/*.json")
for ef in files:
    with open(ef, 'r', encoding='utf-8') as f:
        d = json.load(f)
    e = d.get('exam', {})
    print(f"{ef}: year={e.get('year')}, cat={e.get('category_id')}, questions_len={len(d.get('questions', []))}")
