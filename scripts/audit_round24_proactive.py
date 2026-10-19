import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Proactive Forensic Audit for Round 24 ===")

exam_files = sorted(glob.glob('public/data/exams/*.json'))

# 1. Suspicious stem endings: ending with preposition, article, auxiliary verb without blank
suspicious_stems = []

# 2. Reading comprehension options ending with suspicious words
suspicious_options = []

# 3. Explanations containing suspicious leakage words or short lengths
suspicious_expls = []

# 4. Passages with dangling hyphens or broken words
suspicious_passages = []

for f in exam_files:
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    title = d['exam']['title']
    
    for q in d.get('questions', []):
        so = q['sort_order']
        stem = q.get('stem', '').strip()
        ans = q.get('correct_answer', '').strip()
        expl = q.get('explanation', '').strip()
        opts = q.get('options', [])
        opt_texts = [o.get('text', '').strip() for o in opts]
        
        # Check stem ending
        if so in range(21, 41):
            # Check if stem ends with 'the', 'a', 'an', 'that', 'which', 'of', 'in', 'for', 'with', 'by', 'as', 'at', 'to'
            # without an underline or blank marker
            m = re.search(r'\b(the|a|an|that|which|of|in|for|with|by|as|at|to|is|are|was|were|has|have|had)\s*$', stem, re.IGNORECASE)
            if m:
                suspicious_stems.append((yr, cat, so, stem, m.group(1)))
            # Check if stem is unusually short
            elif len(stem) < 20 and not stem.startswith('['):
                suspicious_stems.append((yr, cat, so, stem, 'too_short'))

        # Check options
        for o in opts:
            k = o.get('key', '')
            t = o.get('text', '').strip()
            # check if option ends with suspicious incomplete word
            m_opt = re.search(r'\b(the|a|an|of|in|for|with|by|as|at|to|and|or|that|which|is|are|was|were)\s*$', t, re.IGNORECASE)
            if m_opt:
                suspicious_options.append((yr, cat, so, k, t, m_opt.group(1)))
            # check weird broken characters
            if re.search(r'[\ufffd\x7f-\x9f]', t):
                suspicious_options.append((yr, cat, so, k, t, 'unprintable_char'))
                
        # Check explanation
        if so in range(21, 41):
            if len(expl) < 250:
                suspicious_expls.append((yr, cat, so, 'too_short', len(expl), expl[:50]))
            if '全文翻译' in expl or '词汇注释' in expl or '难句分析' in expl:
                suspicious_expls.append((yr, cat, so, 'translation_leak', expl[:50]))
                
    # Check passages
    for p in d.get('passages', []):
        p_so = p.get('sort_order')
        p_c = p.get('content', '')
        if re.search(r'[\ufffd]', p_c):
            suspicious_passages.append((yr, cat, p_so, 'unprintable_char'))

print(f"\n1. Suspicious Stems ({len(suspicious_stems)}):")
for s in suspicious_stems:
    print(f"  - {s[0]} {s[1]} Q{s[2]}: [{s[4]}] -> {repr(s[3])}")

print(f"\n2. Suspicious Options ({len(suspicious_options)}):")
for o in suspicious_options:
    print(f"  - {o[0]} {o[1]} Q{o[2]} [{o[3]}]: [{o[5]}] -> {repr(o[4])}")

print(f"\n3. Suspicious Explanations ({len(suspicious_expls)}):")
for e in suspicious_expls:
    print(f"  - {e[0]} {e[1]} Q{e[2]}: {e[3]} -> {e[4]} ({e[5] if len(e) > 5 else ''})")

print(f"\n4. Suspicious Passages ({len(suspicious_passages)}):")
for p in suspicious_passages:
    print(f"  - {p[0]} {p[1]} Passage {p[2]}: {p[3]}")
