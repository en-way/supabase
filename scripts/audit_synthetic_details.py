import os, sys, glob, json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXAMS_DIR = os.path.join(ROOT_DIR, "public", "data", "exams")

synthetic_keywords = [
    'Authentic verified standard key option',
    'The primary contextual factor',
    'Alternative contextual interpretation',
    'Secondary perspective',
    'Comprehensive analytical view',
    'Paragraph A: The underlying psychological mechanisms'
]

files = sorted(glob.glob(os.path.join(EXAMS_DIR, "*.json")))
total_missing = 0
exam_missing = {}

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    exam = d.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')
    title = exam.get('title')
    
    missing_q = []
    for q in d.get('questions', []):
        opts = q.get('options', [])
        if any(any(kw in (opt.get('text', '') if isinstance(opt, dict) else str(opt)) for kw in synthetic_keywords) for opt in opts):
            missing_q.append(q['sort_order'])
            
    if missing_q:
        total_missing += len(missing_q)
        exam_missing[(year, cat)] = (title, missing_q, os.path.basename(f))
        print(f"{year} {cat} ({len(missing_q)}): {missing_q}")

print(f"\nTotal synthetic questions needing calibration: {total_missing}")
