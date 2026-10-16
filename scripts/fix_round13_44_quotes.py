import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update round13_all_calibrated.json
with open('scripts/round13_all_calibrated.json', 'r', encoding='utf-8') as f:
    cal = json.load(f)

cal['2021_ky2_q21']['explanation'] = cal['2021_ky2_q21']['explanation'].replace('44core skills"', '"core skills"').replace('44 core skills"', '"core skills"')
cal['2022_ky1_q32']['explanation'] = cal['2022_ky1_q32']['explanation'].replace('innovations44科学创新"', 'innovations“科学创新”')
cal['2022_ky1_q36']['explanation'] = cal['2022_ky1_q36']['explanation'].replace('44unjustified dismissals"', '"unjustified dismissals"')

with open('scripts/round13_all_calibrated.json', 'w', encoding='utf-8') as f:
    json.dump(cal, f, ensure_ascii=False, indent=2)

# 2. Update local exam JSON files
for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    modified = False
    for q in d['questions']:
        so = q['sort_order']
        if yr == 2021 and cat == 'ky2' and so == 21:
            q['explanation'] = cal['2021_ky2_q21']['explanation']
            modified = True
        elif yr == 2022 and cat == 'ky1' and so == 32:
            q['explanation'] = cal['2022_ky1_q32']['explanation']
            modified = True
        elif yr == 2022 and cat == 'ky1' and so == 36:
            q['explanation'] = cal['2022_ky1_q36']['explanation']
            modified = True
    if modified:
        with open(f, 'w', encoding='utf-8') as out:
            json.dump(d, out, ensure_ascii=False, indent=2)
        print(f"Updated {f} for ({yr}, {cat})")

print("Fixed OCR 44 quotes in JSON files.")
