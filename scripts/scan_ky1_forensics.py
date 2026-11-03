import json
import glob
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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
    'extracurriculars', 'extracurricular', 'distinguishing',
    'constitutionality', 'characteristically', 'individualistic', 'incomprehensible',
    'interchangeable', 'straightforwardly', 'superficiality', 'reconciliation',
    'indistinguishable', 'disproportionately', 'unsatisfactory', 'unquestioningly',
    'unconditionally', 'disillusionment', 'representatives', 'crystallization',
    'experimentation', 'generalizations', 'internationalists', 'proportionality'
}

exams = sorted(glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json'))

print("=== FORENSIC PROBE FOR ENGLISH 1 (2001-2025) ===")

opt_e_issues = []
glued_words = []
dot_glued_issues = []
comma_glued_issues = []
unclosed_brackets = []
standalone_pages = []
corrupt_brackets = []

for p in exams:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cat = d.get('exam', {}).get('category_id')
    yr = d.get('exam', {}).get('year')
    if cat != 'ky1':
        continue
        
    for q in d.get('questions', []):
        qn = q.get('question_number')
        expl = q.get('explanation', '')
        
        # 1. Check [E] in Q1-Q40
        if 1 <= qn <= 40:
            if re.search(r'[\[［]E[\]］]', expl):
                opt_e_issues.append((yr, qn))
                
        # 2. Glued words
        words = re.findall(r'[A-Za-z]{14,}', expl)
        for w in words:
            if w.lower() not in VALID_WORDS:
                glued_words.append((yr, qn, w))
                
        # 3. Period missing space [a-z]\.[A-Z]
        dots = re.findall(r'[a-z]\.[A-Z][a-z]+', expl)
        dots = [x for x in dots if not (x.endswith('.com') or x.endswith('.org') or x.lower() in ['e.g', 'i.e', 'u.s'])]
        if dots:
            dot_glued_issues.append((yr, qn, dots))
            
        # 4. Comma missing space [a-zA-Z],[a-zA-Z]
        commas = re.findall(r'[a-zA-Z],[a-zA-Z]+', expl)
        commas = [x for x in commas if not (x.lower() in ['e.g', 'i.e'])]
        if commas:
            comma_glued_issues.append((yr, qn, commas))

        # 5. Unclosed brackets
        unclosed = re.findall(r'[\[［][A-G][\u4e00-\u9fa5“]', expl)
        unclosed = [x for x in unclosed if not x.startswith('［Fal')]
        if unclosed:
            unclosed_brackets.append((yr, qn, unclosed))

        # 6. Standalone page numbers
        lines = [l.strip() for l in expl.strip().split('\n') if l.strip()]
        for l in lines:
            if re.fullmatch(r'\d{1,3}', l):
                standalone_pages.append((yr, qn, l))

print(f"1. [E] in Q1-Q40: {len(opt_e_issues)} -> {opt_e_issues[:10]}")
print(f"2. Glued words (>=14 chars): {len(glued_words)} -> {glued_words[:10]}")
print(f"3. Dot glued [a-z].[A-Z]: {len(dot_glued_issues)} -> {dot_glued_issues[:10]}")
print(f"4. Comma glued [a-z],[a-z]: {len(comma_glued_issues)} -> {comma_glued_issues[:10]}")
print(f"5. Unclosed brackets: {len(unclosed_brackets)} -> {unclosed_brackets[:10]}")
print(f"6. Standalone page numbers on lines: {len(standalone_pages)} -> {standalone_pages[:10]}")
