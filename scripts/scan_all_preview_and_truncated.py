import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

preview_tags = ["事实细节", "段落主旨", "写作目的", "因果细节", "人物观点", "词义猜测", "篇章主旨", "段落推断", "态度倾向"]

exams = sorted(glob.glob('public/data/exams/*.json'))
suspects = []

for ef in exams:
    with open(ef, 'r', encoding='utf-8') as f:
        d = json.load(f)
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d.get('questions', []):
        so = q.get('sort_order')
        stem = q.get('stem', '')
        opts = q.get('options', [])
        ans = q.get('correct_answer')
        expl = (q.get('explanation') or '').strip()
        
        # 1. Preview table check
        for tag in preview_tags:
            if tag in expl and len(expl) < 250 and not any(k in expl for k in ["【精准定位】", "【命题解密】", "【解题思路】", "【答案】", "【精解】"]):
                suspects.append((yr, cat, so, "PREVIEW_TABLE", len(expl), expl[:60].replace('\n', ' ')))
                break
        
        # 2. Incomplete options
        if len(opts) < 4:
            suspects.append((yr, cat, so, "INCOMPLETE_OPTIONS", len(opts), str([o.get('key') for o in opts])))
        
        # 3. Truncated expl ending
        if expl.endswith(('、', '以及', '因此推测第三、', '由第43 题的分析可知，第三、', '即如何高效地提升')):
            suspects.append((yr, cat, so, "TRUNCATED_ENDING", len(expl), expl[-40:].replace('\n', ' ')))
        
        # 4. Very short expl in Reading (Q21-40) when other questions in same exam are long
        if so >= 21 and so <= 40 and len(expl) < 150:
            if not any(s[0] == yr and s[1] == cat and s[2] == so for s in suspects):
                suspects.append((yr, cat, so, "SHORT_READING_EXPL", len(expl), expl[:60].replace('\n', ' ')))

print(f"Total suspects found: {len(suspects)}")
for s in suspects:
    print(f"[{s[0]} {s[1]} Q{s[2]}] {s[3]} (len={s[4]}): {s[5]}")
