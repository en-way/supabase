import json
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for p in sorted(glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json')):
    d = json.load(open(p, encoding='utf-8'))
    if d.get('exam', {}).get('category_id') != 'ky1':
        continue
    yr = d.get('exam', {}).get('year')
    for q in d.get('questions', []):
        qn = q.get('question_number')
        expl = q.get('explanation', '')
        for wm in ['公众号', '旗胜', '微信', 'QQ', 'qq', '淘宝', '店铺']:
            if wm in expl:
                print(f"{yr} Q{qn}: contains watermark '{wm}'")
