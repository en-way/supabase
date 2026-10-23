# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

VERIFY_SCRIPT = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"

with open(VERIFY_SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add round62_anomalies = [] after round61_anomalies = []
if "round62_anomalies = []" not in content:
    content = content.replace("round61_anomalies = []", "round61_anomalies = []\n    round62_anomalies = []")

# 2. Add round 62 verification logic after round 61 verification block
round62_check_code = '''
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
                if "The study [9] found that the genes for smell were something shared in friends but not genes for immunity." not in cloze.get("content", ""):
                    round62_anomalies.append(('2015_ky1_cloze_missing_sentence', 'not found'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 7:
                    round62_anomalies.append(('2015_ky1_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith('King Juan Carlos of Spain once insisted that "kings don\'t abdicate, they die in their sleep."'):
                    round62_anomalies.append(('2015_ky1_t1_header', 'corrupted'))
                if "It is this apparent transcendence of politics that explains monarchs' continuing popularity as heads of state." not in t1.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t1_missing_sentence', 'not found'))
                if "most royal families have survived because they allow voters to avoid the difficult search for a non-controversial but respected public figure." not in t1.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t1_restored_sentence', 'not found'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 7:
                    round62_anomalies.append(('2015_ky1_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("Just how much does the Constitution protect your digital data?"):
                    round62_anomalies.append(('2015_ky1_t2_header', 'corrupted'))
                if ". The Supreme Court will work out whether, during an arrest" in t2.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t2_hallucinated_stem', 'present'))
                if "The development of \\"cloud computing\\", meanwhile, has made that exploration so much the easier." not in t2.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t2_cloud_computing', 'missing'))
                if "In 1967 it ruled that wiretaps" in t2.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t2_hallucinated_wiretaps', 'present'))
                if "The justices had to specify novel rules for the new personal domain of the passenger car then; they must sort out how the Fourth Amendment applies to digital information now." not in t2.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t2_car_comparison', 'missing'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 6:
                    round62_anomalies.append(('2015_ky1_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("The journal Science is adding an extra round of statistical checks to its peer-review process"):
                    round62_anomalies.append(('2015_ky1_t3_header', 'corrupted'))
                if 'places that may want to model their approach after Science.' not in t3.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t3_parmigiani_quote', 'missing'))
                if "statistical review is more essential than expert review," not in t3.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t3_ioannidis_quote', 'missing'))
                if "it relies on the board of reviewing editors to identify the papers that need scrutiny in the first place." not in t3.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t3_clean_vaux_quote', 'missing'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 6:
                    round62_anomalies.append(('2015_ky1_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith('Two years ago, Rupert Murdoch\'s daughter, Elisabeth, spoke of the "unsettling dearth of integrity across so many of our institutions."'):
                    round62_anomalies.append(('2015_ky1_t4_header', 'corrupted'))
                if 'But "it\'s us, human beings, we the people who create the society we want, not profit."' not in t4.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t4_murdoch_quote', 'missing'))
                if "they take unwarranted risks, they undermine other values" in t4.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t4_hallucinated_paraphrase', 'present'))
                if "The purpose of editing the News of the World was not to promote reader understanding, to be fair in what was written or to betray any common humanity. It was to ruin lives in the quest for circulation and impact." not in t4.get("content", ""):
                    round62_anomalies.append(('2015_ky1_t4_authentic_purpose', 'missing'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 5:
                    round62_anomalies.append(('2015_ky1_pb_paras', len(pb_paras)))
                if "Directions:" in pb.get("content", ""):
                    round62_anomalies.append(('2015_ky1_pb_directions_in_text', 'present'))
                if "[A] Are we studying that text" in pb.get("content", ""):
                    round62_anomalies.append(('2015_ky1_pb_appended_options', 'present'))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"({gap_num})" not in pb.get("content", ""):
                        round62_anomalies.append((f'2015_ky1_pb_gap_{gap_num}', 'missing'))

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
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round62_anomalies.append((f'2015_ky1_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl:
                        round62_anomalies.append((f'2015_ky1_q{i}_explanation', 'missing'))

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
'''

# Find the end of round 61 block
r61_needle = "round61_anomalies.append((f'2014_ky2_q{q_idx}_answer_mismatch', f'expected {exp_ans}, got {act_ans}'))"
if "if yr == 2015 and cat == 'ky1':" not in content:
    idx_needle = content.find(r61_needle)
    if idx_needle != -1:
        end_of_line = content.find("\n", idx_needle)
        content = content[:end_of_line+1] + round62_check_code + content[end_of_line+1:]
        print("Injected Round 62 check code into loop.")

# 3. Add Assertion 84 to results dictionary
r83_needle = 'results["Assertion 83: 2014 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段354词补齐腰斩句、Text 1 恢复4段392词消除黏连、Text 2 恢复5段397词补齐首段Ocean引述与Epley原话、Text 3 恢复4段391词治愈腰斩并理顺结尾设问、Text 4 恢复7段384词补齐政府与拨款计划论述、Part B 恢复8段499词规范艺术家分段切除杂质、Q34纠偏为真题原版选项、彻底治愈全卷45题question_number丢失缺陷、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round61_anomalies) == 0)'
r84_line = 'results["Assertion 84: 2015 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段267词、Text 1 恢复7段410词补齐君主立宪选民服务论述、Text 2 恢复7段437词切除倒灌题干与伪造监听句并补齐云计算与汽车类比、Text 3 恢复6段438词还原Parmigiani/Ioannidis/Vaux三大权威引述、Text 4 恢复6段441词还原默多克之女讲话与审判真实表述、Part B 恢复5段324词剥离Directions与选项、Q22/Q32/Q38致命答案纠偏、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round62_anomalies) == 0)'

if "Assertion 84" not in content:
    idx_r83 = content.find(r83_needle)
    if idx_r83 != -1:
        end_r83 = content.find("\n", idx_r83)
        content = content[:end_r83+1] + "    " + r84_line + "\n" + content[end_r83+1:]
        print("Injected Assertion 84 into results dictionary.")

# 4. Add round62_anomalies failure print
r61_fail_needle = 'if round61_anomalies:\n            print(f"Round 61 anomalies ({len(round61_anomalies)}):", round61_anomalies[:10])'
r62_fail_code = 'if round62_anomalies:\n            print(f"Round 62 anomalies ({len(round62_anomalies)}):", round62_anomalies[:10])'

if "round62_anomalies" in content and "Round 62 anomalies" not in content:
    content = content.replace(r61_fail_needle, r61_fail_needle + "\n        " + r62_fail_code)
    print("Injected Round 62 failure print.")

with open(VERIFY_SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: verify_deep_text_calibration.py updated with Assertion 84.")
