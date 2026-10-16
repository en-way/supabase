# -*- coding: utf-8 -*-
import os, sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2014黄皮书真题解析（英语一）.pdf"
reader = pypdf.PdfReader(fpath)

for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ''
    if any(q in txt for q in ['31.', '32.', '33.', '39.', '40.']) and ('Fundamental Physics' in txt or 'Higgs boson' in txt or 'AAAS' in txt or 'humanities' in txt or 'professors' in txt):
        print(f"=== Page {idx+1} ===")
        print(txt[:1500])
        print("=" * 40)
