import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = 'public/data/exams'
targets = [(2018, 3), (2018, 17), (2018, 20), (2020, 4), (2020, 10), (2020, 15), (2020, 20), (2021, 6), (2021, 20)]

fixed = 0
for f in glob.glob(f'{exams_dir}/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    exam = d.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')
    
    modified = False
    for q in d.get('questions', []):
        q_num = q.get('sort_order')
        if (year, q_num) in targets and cat == 'ky1':
            expl = q.get('explanation', '')
            # Cut at 词汇注释与难句分析
            for marker in ['词汇注释与难句分析', '词汇注释', '•语篇分析']:
                pos = expl.find(marker)
                if pos != -1:
                    clean_expl = expl[:pos].strip()
                    old_len = len(expl)
                    q['explanation'] = clean_expl
                    modified = True
                    fixed += 1
                    print(f"[{year} Q{q_num}] Stripped tail from {old_len} to {len(clean_expl)} chars")
                    break
    if modified:
        with open(f, 'w', encoding='utf-8') as fp:
            json.dump(d, fp, ensure_ascii=False, indent=2)

print(f"Total stripped: {fixed}")
