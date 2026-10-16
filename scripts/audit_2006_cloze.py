import json

d = json.load(open('public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json', encoding='utf-8'))

for q in d['questions']:
    if q['sort_order'] <= 20:
        opt_str = ", ".join([f"[{o['key']}] {o['text']}" for o in q['options']])
        print(f"Q{q['sort_order']} (Ans: {q['correct_answer']}): {opt_str}")
