import json

d = json.load(open('public/data/exams/d80926ab-1841-5d1f-a999-56773986c46d.json', encoding='utf-8'))

for q in d['questions']:
    if q['sort_order'] <= 20:
        opt_str = ", ".join([f"[{o['key']}] {o['text']}" for o in q['options']])
        print(f"Q{q['sort_order']} (Ans: {q['correct_answer']}): {opt_str}")
