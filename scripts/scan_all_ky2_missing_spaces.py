import json
import glob
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams = sorted(glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json'))

for p in exams:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    t = d.get('title', '')
    if '英语（二）' not in t and '英语二' not in t:
        continue
    year = d.get('exam', {}).get('year')
    for q in d.get('questions', []):
        qn = q.get('question_number')
        expl = q.get('explanation', '')
        
        # 1. Period missing space: [a-z]\.[A-Z]
        dot_glued = re.findall(r'[a-z]\.[A-Z][a-z]+', expl)
        dot_glued = [x for x in dot_glued if not (x.endswith('.com') or x.endswith('.org') or x.lower() in ['e.g', 'i.e', 'u.s'])]
        
        # 2. Comma missing space: [a-z],[a-zA-Z]
        comma_glued = re.findall(r'[a-zA-Z],[a-zA-Z]+', expl)
        comma_glued = [x for x in comma_glued if not (x.lower() in ['e.g', 'i.e'])]

        if dot_glued or comma_glued:
            print(f"{year} Q{qn}: dot={dot_glued} comma={comma_glued}")
