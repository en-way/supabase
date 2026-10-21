import json

with open('public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Verifying 2007 Calibrated JSON:")
assert len(d['passages']) == 6, f"Expected 6 passages, got {len(d['passages'])}"
assert d['passages'][0]['type'] == 'cloze' and d['passages'][0]['passage_number'] == 1
assert d['passages'][1]['type'] == 'reading' and d['passages'][1]['passage_number'] == 1
assert d['passages'][2]['type'] == 'reading' and d['passages'][2]['passage_number'] == 2
assert d['passages'][3]['type'] == 'reading' and d['passages'][3]['passage_number'] == 3
assert d['passages'][4]['type'] == 'reading' and d['passages'][4]['passage_number'] == 4
assert d['passages'][5]['type'] == 'reading_part_b' and d['passages'][5]['passage_number'] == 5

# Check Text 3
p3 = d['passages'][3]['content']
assert "During the past generation, the American middle-class family" in p3, "Text 3 missing opening"
assert "From the middle-class family perspective" in p3, "Text 3 missing concluding para"
assert len(p3.split()) >= 420, f"Text 3 word count unexpected: {len(p3.split())}"

# Check questions
assert len(d['questions']) == 45, f"Expected 45 questions, got {len(d['questions'])}"
for i in range(45):
    q = d['questions'][i]
    assert q['question_number'] == i + 1, f"Q{i+1} number mismatch: {q.get('question_number')}"
    if 21 <= i + 1 <= 40:
        assert q['explanation'].startswith("［"), f"Q{i+1} explanation does not start with ［: {q['explanation'][:30]}"
    if i + 1 == 31:
        opt_b = [opt['text'] for opt in q['options'] if opt['key'] == 'B'][0]
        assert "their chances of being laid off" in opt_b, f"Q31 opt B truncated: {opt_b}"
    if i + 1 in [32, 37, 38]:
        assert "［精准定位］" in q['explanation'] and "［命题解密］" in q['explanation'], f"Q{i+1} explanation missing standard blocks"
    if 41 <= i + 1 <= 45:
        assert "［标题匹配］" in q['explanation'] and "［干扰项排除］" in q['explanation'], f"Q{i+1} explanation missing standard blocks"

print("ALL 2007 CALIBRATION CHECKS PASSED PERFECTLY!")
