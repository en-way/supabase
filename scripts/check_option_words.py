import json
import glob
import re

exams = glob.glob('public/data/exams/*.json')

# Collect all words in options (only letters)
# Find words that might be OCR errors: e.g. uncommon capitalization, repeated consonants, weird letter combos, etc.
word_occurrences = {}

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')

    for q in data.get('questions', []):
        q_num = q.get('sort_order')
        opts = q.get('options', [])
        for opt in opts:
            text = opt.get('text', '')
            words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b", text)
            for w in words:
                w_lower = w.lower()
                word_occurrences.setdefault(w_lower, []).append((year, cat, q_num, opt.get('key'), text, w))

print(f"Total unique lower-case words across all options: {len(word_occurrences)}")

# Look for single-letter words other than 'a' and 'i'
single_letters = {w: occ for w, occ in word_occurrences.items() if len(w) == 1 and w not in ('a', 'i')}
print(f"Single letter anomalies: {len(single_letters)}")
for w, occ in single_letters.items():
    print(f"  Word '{w}': {occ[:3]}")

# Look for words containing weird patterns:
# e.g. triple identical letters (like 'lll'), or rare clusters
rare_patterns = []
for w, occ in word_occurrences.items():
    if re.search(r'([a-z])\1\1', w): # 3 identical consecutive letters
        rare_patterns.append((w, occ))
    # Words with no vowels (excluding common abbrevs like 'mr', 'tv', 'by', 'my')
    elif not re.search(r'[aeiouy]', w):
        rare_patterns.append((w, occ))

print(f"Words with 3 consecutive letters or no vowels: {len(rare_patterns)}")
for w, occ in rare_patterns:
    print(f"  Word '{w}': {occ[:2]}")
