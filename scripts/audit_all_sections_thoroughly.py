import json
import glob
import os

files = glob.glob('public/data/exams/*.json')
print(f'Total exam files: {len(files)}')

part_b_stats = {'ky1': 0, 'ky2': 0, 'issues': []}
reading_stats = {'ky1': 0, 'ky2': 0, 'issues': []}
cloze_stats = {'ky1': 0, 'ky2': 0, 'issues': []}

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')
    questions = data.get('questions', [])
    passages = data.get('passages', [])
    
    for q in questions:
        q_num = q.get('sort_order')
        ans = q.get('correct_answer') or q.get('answer') or ''
        expl = q.get('explanation') or ''
        opts = q.get('options') or []
        stem = q.get('stem') or ''
        
        # Check Cloze (1-20)
        if 1 <= q_num <= 20:
            cloze_stats[cat] += 1
            if len(expl) < 60:
                cloze_stats['issues'].append((year, cat, q_num, f'Cloze explanation too short: len={len(expl)}'))
            if len(opts) != 4:
                cloze_stats['issues'].append((year, cat, q_num, f'Cloze options count != 4: {len(opts)}'))

        # Check Reading Part A (21-40)
        elif 21 <= q_num <= 40:
            reading_stats[cat] += 1
            if len(expl) < 60:
                reading_stats['issues'].append((year, cat, q_num, f'Reading explanation too short: len={len(expl)}'))
            if len(opts) != 4:
                reading_stats['issues'].append((year, cat, q_num, f'Reading options count != 4: {len(opts)}'))
        
        # Check Part B (41-45)
        elif 41 <= q_num <= 45:
            part_b_stats[cat] += 1
            if len(expl) < 40:
                part_b_stats['issues'].append((year, cat, q_num, f'Part B explanation too short: len={len(expl)}'))
            if not opts or len(opts) < 2:
                part_b_stats['issues'].append((year, cat, q_num, f'Part B options missing/too few: {len(opts)}'))

print(f'=== Cloze (Q1-Q20) ===')
print(f'Total: ky1={cloze_stats["ky1"]}, ky2={cloze_stats["ky2"]}')
print(f'Issues: {len(cloze_stats["issues"])}')
for iss in cloze_stats['issues'][:10]:
    print(' ', iss)

print(f'\n=== Reading Part A (Q21-Q40) ===')
print(f'Total: ky1={reading_stats["ky1"]}, ky2={reading_stats["ky2"]}')
print(f'Issues: {len(reading_stats["issues"])}')
for iss in reading_stats['issues'][:10]:
    print(' ', iss)

print(f'\n=== Part B (Q41-Q45) ===')
print(f'Total: ky1={part_b_stats["ky1"]}, ky2={part_b_stats["ky2"]}')
print(f'Issues: {len(part_b_stats["issues"])}')
for iss in part_b_stats['issues'][:10]:
    print(' ', iss)
