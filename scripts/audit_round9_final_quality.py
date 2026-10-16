import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = 'public/data/exams'
files = glob.glob(f'{exams_dir}/*.json')

print(f"Total exams in public/data/exams: {len(files)}")

stats = {
    'ky1': {'total': 0, 'with_kd': 0, 'with_sd': 0, 'with_pc': 0, 'too_short': 0, 'defects': []},
    'ky2': {'total': 0, 'with_kd': 0, 'with_sd': 0, 'with_pc': 0, 'too_short': 0, 'defects': []}
}

for f in sorted(files):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    exam = d.get('exam', {})
    cat = exam.get('category_id')
    year = exam.get('year')
    
    for q in d.get('questions', []):
        q_num = q.get('sort_order')
        if 1 <= q_num <= 20:
            stats[cat]['total'] += 1
            expl = q.get('explanation') or ''
            
            has_kd = any(k in expl for k in ['考点', '试题考点', '【考点', '［考点', '[考点'])
            has_sd = any(k in expl for k in ['思路', '解题思路', '【思路', '［思路', '[思路'])
            has_pc = any(k in expl for k in ['排除', '错项排除', '【错项', '［错项', '[错项', '干扰项'])
            
            if has_kd:
                stats[cat]['with_kd'] += 1
            if has_sd:
                stats[cat]['with_sd'] += 1
            if has_pc:
                stats[cat]['with_pc'] += 1
                
            if len(expl) < 120:
                stats[cat]['too_short'] += 1
                stats[cat]['defects'].append((year, q_num, f'Length {len(expl)} < 120', expl[:50]))
                
            # Check for contamination
            if any(k in expl for k in ['词汇注释与难句分析', '结构切分：', '功能注释：']):
                stats[cat]['defects'].append((year, q_num, 'Contaminated with passage analysis', expl[:50]))

print("\n=== English 1 (ky1) Cloze Quality Stats ===")
print(f"Total cloze questions: {stats['ky1']['total']}")
print(f"Has 【考点提炼】: {stats['ky1']['with_kd']} ({stats['ky1']['with_kd']/stats['ky1']['total']*100:.1f}%)")
print(f"Has 【解题思路】: {stats['ky1']['with_sd']} ({stats['ky1']['with_sd']/stats['ky1']['total']*100:.1f}%)")
print(f"Has 【错项排除】: {stats['ky1']['with_pc']} ({stats['ky1']['with_pc']/stats['ky1']['total']*100:.1f}%)")
print(f"Too short (< 120): {stats['ky1']['too_short']}")
print(f"Total defects found: {len(stats['ky1']['defects'])}")
for d in stats['ky1']['defects']:
    print(' ', d)

print("\n=== English 2 (ky2) Cloze Quality Stats ===")
print(f"Total cloze questions: {stats['ky2']['total']}")
print(f"Has 【考点提炼】: {stats['ky2']['with_kd']} ({stats['ky2']['with_kd']/stats['ky2']['total']*100:.1f}%)")
print(f"Too short (< 120): {stats['ky2']['too_short']}")
