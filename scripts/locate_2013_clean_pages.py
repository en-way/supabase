# -*- coding: utf-8 -*-
import pypdf
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def find_year_pages(pdf_path, year_str):
    reader = pypdf.PdfReader(pdf_path)
    print(f"Scanning {pdf_path} (total {len(reader.pages)} pages)...")
    found_pages = []
    for idx, page in enumerate(reader.pages):
        txt = page.extract_text() or ""
        if year_str in txt:
            found_pages.append((idx, txt[:80].replace('\n', ' ')))
    return found_pages

base = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）'
cloze_pdf = f"{base}\\2010-2025完型真题\\【完型真题】-英语一（2010-2024年）.pdf"
reading_pdf = f"{base}\\2001-2025阅读真题\\【大间距】-英语一（2010-2024）.pdf"
newtype_pdf = f"{base}\\2010-2025新题型真题\\【新题型】-英语一（2005-2024年）.pdf"

for name, p in [('Cloze', cloze_pdf), ('Reading', reading_pdf), ('NewType', newtype_pdf)]:
    hits = find_year_pages(p, '2013')
    print(f"=== {name} hits for '2013': {len(hits)} ===")
    for idx, snippet in hits[:5]:
        print(f"  Page {idx}: {snippet}")
