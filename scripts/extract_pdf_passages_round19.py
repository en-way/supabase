# -*- coding: utf-8 -*-
"""
extract_pdf_passages_round19.py
Extract authentic passage text directly from Huang Pi Shu PDFs for the 6 anomalies.
"""

import os
import sys
import glob
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"

def search_text_in_pdfs(keyword, target_year=None, max_results=3):
    print(f"\n================ Searching for: '{keyword}' (Year: {target_year}) ================")
    matches = []
    for root, dirs, files in os.walk(pdf_dir):
        for f in files:
            if not f.lower().endswith('.pdf'):
                continue
            if target_year and str(target_year) not in f:
                continue
            pdf_path = os.path.join(root, f)
            try:
                reader = PdfReader(pdf_path)
                for page_idx, page in enumerate(reader.pages):
                    text = page.extract_text() or ''
                    if keyword.lower() in text.lower():
                        matches.append((f, page_idx + 1, text))
                        if len(matches) >= max_results:
                            break
            except Exception as e:
                pass
            if len(matches) >= max_results:
                break
        if len(matches) >= max_results:
            break

    for f, pnum, text in matches:
        print(f"--- Found in {f} (Page {pnum}) ---")
        # print snippet around keyword
        idx = text.lower().find(keyword.lower())
        start = max(0, idx - 150)
        end = min(len(text), idx + 350)
        print(text[start:end])
        print("--------------------------------------------------")

# 1. 2019 Text 1: "Grade inflation"
search_text_in_pdfs("Grade inflation", 2019)

# 2. 2019 Text 4: "Small Business & Entrepreneurship"
search_text_in_pdfs("Small Business & Entrepreneurship", 2019)

# 3. 2022 ky2 Text 3: "dark patterns"
search_text_in_pdfs("dark patterns", 2022)

# 4. 2021 ky2 Cloze: "critical factors such as time"
search_text_in_pdfs("critical factors such as time", 2021)

# 5. 2008 ky1 Text 3: "feel fairly confident"
search_text_in_pdfs("feel fairly confident", 2008)

# 6. 2010 ky2 Part B: "assemble over Utah"
search_text_in_pdfs("assemble over Utah", 2010)
