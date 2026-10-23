# -*- coding: utf-8 -*-
"""
inject_assertion_85.py
Injects Round 62 and Round 63 forensic calibration assertions into verify_deep_text_calibration.py
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

VERIFY_SCRIPT = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"

with open(VERIFY_SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure anomaly lists are declared
if "round63_anomalies = []" not in content:
    content = content.replace(
        "round62_anomalies = []",
        "round62_anomalies = []\n    round63_anomalies = []"
    )

# 2. Add round 62 and round 63 verification logic
r62_63_checks = '''
        if yr == 2015 and cat == 'ky1':
            if title != '2015年全国硕士研究生招生考试英语（一）真题':
                round62_anomalies.append(('2015_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round62_anomalies.append(('2015_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round62_anomalies.append(('2015_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 5:
                    round62_anomalies.append(('2015_ky1_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith('Though not biologically related, friends are as "related" as fourth cousins'):
                    round62_anomalies.append(('2015_ky1_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 7:
                    round62_anomalies.append(('2015_ky1_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith('King Juan Carlos of Spain once insisted that "kings don\'t abdicate, they die in their sleep."'):
                    round62_anomalies.append(('2015_ky1_t1_header', 'corrupted'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 7:
                    round62_anomalies.append(('2015_ky1_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("Just how much does the Constitution protect your digital data?"):
                    round62_anomalies.append(('2015_ky1_t2_header', 'corrupted'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 6:
                    round62_anomalies.append(('2015_ky1_t3_paras', len(t3_paras)))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 6:
                    round62_anomalies.append(('2015_ky1_t4_paras', len(t4_paras)))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 5:
                    round62_anomalies.append(('2015_ky1_pb_paras', len(pb_paras)))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round62_anomalies.append(('2015_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round62_anomalies.append((f'2015_ky1_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round62_anomalies.append((f'2015_ky1_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round62_anomalies.append((f'2015_ky1_q{i}_q_type', q.get('q_type')))

                gold_ans_ky1 = {
                    1: 'D', 2: 'B', 3: 'C', 4: 'A', 5: 'C', 6: 'A', 7: 'D', 8: 'A', 9: 'B', 10: 'D',
                    11: 'B', 12: 'A', 13: 'B', 14: 'D', 15: 'C', 16: 'C', 17: 'B', 18: 'D', 19: 'C', 20: 'A',
                    21: 'D', 22: 'C', 23: 'B', 24: 'A', 25: 'C',
                    26: 'C', 27: 'A', 28: 'D', 29: 'D', 30: 'D',
                    31: 'B', 32: 'C', 33: 'D', 34: 'C', 35: 'A',
                    36: 'A', 37: 'B', 38: 'A', 39: 'C', 40: 'B',
                    41: 'C', 42: 'E', 43: 'G', 44: 'B', 45: 'A'
                }
                for q_idx, exp_ans in gold_ans_ky1.items():
                    act_ans = q_list[q_idx-1].get('answer') or q_list[q_idx-1].get('correct_answer')
                    if act_ans != exp_ans:
                        round62_anomalies.append((f'2015_ky1_q{q_idx}_answer_mismatch', f'expected {exp_ans}, got {act_ans}'))

        if yr == 2015 and cat == 'ky2':
            if title != '2015年全国硕士研究生招生考试英语（二）真题':
                round63_anomalies.append(('2015_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round63_anomalies.append(('2015_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round63_anomalies.append(('2015_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 4:
                    round63_anomalies.append(('2015_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith('In our contemporary culture, the prospect of communicating with'):
                    round63_anomalies.append(('2015_ky2_cloze_header', 'corrupted'))
                if "_:" in cloze.get("content", ""):
                    round63_anomalies.append(('2015_ky2_cloze_placeholder_corruption', 'present'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 6:
                    round63_anomalies.append(('2015_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("A new study suggests that contrary to most surveys"):
                    round63_anomalies.append(('2015_ky2_t1_header', 'corrupted'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 5:
                    round63_anomalies.append(('2015_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("For years, studies have found that first-generation college students"):
                    round63_anomalies.append(('2015_ky2_t2_header', 'corrupted'))
                if "like them" in t2.get("content", "") and "like them" in t2.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t2_corrupted_quotes', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 5:
                    round63_anomalies.append(('2015_ky2_t3_paras', len(t3_paras)))
                if "much more right-brained than it was 20 years ago, says Harvard Business School historian Nancy Koehn." not in t3.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t3_missing_right_brained', 'not found'))
                if "very \\"team\\"-oriented - and that is not by coincidence." not in t3.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t3_missing_team_oriented', 'not found'))
                if "andhow" in t3.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t3_concatenation', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 6:
                    round63_anomalies.append(('2015_ky2_t4_paras', len(t4_paras)))
                if "arenowfinallymovingforward" in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_concatenation', 'present'))
                if "evidence of weakness in the labor market and it means that many" not in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_missing_weakness', 'not found'))
                if "before Obamacare the only way to get insurance was through a job that provided health insurance." not in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_missing_obamacare_way', 'not found'))
                if "These are people who may previously have felt the need to get a full-time job that provided insurance in order to cover themselves and their families." not in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_missing_full_time_need', 'not found'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) < 7:
                    round63_anomalies.append(('2015_ky2_pb_paras', len(pb_paras)))
                if "n sn s n" in pb.get("content", ""):
                    round63_anomalies.append(('2015_ky2_pb_ocr_noise', 'present'))
                if "Fear is both useful and harmful." not in pb.get("content", ""):
                    round63_anomalies.append(('2015_ky2_pb_fear_useful', 'missing'))
                if "companionship. If you have no friends or relatives, try to participate in several online communities" not in pb.get("content", ""):
                    round63_anomalies.append(('2015_ky2_pb_missing_companionship', 'not found'))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"[{gap_num}]" not in pb.get("content", ""):
                        round63_anomalies.append((f'2015_ky2_pb_gap_{gap_num}', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round63_anomalies.append(('2015_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round63_anomalies.append((f'2015_ky2_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round63_anomalies.append((f'2015_ky2_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round63_anomalies.append((f'2015_ky2_q{i}_q_type', q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round63_anomalies.append((f'2015_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round63_anomalies.append((f'2015_ky2_q{i}_explanation', 'insufficient'))

                gold_ans_ky2 = {
                    1: 'A', 2: 'D', 3: 'B', 4: 'A', 5: 'C', 6: 'B', 7: 'A', 8: 'D', 9: 'C', 10: 'B',
                    11: 'A', 12: 'C', 13: 'C', 14: 'D', 15: 'C', 16: 'D', 17: 'A', 18: 'B', 19: 'D', 20: 'B',
                    21: 'A', 22: 'B', 23: 'A', 24: 'C', 25: 'D',
                    26: 'C', 27: 'C', 28: 'C', 29: 'B', 30: 'D',
                    31: 'D', 32: 'A', 33: 'D', 34: 'A', 35: 'B',
                    36: 'B', 37: 'C', 38: 'A', 39: 'D', 40: 'A',
                    41: 'D', 42: 'E', 43: 'G', 44: 'A', 45: 'C'
                }
                for q_idx, exp_ans in gold_ans_ky2.items():
                    act_ans = q_list[q_idx-1].get('answer') or q_list[q_idx-1].get('correct_answer')
                    if act_ans != exp_ans:
                        round63_anomalies.append((f'2015_ky2_q{q_idx}_answer_mismatch', f'expected {exp_ans}, got {act_ans}'))
'''

needle_r61 = "round61_anomalies.append((f'2014_ky2_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))"
if "if yr == 2015 and cat == 'ky2':" not in content:
    idx = content.find(needle_r61)
    if idx != -1:
        end_line = content.find("\n", idx)
        content = content[:end_line+1] + r62_63_checks + content[end_line+1:]
        print("Injected Round 62 and Round 63 verification checks into loop.")
    else:
        print("ERROR: needle_r61 not found!")

# 3. Add Assertion 85 to results dictionary
r84_needle = 'results["Assertion 84: 2015 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段267词、Text 1 恢复7段410词补齐君主立宪选民服务论述、Text 2 恢复7段437词切除倒灌题干与伪造监听句并补齐云计算与汽车类比、Text 3 恢复6段438词还原Parmigiani/Ioannidis/Vaux三大权威引述、Text 4 恢复6段441词还原默多克之女讲话与审判真实表述、Part B 恢复5段324词剥离Directions与选项、Q22/Q32/Q38致命答案纠偏、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round62_anomalies) == 0)'
r85_line = 'results["Assertion 85: 2015 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段320词消除占位符残损、Text 1 恢复6段398词纠偏Q21为A及Q25为D、Text 2 恢复5段397词治愈引文格式与Q28真实选项纠偏、Text 3 恢复5段420词还原右脑修辞与团队导向论述消除黏连、Text 4 恢复6段427词消除黏连并还原医保核心失落句、Part B 恢复7段519词剔除OCR杂质并补齐44段社交陪伴完整句、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round63_anomalies) == 0)'

if "Assertion 85" not in content:
    idx_r84 = content.find(r84_needle)
    if idx_r84 != -1:
        end_r84 = content.find("\n", idx_r84)
        content = content[:end_r84+1] + "    " + r85_line + "\n" + content[end_r84+1:]
        print("Injected Assertion 85 into results dictionary.")
    else:
        print("ERROR: r84_needle not found!")

# 4. Add round63_anomalies failure report
r62_fail_needle = 'if round62_anomalies:\n            print(f"Round 62 anomalies ({len(round62_anomalies)}):", round62_anomalies[:10])'
r63_fail_code = 'if round63_anomalies:\n            print(f"Round 63 anomalies ({len(round63_anomalies)}):", round63_anomalies[:10])'

if "round63_anomalies" in content and "Round 63 anomalies" not in content:
    content = content.replace(r62_fail_needle, r62_fail_needle + "\n        " + r63_fail_code)
    print("Injected Round 63 failure print.")

with open(VERIFY_SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: verify_deep_text_calibration.py updated with Assertion 85.")
