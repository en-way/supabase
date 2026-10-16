import glob
import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'

for y in [2006, 2007, 2008, 2009]:
    fpath = glob.glob(f'{pdf_dir}/*{y}*.pdf')[0]
    doc = fitz.open(fpath)
    pages = [doc[p].get_text() for p in range(min(10, len(doc)))]
    full_text = '\n'.join(pages)
    kd_pattern = re.compile(r'(?:\[|［|【|1：)(?:试题考点|考点提炼|考点精解|考点)(?:\]|］|】)')
    matches = list(kd_pattern.finditer(full_text))
    print(f"=== Year {y} ({len(matches)} matches) ===")
    for i, m in enumerate(matches, 1):
        pre = full_text[max(0, m.start()-120):m.start()]
        last_l = pre.strip().splitlines()[-1] if pre.strip() else ""
        print(f"  {i}: {last_l[:40]} -> {full_text[m.start():m.start()+30]}")
