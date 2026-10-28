import sys

with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add round88_anomalies = [] after round87_anomalies = []
c = c.replace("round87_anomalies = []", "round87_anomalies = []\n    round88_anomalies = []")

# 2. Add round 88 check logic
r88_check = """
        # Round 88 Verification: 2011 ky2 Text 2 & 2005 ky1 Text 2 Yellow Book authentic texts
        if yr == 2011 and cat == 'ky2':
            for p in data.get('passages', []):
                if p.get('sort_order') == 3:
                    content = p.get('content', '')
                    paras = [x for x in content.split('\\n\\n') if x.strip()]
                    words = len(content.split())
                    if len(paras) != 5:
                        round88_anomalies.append(('2011_ky2_text2_paras_count', len(paras)))
                    if words != 329:
                        round88_anomalies.append(('2011_ky2_text2_words_count', words))
                    if 'San Francisco Chronicle were chronicling their own doom' not in content:
                        round88_anomalies.append(('2011_ky2_text2_missing_sf_chronicle', True))
                    if 'In Japan the proportion is 35%' not in content:
                        round88_anomalies.append(('2011_ky2_text2_missing_japan_stat', True))
            for q in data.get('questions', []):
                if q.get('sort_order') == 26:
                    if 'Newspapers like... their own doom' not in q.get('stem', ''):
                        round88_anomalies.append(('2011_ky2_q26_stem_ellipsis', q.get('stem')))
                elif q.get('sort_order') == 29:
                    opt_b = next((o for o in q.get('options', []) if o.get('key') == 'B'), {})
                    if opt_b.get('text') != 'Completeness is to blame for the failure of newspapers.':
                        round88_anomalies.append(('2011_ky2_q29_opt_b_text', opt_b.get('text')))

        if yr == 2005 and cat == 'ky1':
            for p in data.get('passages', []):
                if p.get('sort_order') == 3:
                    content = p.get('content', '')
                    paras = [x for x in content.split('\\n\\n') if x.strip()]
                    words = len(content.split())
                    if len(paras) != 5:
                        round88_anomalies.append(('2005_ky1_text2_paras_count', len(paras)))
                    if words != 438:
                        round88_anomalies.append(('2005_ky1_text2_words_count', words))
                    if 'paralysis by analysis' not in content:
                        round88_anomalies.append(('2005_ky1_text2_missing_paralysis_by_analysis', True))
                    if 'take the legislative initiative' not in content:
                        round88_anomalies.append(('2005_ky1_text2_missing_legislative_initiative', True))
                    if 'responsible stewards of the planet' not in content:
                        round88_anomalies.append(('2005_ky1_text2_missing_responsible_stewards', True))
                    if 'draft plan wants to slow down changes' in content:
                        round88_anomalies.append(('2005_ky1_text2_has_synthetic_content', True))
"""

target = "invisible_unicode"
idx = c.find(target)
if idx != -1:
    line_end = c.find("\n", idx)
    c = c[:line_end] + "\n" + r88_check + c[line_end:]
else:
    print("Error finding target for r88_check")
    sys.exit(1)

# 3. Add Assertion 110 into results dict
assertion_109_str = 'results["Assertion 109: 全库 41 套真题试题选项完整性与分值自洽法医级校对（2021 英语一 Q35 选项 C/D 彻底修复截断与软连字符软伤、完整恢复 Victorian period? 与 post-Victorian norm?；2017 英语一 Part B Q41-Q45 选项 [A]-[G] 黄金注入狄更斯传记段落首句；全库 1,825 道试题 score 与 points 100% 严格一致零缺失；全库 7,830 个选项 0 处伪前缀、0 处不可见异常字符、0 处重复选项）"] = (len(round87_anomalies) == 0)'

assertion_110_str = assertion_109_str + '\n    results["Assertion 110: 2011 英语二 Text 2 与 2005 英语一 Text 2 黄皮书原汁原味权威重构校准（2011 英语二 Text 2 彻底消除伪造 7 段 441 词异化版本，100% 还原黄皮书 5 段 329 词报业危机真实正文与旧金山纪事报、日本 35% 广告例证，Q26 题干规范省略号，Q29 选项 B 纠正复数 failure of newspapers.；2005 英语一 Text 2 彻底清除后半截合成文本，100% 恢复黄皮书 5 段 438 词全球变暖真题正文与 paralysis by analysis 及立法倡议核心句）"] = (len(round88_anomalies) == 0)'

c = c.replace(assertion_109_str, assertion_110_str)

# 4. Add print if round88_anomalies
if_block = 'if round87_anomalies:\n            print(f"Round 87 anomalies ({len(round87_anomalies)}):", round87_anomalies[:10])'
c = c.replace(if_block, if_block + '\n        if round88_anomalies:\n            print(f"Round 88 anomalies ({len(round88_anomalies)}):", round88_anomalies[:10])')

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully added Assertion 110 to scripts/verify_deep_text_calibration.py")
