import json
import glob

files = glob.glob("public/data/exams/*.json")
for ef in files[:5]:
    with open(ef, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(ef, d.get('exam'))
