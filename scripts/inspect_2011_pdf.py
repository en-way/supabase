# -*- coding: utf-8 -*-
import os, sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

fpath = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2011黄皮书真题解析（英语一）.pdf"
reader = pypdf.PdfReader(fpath)
print(f"Total pages: {len(reader.pages)}")

# Search for Text 1 and Text 3 questions
for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ''
    if 'Gilbert' in txt and ('21.' in txt or '22.' in txt or '23.' in txt):
        print(f"=== Page {idx+1} (Text 1) ===")
        print(txt[:1500])
        print("=" * 40)
    if ('earned media' in txt or 'sold media' in txt or 'Toyota' in txt) and ('32.' in txt or '33.' in txt or '35.' in txt):
        print(f"=== Page {idx+1} (Text 3) ===")
        print(txt[:1500])
        print("=" * 40)
