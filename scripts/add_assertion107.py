# -*- coding: utf-8 -*-
with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    text = f.read()

round85_check = """        elif yr == 2011 and cat == 'ky2':
            pb_c = data['passages'][5].get('content', '')
            if 'Directions:' in pb_c or 'Read the following text' in pb_c:
                round84_anomalies.append(('2011_ky2_pb_directions_leak', pb_c[:60]))

        # Round 85 Verification: 2005 ky1 clean texts, 2012 ky1 sort_orders, 0 glued parens & double dots
        if yr == 2005 and cat == 'ky1':
            p1 = data['passages'][0].get('content', '')
            if '0 The human nose' in p1 or 'indicate(the' in p1 or 'II O' in p1:
                round85_anomalies.append(('2005_ky1_cloze_ocr_artifacts', p1[:60]))
            p2 = data['passages'][1].get('content', '')
            if 'female brown capuchin monkeys' not in p2 or 'vanish(if' in p2 or 'outraged..' in p2 or len(p2.split('\\n\\n')) != 5:
                round85_anomalies.append(('2005_ky1_text1_ocr_artifacts', len(p2.split('\\n\\n'))))
            p4 = data['passages'][3].get('content', '')
            if 'emotional thermostat' not in p4 or 'witn' in p4 or 'con trol..' in p4 or len(p4.split('\\n\\n')) != 5:
                round85_anomalies.append(('2005_ky1_text3_ocr_artifacts', len(p4.split('\\n\\n'))))
            p6 = data['passages'][5].get('content', '')
            if not p6.startswith('Canada’s premiers') or '[A] Quebec' in p6 or len(p6.split('\\n\\n')) != 15:
                round85_anomalies.append(('2005_ky1_partb_structure', len(p6.split('\\n\\n'))))
            for q in data['questions']:
                so = q.get('sort_order')
                if so in [41, 42, 43, 44, 45]:
                    opts = q.get('options', [])
                    if len(opts) != 7 or any(len(o.get('text', '')) < 50 for o in opts):
                        round85_anomalies.append((f'2005_ky1_q{so}_opts_truncated', len(opts)))
        elif yr == 2012 and cat == 'ky1':
            for idx, p in enumerate(data['passages']):
                if p.get('sort_order') != idx + 1:
                    round85_anomalies.append(('2012_ky1_passage_sort_order', (idx, p.get('sort_order'))))"""

target_check = """        elif yr == 2011 and cat == 'ky2':
            pb_c = data['passages'][5].get('content', '')
            if 'Directions:' in pb_c or 'Read the following text' in pb_c:
                round84_anomalies.append(('2011_ky2_pb_directions_leak', pb_c[:60]))"""

assert target_check in text.replace('\r\n', '\n'), "target_check not found!"

# Replace check
text_normalized = text.replace('\r\n', '\n')
text_normalized = text_normalized.replace(target_check, round85_check)

# Add Assertion 107
assertion_target = 'results["Assertion 106: 2001-2025'
assertion_107 = """    results["Assertion 107: 2005 英语一全卷法医级深度校对与黄金重组（完型填空切除0与II O段标及indicate黏连括号、Text 1 恢复5段431词切除双点及卷尾猴OCR碎词、Text 3 恢复5段471词切除witn与con trol错乱并理顺卡特赖特梦境意识调节理论、Part B 恢复15段清晰段落与[41]-[45]填空位并彻底切除末尾倒灌选项与重叠句子、Q41-Q45 恢复官方完整段落选项[A]-[G]及四键规范、2012 英语一 6 篇文章篇章序号 sort_order 黄金对齐）"] = (len(round85_anomalies) == 0)\n"""

idx = text_normalized.find(assertion_target)
assert idx != -1, "assertion_target not found!"
end_of_line = text_normalized.find('\n', idx)
text_normalized = text_normalized[:end_of_line+1] + assertion_107 + text_normalized[end_of_line+1:]

# Add print for round85_anomalies
error_target = 'if round84_anomalies:\n            print(f"Round 84 anomalies ({len(round84_anomalies)}):", round84_anomalies[:10])'
error_replace = error_target + '\n        if round85_anomalies:\n            print(f"Round 85 anomalies ({len(round85_anomalies)}):", round85_anomalies[:10])'

assert error_target in text_normalized, "error_target not found!"
text_normalized = text_normalized.replace(error_target, error_replace)

with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
    f.write(text_normalized)

print("Assertion 107 successfully inserted!")
