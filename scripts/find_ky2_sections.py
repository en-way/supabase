# -*- coding: utf-8 -*-
import fitz
from rapidocr_onnxruntime import RapidOCR

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Scanning 64 pages with low DPI (70) to find all section boundaries...")
sections = []

# Scan with low dpi for speed
for p in range(len(doc)):
    pix = doc[p].get_pixmap(dpi=72)
    res, _ = ocr(pix.tobytes('png'))
    if not res: continue
    text = '\n'.join([r[1] for r in res])
    
    # Check for section markers
    matches = []
    for line in text.splitlines():
        line_clean = line.strip()
        for kw in ["第一部分", "第二部分", "Part A", "Part B", "Text 1", "Text 2", "Text 3", "Text 4", "Section I", "Section II"]:
            if kw in line_clean and len(line_clean) < 40:
                matches.append(line_clean)
    if matches:
        print(f"Page {p+1}: {', '.join(matches[:3])}", flush=True)
        sections.append((p+1, matches))

with open("scripts/ky2_found_sections.txt", "w", encoding="utf-8") as out:
    for p_no, m in sections:
        out.write(f"Page {p_no}: {', '.join(m)}\n")

print("Section boundary scan complete.")
