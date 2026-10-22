# -*- coding: utf-8 -*-
"""
verify_2011_ky2_local.py
Local Forensic Verification for 2011 National Master's Entrance Exam English (II)
UUID: 53a52573-0afc-51a4-86b6-b2f321cbe6a8
"""

import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

exam_json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\53a52573-0afc-51a4-86b6-b2f321cbe6a8.json'

with open(exam_json_path, 'r', encoding='utf-8') as f:
    exam = json.load(f)

print("==================== 2011 ky2 Local Forensic Verification ====================")

# 1. Metadata
assert exam.get('title') == "2011年全国硕士研究生入学统一考试英语（二）真题", f"Title error: {exam.get('title')}"
assert exam.get('category_id') == "ky2", f"category_id error: {exam.get('category_id')}"
assert float(exam.get('total_score', 0)) == 60.0, f"total_score error: {exam.get('total_score')}"
print("✓ Metadata verification PASS (Title, Category, Total Score 60.0)")

# 2. Passages
passages = exam.get('passages', [])
assert len(passages) == 6, f"Passage count error: {len(passages)}"

expected_types = ["cloze", "reading", "reading", "reading", "reading", "reading_part_b"]
expected_nums = [1, 1, 2, 3, 4, 5]

for i, p in enumerate(passages):
    assert p.get('type') == expected_types[i], f"P{i} type mismatch: {p.get('type')} != {expected_types[i]}"
    assert p.get('passage_type') == expected_types[i], f"P{i} passage_type mismatch"
    assert p.get('passage_number') == expected_nums[i], f"P{i} passage_number mismatch: {p.get('passage_number')} != {expected_nums[i]}"
    assert p.get('sort_order') == i + 1, f"P{i} sort_order mismatch: {p.get('sort_order')} != {i+1}"
    content = p.get('content', '')
    assert len(content) > 500, f"P{i} content too short: {len(content)}"
    print(f"✓ Passage {i} ({p.get('title')}): type={p.get('type')}, words={len(content.split())}, chars={len(content)} PASS")

# Text specific assertions
p0 = passages[0]['content']
assert 'The Internet affords anonymity to its users' in p0 and '[20]' in p0 and 'license [10] by the government' in p0, "Cloze content assertion failed"

p1 = passages[1]['content']
assert "Ruth Simmons joined Goldman Sachs" in p1 and "outside directors will follow the example of Ms. Simmons" in p1, "Text 1 assertion failed"
assert "outsidedirectorswillfollowthe" not in p1 and "againverypopular" not in p1, "Text 1 adhesion residue assertion failed"

p2 = passages[2]['content']
assert p2.startswith("A year ago the end seemed near."), f"Text 2 restored beginning assertion failed: {repr(p2[:50])}"
assert "Trade Commission launched" in p2 and "are much more stable" in p2, "Text 2 clean text assertion failed"
assert "TradeCommissionlaunched" not in p2 and "aremuchmorestable" not in p2, "Text 2 adhesion residue assertion failed"

p3 = passages[3]['content']
assert "immediately following World War II" in p3, "Text 3 adhesion fix assertion failed"
assert "both desirable and inevitable was widely shared" in p3, "Text 3 end adhesion fix assertion failed"
assert "immediatelyfollowingWorld" not in p3 and "bothdesirableand" not in p3, "Text 3 adhesion residue assertion failed"

p4 = passages[4]['content']
assert "Will the European Union make it?" in p4 and "economic co-ordination should involve all 27 members" in p4, "Text 4 assertion failed"
assert "ordinationshould" not in p4 and "smallmajority" not in p4, "Text 4 adhesion residue assertion failed"

p5 = passages[5]['content']
assert "Leading doctors today weigh in on the debate" in p5 and "Andrew Lansley" in p5 and "Terence Stephenson" in p5, "Part B assertion failed"
assert not p5.strip().endswith("producers such as McDonald's."), "Part B stray text residue assertion failed"

print("✓ All 6 Passages content and restoration assertions PASS")

# 3. Questions
questions = exam.get('questions', [])
assert len(questions) == 45, f"Question count mismatch: {len(questions)}"

official_answers = [
    # Cloze 1-20
    'A', 'C', 'B', 'D', 'D', 'B', 'A', 'C', 'C', 'B',
    'D', 'B', 'A', 'C', 'A', 'A', 'D', 'A', 'C', 'D',
    # Reading 21-40
    'B', 'D', 'C', 'A', 'B', 'D', 'B', 'C', 'A', 'A',
    'B', 'D', 'C', 'D', 'B', 'B', 'C', 'B', 'A', 'D',
    # Part B 41-45
    'E', 'D', 'C', 'B', 'G'
]

total_calc_score = 0.0

for i, q in enumerate(questions):
    q_num = i + 1
    assert q.get('sort_order') == q_num, f"Q{q_num} sort_order mismatch: {q.get('sort_order')}"
    expected_pts = 0.5 if q_num <= 20 else 2.0
    pts = float(q.get('points', 0))
    assert pts == expected_pts, f"Q{q_num} points mismatch: {pts} != {expected_pts}"
    total_calc_score += pts
    
    # answer check
    ans = q.get('correct_answer')
    assert ans == official_answers[i], f"Q{q_num} answer mismatch: {ans} != {official_answers[i]}"
    
    # options check
    opts = q.get('options', [])
    assert len(opts) >= 4, f"Q{q_num} has fewer than 4 options"
    for opt in opts:
        assert 'key' in opt and 'text' in opt and 'value' in opt, f"Q{q_num} opt missing key/text/value: {opt}"
    
    # explanation check
    exp = q.get('explanation') or ''
    assert len(exp) > 30, f"Q{q_num} explanation too short: {len(exp)}"

assert abs(total_calc_score - 60.0) < 1e-6, f"Total score calculated mismatch: {total_calc_score}"
print(f"✓ All 45 Questions verified: points, sort_orders, 100% official answers, options format, explanations PASS")

# 4. Long word adhesion check
valid_long_words = {
    'cyber-security', 'cybersecurity', 'confidentiality', 'proportionality',
    'reproducible', 'superintendent', 'extraordinary', 'infrastructure',
    'characteristics', 'representatives', 'responsibility', 'responsibilities',
    'standardization', 'consequences', 'destabilize', 'uncomfortable',
    'recommendations', 'recommendation', 'internationally', 'competitiveness',
    'anti-discrimination', 'antidiscrimination', 'countermeasures'
}

adhesion_issues = []
for i, p in enumerate(passages):
    words = re.findall(r'[a-zA-Z]{17,}', p.get('content', ''))
    for w in words:
        if w.lower() not in valid_long_words:
            adhesion_issues.append((f"Passage {i}", w))

for i, q in enumerate(questions):
    stem_words = re.findall(r'[a-zA-Z]{17,}', q.get('stem', ''))
    for w in stem_words:
        if w.lower() not in valid_long_words:
            adhesion_issues.append((f"Q{i+1} stem", w))

assert len(adhesion_issues) == 0, f"Found unexpected adhesion words: {adhesion_issues}"
print("✓ No word adhesion defects detected in entire exam PASS")

print("\n=======================================================")
print("★ 2011 ky2 Local Forensic Verification 100% PERFECT PASS! ★")
print("=======================================================")
