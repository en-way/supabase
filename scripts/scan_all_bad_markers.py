# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_files = sorted(glob.glob('public/data/exams/*.json'))

bad_patterns = [
    '掌柜', '旺旺', '淘宝', '店铺', '新一文化',
    '全文翻译', '长难句分析', '核心词与超纲词',
    '核心词汇与超纲词汇', '文章题材结构分析',
    '【翻译】', '【长难句分析】'
]

results = []
for f in all_files:
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d.get('questions', []):
        expl = q.get('explanation', '') or ''
        so = q.get('sort_order')
        for bp in bad_patterns:
            if bp in expl:
                results.append((yr, cat, so, bp, len(expl)))

print(f"Total matching items across all files: {len(results)}")
for r in results:
    print(r)
