import json
import sys
from calibrations_2014_data import calibrations_2014

sys.stdout.reconfigure(encoding='utf-8')

fpath = 'public/data/exams/240cc48a-439b-5d27-8464-f7dc53e060dc.json'

with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== Applying Round 39 2014 ky1 Calibration ===")
print(f"Exam: {data['exam']['title']} (Year: {data['exam']['year']}, Category: {data['exam']['category_id']})")

updated_count = 0
for q in data.get('questions', []):
    so = q.get('sort_order', 0)
    if so in calibrations_2014:
        c = calibrations_2014[so]
        q['stem'] = c['stem']
        q['correct_answer'] = c['correct_answer']
        q['answer'] = c['correct_answer']
        q['options'] = c['options']
        q['explanation'] = c['explanation']
        updated_count += 1
        print(f"Updated Q{so}: Answer={c['correct_answer']}, Options={len(c['options'])}, ExplLength={len(c['explanation'])}")

print(f"\nTotal questions updated in JSON: {updated_count}")

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON file successfully saved.")
