import json

with open("public/data/exams/e5abf09b-e94d-5994-b944-7c5711cd4e4d.json", "r", encoding="utf-8") as f:
    d = json.load(f)

qs = d.get('questions', [])
print("Number of questions:", len(qs))
if qs:
    print("Question keys:", qs[0].keys())
    print("Q1:", qs[0].get('question_number'), qs[0].get('order_index'), qs[0].get('stem'))
    for q in qs:
        if q.get('question_number') == 26 or q.get('order_index') == 26:
            print("Found 26:", q)
