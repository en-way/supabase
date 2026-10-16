import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams = sorted(glob.glob("public/data/exams/*.json"))
print(f"Total exams: {len(exams)}")

short_expls = []
odd_stems = []
odd_options = []
short_passages = []

for ef in exams:
    with open(ef, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    exam = data['exam']
    yr = exam['year']
    cat = exam['category_id']
    title = exam.get('title', '')

    # Check passages
    for p in data.get('passages', []):
        c = p.get('content', '')
        words = len(c.split())
        pid = p.get('id')
        so = p.get('sort_order', 0)
        pt = p.get('passage_type', '')
        if words < 100:
            short_passages.append((yr, cat, so, pt, words, c[:60]))
        # check Chinese characters in English passage
        cn_chars = len(re.findall(r'[\u4e00-\u9fff]', c))
        if cn_chars > 5:
            print(f"[Passage CN Leaked] {yr} {cat} P{so} has {cn_chars} Chinese characters!")

    # Check questions
    for q in data.get('questions', []):
        so = q.get('sort_order')
        stem = q.get('stem', '')
        opts = q.get('options', [])
        ans = q.get('correct_answer')
        expl = q.get('explanation', '') or ''
        
        # 1. Expl length
        if len(expl.strip()) < 150:
            short_expls.append((yr, cat, so, len(expl.strip()), expl.strip()))
        
        # 2. Odd stem
        if len(stem.strip()) < 10 and 'blank' not in stem:
            odd_stems.append((yr, cat, so, stem))
        if stem.endswith('?') is False and stem.endswith('.') is False and stem.endswith('_') is False and 'blank' not in stem:
            # check if stem is truncated
            pass

        # 3. Odd options
        opt_texts = [o.get('text', '') for o in opts]
        if len(opts) != 4:
            odd_options.append((yr, cat, so, f"Option count {len(opts)} != 4"))
        for o in opts:
            ot = o.get('text', '')
            if len(ot.strip()) == 0:
                odd_options.append((yr, cat, so, f"Empty option {o.get('key')}"))
            if any(k in ot for k in ['[A]', '[B]', '[C]', '[D]', '【A】', '【B】', '【C】', '【D】']):
                odd_options.append((yr, cat, so, f"Leaked tag in option {o.get('key')}: {ot}"))
            if ot.startswith('A.') or ot.startswith('B.') or ot.startswith('C.') or ot.startswith('D.'):
                odd_options.append((yr, cat, so, f"Prefix in option {o.get('key')}: {ot}"))

print(f"\n=== Audit Results ===")
print(f"Passages with <100 words: {len(short_passages)}")
for p in short_passages:
    print(f"  {p}")

print(f"\nQuestions with explanation < 150 chars: {len(short_expls)}")
for se in short_expls[:20]:
    print(f"  [{se[0]} {se[1]} Q{se[2]}] len={se[3]}: {se[4][:70]}...")
if len(short_expls) > 20:
    print(f"  ... and {len(short_expls) - 20} more.")

print(f"\nOdd options count: {len(odd_options)}")
for oo in odd_options:
    print(f"  {oo}")
