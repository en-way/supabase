# -*- coding: utf-8 -*-
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_files = sorted(glob.glob('public/data/exams/*.json'))

mismatches = []

for f in all_files:
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d.get('questions', []):
        so = q.get('sort_order')
        expl = q.get('explanation', '') or ''
        opts = q.get('options', [])
        
        # If explanation explicitly has [A] xxx [B] yyy in it, check if opt text appears
        # Look for pattern [A] <english_text>
        expl_opts = re.findall(r'\[([A-D])\]\s*([A-Za-z][A-Za-z\s\,\'\-\?]+)', expl)
        if len(expl_opts) >= 2:
            # Check overlap with opts
            opt_texts = {o.get('key'): o.get('text', '').strip().lower() for o in opts}
            has_match = False
            for k, text in expl_opts:
                t_clean = text.strip().lower()
                if len(t_clean) > 5 and k in opt_texts:
                    target = opt_texts[k]
                    # check if either contains the other or substantial overlap
                    words_expl = set(t_clean.split()[:4])
                    words_opt = set(target.split()[:4])
                    if len(words_expl.intersection(words_opt)) >= 2 or t_clean in target or target in t_clean:
                        has_match = True
                        break
            # If [A]... [D] were found in expl but NONE matched opts, report mismatch!
            if not has_match and len(opts) == 4:
                mismatches.append((yr, cat, so, [f"[{k}] {t[:25]}" for k, t in expl_opts[:4]], [f"[{o.get('key')}] {o.get('text', '')[:25]}" for o in opts]))

print(f"Total potential option-explanation cross mismatches: {len(mismatches)}")
for m in mismatches:
    print(f"=== {m[0]} {m[1]} Q{m[2]} ===")
    print(f"  In Expl: {m[3]}")
    print(f"  In Opts: {m[4]}")
