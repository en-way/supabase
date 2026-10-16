import glob
import fitz
import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky2 = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语二真题解析（2001-2025）'
exams_dir = 'public/data/exams'

def extract_ky2_year(year):
    matches = glob.glob(f'{pdf_dir_ky2}/*{year}*.pdf')
    if not matches:
        return {}
    doc = fitz.open(matches[0])
    pages = []
    for p in range(min(10, len(doc))):
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
    
    kd_pattern = re.compile(r'(?:\[|［|【|1：)(?:试题考点|考点提炼|考点精解|考点)(?:\]|］|】)')
    matches = list(kd_pattern.finditer(full_text))
    
    extracted = {}
    for i, m in enumerate(matches):
        q_num = i + 1
        if q_num > 20:
            break
        kd_start = m.start()
        
        # Look backwards for options start or number
        pre_chunk = full_text[max(0, kd_start - 500):kd_start]
        opt_a = pre_chunk.rfind('[A]')
        if opt_a == -1:
            opt_a = pre_chunk.rfind('［A］')
        if opt_a == -1:
            opt_a = pre_chunk.rfind('[ A]')
            
        if opt_a != -1:
            q_start = max(0, kd_start - 500) + opt_a
            num_lead = full_text[max(0, q_start - 50):q_start]
            num_m = re.search(r'(?:^|\n)\s*(?:&|\d{1,2})[\.、\s]', num_lead)
            if num_m:
                q_start = max(0, q_start - 50) + num_m.start()
        else:
            q_start = max(0, kd_start - 300)
            
        # Find end
        if i + 1 < len(matches):
            next_kd_start = matches[i + 1].start()
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
            
        block = full_text[q_start:q_end].strip()
        lines = [l for l in block.split('\n') if not re.match(r'^(?:=== PAGE \d+ ===|\d{1,3}|公众号.*|微信.*)$', l.strip())]
        cleaned = '\n'.join(lines).strip()
        extracted[q_num] = cleaned
        
    return extracted

# Apply to 2021 and 2022
applied = 0
for year in [2021, 2022]:
    year_cloze = extract_ky2_year(year)
    print(f"Extracted {len(year_cloze)} questions for ky2 {year}")
    
    target_file = None
    for f in glob.glob(f'{exams_dir}/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        exam = d.get('exam', {})
        if exam.get('category_id') == 'ky2' and exam.get('year') == year:
            target_file = f
            break
            
    if not target_file:
        print(f"File for ky2 {year} not found!")
        continue
        
    with open(target_file, 'r', encoding='utf-8') as fp:
        exam_data = json.load(fp)
        
    modified = False
    for q in exam_data.get('questions', []):
        so = q.get('sort_order')
        if 1 <= so <= 20 and so in year_cloze:
            new_exp = year_cloze[so]
            old_exp = q.get('explanation', '')
            # If current is defective/short or has passage bleed
            if len(old_exp) < 120 or 'that most bestselling' in old_exp or len(new_exp) > len(old_exp) + 50:
                q['explanation'] = new_exp
                modified = True
                applied += 1
                print(f"[{year} ky2 Q{so}] Updated: {len(old_exp)} -> {len(new_exp)} chars")
                
    if modified:
        with open(target_file, 'w', encoding='utf-8') as fp:
            json.dump(exam_data, fp, ensure_ascii=False, indent=2)
        print(f"Saved {target_file}")

print(f"Total ky2 2021-2022 cloze questions upgraded: {applied}")
