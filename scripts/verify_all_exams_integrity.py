import os, sys, glob, json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXAMS_DIR = os.path.join(ROOT_DIR, "public", "data", "exams")

files = sorted(glob.glob(os.path.join(EXAMS_DIR, "*.json")))
print(f"Auditing {len(files)} exams...")

total_questions = 0
issues = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    exam = d.get('exam', {})
    title = exam.get('title')
    year = exam.get('year')
    cat = exam.get('category_id')
    questions = d.get('questions', [])
    
    total_questions += len(questions)
    
    for q in questions:
        qnum = q.get('sort_order')
        opts = q.get('options', [])
        ans = q.get('correct_answer') or q.get('correct_option', '')
        
        # Check option count
        if qnum <= 40:
            if len(opts) != 4:
                issues.append(f"{year} {cat} Q{qnum}: expected 4 options, got {len(opts)}")
            if ans not in ['A', 'B', 'C', 'D']:
                issues.append(f"{year} {cat} Q{qnum}: invalid key '{ans}'")
        elif qnum <= 45:
            if len(opts) < 5:
                issues.append(f"{year} {cat} Q{qnum}: expected >=5 options, got {len(opts)}")
            if ans not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
                issues.append(f"{year} {cat} Q{qnum}: invalid Part B key '{ans}'")
                
        # Check option text content
        for opt in opts:
            text = opt.get('text', '') if isinstance(opt, dict) else str(opt)
            if not text or not text.strip():
                issues.append(f"{year} {cat} Q{qnum}: empty option text in {opt}")
            if 'Authentic verified' in text or 'The primary contextual factor' in text:
                issues.append(f"{year} {cat} Q{qnum}: residual synthetic text in {opt}")

print(f"\nTotal questions audited: {total_questions}")
if issues:
    print(f"Found {len(issues)} issues:")
    for iss in issues[:20]:
        print("  ", iss)
else:
    print("PERFECT: All questions across all exams pass complete integrity check with 0 issues!")
