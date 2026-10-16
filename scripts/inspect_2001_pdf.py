# -*- coding: utf-8 -*-
import os, sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

fpath = None
base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
for f in os.listdir(base):
    if '2001' in f:
        fpath = os.path.join(base, f)
        break

print(f"Matched: {fpath}")
reader = pypdf.PdfReader(fpath)

for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ''
    if any(q in txt for q in ['32.', '37.', '38.', '39.', '40.']) and ('newspaper' in txt or 'downshifting' in txt or 'lifestyle' in txt):
        print(f"=== Page {idx+1} ===")
        print(txt[:1500])
        print("=" * 40)
