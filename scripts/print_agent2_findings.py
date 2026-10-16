import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open(r'C:\Users\57867\.gemini\antigravity\brain\13a05a49-1b90-43dd-b11a-4519b940e00a\scratch\audit_report.json', encoding='utf-8'))

print("=== 1. OPTIONS DEFECTS ===")
for d in data['options_defects']:
    print(f"[{d['year']} Q{d['q']}] field: {d['field']}")
    print(f"   current:      {repr(d['current'])}")
    print(f"   ground_truth: {repr(d['ground_truth'])}")

print("\n=== 2. STEM TRUNCATION DEFECTS ===")
for d in data['stem_truncation_defects']:
    print(f"[{d['year']} Q{d['q']}]")
    print(f"   current:      {repr(d['current'])}")
    print(f"   ground_truth: {repr(d['ground_truth'])}")

print("\n=== 3. PART B DEFECTS ===")
for d in data['part_b_defects']:
    print(f"[{d['year']} Q{d['q']}] field: {d['field']}")
    print(f"   current:      {repr(d['current'])}")
    print(f"   ground_truth: {repr(d['ground_truth'])}")

print("\n=== 4. CLOZE CRITICAL DEFECTS ===")
for d in data['cloze_critical_defects']:
    print(f"[{d['year']} Q{d.get('q', 'ALL')}] type: {d['defect_type']}")
    print(f"   issue: {d['issue']}")
