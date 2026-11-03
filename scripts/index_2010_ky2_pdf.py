import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
import cv2
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2010年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)
engine = RapidOCR()

print(f"=== Indexing 2010 ky2 PDF ({len(doc)} pages) ===")

# Sample every page, crop top 25% of the page for speed
page_index = {}
for p in range(len(doc)):
    pix = doc[p].get_pixmap(dpi=100)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Crop top 30%
    h = img.shape[0]
    top_img = img[:int(h * 0.35), :]
    res, _ = engine(top_img)
    lines = [r[1] for r in res] if res else []
    page_index[p] = lines
    
    # Print if interesting
    text_summary = " | ".join(lines[:3])
    print(f"P{p}: {text_summary}")

import json
with open('scripts/2010_ky2_pdf_index.json', 'w', encoding='utf-8') as f:
    json.dump(page_index, f, ensure_ascii=False, indent=2)

print("Saved page index successfully!")
