import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

targets = [
    (2001, 'ky1', 7),
    (2015, 'ky1', 36),
    (2015, 'ky1', 37),
    (2018, 'ky1', 31),
]

for yr, cat, so in targets:
    fpath = [f for f in glob.glob('public/data/exams/*.json') if json.load(open(f, encoding='utf-8'))['exam']['year'] == yr and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == cat][0]
    data = json.load(open(fpath, encoding='utf-8'))
    q = [x for x in data['questions'] if x['sort_order'] == so][0]
    print(f"\n==================== {yr} {cat} Q{so} ====================")
    print("Stem:", q['stem'])
    print("DB correct_answer:", q['correct_answer'])
    print("Options:", [(o['key'], o['text']) for o in q['options']])
    print("Explanation:\n", q['explanation'][:500])
    print("...\n" + q['explanation'][-300:])
