import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
path = 'public/data/exams/ee996af1-3aaa-5380-9465-08125c4db713.json'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

exam = d.get('exam', d)
print('Exam title:', exam.get('title'))
print('Passages count:', len(d.get('passages', [])))
for i, p in enumerate(d.get('passages', [])):
    content = p.get('content', '')
    paras = [line for line in content.split('\n') if line.strip()]
    print(f"P{i}: id={p.get('id')}, title={p.get('title')}, words={len(content.split())}, chars={len(content)}, paras={len(paras)}")
    print(f"  snippet: {repr(content[:80])}")

questions = d.get('questions', [])
print('Questions count:', len(questions))
missing_qn = [q for q in questions if not q.get('question_number')]
missing_so = [q for q in questions if not q.get('sort_order')]
missing_score = [q for q in questions if not q.get('score')]
print(f"Missing qn: {len(missing_qn)}, missing so: {len(missing_so)}, missing score: {len(missing_score)}")

for q in questions:
    num = q.get('sort_order') or q.get('question_number')
    stem = q.get('stem', '')
    ans = q.get('answer') or q.get('correct_answer')
    score = q.get('score')
    opts = q.get('options')
    print(f"Q{num}: ans={ans}, score={score}, opts_type={type(opts)}, opts_len={len(opts) if opts else 0}, stem={stem[:40]}")
