import glob
import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'
fpath = glob.glob(f'{pdf_dir}/*2001*.pdf')[0]
doc = fitz.open(fpath)

# Extract pages 1 to 8
full_text = ''
for p in range(8):
    full_text += f'\n=== PAGE {p+1} ===\n' + doc[p].get_text()

# We need to extract each question 1..20
# Strategy: find blocks starting with "1. ", "2. ", ... "20. "
# that contain "［试题考点］" or "[试题考点]" or "［考点提炼］" or "[考点提炼]"
# Each question ends before the next question starts or before Reading section starts.

questions = {}

# Regex pattern for question headers in 真题精解
# Usually: number followed by dot/newline, then [A] options, then [试题考点], [解题思路], [错项排除]
for q_num in range(1, 21):
    next_q = q_num + 1
    # Look for start of this question
    # Pattern: a line starting with "{q_num}." or "\n{q_num}."
    # followed within 300 chars by "[试题考点]" or "［试题考点］" or "[考点提炼]"
    # Let's search all occurrences of "\n{q_num}."
    starts = [m.start() for m in re.finditer(rf'(?:^|\n)\s*{q_num}\.\s*', full_text)]
    valid_start = None
    for s in starts:
        snippet = full_text[s:s+1500]
        if ('试题考点' in snippet or '考点提炼' in snippet) and ('解题思路' in snippet):
            valid_start = s
            break
            
    if valid_start is not None:
        questions[q_num] = valid_start
    else:
        print(f'Warning: Could not find valid start for Q{q_num}')

print(f'Found {len(questions)}/20 question starts in 2001')

# Now slice each question up to the next valid start or end marker
sorted_nums = sorted(questions.keys())
q_texts = {}
for i, num in enumerate(sorted_nums):
    start = questions[num]
    if i + 1 < len(sorted_nums):
        end = questions[sorted_nums[i+1]]
    else:
        # For Q20, search for end marker like "Section II" or next page
        snippet = full_text[start:start+2500]
        end_m = re.search(r'(?:Section\s+II|Reading\s+Comprehension|Text\s+1)', snippet, re.IGNORECASE)
        if end_m:
            end = start + end_m.start()
        else:
            end = start + 1500
    q_text = full_text[start:end].strip()
    
    # Clean out any page markers or isolated numbers
    lines = [l for l in q_text.split('\n') if not re.match(r'^\s*(?:=== PAGE \d+ ===|\d{1,3})\s*$', l)]
    q_texts[num] = '\n'.join(lines).strip()
    print(f'Q{num:02d}: length={len(q_texts[num])}, has_考点={"试题考点" in q_texts[num] or "考点提炼" in q_texts[num]}, has_思路={"解题思路" in q_texts[num]}, has_排除={"错项排除" in q_texts[num]}')

