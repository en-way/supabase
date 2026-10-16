import glob
import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky2 = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语二真题解析（2001-2025）'
exams_dir = 'public/data/exams'

exam_files_ky2 = {}
for f in glob.glob(f'{exams_dir}/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data.get('exam', {})
    if exam.get('category_id') == 'ky2':
        exam_files_ky2[exam.get('year')] = f

print(f"Found {len(exam_files_ky2)} ky2 exam files.")

short_ky2_qs = []
for y in sorted(exam_files_ky2.keys()):
    fpath = exam_files_ky2[y]
    with open(fpath, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    for q in data.get('questions', []):
        q_num = q.get('sort_order')
        if 1 <= q_num <= 20:
            expl = q.get('explanation') or ''
            if len(expl) < 70 or '错项排除' not in expl:
                short_ky2_qs.append((y, q_num, len(expl), expl.strip()[:60]))

print(f"Total ky2 cloze questions with short/incomplete explanation: {len(short_ky2_qs)}")
for item in short_ky2_qs[:15]:
    print(item)
