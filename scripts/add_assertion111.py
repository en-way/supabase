import sys

with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add round89_anomalies = [] after round88_anomalies = []
c = c.replace("round88_anomalies = []", "round88_anomalies = []\n    round89_anomalies = []")

# 2. Add round 89 check logic
r89_check = """
        # Round 89 Verification: Options purity and explanation OCR glyphs calibration
        if yr == 2018 and cat == 'ky1':
            for q in data.get('questions', []):
                if q.get('sort_order') == 8:
                    opt_c = next((o for o in q.get('options', []) if o.get('key') == 'C'), {})
                    if opt_c.get('text') != 'of' or opt_c.get('content') != 'of':
                        round89_anomalies.append(('2018_ky1_q8_opt_c_not_of', opt_c.get('text')))
                    expl = q.get('explanation', '')
                    if 'of.........' in expl:
                        round89_anomalies.append(('2018_ky1_q8_expl_has_dots', True))
                    if 'in£ormation' in expl:
                        round89_anomalies.append(('2018_ky1_q8_expl_has_pound_glyph', True))

        if yr == 2021 and cat == 'ky1':
            for q in data.get('questions', []):
                so = q.get('sort_order')
                expl = q.get('explanation', '')
                if so == 23 and '・］£' in expl:
                    round89_anomalies.append(('2021_ky1_q23_expl_has_pound_glyph', True))
                elif so == 26 and 'ef£ect' in expl:
                    round89_anomalies.append(('2021_ky1_q26_expl_has_ef£ect', True))
                elif so == 28 and '・£' in expl:
                    round89_anomalies.append(('2021_ky1_q28_expl_has_pound_glyph', True))

        for q in data.get('questions', []):
            so = q.get('sort_order')
            for opt in q.get('options', []):
                k = opt.get('key')
                t = opt.get('text', '')
                if '....' in t and so <= 40:
                    round89_anomalies.append((f'{yr}_{cat}_q{so}_{k}_has_4_dots', t))
"""

target = "round88_anomalies.append(('2005_ky1_text2_has_synthetic_content', True))"
idx = c.find(target)
if idx != -1:
    line_end = c.find("\n", idx)
    c = c[:line_end] + "\n" + r89_check + c[line_end:]
else:
    print("Error finding target for r89_check")
    sys.exit(1)

# 3. Add Assertion 111 into results dict
assertion_110_str = 'results["Assertion 110: 2011 英语二 Text 2 与 2005 英语一 Text 2 黄皮书原汁原味权威重构校准（2011 英语二 Text 2 彻底消除伪造 7 段 441 词异化版本，100% 还原黄皮书 5 段 329 词报业危机真实正文与旧金山纪事报、日本 35% 广告例证，Q26 题干规范省略号，Q29 选项 B 纠正复数 failure of newspapers.；2005 英语一 Text 2 彻底清除后半截合成文本，100% 恢复黄皮书 5 段 438 词全球变暖真题正文与 paralysis by analysis 及立法倡议核心句）"] = (len(round88_anomalies) == 0)'

assertion_111_str = assertion_110_str + '\n    results["Assertion 111: 全库 7,830 个选项点号噪点彻底归零与试题解析 OCR 异形字符法医级提纯（2018 英语一 Q8 选项 C 彻底治愈 of......... 冗余噪点恢复标准介词 of 并深度净化解析中 in£ormation 乱码；2021 英语一 Q23、Q26、Q28 解析彻底消灭 ef£ect 及・］£ 伪符号恢复 effect 与规范标题；全库 1,825 道试题 Q1-Q40 选项 0 处多点截断残留）"] = (len(round89_anomalies) == 0)'

c = c.replace(assertion_110_str, assertion_111_str)

# 4. Add print if round89_anomalies
if_block = 'if round88_anomalies:\n            print(f"Round 88 anomalies ({len(round88_anomalies)}):", round88_anomalies[:10])'
c = c.replace(if_block, if_block + '\n        if round89_anomalies:\n            print(f"Round 89 anomalies ({len(round89_anomalies)}):", round89_anomalies[:10])')

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully added Assertion 111 to scripts/verify_deep_text_calibration.py")
