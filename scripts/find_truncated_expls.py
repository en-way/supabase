import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams = sorted(glob.glob("public/data/exams/*.json"))
truncated_list = []

for ef in exams:
    with open(ef, 'r', encoding='utf-8') as f:
        data = json.load(f)
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    
    for q in data.get('questions', []):
        so = q.get('sort_order')
        expl = (q.get('explanation') or '').strip()
        
        # Check if explanation ends abruptly:
        # e.g., ends with comma, colon, opening quote, incomplete word, or lacks terminal punctuation
        # or ends with "在", "的", "为", "指", "是", "与", "和", "有", "于", "后文进一步介", "在于\""
        is_trunc = False
        if len(expl) > 0 and len(expl) < 250:
            last_char = expl[-1]
            last_two = expl[-2:]
            if last_char in '，、：(（"“\'_ ':
                is_trunc = True
            elif last_two in ['在于', '关于', '说明', '通过', '指出', '表达', '进一', '步介', '体现', '以及', '因为', '由于', '为了']:
                is_trunc = True
            elif last_char in ['在', '的', '为', '指', '是', '与', '和', '有', '于', '其', '后', '该', '将', '并']:
                is_trunc = True
            elif expl.endswith('・') or expl.endswith('·'):
                is_trunc = True
            elif not expl.endswith(('。', '！', '？', '”', '’', ')', '）', ']', '】', '>', '；', '.')):
                is_trunc = True
        
        if is_trunc:
            truncated_list.append((yr, cat, so, len(expl), expl[-40:], expl))

print(f"Total truncated / incomplete explanations found: {len(truncated_list)}")
for t in truncated_list:
    print(f"[{t[0]} {t[1]} Q{t[2]}] len={t[3]} | tail: ...{t[4]}")
