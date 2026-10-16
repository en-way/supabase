import glob
import json
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

exams = sorted(glob.glob("public/data/exams/*.json"))
expl_stats = defaultdict(lambda: {"total": 0, "short": 0, "samples": []})

for ef in exams:
    with open(ef, 'r', encoding='utf-8') as f:
        data = json.load(f)
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    key = f"{yr} {cat}"
    for q in data.get('questions', []):
        so = q.get('sort_order')
        expl = (q.get('explanation') or '').strip()
        expl_stats[key]["total"] += 1
        if len(expl) < 150:
            expl_stats[key]["short"] += 1
            expl_stats[key]["samples"].append((so, len(expl), expl[:80]))

print(f"{'Exam':<12} | {'Total':<6} | {'Short (<150)':<12} | {'Short Ratio':<10}")
print("-" * 50)
for k, v in sorted(expl_stats.items()):
    ratio = f"{(v['short'] / v['total']) * 100:.1f}%"
    print(f"{k:<12} | {v['total']:<6} | {v['short']:<12} | {ratio:<10}")

print("\n=== Sample of short explanations ===")
for k, v in sorted(expl_stats.items()):
    if v["samples"]:
        print(f"--- {k} ({len(v['samples'])} short) ---")
        for s in v["samples"][:3]:
            print(f"  Q{s[0]} ({s[1]} chars): {s[2]}")
