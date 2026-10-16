import glob
import fitz
import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky2 = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语二真题解析（2001-2025）'

for y in [2021, 2022]:
    matches = glob.glob(f'{pdf_dir_ky2}/*{y}*.pdf')
    if not matches:
        print(f"[{y}] PDF not found!")
        continue
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
    
    # Locate all 考点 markers
    kd_pattern = re.compile(r'(?:\[|［|【|1：)(?:试题考点|考点提炼|考点精解|考点)(?:\]|］|】)')
    matches = list(kd_pattern.finditer(full_text))
    print(f"[{y} ky2] Total text len: {len(full_text)}, 考点 matches: {len(matches)}")
    for i, m in enumerate(matches, 1):
        pre = full_text[max(0, m.start()-100):m.start()]
        print(f"  {i}: {pre.strip().splitlines()[-1] if pre.strip() else ''} -> {full_text[m.start():m.start()+35]}")
