import glob
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import extract_year_cloze from test_batch_extract_cloze
from test_batch_extract_cloze import extract_year_cloze, exam_files

def is_defective(expl):
    if not expl or len(expl) < 120:
        return True, "Too short (< 120 chars)"
    if any(k in expl for k in ['词汇注释与难句分析', '结构切分', '功能注释']) and ('[•真题精解•' in expl or '[试题考点]' in expl or '【试题考点】' in expl):
        return True, "Polluted with passage translation/analysis"
    if '错项排除' not in expl and '［错项排除］' not in expl and '【错项排除】' not in expl:
        return True, "Missing 错项排除"
    if '解题思路' not in expl and '［解题思路］' not in expl and '【解题思路】' not in expl:
        return True, "Missing 解题思路"
    return False, "OK"

# We will apply updates to defective questions across 2001-2015
applied_updates = []
modified_files = set()

for year in range(2001, 2016):
    if year == 2004:
        continue
    fpath = exam_files.get(year)
    if not fpath:
        continue
        
    with open(fpath, 'r', encoding='utf-8') as fp:
        exam_data = json.load(fp)
        
    pdf_cloze = extract_year_cloze(year)
    if not pdf_cloze:
        continue
        
    questions = exam_data.get('questions', [])
    updated_in_file = False
    
    for q in questions:
        q_num = q.get('sort_order')
        if 1 <= q_num <= 20:
            expl = q.get('explanation') or ''
            defective, reason = is_defective(expl)
            
            # Also check if it's explicitly broken (like 2013 Q1)
            if 'unbiasedL>' in expl:
                defective, reason = True, "Truncated OCR corruption"
                
            if defective and q_num in pdf_cloze:
                new_expl = pdf_cloze[q_num]
                # Format clean explanation
                # Ensure it doesn't have stray page markers
                clean_lines = []
                for l in new_expl.split('\n'):
                    l_str = l.strip()
                    if re.match(r'^(?:=== PAGE \d+ ===|\d{1,3}|公众号.*|微信.*)$', l_str):
                        continue
                    clean_lines.append(l)
                formatted_new = '\n'.join(clean_lines).strip()
                
                # Check if it has 考点 and 思路
                if ('考点' in formatted_new or '试题' in formatted_new) and '思路' in formatted_new:
                    q['explanation'] = formatted_new
                    updated_in_file = True
                    applied_updates.append({
                        'year': year,
                        'q_num': q_num,
                        'reason': reason,
                        'old_len': len(expl),
                        'new_len': len(formatted_new),
                        'q_id': q.get('id')
                    })
                    
    if updated_in_file:
        with open(fpath, 'w', encoding='utf-8') as fp:
            json.dump(exam_data, fp, ensure_ascii=False, indent=2)
        modified_files.add(fpath)

print(f"Total cloze questions updated with authentic PDF explanations: {len(applied_updates)}")
print(f"Total exam files modified: {len(modified_files)}")

by_year = {}
for u in applied_updates:
    by_year[u['year']] = by_year.get(u['year'], 0) + 1

for y in sorted(by_year.keys()):
    print(f"  Year {y}: {by_year[y]} questions updated")

# Save applied summary
with open('scripts/round9_cloze_applied_summary.json', 'w', encoding='utf-8') as f:
    json.dump(applied_updates, f, ensure_ascii=False, indent=2)

print("Applied summary saved to scripts/round9_cloze_applied_summary.json")
