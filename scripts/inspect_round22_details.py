import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2008 ky1 Q36-40
f2008 = [f for f in glob.glob('public/data/exams/*.json') if '2008' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
d2008 = json.load(open(f2008, encoding='utf-8'))
print("=== 2008 ky1 Q36-40 ===")
for q in d2008['questions']:
    if q['sort_order'] in [36, 37, 38, 39, 40]:
        print(f"Q{q['sort_order']}: {q['stem']}")
        for o in q['options']:
            print(f"   [{o['key']}]: {repr(o['text'])}")
        print(f"   Ans: {q['correct_answer']}")
        print(f"   Expl preview: {repr(q['explanation'][:120])}")
        print()

# 2. 2009 ky1 Q29-30
f2009 = [f for f in glob.glob('public/data/exams/*.json') if '2009' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
d2009 = json.load(open(f2009, encoding='utf-8'))
print("=== 2009 ky1 Q29-30 ===")
for q in d2009['questions']:
    if q['sort_order'] in [29, 30]:
        print(f"Q{q['sort_order']}: {q['stem']}")
        for o in q['options']:
            print(f"   [{o['key']}]: {repr(o['text'])}")
        print(f"   Ans: {q['correct_answer']}")
        print(f"   Expl preview: {repr(q['explanation'][:120])}")
        print()

# 3. 2010 ky1 Q42-45
f2010 = [f for f in glob.glob('public/data/exams/*.json') if '2010' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
d2010 = json.load(open(f2010, encoding='utf-8'))
print("=== 2010 ky1 Q42-45 ===")
for q in d2010['questions']:
    if q['sort_order'] in [42, 43, 44, 45]:
        print(f"Q{q['sort_order']}: {q['stem']}")
        print(f"   Ans: {q['correct_answer']}")
        print(f"   Expl preview: {repr(q['explanation'][:120])}")
        print()
