import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import extract_year_cloze from test_batch_extract_cloze
from test_batch_extract_cloze import extract_year_cloze, exam_files

def is_defective(expl):
    if not expl or len(expl) < 120:
        return True, "Too short (< 120 chars)"
    if any(k in expl for k in ['词汇注释与难句分析', '结构切分', '功能注释', '①', '②', '③', '④', '⑤']) and ('[•真题精解•' in expl or '[试题考点]' in expl):
        # Polluted with passage analysis
        return True, "Polluted with passage translation/analysis"
    if '错项排除' not in expl and '［错项排除］' not in expl and '【错项排除】' not in expl:
        return True, "Missing 错项排除"
    if '解题思路' not in expl and '［解题思路］' not in expl and '【解题思路】' not in expl:
        return True, "Missing 解题思路"
    return False, "OK"

total_examined = 0
defects_found = []

for year in range(2001, 2016):
    if year == 2004:
        # Already fully calibrated in Round 8
        continue
    fpath = exam_files.get(year)
    if not fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as fp:
        exam_data = json.load(fp)
    
    # Extract authentic PDF cloze
    pdf_cloze = extract_year_cloze(year)
    
    questions = exam_data.get('questions', [])
    for q in questions:
        q_num = q.get('sort_order')
        if 1 <= q_num <= 20:
            total_examined += 1
            expl = q.get('explanation') or ''
            defective, reason = is_defective(expl)
            if defective and q_num in pdf_cloze:
                defects_found.append({
                    'year': year,
                    'q_num': q_num,
                    'reason': reason,
                    'curr_len': len(expl),
                    'new_len': len(pdf_cloze[q_num]),
                    'exam_id': exam_data.get('exam', {}).get('id'),
                    'q_id': q.get('id')
                })

print(f"Total cloze questions examined across 2001-2015 (excl 2004): {total_examined}")
print(f"Defects identified that can be restored from PDF: {len(defects_found)}")

by_year = {}
for d in defects_found:
    by_year[d['year']] = by_year.get(d['year'], 0) + 1

for y in sorted(by_year.keys()):
    print(f"  Year {y}: {by_year[y]} defective cloze questions ready to be restored")
