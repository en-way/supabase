import json
import glob
import re

exams = glob.glob('public/data/exams/*.json')

all_problematic_options = []

for f in sorted(exams):
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data.get('exam', {})
    year = exam.get('year')
    cat = exam.get('category_id')

    for q in data.get('questions', []):
        q_num = q.get('sort_order')
        opts = q.get('options', [])
        for opt in opts:
            k = opt.get('key')
            text = opt.get('text', '')

            # Check 1: single letters separated by space: e.g. "O b se rv e" or "e ne ra ll y"
            # Pattern: 1 or 2 letters followed by space followed by 1 or 2 letters
            has_intra_word_spaces = False
            words = text.split()
            # If multiple consecutive short tokens (length 1 or 2) that are not normal words like 'in a', 'to be', 'on an', 'of it'
            # Let's check regex for letter + space + letter inside what should be a word
            if re.search(r'\b[a-zA-Z]\s+[a-zA-Z]\s+[a-zA-Z]\b', text):
                has_intra_word_spaces = True
            elif re.search(r'\b[a-zA-Z]{2,}\s+[a-zA-Z]{1,2}\s+[a-zA-Z]{2,}\b', text):
                # e.g. "comp l em e nt ary", "developm e nt"
                # check if tokens are in normal english
                common_short = {'a', 'an', 'in', 'on', 'at', 'to', 'of', 'by', 'as', 'is', 'it', 'he', 'we', 'or', 'so', 'if', 'no', 'up', 'do', 'my'}
                for i in range(len(words)-1):
                    w1, w2 = words[i].lower(), words[i+1].lower()
                    if len(w1) <= 2 and w1 not in common_short:
                        has_intra_word_spaces = True
                        break
                    if len(w2) <= 2 and w2 not in common_short:
                        has_intra_word_spaces = True
                        break

            # Check 2: Truncated option: ends with incomplete word or fragment, e.g. "the sp", "keep th", "less ch anc", "p ubli s hi", "rms will I"
            is_truncated = False
            last_word = words[-1].lower() if words else ''
            # If last word is 1 or 2 letters and not a normal ending word (like 'it', 'in', 'on', 'up', 'so', 'to', 'by', 'at', 'no', 'us', 'me')
            normal_ends = {'it', 'in', 'on', 'up', 'so', 'to', 'by', 'at', 'no', 'us', 'me', 'do', 'be', 'he', 'we', 'is', 'as', 'if', 'or', 'an', 'am'}
            if len(last_word) <= 2 and last_word.isalpha() and last_word not in normal_ends:
                is_truncated = True

            # If text has abnormal characters like unclosed parens: e.g. "given up(to s b/ sth"
            has_paren_mismatch = text.count('(') != text.count(')')

            if has_intra_word_spaces or is_truncated or has_paren_mismatch:
                all_problematic_options.append({
                    'year': year,
                    'cat': cat,
                    'q_num': q_num,
                    'key': k,
                    'text': text,
                    'intra_space': has_intra_word_spaces,
                    'truncated': is_truncated,
                    'paren': has_paren_mismatch
                })

print(f"Total problematic options found: {len(all_problematic_options)}")
# Group by exam
by_exam = {}
for item in all_problematic_options:
    key = f"{item['year']} {item['cat']}"
    by_exam.setdefault(key, []).append(item)

for k, items in sorted(by_exam.items()):
    print(f"\n=== {k} ({len(items)} problematic options) ===")
    for it in items:
        flags = []
        if it['intra_space']: flags.append('INTRA_SPACE')
        if it['truncated']: flags.append('TRUNCATED')
        if it['paren']: flags.append('PAREN')
        print(f"  Q{it['q_num']} [{it['key']}]: '{it['text']}' [{', '.join(flags)}]")
