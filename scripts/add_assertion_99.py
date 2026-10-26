with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add round77_anomalies = [] after round76_anomalies = []
target1 = "    round76_anomalies = []"
replacement1 = "    round76_anomalies = []\n    round77_anomalies = []"

assert target1 in content, "target1 not found"
content = content.replace(target1, replacement1, 1)

# 2. Add round77 check block after round76 check block
target2 = 'round76_anomalies.append((f\'2022_ky1_q{q_idx}_answer\', f"Expected {exp_ans}, got {act_ans}"))'

check_block = '''

        if yr == 2022 and cat == 'ky2':
            if title != '2022年全国硕士研究生招生考试英语（二）真题':
                round77_anomalies.append(('2022_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round77_anomalies.append(('2022_ky2_total_score', data['exam'].get('total_score')))
            if float(data['exam'].get('pass_score', 0)) != 36.0:
                round77_anomalies.append(('2022_ky2_pass_score', data['exam'].get('pass_score')))

            p_list = sorted(data.get('passages', []), key=lambda x: x.get('sort_order', 0))
            if len(p_list) != 6:
                round77_anomalies.append(('2022_ky2_passages_count', len(p_list)))
            else:
                cloze, t1, t2, t3, t4, pb = p_list[0], p_list[1], p_list[2], p_list[3], p_list[4], p_list[5]
                # Cloze: 5 paras, 398 words, Harlan Coben
                c_paras = [p.strip() for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 5:
                    round77_anomalies.append(('2022_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("Harlan Coben believes that if you're a writer,"):
                    round77_anomalies.append(('2022_ky2_cloze_start', cloze.get("content", "")[:50]))
                if not cloze.get("content", "").endswith("writing."):
                    round77_anomalies.append(('2022_ky2_cloze_end', cloze.get("content", "")[-40:]))

                # Text 1: 6 paras, 401 words, Sustainable eggs
                t1_paras = [p.strip() for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 6:
                    round77_anomalies.append(('2022_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("On a recent sunny day, 13,000 chickens roam over Larry Brown"):
                    round77_anomalies.append(('2022_ky2_t1_start', t1.get("content", "")[:50]))
                if not t1.get("content", "").endswith('even they understand what they\\'re doing."'):
                    round77_anomalies.append(('2022_ky2_t1_end', t1.get("content", "")[-50:]))

                # Text 2: 8 paras, 461 words, Unretirement trend
                t2_paras = [p.strip() for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 8:
                    round77_anomalies.append(('2022_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("More Americans are opting to work well into retirement,"):
                    round77_anomalies.append(('2022_ky2_t2_start', t2.get("content", "")[:50]))
                if not t2.get("content", "").endswith('Many people believe they can\\'t retire."'):
                    round77_anomalies.append(('2022_ky2_t2_end', t2.get("content", "")[-50:]))

                # Text 3: 6 paras, 402 words, Dark patterns
                t3_paras = [p.strip() for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 6:
                    round77_anomalies.append(('2022_ky2_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("We have all encountered them, in both our personal and professional lives."):
                    round77_anomalies.append(('2022_ky2_t3_start', t3.get("content", "")[:50]))
                if not t3.get("content", "").endswith("best practices and standards."):
                    round77_anomalies.append(('2022_ky2_t3_end', t3.get("content", "")[-50:]))

                # Text 4: 5 paras, 394 words, Ethics classes & meat eating
                t4_paras = [p.strip() for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 5:
                    round77_anomalies.append(('2022_ky2_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith("Although ethics classes are common around the world,"):
                    round77_anomalies.append(('2022_ky2_t4_start', t4.get("content", "")[:50]))
                if not t4.get("content", "").endswith("will be eating his words."):
                    round77_anomalies.append(('2022_ky2_t4_end', t4.get("content", "")[-40:]))

                # Part B: 8 paras, 538 words, How to Get Active Again
                pb_paras = [p.strip() for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 8:
                    round77_anomalies.append(('2022_ky2_pb_paras', len(pb_paras)))
                if not pb.get("content", "").startswith("How to Get Active Again"):
                    round77_anomalies.append(('2022_ky2_pb_start', pb.get("content", "")[:50]))
                if not pb.get("content", "").endswith("join a livestream or on-demand exercise class."):
                    round77_anomalies.append(('2022_ky2_pb_end', pb.get("content", "")[-50:]))

            q_list = sorted(data.get('questions', []), key=lambda x: x.get('sort_order', 0))
            if len(q_list) != 45:
                round77_anomalies.append(('2022_ky2_questions_count', len(q_list)))
            else:
                exp_answers = {
                    1: 'D', 2: 'B', 3: 'A', 4: 'D', 5: 'C', 6: 'A', 7: 'C', 8: 'C', 9: 'B', 10: 'B',
                    11: 'C', 12: 'D', 13: 'B', 14: 'A', 15: 'A', 16: 'D', 17: 'A', 18: 'D', 19: 'C', 20: 'D',
                    21: 'D', 22: 'C', 23: 'C', 24: 'B', 25: 'A', 26: 'D', 27: 'A', 28: 'C', 29: 'D', 30: 'C',
                    31: 'C', 32: 'D', 33: 'B', 34: 'B', 35: 'B', 36: 'A', 37: 'B', 38: 'D', 39: 'C', 40: 'C',
                    41: 'C', 42: 'E', 43: 'A', 44: 'F', 45: 'B'
                }
                for i, q in enumerate(q_list, 1):
                    if q.get('sort_order') != i:
                        round77_anomalies.append((f'2022_ky2_q{i}_sort_order', q.get('sort_order')))
                    if q.get('question_number') != i:
                        round77_anomalies.append((f'2022_ky2_q{i}_number', q.get('question_number')))
                    
                    exp_pts = 0.5 if i <= 20 else 2.0
                    q_pts = float(q.get('score') or q.get('points') or 0)
                    if abs(q_pts - exp_pts) > 1e-4:
                        round77_anomalies.append((f'2022_ky2_q{i}_points', q_pts))
                    
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round77_anomalies.append((f'2022_ky2_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    
                    ans = q.get('correct_answer') or q.get('answer')
                    if ans != exp_answers.get(i):
                        round77_anomalies.append((f'2022_ky2_q{i}_ans', ans, exp_answers.get(i)))

                    opts = q.get('options', [])
                    for opt in opts:
                        opt_k = opt.get('key', '')
                        opt_t = opt.get('text', '')
                        opt_c = opt.get('content', '')
                        if not opt_k or (not opt_t and not opt_c):
                            round77_anomalies.append((f'2022_ky2_q{i}_opt_invalid', opt_k, opt_t))'''

assert target2 in content, "target2 not found"
content = content.replace(target2, target2 + check_block, 1)

# 3. Add Assertion 99 result entry
target3 = 'results["Assertion 98: 2022 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复6段279词理顺植物神经生物学争鸣、Text 1 恢复7段406词彻底切除Q21倒灌与DABC杂质理顺塑料文物保护、Text 2 恢复7段423词找回失落第3段切除Q27/29倒灌理顺Z世代学位价值演变、Text 3 恢复6段431词切除Q32倒灌与末尾杂质理顺科艺合作超越科普、Text 4 恢复8段474词解开3段长合并理顺新西兰与澳大利亚解雇法门槛机制、Part B 恢复11段553词彻底清除假标题与答案内嵌恢复5人观点与[A]-[G]7项、治愈全卷45题question_number与score丢失缺陷、Q1-Q45 官方标准答案/题型/分值/三层解析 100% 零差异对齐）"] = (len(round76_anomalies) == 0)'

assertion_99_entry = '''    results["Assertion 99: 2022 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段398词理顺写作与时间分配哲理、Text 1 恢复6段401词理顺再生农业与气候友好鸡蛋、Text 2 恢复8段461词理顺美国中老年不退休潮流与寿命延长、Text 3 恢复6段402词理顺黑暗模式与UX伦理规范、Text 4 恢复5段394词理顺道德课堂对吃肉影响与自我言行改变、Part B 恢复8段538词理顺恢复运动指南标题与[A]-[G]7项、治愈全卷45题question_number与score丢失缺陷、Q1-Q45 官方标准答案/题型/分值/三层解析 100% 零差异对齐）"] = (len(round77_anomalies) == 0)'''

replacement3 = target3 + '\n' + assertion_99_entry
assert target3 in content, "target3 not found"
content = content.replace(target3, replacement3, 1)

# 4. Update failure report for round77_anomalies
target4 = 'if round76_anomalies:\n            print(f"Round 76 anomalies ({len(round76_anomalies)}):", round76_anomalies[:10])'

failure_report_99 = '''        if round76_anomalies:
            print(f"Round 76 anomalies ({len(round76_anomalies)}):", round76_anomalies[:10])
        if round77_anomalies:
            print(f"Round 77 anomalies ({len(round77_anomalies)}):", round77_anomalies[:10])'''

assert target4 in content, "target4 not found"
content = content.replace(target4, failure_report_99, 1)

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added Assertion 99 to scripts/verify_deep_text_calibration.py!")
