import glob
import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== Scanning remaining potential targets for Round 28 ===")
exam_files = glob.glob(r"public/data/exams/*.json")

long_explanations = []
suspicious_stems = []
echo_explanations = []

for ef in exam_files:
    with open(ef, 'r', encoding='utf-8') as f:
        data = json.load(f)
    meta = data.get('exam', {})
    yr = meta.get('year')
    cat = meta.get('category_id')
    
    for q in data.get('questions', []):
        so = q.get('sort_order')
        stem = (q.get('stem') or '').strip()
        expl = (q.get('explanation') or '').strip()
        
        # 1. Long explanation > 2000 chars (likely contains dumped passage or notes)
        if len(expl) > 2000:
            long_explanations.append((yr, cat, so, len(expl), expl[:60]))
            
        # 2. Suspicious stem endings (like trailing prepositions without blanks or cut off)
        # Note: some legitimate stems end with prepositions, but let's check
        if re.search(r'\b(is|that|by|to|of|in|for|with|about|as|on|at|from)\s*$', stem) and not stem.endswith('________.'):
            suspicious_stems.append((yr, cat, so, stem))
            
        # 3. Echo explanations (starting with digit + dot + English/Chinese stem)
        if re.match(r'^\d+[\.、]\s*', expl):
            echo_explanations.append((yr, cat, so, expl[:40]))

print(f"\n1. Explanations > 2000 chars ({len(long_explanations)}):")
for item in sorted(long_explanations, key=lambda x: (x[0], x[1], x[2])):
    print(f"  {item[0]} {item[1]} Q{item[2]}: len={item[3]} | start={item[4]}")

print(f"\n2. Suspicious stems without blank ({len(suspicious_stems)}):")
for item in sorted(suspicious_stems, key=lambda x: (x[0], x[1], x[2])):
    print(f"  {item[0]} {item[1]} Q{item[2]}: {item[3]}")

print(f"\n3. Echo explanations starting with number prefix ({len(echo_explanations)}):")
for item in sorted(echo_explanations, key=lambda x: (x[0], x[1], x[2])):
    print(f"  {item[0]} {item[1]} Q{item[2]}: {item[3]}")
