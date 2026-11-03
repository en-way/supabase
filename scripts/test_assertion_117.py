import json
import glob
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Valid English words of length >= 14
VALID_WORDS = {
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

round96_anomalies = []

for f in sorted(glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json')):
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    if cat != 'ky2':
        continue
        
    for q in data.get('questions', []):
        qn = q.get('question_number')
        expl = q.get('explanation', '')
        
        # 1. Check for [E] in Q1-Q40
        if 1 <= qn <= 40:
            if re.search(r'[\[［]E[\]］]', expl):
                round96_anomalies.append((f"{yr}_q{qn}_opt_E", "[E] in Q1-Q40"))

        # 2. Check for glued words
        words = re.findall(r'[A-Za-z]{14,}', expl)
        for w in words:
            if w.lower() not in VALID_WORDS:
                round96_anomalies.append((f"{yr}_q{qn}_glued", w))
                
        # 3. Check for punct glued [a-z]\.[A-Z]
        dots = re.findall(r'[a-z]\.[A-Z][a-z]+', expl)
        dots = [x for x in dots if not (x.endswith('.com') or x.endswith('.org') or x.lower() in ['e.g', 'i.e', 'u.s'])]
        if dots:
            round96_anomalies.append((f"{yr}_q{qn}_dot_glued", dots))

        # 4. Check for unclosed brackets
        unclosed = re.findall(r'[\[［][A-G][\u4e00-\u9fa5“]', expl)
        unclosed = [x for x in unclosed if not x.startswith('［Fal')]
        if unclosed:
            round96_anomalies.append((f"{yr}_q{qn}_unclosed", unclosed))

        # 5. Check for OCR residuals
        for residual in ['乙世代', 'w和', 'activityC', '“这(让)”', '代n段', '明u段', 'hit®', '©If', 'feel ^Feeling', '[398 words]', '工精准定位]']:
            if residual in expl:
                round96_anomalies.append((f"{yr}_q{qn}_residual", residual))

        # 6. Check for trailing page number
        lines = [l.strip() for l in expl.strip().split('\n') if l.strip()]
        if lines and re.fullmatch(r'\d{1,3}', lines[-1]) and not (yr == 2020 and qn == 14):
            round96_anomalies.append((f"{yr}_q{qn}_trailing_page", lines[-1]))

print(f"Total Round 96 anomalies: {len(round96_anomalies)}")
if round96_anomalies:
    for a in round96_anomalies:
        print(" ", a)
else:
    print("SUCCESS: 0 anomalies found! Assertion 117 is ready.")
