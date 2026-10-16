import json

d = json.load(open('public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json', encoding='utf-8'))

for q in d['questions']:
    if q['sort_order'] <= 20:
        opt_str = ", ".join([f"[{o['key']}] {o['text']}" for o in q['options']])
        print(f"Q{q['sort_order']} (Ans: {q['correct_answer']}): {opt_str}")
