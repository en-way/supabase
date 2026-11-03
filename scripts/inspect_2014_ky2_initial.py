import json

with open('public/data/exams/307952b3-040c-5ab4-a893-687e97d737ec.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('scripts/ky2_initial_report_utf8.txt', 'w', encoding='utf-8') as out:
    exam = d.get('exam', {})
    out.write(f"Exam title: {exam.get('title')}\n")
    out.write(f"Total score: {exam.get('total_score')}\n")
    out.write(f"Year: {exam.get('year')}, Category: {exam.get('category_id')}\n")

    passages = d.get('passages', [])
    out.write(f"\nPassages count: {len(passages)}\n")
    for idx, p in enumerate(passages):
        paras = [para for para in p.get('content', '').split('\n\n') if para.strip()]
        words = len(p.get('content', '').split())
        out.write(f"Passage {idx} (id: {p.get('id')}, type: {p.get('type')}, p_no: {p.get('passage_number')}): paras={len(paras)}, words={words}, title={p.get('title')}\n")
        out.write(f"  First 120 chars: {p.get('content', '')[:120].strip()}\n")
        out.write(f"  Last 120 chars:  {p.get('content', '')[-120:].strip()}\n")

    questions = d.get('questions', [])
    out.write(f"\nQuestions count: {len(questions)}\n")
    out.write(f"Questions list:\n")
    for q in questions:
        opts = q.get('options', [])
        opt_keys = [o.get('key') if isinstance(o, dict) else str(o) for o in opts]
        pts = q.get('points') if q.get('points') is not None else q.get('score')
        qtype = q.get('q_type')
        out.write(f"  Q{q.get('question_number')}: ans={q.get('answer')}, pts={pts}, type={qtype}, opts={opt_keys}\n")
        out.write(f"    Stem: {q.get('stem')}\n")
        out.write(f"    Expl preview: {q.get('explanation', '')[:80]}...\n")

