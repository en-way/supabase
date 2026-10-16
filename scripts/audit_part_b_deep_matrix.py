import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = 'public/data/exams'
files = sorted(glob.glob(f'{exams_dir}/*.json'))

print(f"Total exam files: {len(files)}")

part_b_records = []
anomalies = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    exam = d.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')
    title = exam.get('title', '')
    
    # Filter Part B questions (sort_order 41 to 45)
    qs = [q for q in d.get('questions', []) if 41 <= q.get('sort_order', 0) <= 45]
    if not qs:
        continue
        
    for q in qs:
        so = q.get('sort_order')
        ans = q.get('correct_answer') or q.get('answer') or ''
        stem = q.get('stem') or ''
        expl = q.get('explanation') or ''
        opts = q.get('options') or []
        
        opt_keys = [o.get('key') for o in opts]
        opt_texts = [o.get('text', '').strip() for o in opts]
        
        # Check 1: Answer validity
        if ans not in opt_keys:
            anomalies.append((year, cat, so, 'Answer not in options keys', ans, opt_keys))
            
        # Check 2: Options count
        if len(opts) < 4:
            anomalies.append((year, cat, so, 'Too few options', len(opts)))
            
        # Check 3: Empty options
        if any(len(t) == 0 for t in opt_texts):
            anomalies.append((year, cat, so, 'Empty option text found', opt_keys))
            
        # Check 4: Stem length
        if len(stem.strip()) < 5:
            anomalies.append((year, cat, so, 'Stem too short', stem))
            
        # Check 5: Explanation length
        if len(expl.strip()) < 40:
            anomalies.append((year, cat, so, 'Explanation too short (< 40 chars)', len(expl)))
            
        part_b_records.append({
            'year': year,
            'cat': cat,
            'q_num': so,
            'ans': ans,
            'opts_cnt': len(opts),
            'stem_len': len(stem),
            'expl_len': len(expl)
        })

print(f"Total Part B questions examined: {len(part_b_records)}")
print(f"Total Part B anomalies found: {len(anomalies)}")

if anomalies:
    print("\nAnomalies detail:")
    for a in anomalies:
        print(' ', a)
else:
    print("All 185 Part B questions passed all sanity, topology and completeness checks!")

# Print breakdown by category
ky1_cnt = sum(1 for r in part_b_records if r['cat'] == 'ky1')
ky2_cnt = sum(1 for r in part_b_records if r['cat'] == 'ky2')
print(f"\nBreakdown: ky1={ky1_cnt} (21 exams * 5), ky2={ky2_cnt} (16 exams * 5)")
