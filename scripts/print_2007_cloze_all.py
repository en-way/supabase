import json

d = json.load(open('public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json', encoding='utf-8'))

for q in d['questions']:
    if q['sort_order'] <= 20:
        print(f"Q{q['sort_order']} (Ans: {q['correct_answer']}):")
        for o in q['options']:
            print(f"  [{o['key']}] {o['text']}")
        print(f"  Exp: {q['explanation'][:60]}...\n")
