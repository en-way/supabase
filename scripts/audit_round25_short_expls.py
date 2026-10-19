import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Proactive Forensic Audit for Round 25 ===")

exam_files = sorted(glob.glob('public/data/exams/*.json'))

short_reading_expls = []

for f in exam_files:
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    title = d['exam']['title']
    
    for q in d.get('questions', []):
        so = q['sort_order']
        stem = q.get('stem', '').strip()
        ans = q.get('correct_answer', '').strip()
        expl = q.get('explanation', '').strip()
        
        # Check Part A reading (Q21-40) explanation length
        if so in range(21, 41):
            if len(expl) < 220:
                short_reading_expls.append((yr, cat, so, len(expl), expl[:60]))

print(f"\nTotal Part A reading questions with short explanations (<220 chars): {len(short_reading_expls)}")
from collections import Counter
counts = Counter([(x[0], x[1]) for x in short_reading_expls])
for (yr, cat), count in sorted(counts.items()):
    print(f"  - {yr} {cat}: {count} questions")
