# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json

json_path = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\17ca33c3-66f2-5ae0-a1ba-847f507dd6e4.json"
with open(json_path, "r", encoding="utf-8") as f:
    d = json.load(f)

exam = d.get("exam", {})
print("Exam Title:", repr(exam.get("title")))
print("Exam Total Score:", exam.get("total_score"))
print("Exam Category:", exam.get("category_id"), "Year:", exam.get("year"))

passages = d.get("passages", [])
print(f"\nPassages Count: {len(passages)}")
for i, p in enumerate(passages):
    content = p.get("content", "")
    paras = [para for para in content.split("\n\n") if para.strip()]
    words = len(content.split())
    print(f"\nPassage {i}: id={p.get('id')}, title={p.get('title')}, type={p.get('type')}, p_no={p.get('passage_number')}")
    print(f"  Paras: {len(paras)}, Words: {words}")
    print(f"  First 120 chars: {content[:120].strip()}")
    print(f"  Last 120 chars:  {content[-120:].strip()}")

questions = d.get("questions", [])
print(f"\nQuestions Count: {len(questions)}")
none_qnums = [i+1 for i, q in enumerate(questions) if q.get("question_number") is None]
print(f"Questions with question_number == None ({len(none_qnums)}): {none_qnums[:15]}...")

for i in [0, 20, 25, 30, 35, 40]:
    if i < len(questions):
        q = questions[i]
        print(f"\nQ so={q.get('sort_order')} num={q.get('question_number')} ans={q.get('answer')} pts={q.get('points')} type={q.get('q_type')}")
        print(f"  Stem: {q.get('stem')}")
        print(f"  Expl preview: {repr(q.get('explanation', '')[:80])}...")
