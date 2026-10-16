import json
import glob
import re

exams = glob.glob('public/data/exams/*.json')

print(f"Total exam files found: {len(exams)}")

# 1. Inspect stem endings
no_punct_stems = []
for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    year = data.get('year')
    category = data.get('category')
    for q in data.get('questions', []):
        stem = q.get('stem', '').strip()
        q_num = q.get('question_number')
        # check if it ends with punctuation (?, ., :, ", ', etc.) or underline
        # Remove trailing quotes
        cleaned = stem.rstrip('""\'\'')
        if cleaned and not cleaned.endswith(('.', '?', '!', ':', '——', '—', '___', '____', '_____', '________', '________.')):
            no_punct_stems.append({
                'year': year,
                'category': category,
                'q_num': q_num,
                'stem': stem[-40:]
            })

print(f"\n1. Incomplete stems without standard punctuation or line: {len(no_punct_stems)}")
if no_punct_stems:
    print("Sample 10 incomplete stems:")
    for s in no_punct_stems[:10]:
        print(f"  {s['year']} {s['category']} Q{s['q_num']}: ...{s['stem']}")

# 2. Check Part B questions across all years
part_b_summary = []
for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    year = data.get('year')
    category = data.get('category')
    part_b_qs = [q for q in data.get('questions', []) if 41 <= q.get('question_number', 0) <= 45]
    if part_b_qs:
        # Check option keys and answer
        opt_keys = [list(q.get('options', {}).keys()) for q in part_b_qs]
        answers = [q.get('answer') for q in part_b_qs]
        part_b_summary.append((year, category, len(part_b_qs), opt_keys[0] if opt_keys else [], answers))

print(f"\n2. Part B summary ({len(part_b_summary)} exams have Part B 41-45):")
for y, cat, count, sample_keys, answers in sorted(part_b_summary, key=lambda x: (x[0], x[1])):
    print(f"  {y} {cat}: {count} Qs, Options: {sample_keys}, Answers: {answers}")

# 3. Check for any missing explanations or empty fields
empty_fields = []
for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    year = data.get('year')
    category = data.get('category')
    for q in data.get('questions', []):
        q_num = q.get('question_number')
        if not q.get('analysis') or len(q.get('analysis', '').strip()) < 10:
            empty_fields.append((year, category, q_num, 'empty/short analysis'))
        if not q.get('options') or len(q.get('options', {})) < 2:
            empty_fields.append((year, category, q_num, 'less than 2 options'))
        for opt_k, opt_v in q.get('options', {}).items():
            if not opt_v or len(opt_v.strip()) == 0:
                empty_fields.append((year, category, q_num, f'empty option {opt_k}'))

print(f"\n3. Empty/short fields: {len(empty_fields)}")
if empty_fields:
    for ef in empty_fields[:10]:
        print(f"  {ef}")
