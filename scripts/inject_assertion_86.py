# -*- coding: utf-8 -*-
import sys

VERIFY_PATH = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"

with open(VERIFY_PATH, "r", encoding="utf-8") as f:
    content = f.read()

round64_block = """
        if yr == 2016 and cat == 'ky1':
            if title != '2016年全国硕士研究生招生考试英语（一）真题':
                round64_anomalies.append(('2016_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round64_anomalies.append(('2016_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round64_anomalies.append(('2016_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 3:
                    round64_anomalies.append(('2016_ky1_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith('In Cambodia, the choice of a spouse is a complex one for the young male.'):
                    round64_anomalies.append(('2016_ky1_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 7:
                    round64_anomalies.append(('2016_ky1_t1_paras', len(t1_paras)))
                if "France 9 which" in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_ocr_noise', 'France 9 which'))
                if "a couple of uplifting motiveso" in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_duplicate_phrase', 'uplifting motiveso'))
                if "The bans, if fully enforced, would suggest to women" not in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_missing_bans_sentence', 'not found'))
                if "Relying on ethical persuasion rather than law to address the misuse of body ideals" not in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_missing_para7', 'not found'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 6:
                    round64_anomalies.append(('2016_ky1_t2_paras', len(t2_paras)))
                if "showT" in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_ocr_showT', 'present'))
                if "At the next election none of the big parties seem likely to endorse this sentiment." not in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_missing_para3_start', 'not found'))
                if "struck terror into many local Conservative parties." not in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_missing_para3_end', 'not found'))
                if "concreted meadows n" in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_corrupted_quotes', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 6:
                    round64_anomalies.append(('2016_ky1_t3_paras', len(t3_paras)))
                if "causes it helps." in t3.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t3_duplicated_phrase', 'causes it helps.'))
                if ":Companies did not receive lower fines." in t3.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t3_duplicated_fines', 'present'))
                if "We estimate < record in CSRO" in t3.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t3_ocr_leak', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 7:
                    round64_anomalies.append(('2016_ky1_t4_paras', len(t4_paras)))
                if "There will eventually come a day when The New York Times ceases to publish" not in t4.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t4_header', 'corrupted'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 8:
                    round64_anomalies.append(('2016_ky1_pb_paras', len(pb_paras)))
                if "Directions:" in pb.get("content", ""):
                    round64_anomalies.append(('2016_ky1_pb_directions_leaked', 'present'))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"[{gap_num}] _________________________________" not in pb.get("content", ""):
                        round64_anomalies.append((f'2016_ky1_pb_gap_{gap_num}', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round64_anomalies.append(('2016_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round64_anomalies.append((f'2016_ky1_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round64_anomalies.append((f'2016_ky1_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round64_anomalies.append((f'2016_ky1_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round64_anomalies.append((f'2016_ky1_q{i}_placeholder_opt', opt_k))
                        if "once.... ..." in opt_v:
                            round64_anomalies.append(('2016_ky1_q20_corrupted_once', opt_v))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round64_anomalies.append((f'2016_ky1_q{i}_explanation', 'insufficient'))

                gold_ans_ky1_2016 = {
                    1: 'A', 2: 'D', 3: 'C', 4: 'A', 5: 'C', 6: 'B', 7: 'D', 8: 'B', 9: 'D', 10: 'A',
                    11: 'D', 12: 'C', 13: 'B', 14: 'B', 15: 'C', 16: 'A', 17: 'B', 18: 'D', 19: 'B', 20: 'A',
                    21: 'A', 22: 'D', 23: 'D', 24: 'C', 25: 'D',
                    26: 'A', 27: 'D', 28: 'C', 29: 'A', 30: 'C',
                    31: 'B', 32: 'C', 33: 'D', 34: 'A', 35: 'B',
                    36: 'A', 37: 'B', 38: 'B', 39: 'C', 40: 'B',
                    41: 'C', 42: 'F', 43: 'D', 44: 'E', 45: 'G'
                }
                for q_idx, exp_ans in gold_ans_ky1_2016.items():
                    act_ans = q_list[q_idx - 1].get('correct_answer') or q_list[q_idx - 1].get('answer')
                    if act_ans != exp_ans:
                        round64_anomalies.append((f'2016_ky1_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))
"""

target_loc = "round63_anomalies.append((f'2015_ky2_q{q_idx}_answer_mismatch', f'expected {exp_ans}, got {act_ans}'))"
if target_loc not in content:
    print("Error: target_loc not found")
    sys.exit(1)

content = content.replace(target_loc, target_loc + "\n" + round64_block)

# Add Assertion 86
assertion_85_target = 'results["Assertion 85: 2015 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段320词消除占位符残损、Text 1 恢复6段398词纠偏Q21为A及Q25为D、Text 2 恢复5段397词治愈引文格式与Q28真实选项纠偏、Text 3 恢复5段420词还原右脑修辞与团队导向论述消除黏连、Text 4 恢复6段427词消除黏连并还原医保核心失落句、Part B 恢复7段519词剔除OCR杂质并补齐44段社交陪伴完整句、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round63_anomalies) == 0)'

assertion_86_str = 'results["Assertion 86: 2016 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型规范3段理顺婚俗脉络、Text 1 恢复7段找回失落第7段并修复首句France注脚与第3段首句截断、Text 2 恢复6段找回第3段6句大篇失落句并剔除showT与倒灌题干、Text 3 恢复6段切除双重重复与OCR乱码并补全罚金论述、Text 4 恢复7段理顺奢侈品转型、Part B 恢复8段剥离指导语与选项、全卷45题question_number彻底自洽赋值1..45、纠偏Q24为真题原版选项、纠偏Q25为D及Q36为A及Q40为B、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round64_anomalies) == 0)'

content = content.replace(assertion_85_target, assertion_85_target + "\n    " + assertion_86_str)

# Add anomaly reporting
anomaly_reporting_target = 'if round63_anomalies:\n            print(f"Round 63 anomalies ({len(round63_anomalies)}):", round63_anomalies[:10])'
anomaly_reporting_add = 'if round64_anomalies:\n            print(f"Round 64 anomalies ({len(round64_anomalies)}):", round64_anomalies[:10])'

content = content.replace(anomaly_reporting_target, anomaly_reporting_target + "\n        " + anomaly_reporting_add)

with open(VERIFY_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected Assertion 86 into verify_deep_text_calibration.py")
