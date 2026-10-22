# -*- coding: utf-8 -*-
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

exam_json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\111d6c78-81a1-53dc-a039-dad4c94ebd35.json'

with open(exam_json_path, encoding='utf-8') as f:
    exam = json.load(f)

print("==================== 2011 ky1 Local Forensic Verification ====================")

# 1. Metadata
assert exam.get('title') == "2011年全国硕士研究生入学统一考试英语（一）真题", f"Title error: {exam.get('title')}"
assert exam.get('category_id') == "ky1", f"category_id error: {exam.get('category_id')}"
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
assert 'Aristotle viewed laughter' in p0 and '[20]' in p0 and 'flow [15] muscular responses' in p0, "Cloze content assertion failed"

p1 = passages[1]['content']
assert "hire Alan Gilbert" in p1 and "change the relationship between America's oldest orchestra and the new audience" in p1, "Text 1 assertion failed"

p2 = passages[2]['content']
assert "Liam McGee" in p2 and "The people who've been hurt the worst are those who've stayed too long" in p2, "Text 2 assertion failed"

p3 = passages[3]['content']
assert "The rough guide to marketing success used to be that you got what you paid for" in p3, "Text 3 restored beginning assertion failed"
assert "Toyota Motor, for example, alleviated some of the damage" in p3, "Text 3 end assertion failed"

p4 = passages[4]['content']
assert "Jennifer Senior's insightful, provocative magazine cover story" in p4, "Text 4 clean start assertion failed"
assert "single mothers like Bullock" in p4 and "gaping baby-size holes" in p4, "Text 4 restored paragraph 4 assertion failed"
assert "delight.99" not in p4 and "persistentlyd" not in p4, "Text 4 junk artifact assertion failed"

p5 = passages[5]['content']
assert "[A] No disciplines have seized" in p5 and "[G] The subtle and intelligent little book" in p5, "Part B assertion failed"

print("✓ All 6 Passages content and restoration assertions PASS")

# 3. Questions
questions = exam.get('questions', [])
assert len(questions) == 45, f"Question count mismatch: {len(questions)}"

official_answers = [
    # Cloze 1-20
    'C', 'D', 'B', 'B', 'A', 'B', 'A', 'D', 'C', 'A',
    'B', 'C', 'D', 'C', 'B', 'D', 'A', 'D', 'A', 'C',
    # Reading 21-40
    'C', 'B', 'D', 'B', 'A', 'B', 'D', 'C', 'A', 'C',
    'D', 'C', 'B', 'A', 'A', 'C', 'D', 'A', 'D', 'B',
    # New Type 41-45
    'B', 'D', 'A', 'C', 'F'
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
    assert len(exp) > 50, f"Q{q_num} explanation too short: {len(exp)}"
    if q_num <= 20:
        assert ('考点提炼' in exp or '解题思路' in exp), f"Q{q_num} cloze missing 考点提炼/解题思路"
    elif q_num <= 40:
        assert ('精准定位' in exp or '命题解密' in exp), f"Q{q_num} reading missing 精准定位/命题解密"
    else:
        assert ('考点' in exp or '选项' in exp or '答案敲定' in exp), f"Q{q_num} part_b missing 知识点/答案敲定"

assert abs(total_calc_score - 60.0) < 1e-6, f"Total score calculated mismatch: {total_calc_score}"
print(f"✓ All 45 Questions verified: points, sort_orders, 100% official answers, options format, explanations PASS")

# 4. Q25 and Q40 specific sanity checks
q25 = questions[24]
assert "feels" in q25.get('stem'), f"Q25 stem mismatch: {q25.get('stem')}"
assert q25.get('options')[0]['text'] == "doubtful", f"Q25 opt A mismatch: {q25.get('options')[0]}"
assert q25.get('correct_answer') == "A", f"Q25 ans mismatch: {q25.get('correct_answer')}"

q40 = questions[39]
assert q40.get('correct_answer') == "B", f"Q40 ans mismatch: {q40.get('correct_answer')}"
print("✓ Specific Q25 and Q40 key assertions PASS")

# 5. Long word adhesion check
valid_long_words = {
    'classical-music', 'sober-sided', 'unpretentious', 'instrumentalists', 'repertoire',
    'straightforward', 'unconventional', 'commodities', 'fundamentally', 'pronouncements',
    'communications', 'well-orchestrated', 'social-networking', 'dissatisfactions',
    'happiness-enhancing', 'moment-to-moment', 'soul-crushingly', 'kitten-killing',
    'professionalising', 'professionalised', 'professionalism', 'specialisation', 'professionalisation',
    'transmissible', 'transferable', 'exclusionary', 'monopolisation', 'anti-discrimination',
    'antidiscrimination', 'countermeasures'
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
print("★ 2011 ky1 Local Forensic Verification 100% PERFECT PASS! ★")
print("=======================================================")
