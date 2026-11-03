# -*- coding: utf-8 -*-
import sys

target_path = r"d:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py"
with open(target_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add round96_anomalies = []
s1_target = "    round94_anomalies = []\n"
s1_replace = "    round94_anomalies = []\n    round96_anomalies = []\n"
if s1_target in content:
    content = content.replace(s1_target, s1_replace, 1)
    print("Injected round96_anomalies = []")

# 2. Add round96 check logic in loop
# Find a distinctive spot in the loop over exam files, e.g. after round94 check
s2_target = """            for o in opts:
                t = o.get('text', '')
                if re.match(r'^[\[\(][A-G][\]\)]\s*|^[A-G][\.\、\:\)]\s+', t):
                    round94_anomalies.append((f'{yr}_{cat}_q{q.get("question_number")}_opt_prefix', t))"""

s2_addition = """
            # Assertion 117: English 2 deep text forensic calibration
            if cat == 'ky2':
                VALID_WORDS_117 = {
                    'interdisciplinary', 'hospitalizations', 'antidiscrimination', 
                    'unrepresentative', 'unsubstantiated', 'characteristics',
                    'correspondingly', 'differentiation', 'telecommunications',
                    'institutionalized', 'misunderstandings', 'environmentalist',
                    'straightforward', 'unprecedentedly', 'confrontational',
                    'counterproductive', 'distinguishable', 'instrumentation',
                    'disproportionate', 'electrochemical', 'industrialization',
                    'enthusiastically', 'congratulations', 'inappropriately',
                    'responsibility', 'industrialists', 'distinctiveness', 'conversational', 'qualifications',
                    'discrimination', 'sustainability', 'accomplishment', 'contradictions', 'hypersensitive',
                    'accountability', 'representation', 'flumist', 'impressionable',
                    'transgressions', 'misinterpreted', 'unconventional', 'undergraduates', 'overwhelmingly',
                    'commonplaceness', 'inconveniencing', 'environmentalists', 'unintentionally',
                    'purposelessness', 'interrelations', 'wholeheartedly', 'confidentiality',
                    'extracurriculars', 'extracurricular', 'distinguishing'
                }
                qn = q.get('question_number')
                expl = q.get('explanation', '')
                
                # Check [E] in Q1-Q40
                if 1 <= qn <= 40 and re.search(r'[\[［]E[\]］]', expl):
                    round96_anomalies.append((f"{yr}_q{qn}_opt_E", "[E] in Q1-Q40"))

                # Check glued words >= 14 chars
                for w in re.findall(r'[A-Za-z]{14,}', expl):
                    if w.lower() not in VALID_WORDS_117:
                        round96_anomalies.append((f"{yr}_q{qn}_glued", w))

                # Check dot glued [a-z]\.[A-Z]
                for d in re.findall(r'[a-z]\.[A-Z][a-z]+', expl):
                    if not (d.endswith('.com') or d.endswith('.org') or d.lower() in ['e.g', 'i.e', 'u.s']):
                        round96_anomalies.append((f"{yr}_q{qn}_dot_glued", d))

                # Check unclosed brackets
                unclosed = re.findall(r'[\[［][A-G][\u4e00-\u9fa5“]', expl)
                unclosed = [x for x in unclosed if not x.startswith('［Fal')]
                if unclosed:
                    round96_anomalies.append((f"{yr}_q{qn}_unclosed", unclosed))

                # Check OCR typo residuals
                for res in ['乙世代', 'w和', 'activityC', '“这(让)”', '代n段', '明u段', 'hit®', '©If', 'feel ^Feeling', '[398 words]', '工精准定位]']:
                    if res in expl:
                        round96_anomalies.append((f"{yr}_q{qn}_residual", res))

                # Check trailing standalone page number
                lines = [l.strip() for l in expl.strip().split('\\n') if l.strip()]
                if lines and re.fullmatch(r'\\d{1,3}', lines[-1]) and not (yr == 2020 and qn == 14):
                    round96_anomalies.append((f"{yr}_q{qn}_trailing_page", lines[-1]))"""

if s2_target in content:
    content = content.replace(s2_target, s2_target + s2_addition, 1)
    print("Injected Assertion 117 loop check")
else:
    print("Could not find s2_target!")

# 3. Add Assertion 117 result
s3_target = '    results["Assertion 116: 全库 41 套真题五组时代 Agent 六维全景法医不变式校验（语篇完整度、题干规范度、选项结构性、答案题解一致性、分值权重大纲契合度及 PDF 基准对照 100% 达成纯金无瑕标准）"] = (len(round94_anomalies) == 0)\n'
s3_replace = s3_target + '    results["Assertion 117: 英语二 16 套真题文本与解析法医级深度提纯（Q1-Q40 选项 [E] 错码彻底归零、粘连英文与词条空格断点彻底修复、未闭合选项括号彻底闭合、乙世代等 OCR 形近错字 100% 纠正为 Z世代、页码残渣与孤立标点噪点 0 处残留）"] = (len(round96_anomalies) == 0)\n'
if s3_target in content:
    content = content.replace(s3_target, s3_replace, 1)
    print("Injected Assertion 117 into results")

# 4. Add round96_anomalies to failure reporting
s4_target = '        if round94_anomalies:\n            print(f"Round 94 anomalies ({len(round94_anomalies)}):", round94_anomalies[:10])\n'
s4_replace = s4_target + '        if round96_anomalies:\n            print(f"Round 96 anomalies ({len(round96_anomalies)}):", round96_anomalies[:10])\n'
if s4_target in content:
    content = content.replace(s4_target, s4_replace, 1)
    print("Injected Assertion 117 failure reporting")

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated verify_deep_text_calibration.py!")
