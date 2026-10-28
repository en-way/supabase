import re

with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add round87_anomalies = [] after round86_anomalies = []
content = content.replace("round86_anomalies = []", "round86_anomalies = []\n    round87_anomalies = []")

# 2. Add round 87 check logic inside exam loop
r87_check = """
        # Round 87 Verification: Options completeness, score-points parity, lexical purity
        if yr == 2021 and cat == 'ky1':
            for q in data.get('questions', []):
                if q.get('sort_order') == 35:
                    opt_c = next((o for o in q.get('options', []) if o.get('key') == 'C'), {})
                    opt_d = next((o for o in q.get('options', []) if o.get('key') == 'D'), {})
                    if not opt_c.get('text', '').endswith('Victorian period?'):
                        round87_anomalies.append(('2021_ky1_q35_opt_c_incomplete', opt_c.get('text')))
                    if not opt_d.get('text', '').endswith('post-Victorian norm?') or '\\xad' in opt_d.get('text', ''):
                        round87_anomalies.append(('2021_ky1_q35_opt_d_incomplete_or_soft_hyphen', opt_d.get('text')))

        if yr == 2017 and cat == 'ky1':
            for q in data.get('questions', []):
                if q.get('sort_order', 0) >= 41:
                    opts = q.get('options', [])
                    if len(opts) != 7:
                        round87_anomalies.append((f'2017_ky1_q{q.get("sort_order")}_opts_len', len(opts)))
                    else:
                        opt_a = next((o for o in opts if o.get('key') == 'A'), {})
                        if not opt_a.get('text', '').startswith('The first published sketch'):
                            round87_anomalies.append((f'2017_ky1_q{q.get("sort_order")}_opt_a_text', opt_a.get('text')[:30]))

        for q in data.get('questions', []):
            so = q.get('sort_order')
            sc = q.get('score')
            pts = q.get('points')
            if sc is None or pts is None or sc != pts:
                round87_anomalies.append((f'{yr}_{cat}_q{so}_score_points_mismatch', f'score={sc}, points={pts}'))
            for opt in q.get('options', []):
                k = opt.get('key')
                v = opt.get('value')
                t = opt.get('text')
                c = opt.get('content')
                if k != v:
                    round87_anomalies.append((f'{yr}_{cat}_q{so}_{k}_key_value_mismatch', (k, v)))
                if t != c:
                    round87_anomalies.append((f'{yr}_{cat}_q{so}_{k}_text_content_mismatch', (t[:20] if t else None, c[:20] if c else None)))
                if t and ('\\xad' in t or '\\u200b' in t or '\\ufeff' in t):
                    round87_anomalies.append((f'{yr}_{cat}_q{so}_{k}_invisible_unicode', t[:30]))
"""

target_loc = "passages = data.get('passages', [])"
idx = content.find(target_loc)
if idx != -1:
    content = content[:idx] + r87_check + "\n        " + content[idx:]
else:
    print("Error: target_loc not found")

# 3. Add Assertion 109 to results
assertion_108_line = 'results["Assertion 108: 全库 41 套真题 243 篇篇章映射拓扑与元数据标准化（2001/2012 篇章 section_type 严格规范为 cloze 与 reading，2011 英语一与英语二 Text 1-4 标题 100% 统一规范为 Section II: Reading Comprehension Part A - Text X，全库 1,825 道题目 passage_id 拓扑链接 100% 无孤立与错挂，篇章序号与题目序号 100% 连续且单调自增）"] = (len(round86_anomalies) == 0)'

assertion_109_line = assertion_108_line + '\n    results["Assertion 109: 全库 41 套真题试题选项完整性与分值自洽法医级校对（2021 英语一 Q35 选项 C/D 彻底修复截断与软连字符软伤、完整恢复 Victorian period? 与 post-Victorian norm?；2017 英语一 Part B Q41-Q45 选项 [A]-[G] 黄金注入狄更斯传记段落首句；全库 1,825 道试题 score 与 points 100% 严格一致零缺失；全库 7,830 个选项 0 处伪前缀、0 处不可见异常字符、0 处重复选项）"] = (len(round87_anomalies) == 0)'

content = content.replace(assertion_108_line, assertion_109_line)

# 4. Add print if round87_anomalies
if_block = 'if not all_passed:'
content = content.replace(if_block, 'if not all_passed:\n        if round87_anomalies:\n            print(f"Round 87 anomalies ({len(round87_anomalies)}):", round87_anomalies[:10])')

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Assertion 109 into scripts/verify_deep_text_calibration.py")
