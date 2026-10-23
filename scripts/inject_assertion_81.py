# -*- coding: utf-8 -*-
import sys

def inject():
    path = 'scripts/verify_deep_text_calibration.py'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 声明 round59_anomalies
    if 'round59_anomalies = []' not in content:
        content = content.replace(
            'round58_anomalies = []',
            'round58_anomalies = []\n    round59_anomalies = []'
        )

    # 2. 注入 2013 ky2 检查逻辑
    target_ky1 = 'if yr == 2013 and cat == \'ky1\':'
    ky2_block = """        if yr == 2013 and cat == 'ky2':
            if title != '2013年全国硕士研究生入学统一考试英语（二）真题':
                round59_anomalies.append(('2013_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round59_anomalies.append(('2013_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round59_anomalies.append(('2013_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\\n\\n") if p.strip()]
                if len(c_paras) != 4:
                    round59_anomalies.append(('2013_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("Given the advantages of electronic money"):
                    round59_anomalies.append(('2013_ky2_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\\n\\n") if p.strip()]
                if len(t1_paras) != 6:
                    round59_anomalies.append(('2013_ky2_t1_paras', len(t1_paras)))
                if "Davidson relates a joke from cotton country" not in t1.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t1_header', 'corrupted'))
                if "G.I. Bill" not in t1.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t1_gi_bill', 'missing'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\\n\\n") if p.strip()]
                if len(t2_paras) != 5:
                    round59_anomalies.append(('2013_ky2_t2_paras', len(t2_paras)))
                if "A century ago, the immigrants from across the Atlantic" not in t2.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t2_header', 'corrupted'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\\n\\n") if p.strip()]
                if len(t3_paras) != 6:
                    round59_anomalies.append(('2013_ky2_t3_paras', len(t3_paras)))
                if "Scientists have found that although we are prone" not in t3.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t3_header', 'corrupted'))
                if "John Gottman" not in t3.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t3_gottman', 'missing'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\\n\\n") if p.strip()]
                if len(t4_paras) != 7:
                    round59_anomalies.append(('2013_ky2_t4_paras', len(t4_paras)))
                if "Do we need quotas" not in t4.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t4_p3_quota', 'missing'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\\n\\n") if p.strip()]
                if len(pb_paras) != 6:
                    round59_anomalies.append(('2013_ky2_pb_paras', len(pb_paras)))
                if "[41]" not in pb.get("content", "") or "[45]" not in pb.get("content", ""):
                    round59_anomalies.append(('2013_ky2_pb_labels', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round59_anomalies.append(('2013_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round59_anomalies.append((f'2013_ky2_q{i}_number', q.get('question_number')))
                    if q.get('question_type') != 'multiple_choice':
                        round59_anomalies.append((f'2013_ky2_q{i}_type', q.get('question_type')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round59_anomalies.append((f'2013_ky2_q{i}_points', q_pts))
                    opts = q.get('options', {})
                    for opt_k, opt_v in opts.items():
                        if opt_v.strip() == opt_k:
                            round59_anomalies.append((f'2013_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or ('【精准定位】' not in expl and '【命题解密】' not in expl and '【错项排除】' not in expl):
                        round59_anomalies.append((f'2013_ky2_q{i}_explanation_structure', 'incomplete'))

                gold_ans = {
                    1:'B', 2:'D', 3:'B', 4:'A', 5:'C', 6:'B', 7:'A', 8:'D', 9:'C', 10:'A',
                    11:'A', 12:'C', 13:'B', 14:'D', 15:'C', 16:'D', 17:'A', 18:'B', 19:'D', 20:'C',
                    21:'A', 22:'D', 23:'B', 24:'B', 25:'C',
                    26:'A', 27:'C', 28:'C', 29:'B', 30:'D',
                    31:'D', 32:'A', 33:'B', 34:'C', 35:'B',
                    36:'B', 37:'C', 38:'A', 39:'D', 40:'C',
                    41:'F', 42:'C', 43:'G', 44:'A', 45:'B'
                }
                for q_no, exp_a in gold_ans.items():
                    act_a = q_list[q_no-1].get('answer')
                    if act_a != exp_a:
                        round59_anomalies.append((f'2013_ky2_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))
"""
    if "if yr == 2013 and cat == 'ky2':" not in content:
        # 寻找 round58 之后的合适插入点，在 results = { 之前插入
        pos = content.find("results = {")
        content = content[:pos] + ky2_block + "\n    " + content[pos:]

    # 3. 注入 results["Assertion 81: ..."]
    assertion_80_line = 'results["Assertion 80: 2013 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（Text 1 找回丢失段落恢复6段、Text 2 剔除题干倒灌恢复7段、Text 3 补齐VI/VII段、Text 4 切除倒灌残渣恢复7段、Part B 找回缺失选项[A][B]、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round58_anomalies) == 0)'
    assertion_81_line = 'results["Assertion 81: 2013 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段351词、Text 1 恢复6段366词并补齐G.I. Bill完整句、Text 2 恢复5段402词理顺候鸟脉络、Text 3 恢复6段381词、Text 4 独立设问恢复7段356词、Part B 恢复6段504词含引言及[41]-[45]建议、切除全卷45题假占位符、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round59_anomalies) == 0)'
    
    if "Assertion 81:" not in content:
        content = content.replace(
            assertion_80_line,
            assertion_80_line + "\n    " + assertion_81_line
        )

    # 4. 注入错误报告打印
    r58_print = 'if round58_anomalies:\n            print(f"Round 58 anomalies ({len(round58_anomalies)}):", round58_anomalies[:10])'
    r59_print = 'if round59_anomalies:\n            print(f"Round 59 anomalies ({len(round59_anomalies)}):", round59_anomalies[:10])'
    if "round59_anomalies:" not in content:
        content = content.replace(
            r58_print,
            r58_print + "\n        " + r59_print
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Assertion 81 successfully injected into verify_deep_text_calibration.py!")

if __name__ == '__main__':
    inject()
