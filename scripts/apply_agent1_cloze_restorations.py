import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

agent1_json = 'C:/Users/57867/.gemini/antigravity/brain/5d33c28a-5549-47f0-bd22-1b9cb339848f/scratch/cloze_restored_2001_2005.json'
with open(agent1_json, 'r', encoding='utf-8') as f:
    restored_data = json.load(f)

exams_dir = 'public/data/exams'
applied = []

for y_str, q_dict in restored_data.items():
    year = int(y_str)
    # find exam file
    target_file = None
    for f in glob.glob(f'{exams_dir}/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        exam = d.get('exam', {})
        if exam.get('category_id') == 'ky1' and exam.get('year') == year:
            target_file = f
            break
            
    if not target_file:
        print(f"File for {year} not found!")
        continue
        
    with open(target_file, 'r', encoding='utf-8') as fp:
        exam_data = json.load(fp)
        
    modified = False
    for q in exam_data.get('questions', []):
        q_num = q.get('sort_order')
        if 1 <= q_num <= 20:
            q_num_str = str(q_num)
            if q_num_str in q_dict:
                clean_exp = q_dict[q_num_str].strip()
                curr_exp = q.get('explanation', '').strip()
                # If current has defect (pollution, missing parts, too short, or much longer due to passage text)
                has_pollution = any(k in curr_exp for k in ['词汇注释与难句分析', '结构切分', '功能注释'])
                is_short = len(curr_exp) < 150
                is_truncated = '错项排除' not in curr_exp and '［错项排除］' not in curr_exp
                is_swapped = (year == 2001 and q_num == 5 and 'tightening' in curr_exp) or (year == 2002 and q_num == 1 and '功能注释' in curr_exp)
                
                if has_pollution or is_short or is_truncated or is_swapped:
                    q['explanation'] = clean_exp
                    modified = True
                    applied.append((year, q_num, len(curr_exp), len(clean_exp)))
                    
    if modified:
        with open(target_file, 'w', encoding='utf-8') as fp:
            json.dump(exam_data, fp, ensure_ascii=False, indent=2)
        print(f"Updated {target_file} for year {year}")

print(f"Total Agent 1 restorations applied: {len(applied)}")
for a in applied:
    print(f"  Year {a[0]} Q{a[1]}: {a[2]} chars -> {a[3]} chars")
