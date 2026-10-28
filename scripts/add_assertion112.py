import sys

with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add round90_anomalies = [] after round89_anomalies = []
c = c.replace("round89_anomalies = []", "round89_anomalies = []\n    round90_anomalies = []")

# 2. Add round 90 check logic
r90_check = """
        # Round 90 Verification: Intra-question options punctuation & ellipsis consistency
        if yr == 2022 and cat == 'ky1':
            for q in data.get('questions', []):
                so = q.get('sort_order')
                if so == 38:
                    opt_c = next((o for o in q.get('options', []) if o.get('key') == 'C'), {})
                    if opt_c.get('text') != 'Limiting the powers of business owners.':
                        round90_anomalies.append(('2022_ky1_q38_opt_c_missing_period', opt_c.get('text')))
                elif so == 39:
                    opt_c = next((o for o in q.get('options', []) if o.get('key') == 'C'), {})
                    if opt_c.get('text') != 'Society sees a rise in overall well-being.':
                        round90_anomalies.append(('2022_ky1_q39_opt_c_missing_period', opt_c.get('text')))

        if yr == 2018 and cat == 'ky1':
            for q in data.get('questions', []):
                if q.get('sort_order') == 22:
                    opt_b = next((o for o in q.get('options', []) if o.get('key') == 'B'), {})
                    opt_c = next((o for o in q.get('options', []) if o.get('key') == 'C'), {})
                    if opt_b.get('text') != "Optimists' opinions on new tech find little support.":
                        round90_anomalies.append(('2018_ky1_q22_opt_b_missing_period', opt_b.get('text')))
                    if opt_c.get('text') != 'Issues arising from automation need to be tackled.':
                        round90_anomalies.append(('2018_ky1_q22_opt_c_missing_period', opt_c.get('text')))

        if yr == 2025 and cat == 'ky1':
            for q in data.get('questions', []):
                if 41 <= q.get('sort_order', 0) <= 45:
                    opt_f = next((o for o in q.get('options', []) if o.get('key') == 'F'), {})
                    if not opt_f.get('text', '').endswith('...'):
                        round90_anomalies.append((f'2025_ky1_q{q.get("sort_order")}_opt_f_missing_ellipsis', opt_f.get('text')))
"""

target = "round89_anomalies.append((f'{yr}_{cat}_q{so}_{k}_has_4_dots', t))"
idx = c.find(target)
if idx != -1:
    line_end = c.find("\n", idx)
    c = c[:line_end] + "\n" + r90_check + c[line_end:]
else:
    print("Error finding target for r90_check")
    sys.exit(1)

# 3. Add Assertion 112 into results dict
assertion_111_str = 'results["Assertion 111: 全库 7,830 个选项点号噪点彻底归零与试题解析 OCR 异形字符法医级提纯（2018 英语一 Q8 选项 C 彻底治愈 of......... 冗余噪点恢复标准介词 of 并深度净化解析中 in£ormation 乱码；2021 英语一 Q23、Q26、Q28 解析彻底消灭 ef£ect 及・］£ 伪符号恢复 effect 与规范标题；全库 1,825 道试题 Q1-Q40 选项 0 处多点截断残留）"] = (len(round89_anomalies) == 0)'

assertion_112_str = assertion_111_str + '\n    results["Assertion 112: 全库选项同题标点句号与省略号对齐一致性法医级校准（2022 英语一 Q38 选项 C 与 Q39 选项 C 彻底补全末尾遗漏句号；2018 英语一 Q22 选项 B 与选项 C 彻底补全末尾遗漏句号；2025 英语一 Part B Q41-Q45 选项 [F] 黄金补全段落首句末尾省略号 ... 完美对齐 [A]-[G] 统一规范）"] = (len(round90_anomalies) == 0)'

c = c.replace(assertion_111_str, assertion_112_str)

# 4. Add print if round90_anomalies
if_block = 'if round89_anomalies:\n            print(f"Round 89 anomalies ({len(round89_anomalies)}):", round89_anomalies[:10])'
c = c.replace(if_block, if_block + '\n        if round90_anomalies:\n            print(f"Round 90 anomalies ({len(round90_anomalies)}):", round90_anomalies[:10])')

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully added Assertion 112 to scripts/verify_deep_text_calibration.py")
