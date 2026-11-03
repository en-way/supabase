import json
with open('public/data/exams/207d2963-734a-52bd-9fa3-6c341efb5974.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for idx, q in enumerate(d['questions']):
    qnum = idx + 1
    print(f"Q{qnum}: {q.get('correct_answer')}")
