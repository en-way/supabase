import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

agent2_json = 'C:/Users/57867/.gemini/antigravity/brain/ec10f8d3-6e9f-421b-a9be-72a82dd5de9b/scratch/cloze_2006_2010_restored_explanations.json'
with open(agent2_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

years_data = data.get('years', {})
audit_summary = data.get('audit_summary', {})

exams_dir = 'public/data/exams'
applied_count = 0

for yr_str, q_list in years_data.items():
    year = int(yr_str)
    defective_qs = set(audit_summary.get(yr_str, {}).get('defective_questions', []))
    if not defective_qs:
        continue
        
    # Find exam file
    matched_file = None
    for f in glob.glob(f'{exams_dir}/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        exam = d.get('exam', {})
        if exam.get('category_id') == 'ky1' and exam.get('year') == year:
            matched_file = f
            break
            
    if not matched_file:
        print(f"File for year {year} not found!")
        continue
        
    with open(matched_file, 'r', encoding='utf-8') as fp:
        exam_data = json.load(fp)
        
    modified = False
    for item in q_list:
        q_num = item['question_number']
        if q_num in defective_qs:
            restored = item['restored_explanation']
            # Find in exam_data
            for q in exam_data.get('questions', []):
                if q.get('sort_order') == q_num:
                    old_len = len(q.get('explanation', ''))
                    q['explanation'] = restored
                    modified = True
                    applied_count += 1
                    print(f"[{year} Q{q_num}] Applied Agent 2 restoration: {old_len} -> {len(restored)} chars")
                    break
                    
    if modified:
        with open(matched_file, 'w', encoding='utf-8') as fp:
            json.dump(exam_data, fp, ensure_ascii=False, indent=2)
        print(f"Saved {matched_file}")

print(f"Total Agent 2 defective questions restored: {applied_count}")
