import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Inspect 2001 ky1 Q7
f2001 = [f for f in glob.glob('public/data/exams/*.json') if '2001' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
d2001 = json.load(open(f2001, encoding='utf-8'))
q7_2001 = [q for q in d2001['questions'] if q['sort_order'] == 7][0]
print("=== 2001 ky1 Q7 ===")
print("Stem:", q7_2001['stem'])
print("Options:", [(o['key'], o['text']) for o in q7_2001['options']])
print("Correct Answer:", q7_2001['correct_answer'])
print("Explanation:", q7_2001['explanation'][:300])

# 2. Inspect 2003 ky1 Q25
f2003 = [f for f in glob.glob('public/data/exams/*.json') if '2003' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
d2003 = json.load(open(f2003, encoding='utf-8'))
q25_2003 = [q for q in d2003['questions'] if q['sort_order'] == 25][0]
print("\n=== 2003 ky1 Q25 ===")
print("Stem:", q25_2003['stem'])
print("Options:", [(o['key'], o['text']) for o in q25_2003['options']])
print("Correct Answer:", q25_2003['correct_answer'])
print("Explanation:", q25_2003['explanation'][:300])

# 3. Inspect 2003 ky1 Q24
q24_2003 = [q for q in d2003['questions'] if q['sort_order'] == 24][0]
print("\n=== 2003 ky1 Q24 ===")
print("Stem:", q24_2003['stem'])
print("Options:", [(o['key'], o['text']) for o in q24_2003['options']])

# 4. Inspect 2023 ky2 Q41
f2023_ky2 = [f for f in glob.glob('public/data/exams/*.json') if '2023' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky2'][0]
d2023_ky2 = json.load(open(f2023_ky2, encoding='utf-8'))
q41_2023 = [q for q in d2023_ky2['questions'] if q['sort_order'] == 41][0]
print("\n=== 2023 ky2 Q41 ===")
for o in q41_2023['options']:
    raw = repr(o['text'])
    print(f"[{o['key']}]: {raw}")
