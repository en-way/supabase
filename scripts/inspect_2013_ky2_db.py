import sys
import json
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

exam_id = '1ac5713f-fb5d-560f-a22a-3c5c3431d03f'

exam = db_ops.run_sql(f"select id, title, year, category_id, total_score from exams where id = '{exam_id}'")
print('Exam in DB:', exam)

passages = db_ops.run_sql(f"select id, title, section_type, sort_order, length(content) as content_len, content from passages where exam_id = '{exam_id}' order by sort_order")
print(f'Passages in DB: {len(passages)}')
for p in passages:
    cnt = p.get('content') or ''
    print(f"ID: {p['id']}, sort: {p.get('sort_order')}, section: {p.get('section_type')}, title: {p.get('title')}, content_len: {p.get('content_len')}, sample: {cnt[:60]!r}")

questions = db_ops.run_sql(f"select id, sort_order, question_type, points, correct_answer, answer, length(explanation) as expl_len, stem from questions where exam_id = '{exam_id}' order by sort_order")
print(f'Questions in DB: {len(questions)}')
for q in questions[:5]:
    print(q)
