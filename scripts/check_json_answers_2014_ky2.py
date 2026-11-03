import json

d = json.load(open('public/data/exams/307952b3-040c-5ab4-a893-687e97d737ec.json', encoding='utf-8'))
qs = d.get('questions', [])
for i, q in enumerate(qs, 1):
    print(f"Q{i}: {q.get('answer')}", end='  ' if i % 5 != 0 else '\n')
