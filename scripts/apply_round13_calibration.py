import glob
import json
import re
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/round13_all_calibrated.json', 'r', encoding='utf-8') as f:
    calibrated_data = json.load(f)

# Parse targets from keys
targets = {}
for k, v in calibrated_data.items():
    parts = k.split('_')
    yr = int(parts[0])
    cat = parts[1]
    so = int(parts[2].replace('q', ''))
    targets[(yr, cat, so)] = (k, v)

print(f"Applying {len(targets)} calibrations to local exam files...")

exam_files = sorted(glob.glob('public/data/exams/*.json'))
updated_exams = set()
updated_questions = 0

for ef in exam_files:
    with open(ef, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    file_modified = False
    
    for q in data.get('questions', []):
        so = q.get('sort_order')
        if (yr, cat, so) in targets:
            k, patch = targets[(yr, cat, so)]
            # Apply fields
            if 'explanation' in patch:
                q['explanation'] = patch['explanation']
            if 'options' in patch:
                q['options'] = patch['options']
            if 'stem' in patch:
                q['stem'] = patch['stem']
            if 'correct_answer' in patch:
                q['correct_answer'] = patch['correct_answer']
            if 'answer' in patch:
                q['answer'] = patch['answer']
            
            file_modified = True
            updated_questions += 1
            print(f"  [Updated] {yr} {cat} Q{so} ({k}): expl_len={len(q.get('explanation',''))}")

    if file_modified:
        with open(ef, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        updated_exams.add(ef)

print(f"\nDone: {updated_questions} questions updated across {len(updated_exams)} exam files.")

# Update version.json
v_path = 'public/data/version.json'
with open(v_path, 'r', encoding='utf-8') as f:
    v_data = json.load(f)

old_ver = v_data.get('version', '')
new_ver = hex(int(time.time()))[2:] + hex(len(targets))[2:]
v_data['version'] = new_ver
v_data['timestamp'] = int(time.time() * 1000)
v_data['round'] = "Round 13 Calibration"
v_data['description'] = "Restored 25 truncated reading and Part B explanations across 2002, 2009, 2010, 2016, 2017, 2020, 2021, 2022"

with open(v_path, 'w', encoding='utf-8') as f:
    json.dump(v_data, f, ensure_ascii=False, indent=2)

print(f"Updated {v_path}: {old_ver} -> {new_ver}")
