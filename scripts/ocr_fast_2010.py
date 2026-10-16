# -*- coding: utf-8 -*-
import pymupdf
import glob
import os
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')

f = glob.glob(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\*2010*.pdf")[0]
doc = pymupdf.open(f)
ocr = RapidOCR()

scratch_dir = r"C:\Users\57867\.gemini\antigravity\brain\ad55b338-cd23-471c-97b5-4da0d8132180\scratch"
os.makedirs(scratch_dir, exist_ok=True)

# First find which page has Part B or Copying Birds
print("Finding Part B page...", flush=True)
for pnum in range(30, 45):
    page = doc[pnum]
    pix = page.get_pixmap(dpi=100) # fast preview
    img_bytes = pix.tobytes("png")
    result, _ = ocr(img_bytes)
    if result:
        text = " ".join([r[1] for r in result])
        if "Part B" in text or "Copying Birds" in text or "Boeing" in text:
            print(f"FOUND ON PAGE {pnum+1}!", flush=True)
            # Re-render at 200 dpi for high precision OCR
            pix_hd = page.get_pixmap(dpi=200)
            hd_bytes = pix_hd.tobytes("png")
            hd_res, _ = ocr(hd_bytes)
            print(f"=== FULL OCR OF PAGE {pnum+1} ===", flush=True)
            for r in hd_res:
                print(r[1], flush=True)
            # Also check next page for questions/continuation
            p_next = doc[pnum+1]
            p_next_pix = p_next.get_pixmap(dpi=200)
            p_next_res, _ = ocr(p_next_pix.tobytes("png"))
            print(f"\n=== FULL OCR OF PAGE {pnum+2} ===", flush=True)
            for r in p_next_res:
                print(r[1], flush=True)
            break
        elif any(k in text for k in ["41.", "42.", "43."]):
            print(f"Found questions on page {pnum+1}!", flush=True)
