import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json", "r", encoding="utf-8") as f:
    d = json.load(f)

# Common words to exclude from genuine words
EXCLUDE = {
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
    'accountability', 'representation', 'fluMist'
}

for q in d['questions']:
    qn = q['question_number']
    expl = q.get('explanation', '')
    
    # 1. Punctuation glued: [a-z]\.[A-Z]
    p_glued = re.findall(r'[a-zA-Z]\.[A-Za-z]+', expl)
    # filter out file extensions like .com, .org, or initials like e.g., i.e.
    p_glued = [x for x in p_glued if not (x.endswith('.com') or x.endswith('.org') or x.lower() in ['e.g', 'i.e', 'u.s', 'etc'])]
    
    # 2. Long words >= 14
    words = re.findall(r'[A-Za-z]{14,}', expl)
    long_glued = [w for w in words if w.lower() not in EXCLUDE]
    
    # 3. camelCase [a-z]{2,}[A-Z]
    camel = re.findall(r'[a-z]{2,}[A-Z][a-zA-Z]*', expl)
    
    all_issues = set(p_glued + long_glued + camel)
    if all_issues:
        print(f"=== Q{qn} ===")
        for issue in sorted(all_issues):
            # find surrounding snippet
            idx = expl.find(issue)
            snippet = expl[max(0, idx-30):min(len(expl), idx+len(issue)+30)].replace('\n', ' ')
            print(f"  [{issue}] -> ...{snippet}...")
