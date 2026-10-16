import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for ef in glob.glob('public/data/exams/*.json'):
    d = json.load(open(ef, encoding='utf-8'))
    if d['exam']['year'] == 2004 and d['exam']['category_id'] == 'ky1':
        print("Found 2004 ky1 file:", ef)
        for q in d['questions']:
            so = q['sort_order']
            if 21 <= so <= 40:
                print(f"=== Q{so} (Ans: {q.get('correct_answer')}) ===")
                print("Stem:", q.get('stem'))
                opts = [f"[{o.get('key')}] {o.get('text')}" for o in q.get('options', [])]
                print("Opts:", " | ".join(opts))
                print("Expl:", q.get('explanation')[:120].replace('\n', ' '))
