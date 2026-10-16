import json
import glob
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Paths
agent1_json = 'C:/Users/57867/.gemini/antigravity/brain/5d33c28a-5549-47f0-bd22-1b9cb339848f/scratch/cloze_restored_2001_2005.json'
agent3_json = 'C:/Users/57867/.gemini/antigravity/brain/bff42094-214a-421b-9c4b-ebcabd69b641/scratch/cloze_restored_2011_2015.json'
exams_dir = 'public/data/exams'

# Load Agent 1 (2001-2005)
with open(agent1_json, 'r', encoding='utf-8') as f:
    data_agent1 = json.load(f)

# Load Agent 3 (2011-2015)
with open(agent3_json, 'r', encoding='utf-8') as f:
    data_agent3 = json.load(f).get('all_ground_truth_by_year', {})

# Load 2006-2010 via test_batch_extract_cloze
sys.path.insert(0, 'scripts')
from test_batch_extract_cloze import extract_year_cloze, exam_files

data_2006_2010 = {}
for y in range(2006, 2011):
    data_2006_2010[str(y)] = extract_year_cloze(y)

# Unified ground truth dictionary: year_str -> {q_str -> clean_explanation}
ground_truth = {}
# Agent 1
for y_str, q_dict in data_agent1.items():
    ground_truth[y_str] = q_dict
# 2006-2010
for y_str, q_dict in data_2006_2010.items():
    ground_truth[y_str] = {str(k): v for k, v in q_dict.items()}
# Agent 3
for y_str, q_dict in data_agent3.items():
    ground_truth[y_str] = {}
    for q_str, q_val in q_dict.items():
        if isinstance(q_val, str):
            ground_truth[y_str][q_str] = q_val
        elif isinstance(q_val, dict):
            ground_truth[y_str][q_str] = q_val.get('explanation', '')

print(f"Ground truth assembled for years: {sorted(ground_truth.keys(), key=int)}")
for y in sorted(ground_truth.keys(), key=int):
    print(f"  {y}: {len(ground_truth[y])} clean explanations ready")

def is_defective(year, q_num, expl):
    if not expl or len(expl) < 120:
        return True, "Too short (< 120 chars)"
    if 'unbiasedL>' in expl:
        return True, "OCR corruption (unbiasedL>)"
    if any(k in expl for k in ['词汇注释与难句分析', '结构切分', '功能注释', '①', '②', '③', '④']) and any(k in expl for k in ['[•真题精解•', '[试题考点]', '【试题考点】', '•真题精解•']):
        return True, "Polluted with passage translation/analysis"
    if '错项排除' not in expl and '［错项排除］' not in expl and '【错项排除】' not in expl:
        return True, "Missing 错项排除"
    if '解题思路' not in expl and '［解题思路］' not in expl and '【解题思路】' not in expl:
        return True, "Missing 解题思路"
    # Specific known swaps: 2011 Q8, 2012 Q8, 2013 Q8, 2015 Q8 (where Q8 was overwritten by Q18)
    if q_num == 8 and year in (2011, 2012, 2013, 2015):
        if any(w in expl for w in ['hardens', 'evade', 'test', 'resemble']):
            pass # correct
        else:
            return True, "Q8 was overwritten by Q18 or placeholder"
    # 2001 Q5 was overwritten by Q2
    if year == 2001 and q_num == 5:
        if 'tightening' in expl:
            return True, "2001 Q5 was overwritten by Q2"
    # 2014 Q20 truncated
    if year == 2014 and q_num == 20:
        if '[B]' not in expl:
            return True, "2014 Q20 truncated at [A]"
    # 2015 Q20 truncated icon
    if year == 2015 and q_num == 20:
        if '眷' in expl or len(expl) < 300:
            return True, "2015 Q20 truncated/icon corrupted"
    return False, "OK"

applied_corrections = []
files_modified = set()

for year_str, q_dict in ground_truth.items():
    year = int(year_str)
    if year == 2004:
        continue
    fpath = exam_files.get(year)
    if not fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as fp:
        exam_data = json.load(fp)
        
    questions = exam_data.get('questions', [])
    modified = False
    
    for q in questions:
        q_num = q.get('sort_order')
        if 1 <= q_num <= 20:
            expl = q.get('explanation') or ''
            defective, reason = is_defective(year, q_num, expl)
            q_num_str = str(q_num)
            if defective and q_num_str in q_dict:
                clean_exp = q_dict[q_num_str].strip()
                # Remove stray page markers
                lines = [l for l in clean_exp.split('\n') if not re.match(r'^(?:=== PAGE \d+ ===|\d{1,3}|公众号.*|微信.*)$', l.strip())]
                clean_final = '\n'.join(lines).strip()
                
                # Verify that it is substantially better
                if len(clean_final) >= 150:
                    q['explanation'] = clean_final
                    modified = True
                    applied_corrections.append({
                        'year': year,
                        'q_num': q_num,
                        'reason': reason,
                        'old_len': len(expl),
                        'new_len': len(clean_final),
                        'q_id': q.get('id'),
                        'preview': clean_final[:100].replace('\n', ' ')
                    })
                    
    if modified:
        with open(fpath, 'w', encoding='utf-8') as fp:
            json.dump(exam_data, fp, ensure_ascii=False, indent=2)
        files_modified.add(fpath)

print(f"\n==================== APPLIED CALIBRATIONS ====================")
print(f"Total cloze questions calibrated: {len(applied_corrections)}")
print(f"Total exam files modified: {len(files_modified)}")

by_year = {}
for c in applied_corrections:
    by_year[c['year']] = by_year.get(c['year'], 0) + 1

for y in sorted(by_year.keys()):
    print(f"  {y}: {by_year[y]} questions calibrated")

with open('scripts/round9_final_applied_cloze.json', 'w', encoding='utf-8') as f:
    json.dump(applied_corrections, f, ensure_ascii=False, indent=2)

print("Saved detailed changelog to scripts/round9_final_applied_cloze.json")
