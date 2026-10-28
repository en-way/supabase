import glob
import json
import re
import os

exam_files = sorted(glob.glob('public/data/exams/*.json'))

suspicious = []

# Trailing particles that strongly suggest an option was truncated mid-sentence
trailing_particles = r'\b(the|a|an|in|on|at|of|for|with|by|to|and|or|but|as|that|which|is|are|was|were|be|been|into|onto|upon|from|about)\s*$'

for ef in exam_files:
    with open(ef, 'r', encoding='utf-8') as f:
        data = json.load(f)
    exam_title = data.get('title') or (data.get('exam', {}).get('title') if 'exam' in data else os.path.basename(ef))
    
    for q in data.get('questions', []):
        qn = q.get('question_number')
        # Skip Part B ordering/matching if options are paragraph summaries or headings
        for opt in q.get('options', []):
            k = opt.get('key')
            t = opt.get('text', '')
            
            # Check soft hyphen or regular trailing hyphen
            if '\xad' in t or t.endswith(('-', '—')):
                suspicious.append((exam_title, qn, k, 'HYPHEN_OR_SOFT_HYPHEN', t))
                
            # Check if Part A reading option ends with a preposition/conjunction/article
            if 21 <= qn <= 40:
                if re.search(trailing_particles, t, re.IGNORECASE):
                    suspicious.append((exam_title, qn, k, 'TRAILING_PARTICLE', t))

print(f"Total suspicious truncated options found across all 41 exams: {len(suspicious)}")
for item in suspicious:
    print(f"[{item[3]}] {item[0]} | Q{item[1]}[{item[2]}]: {repr(item[4])}")
