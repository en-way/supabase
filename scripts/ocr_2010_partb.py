# -*- coding: utf-8 -*-
import pymupdf
import glob
from rapidocr_onnxruntime import RapidOCR
import sys

sys.stdout.reconfigure(encoding='utf-8')

ocr = RapidOCR()
f = glob.glob(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\*2010*.pdf")[0]
doc = pymupdf.open(f)

print(f"Scanning {f} (total {len(doc)} pages)...")

for pnum in range(25, 55):
    page = doc[pnum]
    pix = page.get_pixmap(dpi=150)
    img_bytes = pix.tobytes("png")
    result, elapse = ocr(img_bytes)
    if not result:
        continue
    full_text = " ".join([r[1] for r in result])
    if any(k in full_text for k in ["Part B", "Boeing", "Airbus", "Stanford", "Kroo", "41", "birds"]):
        print(f"\n=== Page {pnum+1} ===")
        for r in result:
            txt = r[1]
            if any(k in txt.lower() for k in ["part b", "boeing", "airbus", "stanford", "kroo", "formation", "birds", "drag", "fuel", "41.", "42.", "43.", "44.", "45."]):
                print("  ", txt)
        # If this is the passage page, print all text
        if "Stanford" in full_text and "birds" in full_text:
            print("--- FULL PAGE TEXT ---")
            for r in result:
                print(r[1])
            break
