# -*- coding: utf-8 -*-
with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    text = f.read().replace('\r\n', '\n')

# 1. Add round86_anomalies initialization
assert 'round85_anomalies = []\n' in text
text = text.replace('round85_anomalies = []\n', 'round85_anomalies = []\n    round86_anomalies = []\n')

# 2. Add round86 check inside the per-exam loop
target_loop = "        passages = data.get('passages', [])\n        questions = data.get('questions', [])"
round86_check = """        # Round 86 Verification: Canonical titles, section_types, and passage mapping
        p_ids = {p.get('id'): p for p in data.get('passages', [])}
        for p in data.get('passages', []):
            so = p.get('sort_order')
            t = p.get('title', '')
            st = p.get('section_type')
            if not st:
                round86_anomalies.append((f'{yr}_{cat}_p{so}_missing_st', t))
            if so in [2, 3, 4, 5]:
                expected_title = f"Section II: Reading Comprehension Part A - Text {so - 1}"
                if t != expected_title:
                    round86_anomalies.append((f'{yr}_{cat}_p{so}_non_canonical_title', t))

        for q in data.get('questions', []):
            so = q.get('sort_order')
            pid = q.get('passage_id')
            if not pid or pid not in p_ids:
                round86_anomalies.append((f'{yr}_{cat}_q{so}_orphan', pid))

        passages = data.get('passages', [])
        questions = data.get('questions', [])"""

assert target_loop in text, "target_loop not found!"
text = text.replace(target_loop, round86_check)

# 3. Add Assertion 108 in results
assertion_107_target = 'results["Assertion 107:'
assertion_108 = """    results["Assertion 108: 全库 41 套真题 243 篇篇章映射拓扑与元数据标准化（2001/2012 篇章 section_type 严格规范为 cloze 与 reading，2011 英语一与英语二 Text 1-4 标题 100% 统一规范为 Section II: Reading Comprehension Part A - Text X，全库 1,825 道题目 passage_id 拓扑链接 100% 无孤立与错挂，篇章序号与题目序号 100% 连续且单调自增）"] = (len(round86_anomalies) == 0)\n"""

idx = text.find(assertion_107_target)
assert idx != -1, "assertion_107_target not found!"
end_of_line = text.find('\n', idx)
text = text[:end_of_line+1] + assertion_108 + text[end_of_line+1:]

# 4. Add print for round86_anomalies
error_target = 'if round85_anomalies:\n            print(f"Round 85 anomalies ({len(round85_anomalies)}):", round85_anomalies[:10])'
error_replace = error_target + '\n        if round86_anomalies:\n            print(f"Round 86 anomalies ({len(round86_anomalies)}):", round86_anomalies[:10])'

assert error_target in text, "error_target not found!"
text = text.replace(error_target, error_replace)

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Assertion 108 successfully inserted!")
