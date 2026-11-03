import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ex = data.get('exam', {})
print("=== EXAM METADATA ===")
for k in ['id', 'title', 'year', 'category_id', 'total_score', 'pass_score', 'duration_minutes', 'approval_status', 'is_published', 'exam_type']:
    print(f"  {k}: {repr(ex.get(k))}")

passages = data.get('passages', [])
print(f"\n=== PASSAGES ({len(passages)}) ===")
for p in passages:
    so = p.get('sort_order')
    title = p.get('title')
    content = p.get('content', '')
    paras = [para.strip() for para in content.split('\n\n') if para.strip()]
    words = len(content.split())
    print(f"P{so} [{title}]: {len(paras)} paras, {words} words")
    print(f"   start: {repr(content[:60])}")
    print(f"   end:   {repr(content[-60:])}")

questions = data.get('questions', [])
print(f"\n=== QUESTIONS ({len(questions)}) ===")
qn_list = [q.get('question_number') for q in questions]
so_list = [q.get('sort_order') for q in questions]
scores = [q.get('score') for q in questions]
print("question_numbers:", qn_list[:5], "...", qn_list[-5:])
print("sort_orders:", so_list[:5], "...", so_list[-5:])
print("scores:", scores[:5], scores[20:25])

answers = [(q.get('sort_order'), q.get('answer'), q.get('correct_answer')) for q in questions]
mismatched = [a for a in answers if a[1] != a[2]]
print("Mismatched answers:", mismatched)

for idx in [0, 19, 20, 24, 25, 29, 30, 34, 35, 39, 40, 44]:
    if idx < len(questions):
        q = questions[idx]
        opts = {o['key']: o['text'] for o in q.get('options', [])}
        print(f"\nQ{q.get('sort_order')}: ans={q.get('correct_answer')}, stem={repr(q.get('stem'))}")
        print(f"   opts: {opts}")
        expl = q.get('explanation', '')
        print(f"   expl ({len(expl)} chars): {repr(expl[:60])}")
