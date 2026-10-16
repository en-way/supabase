import json
import glob
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

exams = sorted(glob.glob('public/data/exams/*.json'))
mismatches = []
total_checked = 0

patterns = [
    r'【答案\s*([A-G])】',
    r'敲定\s*[\[［]?([A-G])[\]］]?\s*为(?:本题)?答案',
    r'故敲定\s*[\[［]?([A-G])[\]］]?',
    r'因此\s*[\[［]?([A-G])[\]］]?\s*(?:项)?为正确',
    r'故\s*[\[［]?([A-G])[\]］]?\s*(?:项)?正确',
    r'故选\s*[\[［]?([A-G])[\]］]?',
    r'应选\s*[\[［]?([A-G])[\]］]?',
    r'选\s*[\[［]?([A-G])[\]］]?(?:。|，|,|$)',
    r'[\[［]([A-G])[\]］]\s*项符合题意',
    r'[\[［]([A-G])[\]］]\s*符合文意',
    r'[\[［]([A-G])[\]］]\s*正确'
]

for ep in exams:
    with open(ep, 'r', encoding='utf-8') as f:
        d = json.load(f)
    yr = d.get('exam', {}).get('year')
    cat = d.get('exam', {}).get('category_id')
    title = d.get('exam', {}).get('title')
    
    for q in d.get('questions', []):
        so = q.get('sort_order', 0)
        ans = (q.get('correct_answer') or '').strip()
        exp = q.get('explanation') or ''
        
        found_answers = []
        for pat in patterns:
            for m in re.finditer(pat, exp):
                found_answers.append((m.start(), m.group(1), pat))
                
        if found_answers:
            total_checked += 1
            # Sort by position in explanation
            found_answers.sort(key=lambda x: x[0])
            
            # If there's an explicit 【答案X】 or 敲定X为答案, prioritize it
            priority_ans = None
            for pos, letter, pat in found_answers:
                if '【答案' in pat or '敲定' in pat:
                    priority_ans = letter
                    break
            
            # Otherwise use the concluding answer assertion
            if not priority_ans:
                priority_ans = found_answers[-1][1]
                
            if priority_ans != ans and ans not in ['T', 'F']:
                mismatches.append((cat, yr, so, ans, priority_ans, exp[:120]))

print(f"Checked {total_checked} questions with explicit answer affirmations.")
print(f"Mismatches found: {len(mismatches)}")
for m in mismatches:
    print(f"[{m[0]} {m[1]} Q{m[2]}] DB correct_answer='{m[3]}', Explanation concludes='{m[4]}' | snippet:\n  {repr(m[5])}")
