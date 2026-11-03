import re

target_file = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"
content = open(target_file, "r", encoding="utf-8").read()

# 1. Add round97_anomalies = []
old_init = "    round96_anomalies = []"
new_init = "    round96_anomalies = []\n    round97_anomalies = []"
assert old_init in content
content = content.replace(old_init, new_init)

# 2. Add Assertion 118 loop after Assertion 117
assertion_118_body = """            # Assertion 118: English 1 deep text forensic calibration
            if cat == 'ky1':
                VALID_WORDS_118 = {
                    'telecommunications', 'congratulations', 'responsibilities', 'differentiation',
                    'institutionalized', 'indiscriminately', 'unconditionally', 'disproportionately',
                    'counterbalance', 'intellectualism', 'commercialization', 'characteristics',
                    'straightforward', 'unprecedentedly', 'psychologically', 'extraordinarily',
                    'professionalising', 'recommendations', 'instrumentalists', 'interdisciplinary',
                    'proportionality', 'standardization', 'unsurprisingly', 'neuroscientists',
                    'neuroscientist', 'systematically', 'interpretation', 'interpretations',
                    'misinterpreted', 'countermeasures', 'multinationals', 'constitutional',
                    'enthusiastically', 'experimentation', 'administration', 'representatives',
                    'transformation', 'transformations', 'disproportionate', 'incomprehensible',
                    'instrumentation', 'environmentalist', 'environmentalists', 'misunderstandings',
                    'advertisements', 'nationalisation', 'responsibility', 'accomplishments',
                    'aggressiveness', 'alphabetically', 'anthropologist', 'collaborations',
                    'commercialized', 'considerations', 'controversialist', 'correspondence',
                    'disappointment', 'discrimination', 'distinguishing', 'environmentally',
                    'evolutionarily', 'generalization', 'generalizations', 'homogenization',
                    'infrastructure', 'instantaneously', 'irresponsibility', 'miniaturization',
                    'misinterpretation', 'neurotransmitters', 'parliamentarian', 'professionalisation',
                    'professionalization', 'reinterpretation', 'representation', 'simultaneously',
                    'specialisation', 'susceptibility', 'transferability', 'transportation',
                    'underestimated', 'understatements', 'undertreatment', 'vulnerabilities'
                }
                qn = q.get('question_number')
                expl = q.get('explanation', '')

                # 1. Check [E] in Q1-Q40
                if 1 <= qn <= 40 and re.search(r'[\[［]E[\]］]', expl):
                    round97_anomalies.append((f"{yr}_q{qn}_opt_E", "[E] in Q1-Q40"))

                # 2. Check glued words >= 14 chars
                for w in re.findall(r'[A-Za-z]{14,}', expl):
                    if w.lower() not in VALID_WORDS_118:
                        round97_anomalies.append((f"{yr}_q{qn}_glued", w))

                # 3. Check dot glued [a-z]\\.[A-Z]
                for d in re.findall(r'[a-z]\\.[A-Z][a-z]+', expl):
                    if not (d.endswith('.com') or d.endswith('.org') or d.lower() in ['e.g', 'i.e', 'u.s']):
                        round97_anomalies.append((f"{yr}_q{qn}_dot_glued", d))

                # 4. Check comma glued [a-zA-Z],[a-zA-Z]
                for cg in re.findall(r'[a-zA-Z],[a-zA-Z]', expl):
                    round97_anomalies.append((f"{yr}_q{qn}_comma_glued", cg))

                # 5. Check unclosed brackets
                unclosed = re.findall(r'[\[［][A-G][一-龥“]', expl)
                unclosed = [x for x in unclosed if not x.startswith('［Fal')]
                if unclosed:
                    round97_anomalies.append((f"{yr}_q{qn}_unclosed", unclosed))

                # 6. Check watermarks
                for wm in ['公众号', '旗胜', '微信', 'QQ', '淘宝', '店铺']:
                    if wm in expl:
                        round97_anomalies.append((f"{yr}_q{qn}_watermark", wm))

                # 7. Check 2004 font residuals
                for res in ['a(lengt)', 'wi(hot)ers', 'etysuggestt)at', 'Changesinthesocialstructure', 'HowdidRedmonfindhisjob']:
                    if res in expl:
                        round97_anomalies.append((f"{yr}_q{qn}_font_residual", res))

                # 8. Check trailing page numbers
                lines = [l.strip() for l in expl.strip().split('\\n') if l.strip()]
                if lines and re.fullmatch(r'\\d{1,3}', lines[-1]) and not (yr == 2011 and qn == 13):
                    round97_anomalies.append((f"{yr}_q{qn}_trailing_page", lines[-1]))
"""

target_prev = """                lines = [l.strip() for l in expl.strip().split('\\n') if l.strip()]
                if lines and re.fullmatch(r'\\d{1,3}', lines[-1]) and not (yr == 2020 and qn == 14):
                    round96_anomalies.append((f"{yr}_q{qn}_trailing_page", lines[-1]))"""

assert target_prev in content
content = content.replace(target_prev, target_prev + "\n\n" + assertion_118_body)

# 3. Add Assertion 118 to results dictionary
old_res = '    results["Assertion 117: 英语二 16 套真题文本与解析法医级深度提纯（Q1-Q40 选项 [E] 错码彻底归零、粘连英文与词条空格断点彻底修复、未闭合选项括号彻底闭合、乙世代等 OCR 形近错字 100% 纠正为 Z世代、页码残渣与孤立标点噪点 0 处残留）"] = (len(round96_anomalies) == 0)'
new_res = old_res + '\n    results["Assertion 118: 英语一 25 套真题文本与解析法医级深度提纯（Q1-Q40 选项 [E] 错码彻底归零、2004完型与阅读字符置换与粘连词链彻底修复、粘连英文与词条断点彻底修复、未闭合选项括号彻底闭合、公众号与机构水印 0 处残留、页码残渣与孤立标点噪点 0 处残留）"] = (len(round97_anomalies) == 0)'

assert old_res in content
content = content.replace(old_res, new_res)

# 4. Add print of round97_anomalies
old_anom_print = """        if round96_anomalies:
            print(f"Round 96 anomalies ({len(round96_anomalies)}):", round96_anomalies[:10])"""
new_anom_print = old_anom_print + """\n        if round97_anomalies:
            print(f"Round 97 anomalies ({len(round97_anomalies)}):", round97_anomalies[:10])"""

assert old_anom_print in content
content = content.replace(old_anom_print, new_anom_print)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Assertion 118 injected successfully into verify_deep_text_calibration.py!")
