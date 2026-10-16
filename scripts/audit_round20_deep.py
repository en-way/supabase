import json
import glob
import re

exams = glob.glob('public/data/exams/*.json')
print(f"Total exam files found: {len(exams)}")

# 1. Inspect stem endings
no_punct_stems = []
# 2. Check Part B questions across all years
part_b_summary = []
# 3. Check for any missing explanations or empty fields
empty_fields = []
# 4. Check for anomalous options or mismatched options
option_anomalies = []
# 5. Check Q21-40 reading stems
reading_stems_without_blank = []

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam_meta = data.get('exam', {})
    year = exam_meta.get('year')
    category = exam_meta.get('category_id')
    title = exam_meta.get('title')
    questions = data.get('questions', [])

    part_b_qs = [q for q in questions if 41 <= q.get('sort_order', 0) <= 45]
    if part_b_qs:
        opt_keys = [opt.get('key') for opt in part_b_qs[0].get('options', [])]
        answers = [q.get('correct_answer') for q in part_b_qs]
        part_b_summary.append((year, category, len(part_b_qs), opt_keys, answers))

    for q in questions:
        q_num = q.get('sort_order')
        stem = q.get('stem', '').strip()
        q_type = q.get('q_type')
        opts = q.get('options', [])
        exp = q.get('explanation', '')
        ans = q.get('correct_answer')

        # Check empty or short analysis
        if not exp or len(exp.strip()) < 10:
            empty_fields.append((year, category, q_num, 'empty/short analysis', exp))

        # Check options
        if not opts or len(opts) < 2:
            empty_fields.append((year, category, q_num, f'fewer than 2 options ({len(opts)})'))
        for opt in opts:
            text = opt.get('text', '')
            if not text or len(text.strip()) == 0:
                empty_fields.append((year, category, q_num, f"empty option {opt.get('key')}"))
            # Check if option text has strange punctuation or formatting
            if re.search(r'[\u4e00-\u9fa5]', text) and category in ['ky1', 'ky2'] and q_type not in ['translation_item']:
                option_anomalies.append((year, category, q_num, opt.get('key'), f'Chinese in option: {text}'))

        # Check reading stems (Q21-Q40 or reading_comprehension)
        if 21 <= q_num <= 40:
            cleaned = stem.rstrip('""\'\'')
            if cleaned and not cleaned.endswith(('.', '?', '!', ':', '——', '—', '___', '____', '_____', '________', '________.')):
                reading_stems_without_blank.append({
                    'year': year,
                    'category': category,
                    'q_num': q_num,
                    'stem': stem
                })

print(f"\n1. Part B Summary ({len(part_b_summary)} exams have Q41-45):")
for y, cat, count, sample_keys, answers in sorted(part_b_summary, key=lambda x: (x[0], x[1])):
    print(f"  {y} {cat}: {count} Qs | Opt keys: {sample_keys} | Ans: {answers}")

print(f"\n2. Empty or Short Fields: {len(empty_fields)}")
if empty_fields:
    for ef in empty_fields[:10]:
        print(f"  {ef}")

print(f"\n3. Option Anomalies: {len(option_anomalies)}")
if option_anomalies:
    for oa in option_anomalies[:10]:
        print(f"  {oa}")

print(f"\n4. Reading Stems (Q21-40) lacking ending punctuation or underline: {len(reading_stems_without_blank)}")
if reading_stems_without_blank:
    print("Sample 15 stems:")
    for rs in reading_stems_without_blank[:15]:
        print(f"  {rs['year']} {rs['category']} Q{rs['q_num']}: {rs['stem']}")
