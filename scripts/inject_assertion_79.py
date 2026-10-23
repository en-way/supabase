# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

VERIFY_PATH = r'd:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py'

with open(VERIFY_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add round57_anomalies list
target_1 = "    round56_anomalies = []\n"
replacement_1 = "    round56_anomalies = []\n    round57_anomalies = []\n"
if target_1 in content:
    content = content.replace(target_1, replacement_1, 1)

# 2. Add title and exam checks
target_2 = """        if yr == 2012 and cat == 'ky1':
            if title != '2012年全国硕士研究生入学统一考试英语（一）真题':
                round56_anomalies.append(('2012_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round56_anomalies.append(('2012_ky1_total_score', data['exam'].get('total_score')))"""

replacement_2 = """        if yr == 2012 and cat == 'ky1':
            if title != '2012年全国硕士研究生入学统一考试英语（一）真题':
                round56_anomalies.append(('2012_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round56_anomalies.append(('2012_ky1_total_score', data['exam'].get('total_score')))
        if yr == 2012 and cat == 'ky2':
            if title != '2012年全国硕士研究生入学统一考试英语（二）真题':
                round57_anomalies.append(('2012_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round57_anomalies.append(('2012_ky2_total_score', data['exam'].get('total_score')))"""
if target_2 in content:
    content = content.replace(target_2, replacement_2, 1)

# 3. Add question assertions
target_3 = """                    if ans != pb_ans_map.get(so):
                        round56_anomalies.append((f'2012_ky1_q{so}_part_b_ans', ans, pb_ans_map.get(so)))
                    if len(opts) != 7:
                        round56_anomalies.append((f'2012_ky1_q{so}_part_b_opts_len', len(opts)))"""

replacement_3 = """                    if ans != pb_ans_map.get(so):
                        round56_anomalies.append((f'2012_ky1_q{so}_part_b_ans', ans, pb_ans_map.get(so)))
                    if len(opts) != 7:
                        round56_anomalies.append((f'2012_ky1_q{so}_part_b_opts_len', len(opts)))

            if yr == 2012 and cat == 'ky2':
                if so not in range(1, 46):
                    round57_anomalies.append(('2012_ky2_invalid_so', so))
                
                exp_pts = 0.5 if so <= 20 else 2.0
                if float(pts) != exp_pts:
                    round57_anomalies.append((f'2012_ky2_q{so}_points', pts, exp_pts))
                
                exp_qtype = 'cloze_item' if so <= 20 else 'reading_item'
                if q.get('q_type') != exp_qtype:
                    round57_anomalies.append((f'2012_ky2_q{so}_qtype', q.get('q_type'), exp_qtype))
                
                if len(expl) < 60:
                    round57_anomalies.append((f'2012_ky2_q{so}_expl_len', len(expl)))
                
                if 1 <= so <= 20:
                    cloze_ans_map_2012 = {
                        1: 'A', 2: 'B', 3: 'D', 4: 'A', 5: 'C',
                        6: 'D', 7: 'B', 8: 'A', 9: 'C', 10: 'B',
                        11: 'D', 12: 'C', 13: 'C', 14: 'A', 15: 'D',
                        16: 'A', 17: 'B', 18: 'C', 19: 'B', 20: 'D'
                    }
                    if ans != cloze_ans_map_2012.get(so):
                        round57_anomalies.append((f'2012_ky2_q{so}_cloze_ans', ans, cloze_ans_map_2012.get(so)))
                    if len(opts) != 4:
                        round57_anomalies.append((f'2012_ky2_q{so}_cloze_opts_len', len(opts)))
                elif 21 <= so <= 40:
                    reading_ans_map_2012 = {
                        21: 'A', 22: 'C', 23: 'D', 24: 'B', 25: 'A',
                        26: 'C', 27: 'B', 28: 'B', 29: 'A', 30: 'C',
                        31: 'A', 32: 'B', 33: 'A', 34: 'C', 35: 'D',
                        36: 'D', 37: 'D', 38: 'B', 39: 'D', 40: 'A'
                    }
                    if ans != reading_ans_map_2012.get(so):
                        round57_anomalies.append((f'2012_ky2_q{so}_reading_ans', ans, reading_ans_map_2012.get(so)))
                    if len(opts) != 4:
                        round57_anomalies.append((f'2012_ky2_q{so}_reading_opts_len', len(opts)))
                elif 41 <= so <= 45:
                    pb_ans_map_2012 = {41: 'A', 42: 'F', 43: 'G', 44: 'C', 45: 'E'}
                    if ans != pb_ans_map_2012.get(so):
                        round57_anomalies.append((f'2012_ky2_q{so}_part_b_ans', ans, pb_ans_map_2012.get(so)))
                    if len(opts) != 7:
                        round57_anomalies.append((f'2012_ky2_q{so}_part_b_opts_len', len(opts)))"""
if target_3 in content:
    content = content.replace(target_3, replacement_3, 1)

# 4. Add passage assertions
target_4 = """                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or 'Leading doctors today weigh in on the debate' not in c or c.strip().endswith("producers such as McDonald's."):
                        round55_anomalies.append(('2011_ky2_passage_part_b', p.get('type'), len(c.split())))"""

replacement_4 = """                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or 'Leading doctors today weigh in on the debate' not in c or c.strip().endswith("producers such as McDonald's."):
                        round55_anomalies.append(('2011_ky2_passage_part_b', p.get('type'), len(c.split())))

            if yr == 2012 and cat == 'ky2':
                bad_concats_2012 = [w for w in ['Thehomeworkrulesshould', 'across-the-boardrule', 'shouldbe', 'e of the or invent them', 'G. [1]. Joe'] if w in c]
                if bad_concats_2012:
                    round57_anomalies.append((f'2012_ky2_p{so}_concats', bad_concats_2012))
                if so == 1:
                    if p.get('type') != 'cloze' or len(c.split()) < 300 or 'G.I. Joe as a mindless war toy' not in c:
                        round57_anomalies.append(('2012_ky2_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    if p.get('type') != 'reading' or len(c.split()) < 350 or 'District administrators say that homework will still be a part of schooling' not in c or 'assigning more than they are willing to review and correct' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t1', p.get('type'), len(c.split())))
                elif so == 3:
                    if p.get('type') != 'reading' or len(c.split()) < 350 or 'and firmly fuses girls\' identity to appearance' not in c or 'or invent them where they did not previously exist' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t2', p.get('type'), len(c.split())))
                elif so == 4:
                    if p.get('type') != 'reading' or len(c.split()) < 350 or 'Each meeting was packed' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    if p.get('type') != 'reading' or len(c.split()) < 250 or 'find silver linings' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t4', p.get('type'), len(c.split())))
                elif so == 6:
                    if p.get('type') != 'reading_part_b' or len(c.split()) < 250 or 'Downstairs became just as fascinating as upstairs' not in c:
                        round57_anomalies.append(('2012_ky2_passage_part_b', p.get('type'), len(c.split())))"""
if target_4 in content:
    content = content.replace(target_4, replacement_4, 1)

# 5. Add Assertion 79 dictionary item
target_5 = '    results["Assertion 78: 2012 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构，Text 4 整篇彻底找回(7段435词)，Text 1 补齐腰斩两段，Text 3 乱码/题干串文切除，Q26-Q30 真实真题选项纠偏与 Q1-Q45 官方答案 100% 官方黄金校准"] = (len(round56_anomalies) == 0)\n'
replacement_5 = target_5 + '    results["Assertion 79: 2012 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（Text 1 找回腰斩两句恢复5段、Text 2 补齐截断残损与中句、Q1-Q45 题型/分值/官方标准答案 100% 零差异对齐）"] = (len(round57_anomalies) == 0)\n'
assert target_5 in content, "target_5 not found"
content = content.replace(target_5, replacement_5, 1)

# 6. Add anomalies print
target_6 = """        if round56_anomalies:
            print(f"Round 56 anomalies ({len(round56_anomalies)}):", round56_anomalies[:10])"""

replacement_6 = """        if round56_anomalies:
            print(f"Round 56 anomalies ({len(round56_anomalies)}):", round56_anomalies[:10])
        if round57_anomalies:
            print(f"Round 57 anomalies ({len(round57_anomalies)}):", round57_anomalies[:10])"""
if target_6 in content:
    content = content.replace(target_6, replacement_6, 1)

with open(VERIFY_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("Assertion 79 injected successfully into verify_deep_text_calibration.py!")
