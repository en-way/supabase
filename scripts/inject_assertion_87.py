# -*- coding: utf-8 -*-
"""
Inject Assertion 87 into verify_deep_text_calibration.py
"""

TARGET_FILE = r'd:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py'

def inject():
    with open(TARGET_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add round65_anomalies = [] after round64_anomalies = []
    target_1 = '    round64_anomalies = []\n'
    repl_1 = target_1 + '    round65_anomalies = []\n'
    assert target_1 in content, "target_1 not found"
    content = content.replace(target_1, repl_1, 1)

    # 2. Add round 65 check logic after round 64 check
    target_2 = """                for q_idx, exp_ans in gold_ans_ky1_2016.items():
                    act_ans = q_list[q_idx - 1].get('correct_answer') or q_list[q_idx - 1].get('answer')
                    if act_ans != exp_ans:
                        round64_anomalies.append((f'2016_ky1_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))"""

    repl_2 = target_2 + """

        if yr == 2016 and cat == 'ky2':
            if title != '2016年全国硕士研究生招生考试英语（二）真题':
                round65_anomalies.append(('2016_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round65_anomalies.append(('2016_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round65_anomalies.append(('2016_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 4:
                    round65_anomalies.append(('2016_ky2_cloze_paras', len(c_paras)))
                if "averagehappiness" in cloze.get("content", ""):
                    round65_anomalies.append(('2016_ky2_cloze_ocr_noise', 'averagehappiness'))
                if "The correlation between happiness and investment was particularly strong for younger" not in cloze.get("content", ""):
                    round65_anomalies.append(('2016_ky2_cloze_missing_text', 'younger firms'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 6:
                    round65_anomalies.append(('2016_ky2_t1_paras', len(t1_paras)))
                if "computer-science TOT classes" in t1.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t1_ocr_noise', 'computer-science TOT classes'))
                if "Programming languages have a short shelf life, and the ones Flatiron teaches may not even be relevant" not in t1.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t1_missing_shelf_life', 'not found'))
                if "learnthat" in t1.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t1_typo_learnthat', 'present'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 4:
                    round65_anomalies.append(('2016_ky2_t2_paras', len(t2_paras)))
                if "withfederal" in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_typo_withfederal', 'present'))
                if "privatelandowners" in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_typo_privatelandowners', 'present'))
                if "as part of their operations to pay into a fund to replace every acre of destroyed habitat with 2 new acres of suitable habitat." not in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_missing_fund_sentence', 'not found'))
                if "says Jay Lininger, a senior scientist at the Center for Biological Diversity." not in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_cut_off_ending', 'not found'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 4:
                    round65_anomalies.append(('2016_ky2_t3_paras', len(t3_paras)))
                if "theproblem" in t3.get("content", "") or "isthat" in t3.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t3_typo_squashed', 'present'))
                if "writes Gary Eberle in Sacred Time, “and we feel a pressure to fill these different-sized bottles" not in t3.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t3_missing_eberle_quote', 'not found'))
                if "helps us “step outside time's flow” into “soul time.” You might also consider reading only physical books" not in t3.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t3_missing_soul_time', 'not found'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 6:
                    round65_anomalies.append(('2016_ky2_t4_paras', len(t4_paras)))
                if "preferencestohousingpatternstopolitics" in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_typo_squashed', 'present'))
                if "affordablehousing" in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_typo_affordablehousing', 'present'))
                if "says he struggled to find a job after graduating from college." not in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_missing_schneider_struggle', 'not found'))
                if "to rent rooms out to people to make that happen.” Looking back, he is struck that his parents could provide a comfortable life" not in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_missing_schneider_parents', 'not found'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 7:
                    round65_anomalies.append(('2016_ky2_pb_paras', len(pb_paras)))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"[{gap_num}] _________________________________" not in pb.get("content", ""):
                        round65_anomalies.append((f'2016_ky2_pb_gap_{gap_num}', 'missing'))
                if "- n s move on" in pb.get("content", ""):
                    round65_anomalies.append(('2016_ky2_pb_mangled_ns', 'present'))
                if "What we need to do is find a way to acknowledge and express what we feel appropriately, and then move on." not in pb.get("content", ""):
                    round65_anomalies.append(('2016_ky2_pb_missing_express_sentence', 'not found'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round65_anomalies.append(('2016_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round65_anomalies.append((f'2016_ky2_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round65_anomalies.append((f'2016_ky2_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round65_anomalies.append((f'2016_ky2_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round65_anomalies.append((f'2016_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round65_anomalies.append((f'2016_ky2_q{i}_explanation', 'insufficient'))

                gold_ans_ky2_2016 = {
                    1: 'B', 2: 'B', 3: 'A', 4: 'C', 5: 'D', 6: 'B', 7: 'A', 8: 'D', 9: 'C', 10: 'A',
                    11: 'A', 12: 'C', 13: 'B', 14: 'D', 15: 'C', 16: 'D', 17: 'A', 18: 'C', 19: 'D', 20: 'B',
                    21: 'B', 22: 'B', 23: 'A', 24: 'C', 25: 'A',
                    26: 'A', 27: 'C', 28: 'A', 29: 'D', 30: 'C',
                    31: 'D', 32: 'B', 33: 'D', 34: 'A', 35: 'B',
                    36: 'B', 37: 'C', 38: 'D', 39: 'D', 40: 'C',
                    41: 'D', 42: 'F', 43: 'A', 44: 'B', 45: 'E'
                }
                for q_idx, exp_ans in gold_ans_ky2_2016.items():
                    act_ans = q_list[q_idx - 1].get('correct_answer') or q_list[q_idx - 1].get('answer')
                    if act_ans != exp_ans:
                        round65_anomalies.append((f'2016_ky2_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))"""

    assert target_2 in content, "target_2 not found"
    content = content.replace(target_2, repl_2, 1)

    # 3. Add Assertion 87 to results dictionary
    target_3 = '    results["Assertion 86: 2016 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型规范3段理顺婚俗脉络、Text 1 恢复7段找回失落第7段并修复首句France注脚与第3段首句截断、Text 2 恢复6段找回第3段6句大篇失落句并剔除showT与倒灌题干、Text 3 恢复6段切除双重重复与OCR乱码并补全罚金论述、Text 4 恢复7段理顺奢侈品转型、Part B 恢复8段剥离指导语与选项、全卷45题question_number彻底自洽赋值1..45、纠偏Q24为真题原版选项、纠偏Q25为D及Q36为A及Q40为B、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round64_anomalies) == 0)\n'
    repl_3 = target_3 + '    results["Assertion 87: 2016 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段并补齐年轻企业关联句、Text 1 恢复6段修复101班级与shelf life、Text 2 恢复4段补齐栖息地补偿金论述与Lininger引述、Text 3 恢复4段补全Eberle空瓶子比喻与灵魂时间、Text 4 恢复6段理顺里程碑与Schneider失落求职句、Part B 恢复7段切除乱码-ns与补齐情绪宣泄句、全卷45题question_number自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round65_anomalies) == 0)\n'

    assert target_3 in content, "target_3 not found"
    content = content.replace(target_3, repl_3, 1)

    # 4. Add summary anomaly print
    target_4 = """        if round64_anomalies:
            print(f"Round 64 anomalies ({len(round64_anomalies)}):", round64_anomalies[:10])"""

    repl_4 = target_4 + """
        if round65_anomalies:
            print(f"Round 65 anomalies ({len(round65_anomalies)}):", round65_anomalies[:10])"""

    assert target_4 in content, "target_4 not found"
    content = content.replace(target_4, repl_4, 1)

    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully injected Assertion 87 into verify_deep_text_calibration.py!")

if __name__ == '__main__':
    inject()
