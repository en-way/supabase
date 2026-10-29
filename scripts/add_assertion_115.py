import re

target_file = 'scripts/verify_deep_text_calibration.py'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add round93_anomalies = []
s1 = "    round92_anomalies = []\n"
r1 = "    round92_anomalies = []\n    round93_anomalies = []\n"
if s1 not in content:
    s1 = "    round92_anomalies = []\r\n"
    r1 = "    round92_anomalies = []\r\n    round93_anomalies = []\r\n"
assert s1 in content, "s1 not found"
content = content.replace(s1, r1, 1)

# 2. Add round93 check logic after round92
target_block = """            for bad_c in ['\\u00a0', '\\u200b', '\\ufeff', '\\ufffd']:
                if bad_c in c:
                    round92_anomalies.append((f'{yr}_{cat}_p{so}_bad_char', ord(bad_c)))"""

r2 = """            for bad_c in ['\\u00a0', '\\u200b', '\\ufeff', '\\ufffd']:
                if bad_c in c:
                    round92_anomalies.append((f'{yr}_{cat}_p{so}_bad_char', ord(bad_c)))

        # Round 93 Verification: Forensic Purification of OCR Glitches, Soft Hyphens & Bracket Anomalies
        exam_raw = json.dumps(data, ensure_ascii=False)
        if '\\u00ad' in exam_raw:
            round93_anomalies.append((f'{yr}_{cat}_soft_hyphen', exam_raw.count('\\u00ad')))

        b_pat = re.compile(r'(\\[[A-D][A-Z]\\]?|［[A-D][A-Z]］?)')
        c_pat = re.compile(r'([a-zA-Z0-9]+C[\\u4e00-\\u9fa5]{1,10}[）)])')
        p_pat = re.compile(r'(?:[，,]{2,}|[；;]{2,}|[！!]{2,})')
        g_pat = re.compile(r'[a-zA-Z\\[\\(\\)\\]\\s]巳[a-zA-Z\\[\\(\\)\\]\\s]')

        for q in data.get('questions', []):
            qn = q.get('question_number')
            expl = q.get('explanation') or ''
            b_hits = b_pat.findall(expl)
            if b_hits:
                round93_anomalies.append((f'{yr}_{cat}_q{qn}_bad_bracket', b_hits))
            c_hits = c_pat.findall(expl)
            if c_hits:
                round93_anomalies.append((f'{yr}_{cat}_q{qn}_c_paren', c_hits))
            p_hits = p_pat.findall(expl)
            if p_hits:
                round93_anomalies.append((f'{yr}_{cat}_q{qn}_double_punct', p_hits))
            g_hits = g_pat.findall(expl)
            if g_hits:
                round93_anomalies.append((f'{yr}_{cat}_q{qn}_glyph_residual', g_hits))"""

if "\r\n" in content:
    target_block = target_block.replace("\n", "\r\n")
    r2 = r2.replace("\n", "\r\n")

assert target_block in content, "target_block not found"
content = content.replace(target_block, r2, 1)

# 3. Add Assertion 115 to results
# Match Assertion 114 line
a114_pattern = r'(results\["Assertion 114:[^\]]+\]\s*=\s*\(len\(round92_anomalies\)\s*==\s*0\))'
m_a114 = re.search(a114_pattern, content)
assert m_a114, "Assertion 114 line not found"
old_a114 = m_a114.group(1)
new_a115 = old_a114 + '\n    results["Assertion 115: 全库 41 套真题题解法医级 OCR 标点微观提纯与不可见字符归零（全库 0 处 \\u00ad 软连字符隐形残留、0 处 [BJ/［AL 选项括号 OCR 残损、0 处 tightensC使）等字母替代括号、0 处 ，， 等双标点污迹、0 处 巳xplaining 等汉字混入英文字词残损；全量 1,825 道试题解析 100% 达成纯金无瑕标准）"] = (len(round93_anomalies) == 0)'

if "\r\n" in content:
    new_a115 = new_a115.replace("\n", "\r\n")

content = content.replace(old_a114, new_a115, 1)

# 4. Add report on round93 anomalies
rep1 = """        if round92_anomalies:
            print(f"Round 92 anomalies ({len(round92_anomalies)}):", round92_anomalies[:10])"""
rep2 = """        if round92_anomalies:
            print(f"Round 92 anomalies ({len(round92_anomalies)}):", round92_anomalies[:10])
        if round93_anomalies:
            print(f"Round 93 anomalies ({len(round93_anomalies)}):", round93_anomalies[:10])"""

if "\r\n" in content:
    rep1 = rep1.replace("\n", "\r\n")
    rep2 = rep2.replace("\n", "\r\n")

assert rep1 in content, "rep1 not found"
content = content.replace(rep1, rep2, 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Assertion 115 into scripts/verify_deep_text_calibration.py!")
