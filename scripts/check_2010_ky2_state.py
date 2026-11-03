import json
with open('public/data/exams/207d2963-734a-52bd-9fa3-6c341efb5974.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('Title:', d.get('title'))
passages = d.get('passages', [])
print('Passages count:', len(passages))
for i, p in enumerate(passages):
    print(f"  P{i}: id={p.get('id')}, type={p.get('type')}, pnum={p.get('passage_number')}, words={len(p.get('content', '').split())}, title={p.get('title')}")

questions = d.get('questions', [])
print('Questions count:', len(questions))
for i, q in enumerate(questions):
    print(f"  Q{i+1}: id={q.get('id')}, qnum={q.get('question_number')}, pid={q.get('passage_id')}, ans={q.get('correct_answer')}, score={q.get('score')}")
