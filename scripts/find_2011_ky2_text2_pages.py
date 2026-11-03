import pymupdf
import os
from rapidocr_onnxruntime import RapidOCR

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2011年真题解析及复习思路.pdf"
doc = pymupdf.open(pdf_path)
ocr = RapidOCR()

print(f"Total pages in 2011 ky2 PDF: {len(doc)}")

for page_idx in range(len(doc)):
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes("png")
    result, _ = ocr(img_bytes)
    
    if result:
        text = " ".join([line[1] for line in result])
        if "Text 2" in text or "Newspapers" in text or "whatever happened" in text.lower():
            print(f"=== Page {page_idx+1} contains Text 2 keywords ===")
            for line in result:
                if any(k in line[1].lower() for k in ["text 2", "newspapers", "whatever happened", "francisco", "doom", "26."]):
                    print(f"   {line[1]}")
