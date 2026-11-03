import json, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

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

round97_anomalies = []

for fpath in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(fpath, encoding='utf-8'))
    title = data.get('title') or data.get('exam', {}).get('title', '')
    cat = data.get('category_id') or data.get('exam', {}).get('category_id')
    if cat != 'ky1' and '英语（一）' not in title and '英语一' not in title:
        continue
    yr = data.get('year') or data.get('exam', {}).get('year')
    for q in data.get('questions', []):
        qn = q.get('question_number')
        expl = q.get('explanation', '')
        
        # 1. [E] in Q1-Q40
        if 1 <= qn <= 40 and re.search(r'[\[［]E[\]］]', expl):
            round97_anomalies.append((f"{yr}_q{qn}_opt_E", "[E] in Q1-Q40"))
            
        # 2. Glued words
        for w in re.findall(r'[A-Za-z]{14,}', expl):
            if w.lower() not in VALID_WORDS_118:
                round97_anomalies.append((f"{yr}_q{qn}_glued", w))
                
        # 3. Dot glued
        for d in re.findall(r'[a-z]\.[A-Z][a-z]+', expl):
            if not (d.endswith('.com') or d.endswith('.org') or d.lower() in ['e.g', 'i.e', 'u.s']):
                round97_anomalies.append((f"{yr}_q{qn}_dot_glued", d))
                
        # 4. Comma glued
        for cg in re.findall(r'[a-zA-Z],[a-zA-Z]', expl):
            round97_anomalies.append((f"{yr}_q{qn}_comma_glued", cg))
            
        # 5. Unclosed brackets
        unclosed = re.findall(r'[\[［][A-G][一-龥“]', expl)
        unclosed = [x for x in unclosed if not x.startswith('［Fal')]
        if unclosed:
            round97_anomalies.append((f"{yr}_q{qn}_unclosed", unclosed))
            
        # 6. Watermarks
        for wm in ['公众号', '旗胜', '微信', 'QQ', '淘宝', '店铺']:
            if wm in expl:
                round97_anomalies.append((f"{yr}_q{qn}_watermark", wm))
                
        # 7. 2004 font residuals
        for res in ['a(lengt)', 'wi(hot)ers', 'etysuggestt)at', 'Changesinthesocialstructure', 'HowdidRedmonfindhisjob']:
            if res in expl:
                round97_anomalies.append((f"{yr}_q{qn}_font_residual", res))
                
        # 8. Trailing page numbers
        lines = [l.strip() for l in expl.strip().split('\n') if l.strip()]
        if lines and re.fullmatch(r'\d{1,3}', lines[-1]) and not (yr == 2011 and qn == 13):
            round97_anomalies.append((f"{yr}_q{qn}_trailing_page", lines[-1]))

print(f"Total round97_anomalies: {len(round97_anomalies)}")
if round97_anomalies:
    for a in round97_anomalies[:10]:
        print(" ", a)
else:
    print("PERFECT: 0 anomalies across all English 1 exams!")
