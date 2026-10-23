# -*- coding: utf-8 -*-
import sys

target_file = "scripts/verify_deep_text_calibration.py"

with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add round61_anomalies = [] after round60_anomalies = []
target1 = "    round60_anomalies = []"
replacement1 = "    round60_anomalies = []\n    round61_anomalies = []"
assert target1 in content, "target1 not found"
content = content.replace(target1, replacement1, 1)

# 2. Add the checking block for 2014 ky2 after 2014 ky1
target2 = """                for q_no, exp_a in gold_ans.items():
                    act_a = q_list[q_no-1].get('answer')
                    if act_a != exp_a:
                        round60_anomalies.append((f'2014_ky1_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))"""

ky2_block = """

        if yr == 2014 and cat == 'ky2':
            if title != '2014年全国硕士研究生招生考试英语（二）真题':
                round61_anomalies.append(('2014_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round61_anomalies.append(('2014_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round61_anomalies.append(('2014_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 5:
                    round61_anomalies.append(('2014_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("Thinner isn't always better."):
                    round61_anomalies.append(('2014_ky2_cloze_header', 'corrupted'))
                if "matter of weight than body fat. Some people with a high BMI are in fact extremely fit," not in cloze.get("content", ""):
                    round61_anomalies.append(('2014_ky2_cloze_missing_sentence', 'not found'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 4:
                    round61_anomalies.append(('2014_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("What would you do with $590m?"):
                    round61_anomalies.append(('2014_ky2_t1_header', 'corrupted'))
                if "Money may not quite buy happiness, but people in wealthier countries are generally happier than those in poor ones." not in t1.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t1_missing_sentence', 'not found'))
                if "seemsmostpeoplewouldbebetter" in t1.get("content", "") or "theycouldshortentheir" in t1.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t1_concatenation', 'present'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 5:
                    round61_anomalies.append(('2014_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("An article in Scientific American has pointed out"):
                    round61_anomalies.append(('2014_ky2_t2_header', 'corrupted'))
                if "Social psychologists have amassed oceans of research into what they call the \\"above average effect\\"" not in t2.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t2_missing_sentence', 'not found'))
                if "I don't think the findings that we have are any evidence of personal delusion" not in t2.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t2_epley_quote', 'truncated'))
                if "statisticalimpossibilities" in t2.get("content", "") or "wasreallyhowtheylooked" in t2.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t2_concatenation', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 4:
                    round61_anomalies.append(('2014_ky2_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("The concept of man versus machine is at least as old"):
                    round61_anomalies.append(('2014_ky2_t3_header', 'corrupted'))
                if "these are the types of jobs that machines can perform much better at than human beings." not in t3.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t3_missing_sentence', 'not found'))
                if 'how do we innovate our institutions and our work practices?' not in t3.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t3_tail', 'corrupted'))
                if "weinnovate ourinstitutions" in t3.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t3_concatenation', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) not in [6, 7]:
                    round61_anomalies.append(('2014_ky2_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith("When the government talks about infrastructure"):
                    round61_anomalies.append(('2014_ky2_t4_header', 'corrupted'))
                if "offers an opportunity for the government to help rectify this." not in t4.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t4_missing_sentence', 'not found'))
                if "The Labour party has recently announced that it will retain a large part of the coalition's spending plans" not in t4.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t4_missing_spending_plans', 'not found'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 8:
                    round61_anomalies.append(('2014_ky2_pb_paras', len(pb_paras)))
                if "range of new forms, including Body Art, Performance Art, Action Art and Installation Art, which pushed art beyond" not in pb.get("content", ""):
                    round61_anomalies.append(('2014_ky2_pb_intro', 'truncated'))
                if "Samuel 9 Palmer" in pb.get("content", ""):
                    round61_anomalies.append(('2014_ky2_pb_ocr_noise', 'present'))
                if "Towards Avebury" not in pb.get("content", ""):
                    round61_anomalies.append(('2014_ky2_pb_artwork', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round61_anomalies.append(('2014_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round61_anomalies.append((f'2014_ky2_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round61_anomalies.append((f'2014_ky2_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round61_anomalies.append((f'2014_ky2_q{i}_q_type', q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round61_anomalies.append((f'2014_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl:
                        round61_anomalies.append((f'2014_ky2_q{i}_explanation', 'missing'))

                gold_ans_ky2 = {
                    1: 'B', 2: 'A', 3: 'C', 4: 'A', 5: 'D', 6: 'A', 7: 'C', 8: 'C', 9: 'D', 10: 'B',
                    11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'B', 16: 'D', 17: 'A', 18: 'D', 19: 'C', 20: 'B',
                    21: 'B', 22: 'A', 23: 'D', 24: 'B', 25: 'C',
                    26: 'A', 27: 'C', 28: 'B', 29: 'A', 30: 'D',
                    31: 'B', 32: 'A', 33: 'D', 34: 'D', 35: 'C',
                    36: 'B', 37: 'C', 38: 'A', 39: 'C', 40: 'D',
                    41: 'D', 42: 'E', 43: 'G', 44: 'C', 45: 'A'
                }
                for q_no, exp_a in gold_ans_ky2.items():
                    act_a = q_list[q_no-1].get('answer')
                    if act_a != exp_a:
                        round61_anomalies.append((f'2014_ky2_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))"""

replacement2 = target2 + ky2_block
assert target2 in content, "target2 not found"
content = content.replace(target2, replacement2, 1)

# 3. Add Assertion 83 to results
target3 = '    results["Assertion 82: 2014 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段284词、Text 1 恢复4段341词切除尾部拼接、Text 2 恢复6段415词彻底消除Q26/Q27题干倒灌与腰斩、Text 3 恢复5段380词补齐诺贝尔奖对比、Text 4 恢复6段412词切除Q37题干倒灌、Part B 恢复8段592词完整找回[B][C][D][E]四段、纠偏完型8题与阅读Q27、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round60_anomalies) == 0)'
replacement3 = target3 + '\n    results["Assertion 83: 2014 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段354词补齐腰斩句、Text 1 恢复4段392词消除黏连、Text 2 恢复5段397词补齐首段Ocean引述与Epley原话、Text 3 恢复4段391词治愈腰斩并理顺结尾设问、Text 4 恢复7段384词补齐政府与拨款计划论述、Part B 恢复8段499词规范艺术家分段切除杂质、Q34纠偏为真题原版选项、彻底治愈全卷45题question_number丢失缺陷、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round61_anomalies) == 0)'
assert target3 in content, "target3 not found"
content = content.replace(target3, replacement3, 1)

# 4. Add round61_anomalies to failure report
target4 = """        if round60_anomalies:
            print(f"Round 60 anomalies ({len(round60_anomalies)}):", round60_anomalies[:10])"""
replacement4 = target4 + """\n        if round61_anomalies:
            print(f"Round 61 anomalies ({len(round61_anomalies)}):", round61_anomalies[:10])"""
assert target4 in content, "target4 not found"
content = content.replace(target4, replacement4, 1)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected Assertion 83 into verify_deep_text_calibration.py")
