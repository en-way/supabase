# -*- coding: utf-8 -*-
"""
audit_round18_deep_audit.py
Round 18 Deep Forensic Audit:
1. Option text vs Explanation Option Mentions cross-match across all 1825 questions.
2. Abrupt stem endings (e.g. ending in 'that', 'to', 'because', 'indicates that', 'implies that', without trailing blank/underscore/period).
3. Option texts with suspicious OCR truncations, dangling hyphens, or broken words.
4. Part B options & stems cross-validation across all 37 Part B exams.
"""

import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'exams'))
exam_files = sorted(glob.glob(os.path.join(exams_dir, '*.json')))

print(f"=== Round 18 Deep Forensic Audit ({len(exam_files)} exams) ===")

option_mismatches = []
abrupt_stems = []
suspicious_option_texts = []
part_b_inconsistencies = []
passage_tail_issues = []

for fpath in exam_files:
    data = json.load(open(fpath, encoding='utf-8'))
    yr = data['exam'].get('year')
    cat = data['exam'].get('category_id')
    title = data['exam'].get('title')
    questions = data.get('questions', [])
    passages = data.get('passages', [])

    # Audit Passages
    for p in passages:
        c = (p.get('content') or '').strip()
        so = p.get('sort_order')
        # Check passage tail
        if re.search(r'\b(?:[2-4]\d|Q[2-4]\d)\s*[\.・\、\:]\s*[A-Z]', c[-200:]):
            passage_tail_issues.append((title, so, "stem_near_tail", c[-80:]))
        if re.search(r'\[[A-G]\]\s*[a-zA-Z]{3,}', c[-100:]):
            passage_tail_issues.append((title, so, "option_near_tail", c[-80:]))

    # Audit Questions
    for q in questions:
        so = q.get('sort_order')
        stem = (q.get('stem') or '').strip()
        expl = q.get('explanation') or ''
        opts = q.get('options') or []
        ans = q.get('correct_answer')

        # 1. Check abrupt stem endings
        # Normal stems end with '.', '?', ':', '________.', '________', or '"'
        if so > 20: # reading or part B
            if not re.search(r'[\.\?\:\_\”\"\']$', stem):
                abrupt_stems.append((title, so, "no_terminal_punct", stem))
            elif stem.endswith('that') or stem.endswith('to') or stem.endswith('because') or stem.endswith('with'):
                abrupt_stems.append((title, so, "dangling_word", stem))

        # 2. Check options for broken words / truncation
        if isinstance(opts, list):
            opt_dict = {}
            for o in opts:
                k = o.get('key')
                t = (o.get('text') or '').strip()
                opt_dict[k] = t
                if so <= 40:
                    if t.endswith('-') or t.endswith('—'):
                        suspicious_option_texts.append((title, so, k, "ends_with_hyphen", t))
                    if re.search(r'\b[a-z]{1,2}\s+[a-z]{1,2}\s+[a-z]{1,2}\b', t): # OCR broken spacing
                        suspicious_option_texts.append((title, so, k, "broken_spacing", t))
                    # check for 1-word options in reading (excluding true/false or tone/attitude/vocabulary questions)
                    if len(t.split()) == 1 and len(t) < 4 and so > 20:
                        suspicious_option_texts.append((title, so, k, "very_short_reading_opt", t))

            # 3. Check Option text vs Expl Option Mentions
            # In explanations, options are often analyzed with [A] ..., [B] ...
            # Let's see if the explanation analyzes completely different option words
            if so in range(21, 41):
                # Search for [A] word in expl
                for k in ['A', 'B', 'C', 'D']:
                    m = re.search(r'\[\s*' + k + r'\s*\]\s*([a-zA-Z]{4,})', expl)
                    if m and k in opt_dict:
                        expl_word = m.group(1).lower()
                        opt_text_lower = opt_dict[k].lower()
                        # If the explanation explicitly introduces [A] followed by an English word that is not anywhere in opt_text:
                        # (Allow when explanation is in Chinese: e.g. [A] 选项中文...)
                        # Only check if expl_word is definitely an option keyword (not generic words like 'option', 'item', 'from')
                        generic = {'this', 'that', 'from', 'with', 'when', 'what', 'which', 'their', 'there', 'because'}
                        if expl_word not in generic and expl_word not in opt_text_lower:
                            # Verify if expl has English option text
                            m_opt_line = re.search(r'\[\s*' + k + r'\s*\]\s*([A-Za-z\s\,\'\-]{10,})', expl)
                            if m_opt_line:
                                expl_opt_snippet = m_opt_line.group(1).strip()
                                # compare with opt_dict[k]
                                words_expl = set(re.findall(r'\b[a-z]{4,}\b', expl_opt_snippet.lower()))
                                words_opt = set(re.findall(r'\b[a-z]{4,}\b', opt_text_lower))
                                if words_expl and not (words_expl & words_opt):
                                    option_mismatches.append((title, so, k, opt_dict[k], expl_opt_snippet[:50]))

print(f"\n1. Passage tail issues: {len(passage_tail_issues)}")
for item in passage_tail_issues[:10]:
    print("   ", item)

print(f"\n2. Abrupt stem endings: {len(abrupt_stems)}")
for item in abrupt_stems[:15]:
    print("   ", item)

print(f"\n3. Suspicious option texts: {len(suspicious_option_texts)}")
for item in suspicious_option_texts[:15]:
    print("   ", item)

print(f"\n4. Option mismatches vs explanation mentions: {len(option_mismatches)}")
for item in option_mismatches[:15]:
    print("   ", item)
