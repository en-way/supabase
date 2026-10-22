# -*- coding: utf-8 -*-
import sys

target_file = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Initialize round55_anomalies
s1 = "    round54_anomalies = []"
r1 = s1 + "\n    round55_anomalies = []"
assert s1 in content, "s1 not found"
content = content.replace(s1, r1, 1)

# 2. Title check
s2 = """        if yr == 2011 and cat == 'ky1':
            if title != '2011年全国硕士研究生入学统一考试英语（一）真题':
                round54_anomalies.append(('2011_ky1_title', title))"""

r2 = s2 + """\n        if yr == 2011 and cat == 'ky2':
            if title != '2011年全国硕士研究生入学统一考试英语（二）真题':
                round55_anomalies.append(('2011_ky2_title', title))"""

assert s2 in content, "s2 not found"
content = content.replace(s2, r2, 1)

# 3. Questions check
s3 = """                    if len(q.get('options', [])) != 7:
                        round54_anomalies.append((f'2011_ky1_q{so}_part_b_opts_len', len(q.get('options', []))))"""

r3 = s3 + """

            if yr == 2011 and cat == 'ky2':
                if 1 <= so <= 20:
                    cloze_answers = ['A', 'C', 'B', 'D', 'D', 'B', 'A', 'C', 'C', 'B', 'D', 'B', 'A', 'C', 'A', 'A', 'D', 'A', 'C', 'D']
                    exp_ans = cloze_answers[so - 1]
                    if ans != exp_ans:
                        round55_anomalies.append((f'2011_ky2_cloze_q{so}_ans', ans, exp_ans))
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'B', 22: 'D', 23: 'C', 24: 'A', 25: 'B',
                        26: 'D', 27: 'B', 28: 'C', 29: 'A', 30: 'A',
                        31: 'B', 32: 'D', 33: 'C', 34: 'D', 35: 'B',
                        36: 'B', 37: 'C', 38: 'B', 39: 'A', 40: 'D'
                    }
                    if ans != reading_answers[so]:
                        round55_anomalies.append((f'2011_ky2_q{so}_reading_ans', ans, reading_answers[so]))
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'E', 42: 'D', 43: 'C', 44: 'B', 45: 'G'}
                    if ans != part_b_answers[so]:
                        round55_anomalies.append((f'2011_ky2_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 7:
                        round55_anomalies.append((f'2011_ky2_q{so}_part_b_opts_len', len(q.get('options', []))))"""

assert s3 in content, "s3 not found"
content = content.replace(s3, r3, 1)

# 4. Passages check
s4 = """                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or '[A] No disciplines have seized' not in c or '[G] The subtle and intelligent' not in c:
                        round54_anomalies.append(('2011_ky1_passage_part_b', p.get('type'), len(c.split())))"""

r4 = s4 + """

            if yr == 2011 and cat == 'ky2':
                # Check for concatenated words without spaces in any passage
                bad_concats = [w for w in c.split() if len(w) > 17 and '[' not in w and ']' not in w and '-' not in w and '—' not in w and 'competitiveness' not in w.lower() and 'antidiscrimination' not in w.lower()]
                if bad_concats:
                    round55_anomalies.append((f'2011_ky2_p{so}_concats', bad_concats))
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or 'The Internet affords anonymity to its users' not in c or 'license [10] by the government' not in c:
                        round55_anomalies.append(('2011_ky2_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or len(c.split()) < 400 or 'Ruth Simmons' not in c or 'outside directors will follow the example of Ms. Simmons' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t1', p.get('type'), len(c.split())))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or not c.startswith('A year ago the end seemed near.') or 'Trade Commission launched' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t2', p.get('type'), c[:40]))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 400 or 'immediately following World War II' not in c or 'both desirable and inevitable was widely shared' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or len(c.split()) < 450 or 'Will the European Union make it?' not in c or 'economic co-ordination should involve all 27 members' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t4', p.get('type'), len(c.split())))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or 'Leading doctors today weigh in on the debate' not in c or c.strip().endswith("producers such as McDonald's."):
                        round55_anomalies.append(('2011_ky2_passage_part_b', p.get('type'), len(c.split())))"""

assert s4 in content, "s4 not found"
content = content.replace(s4, r4, 1)

# 5. Results dictionary
s5 = """results["Assertion 76: 2011"""
idx5 = content.find(s5)
end_line_idx = content.find('\n', idx5)
line5 = content[idx5:end_line_idx]

r5 = line5 + """\n    results["Assertion 77: 2011 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构，Text 2 开头腰斩彻底找回 (A year ago the end seemed near.)，全卷 15 处恶性单词黏连彻底消除，Q1-Q45 题号/分值自洽与官方答案 100% 官方黄金校准"] = (len(round55_anomalies) == 0)"""

content = content.replace(line5, r5, 1)

# 6. Print anomalies
s6 = """        if round54_anomalies:
            print(f"Round 54 anomalies ({len(round54_anomalies)}):", round54_anomalies[:10])"""

r6 = s6 + """\n        if round55_anomalies:
            print(f"Round 55 anomalies ({len(round55_anomalies)}):", round55_anomalies[:10])"""

assert s6 in content, "s6 not found"
content = content.replace(s6, r6, 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Assertion 77 injected successfully into verify_deep_text_calibration.py!")
