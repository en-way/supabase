import glob
import fitz
import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky1 = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'

def get_pdf_path(year):
    matches = glob.glob(f'{pdf_dir_ky1}/*{year}*.pdf')
    if matches:
        return matches[0]
    return None

def extract_cloze_for_year(year):
    pdf_path = get_pdf_path(year)
    if not pdf_path:
        print(f"[{year}] PDF not found!")
        return {}
    
    doc = fitz.open(pdf_path)
    # Collect text up to 10-12 pages, stop at Reading Comprehension / Text 1
    pages_text = []
    for p_idx in range(min(12, len(doc))):
        t = doc[p_idx].get_text()
        if p_idx > 2 and ('Text 1' in t or 'Section II Reading' in t or '语篇分析及试题精解' in t):
            # Cut at Text 1
            if 'Text 1' in t:
                t = t.split('Text 1')[0]
            elif 'Section II Reading' in t:
                t = t.split('Section II Reading')[0]
            pages_text.append(f'\n=== PAGE {p_idx+1} ===\n' + t)
            break
        pages_text.append(f'\n=== PAGE {p_idx+1} ===\n' + t)
        
    full_text = '\n'.join(pages_text)
    
    # We find each question 1..20
    # A question must have:
    # 1. Question header: number (or OCR alias like '&' for 8)
    # 2. Options: [A]... [B]... [C]... [D]...
    # 3. [试题考点] or [考点提炼] or [考点分析]
    # 4. [解题思路]
    # 5. [错项排除]
    
    results = {}
    
    # We search for the positions of [试题考点] or [考点提炼]
    kd_pattern = re.compile(r'(?:\[|［|【|1：)(?:试题考点|考点提炼|考点精解|考点)(?:\]|］|】)')
    kd_matches = list(kd_pattern.finditer(full_text))
    
    # For each 考点, look backwards for the question number and options
    for idx, km in enumerate(kd_matches):
        kd_start = km.start()
        # Look backwards up to 600 chars for question number
        pre_text = full_text[max(0, kd_start - 600):kd_start]
        
        # Look for question number pattern
        # e.g., "1.", "1 ", "10.", "& ", "8.", "8 "
        # Also check if it's the i-th question
        q_num = None
        # Try finding standard numbers in reverse
        num_matches = list(re.finditer(r'(?:^|\n)\s*(?:&|(?P<num>\d{1,2}))\s*[\.、\s]?(?:\s*\[A\]|\s*\[\s*A\s*\])?', pre_text))
        if num_matches:
            last_m = num_matches[-1]
            if last_m.group('num'):
                val = int(last_m.group('num'))
                if 1 <= val <= 20:
                    q_num = val
            elif '&' in last_m.group(0):
                q_num = 8
                
        # If not matched by regex, infer from index if reasonable
        if q_num is None:
            if 1 <= (idx + 1) <= 20:
                q_num = idx + 1
                
        # Now find where this question starts
        q_start = max(0, kd_start - 400)
        if num_matches:
            q_start = max(0, kd_start - 600) + num_matches[-1].start()
            
        # Find where this question ends (start of next question, or next 考点 backwards, or end of cloze)
        if idx + 1 < len(kd_matches):
            next_kd_start = kd_matches[idx + 1].start()
            # Look backwards from next_kd_start for next question number
            next_pre = full_text[max(0, next_kd_start - 600):next_kd_start]
            next_num_matches = list(re.finditer(r'(?:^|\n)\s*(?:&|\d{1,2})\s*[\.、\s]?(?:\s*\[A\]|\s*\[\s*A\s*\])?', next_pre))
            if next_num_matches:
                q_end = max(0, next_kd_start - 600) + next_num_matches[-1].start()
            else:
                q_end = next_kd_start - 50
        else:
            # Last question
            q_end = min(len(full_text), kd_start + 1800)
            
        block = full_text[q_start:q_end].strip()
        
        # Clean block: remove page markers, isolated line numbers, and long translation chunks if present
        clean_lines = []
        for l in block.split('\n'):
            l_str = l.strip()
            # skip page header/footer
            if re.match(r'^(?:=== PAGE \d+ ===|\d{1,3}|公众号.*|微信.*)$', l_str):
                continue
            # skip if long translation header accidentally slipped in
            if '词汇注释与难句分析' in l_str or '结构切分：' in l_str or '功能注释：' in l_str:
                break
            clean_lines.append(l)
            
        clean_text = '\n'.join(clean_lines).strip()
        if q_num and 1 <= q_num <= 20:
            # If already exists, keep longer one
            if q_num not in results or len(clean_text) > len(results[q_num]):
                results[q_num] = clean_text

    print(f"[{year}] Extracted {len(results)}/20 questions (found {len(kd_matches)} 考点 markers)")
    missing = [i for i in range(1, 21) if i not in results]
    if missing:
        print(f"  Missing Qs: {missing}")
    return results

all_cloze_data = {}
for y in range(2001, 2016):
    all_cloze_data[y] = extract_cloze_for_year(y)

out_file = 'scripts/calibrated_cloze_2001_2015.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(all_cloze_data, f, ensure_ascii=False, indent=2)

print(f"\nSaved all extracted data to {out_file}")
