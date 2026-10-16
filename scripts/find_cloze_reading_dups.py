import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

files = sorted([f for f in os.listdir(data_dir) if f.endswith('.json')])

print("=== CLOZE & READING (Q1-Q40) DUPLICATE OPTIONS AUDIT ===")
cloze_reading_dups = []

for f in files:
    fp = os.path.join(data_dir, f)
    with open(fp, 'r', encoding='utf-8') as fp_in:
        d = json.load(fp_in)
    exam = d.get('exam', d)
    cat = exam.get('category_id') or d.get('category_id')
    yr = exam.get('year') or d.get('year')
    exam_title = f"{yr} {cat}"
    
    questions = d.get('questions', [])
    opt_map = {}
    for q in questions:
        so = q.get('sort_order')
        if so not in range(1, 41):
            continue
        opts = q.get('options')
        if isinstance(opts, list):
            opt_texts = tuple(sorted([str(o.get('text', '')).strip().lower() for o in opts]))
        elif isinstance(opts, dict):
            opt_texts = tuple(sorted([str(v).strip().lower() for v in opts.values()]))
        else:
            continue
            
        if opt_texts in opt_map:
            prev_q = opt_map[opt_texts]
            cloze_reading_dups.append((exam_title, f, prev_q, so, opt_texts))
            print(f"[{exam_title}] Q{so} duplicates Q{prev_q}: {opt_texts}")
        else:
            opt_map[opt_texts] = so

print(f"\nTotal Cloze/Reading duplicate options found: {len(cloze_reading_dups)}")
