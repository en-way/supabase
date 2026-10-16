import json
import glob
import re

exams = glob.glob('public/data/exams/*.json')

issues = {
    'broken_hyphens_passage': [],
    'punct_spacing_passage': [],
    'html_entities_passage': [],
    'broken_hyphens_options': [],
    'option_spacing_issues': [],
    'reading_stems_incomplete': [],
    'duplicate_options': [],
    'suspicious_ocr_words': []
}

# Suspicious OCR patterns: e.g. words containing digits, symbols like |, {, }, ~, \, ^, weird characters
suspicious_word_pat = re.compile(r'\b[a-zA-Z]+[\d@#$%&*_=+[\]{}|\\/][a-zA-Z0-9]*\b')

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')

    # Passages
    for p in data.get('passages', []):
        p_id = p.get('id')
        p_type = p.get('passage_type')
        text = p.get('text', '')

        # HTML entities
        if '&' in text and re.search(r'&(quot|amp|lt|gt|#\d+);', text):
            issues['html_entities_passage'].append((year, cat, p_type, 'HTML entity in passage'))

        # Space after hyphen in the middle of words: e.g. "pre- requisites" or "macro- economics" vs soft hyphens
        # Look for e.g. " [a-z]+- [a-z]+ "
        broken_hy = re.findall(r'[a-zA-Z]{3,}-\s+[a-z]{3,}', text)
        if broken_hy:
            issues['broken_hyphens_passage'].append((year, cat, p_type, broken_hy[:5]))

        # Punctuation spacing: e.g. "word ," or "word ."
        punct_sp = re.findall(r'[a-zA-Z]{2,}\s+[,.?!;:]', text)
        if punct_sp:
            issues['punct_spacing_passage'].append((year, cat, p_type, punct_sp[:5]))

        # Suspicious OCR words
        susp = suspicious_word_pat.findall(text)
        if susp:
            # Filter out known safe ones if any
            susp_filtered = [w for w in susp if not re.match(r'^(COVID-19|3D|2D|U\.S\.?)$', w, re.I)]
            if susp_filtered:
                issues['suspicious_ocr_words'].append((year, cat, p_type, 'passage', susp_filtered[:5]))

    # Questions
    for q in data.get('questions', []):
        q_num = q.get('sort_order')
        stem = q.get('stem', '')
        opts = q.get('options', [])

        # Check duplicate options
        opt_texts = [o.get('text', '').strip().lower() for o in opts if o.get('text')]
        if len(opt_texts) != len(set(opt_texts)) and len(opt_texts) > 1:
            issues['duplicate_options'].append((year, cat, q_num, opt_texts))

        # Check options for broken hyphens
        for o in opts:
            otext = o.get('text', '')
            broken_o_hy = re.findall(r'[a-zA-Z]{3,}-\s+[a-z]{3,}', otext)
            if broken_o_hy:
                issues['broken_hyphens_options'].append((year, cat, q_num, o.get('key'), broken_o_hy))

        # Check reading stems (Q21-Q40)
        if 21 <= q_num <= 40:
            cleaned = stem.rstrip('""\'\'')
            if cleaned and not cleaned.endswith(('.', '?', '!', ':', '——', '—', '___', '____', '_____', '________', '________.')):
                issues['reading_stems_incomplete'].append((year, cat, q_num, stem))

print("=== AUDIT SUMMARY ===")
for k, v in issues.items():
    print(f"{k}: {len(v)} occurrences")
    if v and k != 'reading_stems_incomplete':
        for item in v[:5]:
            print(f"  {item}")

if issues['broken_hyphens_passage']:
    print(f"\nSample broken hyphens in passages ({len(issues['broken_hyphens_passage'])}):")
    for item in issues['broken_hyphens_passage'][:10]:
        print(f"  {item}")

if issues['punct_spacing_passage']:
    print(f"\nSample punctuation spacing in passages ({len(issues['punct_spacing_passage'])}):")
    for item in issues['punct_spacing_passage'][:10]:
        print(f"  {item}")

if issues['suspicious_ocr_words']:
    print(f"\nSample suspicious OCR words ({len(issues['suspicious_ocr_words'])}):")
    for item in issues['suspicious_ocr_words'][:10]:
        print(f"  {item}")
