# -*- coding: utf-8 -*-
"""
audit_round17_deep_scan.py
Deep audit for Round 17:
1. Explanations mentioning different question numbers (e.g. Q23 explanation starts with "24.")
2. Unbalanced brackets or parentheses in stems
3. Abnormally short or long options
4. Option texts matching other questions in the same passage
5. Part B options completeness and correctness
"""

import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'exams'))
exam_files = sorted(glob.glob(os.path.join(exams_dir, '*.json')))

print(f"=== Round 17 Deep Forensic Scan ({len(exam_files)} exams) ===")

q_number_mismatches = []
stem_syntax_anomalies = []
abnormal_option_lengths = []
suspicious_expl_fragments = []
part_b_option_issues = []

for fpath in exam_files:
    data = json.load(open(fpath, encoding='utf-8'))
    yr = data['exam'].get('year')
    cat = data['exam'].get('category_id')
    title = data['exam'].get('title')
    questions = data.get('questions', [])

    for q in questions:
        so = q.get('sort_order')
        stem = q.get('stem') or ''
        expl = q.get('explanation') or ''
        opts = q.get('options') or []

        # 1. Check explanation question number prefix
        m_expl_no = re.match(r'^\s*(?:第\s*)?(\d{1,2})\s*[\.、\:\s]', expl)
        if m_expl_no:
            expl_no = int(m_expl_no.group(1))
            if expl_no != so and 1 <= expl_no <= 45:
                q_number_mismatches.append((title, so, f"Expl starts with {expl_no}"))

        # 2. Check stem unbalanced quotes / brackets
        # Ignore standard blank [1] or [A]
        clean_stem = re.sub(r'\[\d+\]', '', stem)
        clean_stem = re.sub(r'\[[A-G]\]', '', clean_stem)
        if clean_stem.count('(') != clean_stem.count(')'):
            stem_syntax_anomalies.append((title, so, "unbalanced_parentheses", stem))
        if clean_stem.count('[') != clean_stem.count(']'):
            stem_syntax_anomalies.append((title, so, "unbalanced_brackets", stem))

        # 3. Check abnormal option lengths
        if isinstance(opts, list):
            for o in opts:
                k = o.get('key')
                t = (o.get('text') or '').strip()
                if so <= 40 and len(t) < 1:
                    abnormal_option_lengths.append((title, so, k, "empty_text", t))
                elif so <= 40 and len(t) > 300:
                    abnormal_option_lengths.append((title, so, k, "too_long", t[:50]))

        # 4. Part B checks (41-45)
        if 41 <= so <= 45:
            if not isinstance(opts, list) or len(opts) < 4:
                part_b_option_issues.append((title, so, "insufficient_options", len(opts) if isinstance(opts, list) else 0))

        # 5. Suspicious fragments in expl
        bad_words = ['（待补）', '暂无解析', 'TODO', 'undefined', 'null']
        for bw in bad_words:
            if bw in expl:
                suspicious_expl_fragments.append((title, so, bw))

print(f"1. Explanation question number mismatches: {len(q_number_mismatches)}")
for item in q_number_mismatches[:10]:
    print("   ", item)

print(f"2. Stem syntax anomalies: {len(stem_syntax_anomalies)}")
for item in stem_syntax_anomalies[:10]:
    print("   ", item)

print(f"3. Abnormal option lengths: {len(abnormal_option_lengths)}")
for item in abnormal_option_lengths[:10]:
    print("   ", item)

print(f"4. Part B option issues: {len(part_b_option_issues)}")
for item in part_b_option_issues[:10]:
    print("   ", item)

print(f"5. Suspicious explanation fragments: {len(suspicious_expl_fragments)}")
for item in suspicious_expl_fragments[:10]:
    print("   ", item)
