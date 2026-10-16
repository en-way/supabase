import json

d = json.load(open('public/data/exams/240cc48a-439b-5d27-8464-f7dc53e060dc.json', encoding='utf-8'))

for q in d['questions']:
    if q['sort_order'] <= 20:
        opt_str = ", ".join([f"[{o['key']}] {o['text']}" for o in q['options']])
        print(f"Q{q['sort_order']} (Ans: {q['correct_answer']}): {opt_str}")
