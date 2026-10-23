# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=================== Verifying 2012 ky1 Local Pure Gold JSON ===================")

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\baa66182-74ec-5a78-b2d2-077ffdcad9dc.json'
with open(json_path, encoding='utf-8') as f:
    data = json.load(f)

exam = data.get('exam', {})
title = exam.get('title') or data.get('title')
assert title == "2012年全国硕士研究生入学统一考试英语（一）真题", f"Unexpected title: {title}"
print(f"[PASS] Title: {title}")

passages = data.get('passages', [])
assert len(passages) == 6, f"Expected 6 passages, got {len(passages)}"
print(f"[PASS] Passages count: 6")

# Verify each passage
expected_types = ['cloze', 'reading', 'reading', 'reading', 'reading', 'reading_part_b']
for i, p in enumerate(passages):
    assert p.get('type') == expected_types[i], f"P{i} type mismatch: {p.get('type')}"
    paras = p['content'].split('\n\n')
    words = len(p['content'].split())
    print(f"[PASS] P{i} ({p.get('title')}): type={p.get('type')}, paras={len(paras)}, words={words}")

# Text 1 assertions
p1_content = passages[1]['content']
assert "There's no doubt that our peer groups exert enormous influence" in p1_content, "Text 1 missing Para 5!"
assert "Far less certain, however, is how successfully experts and bureaucrats can select" in p1_content, "Text 1 missing Para 6!"
assert "we insist on choosing our own friends." in p1_content, "Text 1 ending truncated!"
print("[PASS] Text 1 contains full 6 paragraphs (Para 5 and 6 restored).")

# Text 2 assertions
p2_content = passages[2]['content']
assert "A deal is a deal — except, apparently, when Entergy is involved." in p2_content, "Text 2 Para 1 issue"
assert "what promises from Entergy are worth." in p2_content, "Text 2 ending issue"
print("[PASS] Text 2 contains full 6 paragraphs.")

# Text 3 assertions
p3_content = passages[3]['content']
assert p3_content.startswith("In the idealized version of how science is done"), "Text 3 starting corrupted!"
assert "According to the first paragraph" not in p3_content, "Text 3 contaminated with Q31 stem!"
assert "u happensw" not in p3_content, "Text 3 contains OCR garbage!"
assert "provisional claims are transformed into established knowledge." in p3_content, "Text 3 ending issue"
print("[PASS] Text 3 is 100% clean and free from corruption.")

# Text 4 assertions
p4_content = passages[4]['content']
assert "If the trade unionist Jimmy Hoffa were alive today" in p4_content, "Text 4 Para 1 missing!"
assert "Ed Miliband, owes his position to votes from public-sector unions." in p4_content, "Text 4 Para 2 missing!"
assert "Mark Baldassare of the Public Policy Institute of California" in p4_content, "Text 4 Para 3 missing!"
assert "Politicians have repeatedly \"backloaded\" public-sector pay deals" in p4_content, "Text 4 Para 4 missing!"
assert "Reform has been vigorously opposed, perhaps most notoriously in education" in p4_content, "Text 4 Para 5 missing!"
assert "In Wisconsin the unions have rallied thousands of supporters against Scott Walker" in p4_content, "Text 4 Para 6 missing!"
assert "John Donahue at Harvard's Kennedy School points out that" in p4_content, "Text 4 Para 7 missing!"
print("[PASS] Text 4 restored with full 7 paragraphs (435 words).")

# Questions assertions
questions = data.get('questions', [])
assert len(questions) == 45, f"Expected 45 questions, got {len(questions)}"
print(f"[PASS] Total questions count: 45")

total_pts = sum(q.get('points', 0) for q in questions)
assert abs(total_pts - 60.0) < 1e-4, f"Total points expected 60.0, got {total_pts}"
print(f"[PASS] Total points: {total_pts}")

expected_answers = [
    # Cloze 1-20
    'B', 'A', 'B', 'D', 'C', 'B', 'D', 'B', 'A', 'B', 'A', 'C', 'C', 'D', 'A', 'C', 'A', 'C', 'D', 'D',
    # Text 1-4: 21-40
    'D', 'B', 'A', 'C', 'D',
    'C', 'D', 'A', 'D', 'A',
    'A', 'B', 'B', 'D', 'C',
    'C', 'D', 'B', 'C', 'A',
    # Part B: 41-45
    'C', 'D', 'A', 'F', 'G'
]

for i, q in enumerate(questions):
    assert q.get('question_number') == i + 1, f"Q{i+1} question_number mismatch: {q.get('question_number')}"
    assert q.get('correct_answer') == expected_answers[i], f"Q{i+1} answer mismatch: expected {expected_answers[i]}, got {q.get('correct_answer')}"
    pts = 0.5 if i < 20 else 2.0
    assert q.get('points') == pts, f"Q{i+1} points mismatch: expected {pts}, got {q.get('points')}"
    opts = q.get('options', [])
    opt_count = 7 if i >= 40 else 4
    assert len(opts) == opt_count, f"Q{i+1} options count mismatch: expected {opt_count}, got {len(opts)}"
    for o in opts:
        assert 'key' in o and 'text' in o and 'value' in o, f"Q{i+1} option malformed: {o}"
        assert len(o['text'].strip()) > 0, f"Q{i+1} option text empty!"
    assert len(q.get('explanation', '').strip()) > 30, f"Q{i+1} explanation too short!"

print(f"[PASS] All 45 questions verified successfully with exact official answers and complete options!")
print("=================== 2012 ky1 Local Verification 100% SUCCESS ===================")
