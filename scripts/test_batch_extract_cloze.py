import glob
import fitz
import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky1 = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'
exams_dir = 'public/data/exams'

# Map year to JSON file
exam_files = {}
for f in glob.glob(f'{exams_dir}/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data.get('exam', {})
    if exam.get('category_id') == 'ky1':
        exam_files[exam.get('year')] = f

print(f"Found {len(exam_files)} ky1 exam files.")

def get_pdf_path(year):
    matches = glob.glob(f'{pdf_dir_ky1}/*{year}*.pdf')
    if matches:
        return matches[0]
    return None

def extract_year_cloze(year):
    pdf_path = get_pdf_path(year)
    if not pdf_path:
        return {}
    doc = fitz.open(pdf_path)
    pages = []
    for p in range(min(12, len(doc))):
        t = doc[p].get_text()
        if p > 1 and ('Section II Reading' in t or 'Text 1' in t):
            if 'Text 1' in t:
                t = t.split('Text 1')[0]
            elif 'Section II Reading' in t:
                t = t.split('Section II Reading')[0]
            pages.append(t)
            break
        pages.append(t)
    full_text = '\n'.join(pages)
    
    # Locate all 考点 markers
    # Pattern: [考点提炼], ［考点提炼］, [试题考点], ［试题考点］, 【考点提炼】, etc.
    kd_pattern = re.compile(r'(?:\[|［|【|1：)(?:试题考点|考点提炼|考点精解|考点)(?:\]|］|】)')
    matches = list(kd_pattern.finditer(full_text))
    
    if len(matches) < 15:
        return {}
        
    extracted = {}
    for i, m in enumerate(matches):
        q_num = i + 1
        if q_num > 20:
            break
            
        kd_start = m.start()
        # Find start of this question: look backwards for question number or options [A]
        pre_chunk = full_text[max(0, kd_start - 500):kd_start]
        # Look for [A] or number
        opt_a_pos = pre_chunk.rfind('[A]')
        if opt_a_pos == -1:
            opt_a_pos = pre_chunk.rfind('［A］')
        if opt_a_pos == -1:
            opt_a_pos = pre_chunk.rfind('[ A]')
            
        if opt_a_pos != -1:
            q_start = max(0, kd_start - 500) + opt_a_pos
            # look slightly before for question number
            num_lead = full_text[max(0, q_start - 50):q_start]
            num_m = re.search(r'(?:^|\n)\s*(?:&|\d{1,2})[\.、\s]', num_lead)
            if num_m:
                q_start = max(0, q_start - 50) + num_m.start()
        else:
            q_start = max(0, kd_start - 300)
            
        # Find end of this question: start of next question
        if i + 1 < len(matches):
            next_kd_start = matches[i + 1].start()
            # look backwards from next_kd_start for its [A]
            next_pre = full_text[max(0, next_kd_start - 500):next_kd_start]
            next_a = next_pre.rfind('[A]')
            if next_a == -1:
                next_a = next_pre.rfind('［A］')
            if next_a == -1:
                next_a = next_pre.rfind('[ A]')
            if next_a != -1:
                q_end = max(0, next_kd_start - 500) + next_a
                num_lead2 = full_text[max(0, q_end - 50):q_end]
                num_m2 = re.search(r'(?:^|\n)\s*(?:&|\d{1,2})[\.、\s]', num_lead2)
                if num_m2:
                    q_end = max(0, q_end - 50) + num_m2.start()
            else:
                q_end = next_kd_start - 30
        else:
            q_end = min(len(full_text), kd_start + 1500)
            
        raw_exp = full_text[q_start:q_end].strip()
        
        # Clean lines: remove page headers/footers, isolated numbers, long translation chunks
        lines = []
        for l in raw_exp.split('\n'):
            l_str = l.strip()
            if re.match(r'^(?:=== PAGE \d+ ===|\d{1,3}|公众号.*|微信.*)$', l_str):
                continue
            if '词汇注释与难句分析' in l_str or '结构切分：' in l_str or '功能注释：' in l_str:
                break
            lines.append(l)
            
        cleaned = '\n'.join(lines).strip()
        extracted[q_num] = cleaned
        
    return extracted

# Test extraction across 2001-2015
summary = {}
for y in range(2001, 2016):
    res = extract_year_cloze(y)
    summary[y] = len(res)
    print(f"Year {y}: extracted {len(res)}/20 questions")

print("Extraction summary:", summary)
