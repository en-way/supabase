import json
import glob
import re

exams = sorted(glob.glob('public/data/exams/*.json'))

real_issues = []

# Exclude legitimate English two-word combos with single letters like 'a boy', 'I think', 'A & P', 'U.S.', etc.
legit_single = {'a', 'i'}

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data['exam']
    year = exam['year']
    cat = exam['category_id']

    for q in data['questions']:
        q_num = q['sort_order']
        for o in q.get('options', []):
            text = o.get('text', '')
            k = o.get('key')
            
            # Check 1: single letters not in ('a', 'i')
            tokens = re.findall(r"\b[a-zA-Z]+\b", text)
            bad_single = [t for t in tokens if len(t) == 1 and t.lower() not in legit_single]
            if bad_single:
                real_issues.append((year, cat, q_num, k, text, f"Isolated single letters: {bad_single}"))

            # Check 2: truncated words at end of option
            if tokens:
                last_tok = tokens[-1].lower()
                # Common valid short ending words
                valid_short_end = {'it', 'in', 'on', 'up', 'so', 'to', 'by', 'at', 'no', 'us', 'me', 'do', 'be', 'he', 'we', 'is', 'as', 'if', 'or', 'an', 'am', 'all', 'out', 'off', 'not', 'too', 'day', 'one', 'new', 'now', 'way', 'law', 'art', 'men', 'job', 'car', 'war', 'oil', 'tax', 'bed', 'end', 'dog', 'sea', 'sky', 'sun', 'air', 'eye', 'god', 'act', 'age', 'arm', 'bar', 'box', 'boy', 'bus', 'cat', 'cup', 'ear', 'egg', 'fan', 'fat', 'fee', 'fit', 'fix', 'fly', 'fun', 'gap', 'gas', 'gun', 'guy', 'hat', 'hit', 'ice', 'ink', 'jar', 'jaw', 'joy', 'key', 'kid', 'lab', 'leg', 'lie', 'lip', 'log', 'lot', 'map', 'mud', 'net', 'nut', 'pan', 'pen', 'pet', 'pie', 'pig', 'pin', 'pit', 'pot', 'rag', 'rat', 'raw', 'ray', 'rib', 'rip', 'rod', 'row', 'rug', 'run', 'sad', 'set', 'sin', 'sir', 'son', 'spy', 'tap', 'tea', 'tie', 'tin', 'tip', 'toe', 'ton', 'top', 'toy', 'van', 'vet', 'via', 'vow', 'wet', 'win', 'zoo', 'dna', 'fcc', 'ftc', 'rsc', 'nrc', 'dnt', 'prh', 'cct', 'gpa', 'ai', 'tv'}
                if len(last_tok) <= 2 and last_tok not in valid_short_end:
                    real_issues.append((year, cat, q_num, k, text, f"Truncated last word: '{tokens[-1]}'"))

            # Check 3: unclosed parens
            if text.count('(') != text.count(')'):
                real_issues.append((year, cat, q_num, k, text, "Mismatched parens"))

print(f"Total real option issues found: {len(real_issues)}")
for it in real_issues:
    print(f"{it[0]} {it[1]} Q{it[2]} [{it[3]}]: '{it[4]}' --> {it[5]}")
