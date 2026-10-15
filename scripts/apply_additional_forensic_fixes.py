import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Starting secondary forensic calibration of newly discovered exam defects...")

ADDITIONAL_FIXES = {
    # 2001 ky1
    (2001, 'ky1', 3): 'D',
    # 2002 ky1
    (2002, 'ky1', 3): 'C',
    (2002, 'ky1', 9): 'C',
    (2002, 'ky1', 25): 'A',
    (2002, 'ky1', 35): 'A',
    # 2003 ky1
    (2003, 'ky1', 21): 'B',
    (2003, 'ky1', 22): 'A',
    (2003, 'ky1', 24): 'D',
    (2003, 'ky1', 29): 'A',
    (2003, 'ky1', 30): 'D',
    (2003, 'ky1', 34): 'B',
    (2003, 'ky1', 35): 'A',
    (2003, 'ky1', 38): 'B',
    # 2009 ky1
    (2009, 'ky1', 42): 'E',
    (2009, 'ky1', 43): 'A',
    (2009, 'ky1', 44): 'B',
    (2009, 'ky1', 45): 'G',
    # 2013 ky1
    (2013, 'ky1', 27): 'A',
    (2013, 'ky1', 32): 'A',
    (2013, 'ky1', 34): 'B',
    (2013, 'ky1', 35): 'A',
    # 2014 ky1
    (2014, 'ky1', 24): 'A',
    # 2015 ky1
    (2015, 'ky1', 41): 'C',
    (2015, 'ky1', 42): 'E',
    (2015, 'ky1', 45): 'A',
    # 2017 ky1 Part B
    (2017, 'ky1', 41): 'F',
    (2017, 'ky1', 42): 'E',
    (2017, 'ky1', 43): 'A',
    (2017, 'ky1', 44): 'C',
    (2017, 'ky1', 45): 'G',
    # 2018 ky1 Part B
    (2018, 'ky1', 41): 'E',
    (2018, 'ky1', 42): 'G',
    (2018, 'ky1', 43): 'A',
    # 2020 ky1
    (2020, 'ky1', 28): 'C'
}

exams_dir = 'public/data/exams'
total_updated = 0
files_touched = 0

for filepath in sorted(glob.glob(os.path.join(exams_dir, '*.json'))):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    exam = data.get('exam', {})
    yr = exam.get('year')
    cat = exam.get('category_id')
    
    file_modified = False
    
    for q in data.get('questions', []):
        so = q.get('sort_order')
        key = (yr, cat, so)
        if key in ADDITIONAL_FIXES:
            target_ans = ADDITIONAL_FIXES[key]
            old_ans = q.get('answer')
            if old_ans != target_ans or q.get('correct_answer') != target_ans:
                q['answer'] = target_ans
                q['correct_answer'] = target_ans
                file_modified = True
                total_updated += 1
                print(f"[{yr} {cat} Q{so}] Calibrated: {old_ans} -> {target_ans}")
                
        # Enforce answer == correct_answer
        if q.get('answer') != q.get('correct_answer'):
            q['correct_answer'] = q.get('answer')
            file_modified = True
            
    if file_modified:
        files_touched += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n Secondary Calibration Complete!")
print(f"Files touched: {files_touched}")
print(f"Questions calibrated: {total_updated}")
