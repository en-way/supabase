import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

valid_short = {
    'is', 'in', 'on', 'at', 'to', 'by', 'of', 'as', 'it', 'or', 'an', 'be', 'do',
    'no', 'so', 'up', 'us', 'we', 'he', 'me', 'my', 'if', 'go', 'am', 'pm', 'tv',
    'ok', 'vs', 'ad', 'ai', 'ex', 'id', 're', 'ah', 'oh', 'ha'
}

suspicious_items = []

for f in sorted(glob.glob('public/data/exams/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d.get('questions', []):
        so = q['sort_order']
        # check options
        for opt in q.get('options', []):
            txt = opt['text'].strip()
            # check weird broken words like 'fish eries', 'knowl edge', 'Ameri cans', 'fo llows'
            matches = re.finditer(r'\b([a-zA-Z]{2,})\s+([a-zA-Z]{1,2})\b', txt)
            for m in matches:
                w1, w2 = m.group(1), m.group(2)
                if w2.lower() not in valid_short and not (len(w2) == 1 and w2.lower() in ['a', 'i']):
                    suspicious_items.append((yr, cat, so, opt['key'], f"{w1} {w2}", txt))

print(f"Total suspicious broken words in options: {len(suspicious_items)}")
for item in suspicious_items:
    print(f"{item[0]} {item[1]} Q{item[2]} [{item[3]}]: '{item[4]}' in: {repr(item[5])}")
