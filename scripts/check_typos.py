import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_files = sorted(glob.glob("public/data/exams/*.json"))
count = 0
for fpath in exam_files:
    d = json.load(open(fpath, encoding='utf-8'))
    yr, cat = d['exam']['year'], d['exam']['category_id']
    for q in d['questions']:
        so = q['sort_order']
        stem = q['stem']
        if re.search(r'\b[uU]\s+[a-z]{4,}"', stem):
            print(yr, cat, so, 'stray_u_quote:', repr(stem))
            count += 1
        if re.search(r'[a-z]+rmarket', stem):
            print(yr, cat, so, 'typo_market:', repr(stem))
            count += 1
        if re.search(r'[a-zA-Z]+[0-9]+[a-zA-Z]+', stem):
            print(yr, cat, so, 'digit_in_word:', repr(stem))
            count += 1
        if re.search(r'M[a-zA-Z\-]+H', stem):
            print(yr, cat, so, 'OCR_quote_MH:', repr(stem))
            count += 1
        if "”" in stem and "“" not in stem and '"' not in stem:
            print(yr, cat, so, 'unmatched_right_curly_quote:', repr(stem))
            count += 1
        if "“" in stem and "”" not in stem and '"' not in stem:
            print(yr, cat, so, 'unmatched_left_curly_quote:', repr(stem))
            count += 1

print("Found total defects:", count)
