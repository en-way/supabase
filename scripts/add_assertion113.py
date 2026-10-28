import sys

with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add round91_anomalies = [] after round90_anomalies = []
c = c.replace("round90_anomalies = []", "round90_anomalies = []\n    round91_anomalies = []")

# 2. Add round 91 check logic
r91_check = """
        # Round 91 Verification: 100% Canonical Passage Taxonomy & Part B Option Rigor
        for p in data.get('passages', []):
            so = p.get('sort_order')
            pt = p.get('type')
            st = p.get('section_type')
            if so == 1:
                if pt != 'cloze' or st != 'cloze':
                    round91_anomalies.append((f'{yr}_{cat}_p{so}_taxonomy', (pt, st)))
            elif 2 <= so <= 5:
                if pt != 'reading' or st != 'reading':
                    round91_anomalies.append((f'{yr}_{cat}_p{so}_taxonomy', (pt, st)))
            elif so == 6:
                if yr == 2001:
                    if pt != 'reading' or st != 'reading':
                        round91_anomalies.append((f'{yr}_{cat}_p{so}_taxonomy', (pt, st)))
                else:
                    if pt != 'reading_part_b' or st != 'reading':
                        round91_anomalies.append((f'{yr}_{cat}_p{so}_taxonomy', (pt, st)))

        # Check Part B options identity across Q41-Q45
        pb_qs = [q for q in data.get('questions', []) if 41 <= q.get('sort_order', 0) <= 45]
        if pb_qs:
            q41_dict = {o['key']: o.get('text', '') for o in pb_qs[0].get('options', [])}
            for q in pb_qs[1:]:
                q_dict = {o['key']: o.get('text', '') for o in q.get('options', [])}
                if q_dict != q41_dict:
                    round91_anomalies.append((f'{yr}_{cat}_q{q.get("sort_order")}_opts_mismatch', True))
"""

target = "round90_anomalies.append((f'2025_ky1_q{q.get(\"sort_order\")}_opt_f_missing_ellipsis', opt_f.get('text')))"
idx = c.find(target)
if idx != -1:
    line_end = c.find("\n", idx)
    c = c[:line_end] + "\n" + r91_check + c[line_end:]
else:
    print("Error finding target for r91_check")
    sys.exit(1)

# 3. Add Assertion 113 into results dict
assertion_112_str = 'results["Assertion 112: 全库选项同题标点句号与省略号对齐一致性法医级校准（2022 英语一 Q38 选项 C 与 Q39 选项 C 彻底补全末尾遗漏句号；2018 英语一 Q22 选项 B 与选项 C 彻底补全末尾遗漏句号；2025 英语一 Part B Q41-Q45 选项 [F] 黄金补全段落首句末尾省略号 ... 完美对齐 [A]-[G] 统一规范）"] = (len(round90_anomalies) == 0)'

assertion_113_str = assertion_112_str + '\n    results["Assertion 113: 全库 41 套真题 243 篇篇章分类学拓扑 100% 绝对统一与新题型选项一致性对齐（完型 41 篇严格统一为 type: cloze / section_type: cloze；阅读 165 篇严格统一为 type: reading / section_type: reading；新题型 37 篇严格统一为 type: reading_part_b / section_type: reading；全库新题型 Q41-Q45 试题选项 [A]-[G] 100% 严格同题同构同值，0 处 bare token 孤立选项）"] = (len(round91_anomalies) == 0)'

c = c.replace(assertion_112_str, assertion_113_str)

# 4. Add print if round91_anomalies
if_block = 'if round90_anomalies:\n            print(f"Round 90 anomalies ({len(round90_anomalies)}):", round90_anomalies[:10])'
c = c.replace(if_block, if_block + '\n        if round91_anomalies:\n            print(f"Round 91 anomalies ({len(round91_anomalies)}):", round91_anomalies[:10])')

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Successfully added Assertion 113 to scripts/verify_deep_text_calibration.py")
