import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('public/data/exams/207d2963-734a-52bd-9fa3-6c341efb5974.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== 2010 ky2 Questions Overview ===")
for idx, q in enumerate(d['questions']):
    qnum = idx + 1
    stem = q.get('stem', '')
    opts = q.get('options', [])
    ans = q.get('correct_answer', '')
    expl = q.get('explanation', '')
    
    # Check if opts is list
    opts_str = ", ".join(f"[{o.get('key')}] {o.get('text')}" for o in opts) if isinstance(opts, list) else str(opts)
    print(f"Q{qnum}: ans={ans} | stem={stem}")
    print(f"   opts: {opts_str}")
    print(f"   expl: {expl}")
    print("-" * 50)
