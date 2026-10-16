# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_files = sorted(glob.glob('public/data/exams/*.json'))

short_expls = []
suspicious_stems = []
suspicious_options = []

for f in all_files:
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d.get('questions', []):
        so = q.get('sort_order')
        stem = q.get('stem', '')
        expl = q.get('explanation', '') or ''
        opts = q.get('options', [])
        
        # 1. Expl length
        if len(expl.strip()) < 150:
            short_expls.append((yr, cat, so, len(expl.strip()), expl.strip()[:60]))
            
        # 2. Suspicious stem
        if stem.endswith('_') or stem.endswith('__') or '  ' in stem:
            suspicious_stems.append((yr, cat, so, stem))
            
        # 3. Suspicious options
        for opt in opts:
            ot = opt.get('text', '')
            if len(ot) > 250:
                suspicious_options.append((yr, cat, so, opt.get('key'), len(ot), ot[:80]))

print(f"=== Round 16 Deep Forensic Scan ===")
print(f"1. Total questions with explanation length < 150 chars: {len(short_expls)}")
for se in sorted(short_expls, key=lambda x: x[3])[:15]:
    print(f"   {se[0]} {se[1]} Q{se[2]}: len={se[3]} | {repr(se[4])}")

print(f"\n2. Total suspicious stems: {len(suspicious_stems)}")
for ss in suspicious_stems[:10]:
    print(f"   {ss[0]} {ss[1]} Q{ss[2]}: {repr(ss[3])}")

print(f"\n3. Total suspiciously long options (> 250 chars): {len(suspicious_options)}")
for so in suspicious_options[:10]:
    print(f"   {so[0]} {so[1]} Q{so[2]} opt [{so[3]}]: len={so[4]} | {repr(so[5])}")
