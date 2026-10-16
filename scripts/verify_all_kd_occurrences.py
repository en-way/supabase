import glob
import fitz
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'

# Let's test on 2011, 2012, 2013, 2015, 2010
for y in [2001, 2002, 2003, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]:
    fpath = glob.glob(f'{pdf_dir}/*{y}*.pdf')[0]
    doc = fitz.open(fpath)
    # Collect text from pages where 试题精解 is located
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
    # Pattern includes [考点提炼], ［考点提炼］, [试题考点], ［试题考点］, 1：考点提炼］
    kd_pattern = re.compile(r'(?:\[|［|【|1：)(?:试题考点|考点提炼|考点精解|考点)(?:\]|］|】)')
    matches = list(kd_pattern.finditer(full_text))
    print(f"Year {y}: found {len(matches)} 考点 occurrences")
