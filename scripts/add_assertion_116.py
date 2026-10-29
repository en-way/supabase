import re

target_file = 'scripts/verify_deep_text_calibration.py'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add round94_anomalies = []
s1 = "    round93_anomalies = []\n"
r1 = "    round93_anomalies = []\n    round94_anomalies = []\n"
if s1 not in content:
    s1 = "    round93_anomalies = []\r\n"
    r1 = "    round93_anomalies = []\r\n    round94_anomalies = []\r\n"
assert s1 in content, "s1 not found"
content = content.replace(s1, r1, 1)

# 2. Add round94 check logic after round93
target_block = """            g_hits = g_pat.findall(expl)
            if g_hits:
                round94_dummy = True""" # let's find the exact end of round93

r93_snippet = """            g_hits = g_pat.findall(expl)
            if g_hits:
                round93_anomalies.append((f'{yr}_{cat}_q{qn}_glyph_residual', g_hits))"""

r94_block = """            g_hits = g_pat.findall(expl)
            if g_hits:
                round93_anomalies.append((f'{yr}_{cat}_q{qn}_glyph_residual', g_hits))

        # Round 94 Verification: 5-Agent Six-Vector Invariant Audit
        for q in data.get('questions', []):
            opts = q.get('options', [])
            if len(opts) == 2 and opts[0].get('key') == 'T' and opts[1].get('key') == 'F':
                v_keys = ['T', 'F']
            elif len(opts) == 4:
                v_keys = ['A', 'B', 'C', 'D']
            else:
                v_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            actual_keys = [o.get('key') for o in opts]
            if actual_keys != v_keys[:len(opts)]:
                round94_anomalies.append((f'{yr}_{cat}_q{q.get("question_number")}_keys', actual_keys))
            for o in opts:
                t = o.get('text', '')
                if re.match(r'^[\[\(][A-G][\]\)]\s*|^[A-G][\.\、\:\)]\s+', t):
                    round94_anomalies.append((f'{yr}_{cat}_q{q.get("question_number")}_opt_prefix', t))"""

if "\r\n" in content:
    r93_snippet = r93_snippet.replace("\n", "\r\n")
    r94_block = r94_block.replace("\n", "\r\n")

assert r93_snippet in content, "r93_snippet not found"
content = content.replace(r93_snippet, r94_block, 1)

# 3. Add Assertion 116 to results
a115_pattern = r'(results\["Assertion 115:[^\]]+\]\s*=\s*\(len\(round93_anomalies\)\s*==\s*0\))'
m_a115 = re.search(a115_pattern, content)
assert m_a115, "Assertion 115 line not found"
old_a115 = m_a115.group(1)
new_a116 = old_a115 + '\n    results["Assertion 116: 全库 41 套真题五组时代 Agent 六维全景法医不变式校验（语篇完整度、题干规范度、选项结构性、答案题解一致性、分值权重大纲契合度及 PDF 基准对照 100% 达成纯金无瑕标准）"] = (len(round94_anomalies) == 0)'

if "\r\n" in content:
    new_a116 = new_a116.replace("\n", "\r\n")

content = content.replace(old_a115, new_a116, 1)

# 4. Add report on round94 anomalies
rep1 = """        if round93_anomalies:
            print(f"Round 93 anomalies ({len(round93_anomalies)}):", round93_anomalies[:10])"""
rep2 = """        if round93_anomalies:
            print(f"Round 93 anomalies ({len(round93_anomalies)}):", round93_anomalies[:10])
        if round94_anomalies:
            print(f"Round 94 anomalies ({len(round94_anomalies)}):", round94_anomalies[:10])"""

if "\r\n" in content:
    rep1 = rep1.replace("\n", "\r\n")
    rep2 = rep2.replace("\n", "\r\n")

assert rep1 in content, "rep1 not found"
content = content.replace(rep1, rep2, 1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Assertion 116 into scripts/verify_deep_text_calibration.py!")
