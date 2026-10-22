# -*- coding: utf-8 -*-
import sys

target_file = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title check
s1 = """        if yr == 2010 and cat == 'ky2':
            if title != '2010年全国硕士研究生入学统一考试英语（二）真题':
                round53_anomalies.append(('2010_ky2_title', title))"""

r1 = """        if yr == 2010 and cat == 'ky2':
            if title != '2010年全国硕士研究生入学统一考试英语（二）真题':
                round53_anomalies.append(('2010_ky2_title', title))
        if yr == 2011 and cat == 'ky1':
            if title != '2011年全国硕士研究生入学统一考试英语（一）真题':
                round54_anomalies.append(('2011_ky1_title', title))"""

assert s1 in content, "s1 not found"
content = content.replace(s1, r1, 1)

# 2. Questions check
s2 = """                elif 41 <= so <= 45:
                    part_b_answers = {41: 'F', 42: 'T', 43: 'F', 44: 'T', 45: 'F'}
                    if ans != part_b_answers[so]:
                        round53_anomalies.append((f'2010_ky2_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 2:
                        round53_anomalies.append((f'2010_ky2_q{so}_part_b_opts_len', len(q.get('options', []))))
                    if not expl.startswith('［精准定位］') or '［命题解密］' not in expl:
                        round53_anomalies.append((f'2010_ky2_q{so}_part_b_expl', expl[:40]))"""

r2 = s2 + """

            if yr == 2011 and cat == 'ky1':
                if 1 <= so <= 20:
                    cloze_answers = ['C', 'D', 'B', 'B', 'A', 'B', 'A', 'D', 'C', 'A', 'B', 'C', 'D', 'C', 'B', 'D', 'A', 'D', 'A', 'C']
                    exp_ans = cloze_answers[so - 1]
                    if ans != exp_ans:
                        round54_anomalies.append((f'2011_ky1_cloze_q{so}_ans', ans, exp_ans))
                    if '考点提炼' not in expl:
                        round54_anomalies.append((f'2011_ky1_cloze_q{so}_expl_kd', expl[:40]))
                    if '解题思路' not in expl:
                        round54_anomalies.append((f'2011_ky1_cloze_q{so}_expl_sl', expl[:40]))
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'C', 22: 'B', 23: 'D', 24: 'B', 25: 'A',
                        26: 'B', 27: 'D', 28: 'C', 29: 'A', 30: 'C',
                        31: 'D', 32: 'C', 33: 'B', 34: 'A', 35: 'A',
                        36: 'C', 37: 'D', 38: 'A', 39: 'D', 40: 'B'
                    }
                    if ans != reading_answers[so]:
                        round54_anomalies.append((f'2011_ky1_q{so}_reading_ans', ans, reading_answers[so]))
                    if not expl.startswith('［精准定位］'):
                        round54_anomalies.append((f'2011_ky1_q{so}_reading_expl_start', expl[:40]))
                    if '［命题解密］' not in expl:
                        round54_anomalies.append((f'2011_ky1_q{so}_reading_expl_decrypt', expl[:40]))
                    if so == 25:
                        if 'feels' not in q.get('stem', '') or q.get('options', [])[0].get('text') != 'doubtful':
                            round54_anomalies.append(('2011_ky1_q25_stem_opts', q.get('stem')))
                    if so == 40 and ans != 'B':
                        round54_anomalies.append(('2011_ky1_q40_ans_not_b', ans))
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'B', 42: 'D', 43: 'A', 44: 'C', 45: 'F'}
                    if ans != part_b_answers[so]:
                        round54_anomalies.append((f'2011_ky1_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 7:
                        round54_anomalies.append((f'2011_ky1_q{so}_part_b_opts_len', len(q.get('options', []))))"""

assert s2 in content, "s2 not found"
content = content.replace(s2, r2, 1)

# 3. Passages check
s3 = """                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or 'Directions:' in c or 'Copying Birds' not in c:
                        round53_anomalies.append(('2010_ky2_passage_part_b', p.get('type'), p.get('passage_number')))"""

r3 = s3 + """

            if yr == 2011 and cat == 'ky1':
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or 'Aristotle viewed laughter' not in c or 'flow [15] muscular responses' not in c:
                        round54_anomalies.append(('2011_ky1_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or len(c.split()) < 400 or 'Alan Gilbert' not in c or "change the relationship between America's oldest orchestra and the new audience" not in c:
                        round54_anomalies.append(('2011_ky1_passage_t1', p.get('type'), len(c.split())))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or len(c.split()) < 400 or 'Liam McGee' not in c or "The people who've been hurt the worst are those who've stayed too long" not in c:
                        round54_anomalies.append(('2011_ky1_passage_t2', p.get('type'), len(c.split())))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 420 or 'The rough guide to marketing success used to be that you got what you paid for.' not in c or 'Toyota Motor, for example, alleviated some of the damage' not in c:
                        round54_anomalies.append(('2011_ky1_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or len(c.split()) < 430 or 'single mothers like Bullock' not in c or 'delight.99' in c or 'persistentlyd' in c:
                        round54_anomalies.append(('2011_ky1_passage_t4', p.get('type'), len(c.split())))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or '[A] No disciplines have seized' not in c or '[G] The subtle and intelligent' not in c:
                        round54_anomalies.append(('2011_ky1_passage_part_b', p.get('type'), len(c.split())))"""

assert s3 in content, "s3 not found"
content = content.replace(s3, r3, 1)

# 4. Results dictionary
s4 = """results["Assertion 75: 2010"""
# find where results["Assertion 75 ends
idx4 = content.find(s4)
end_line_idx = content.find('\n', idx4)
line4 = content[idx4:end_line_idx]

r4 = line4 + """\n    results["Assertion 76: 2011 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构，Text 3 首部腰斩彻底找回，Text 4 丢失段落补齐与生词残片消除，Q25 官方原版题干选项校准，Q40 官方答案锁定与 Q1-Q45 黄金三段论精解 100% 官方黄金校准"] = (len(round54_anomalies) == 0)"""

content = content.replace(line4, r4, 1)

# 5. Print anomalies
s5 = """        if round53_anomalies:
            print(f"Round 53 anomalies ({len(round53_anomalies)}):", round53_anomalies[:10])"""

r5 = s5 + """\n        if round54_anomalies:
            print(f"Round 54 anomalies ({len(round54_anomalies)}):", round54_anomalies[:10])"""

assert s5 in content, "s5 not found"
content = content.replace(s5, r5, 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Assertion 76 injected successfully into verify_deep_text_calibration.py!")
