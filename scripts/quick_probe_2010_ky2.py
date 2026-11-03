import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
import cv2
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2010年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)
engine = RapidOCR()

for p in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]:
    pix = doc[p].get_pixmap(dpi=80)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Crop top 20%
    h = img.shape[0]
    res, _ = engine(img[:int(h * 0.25), :])
    first_few = " | ".join([r[1] for r in res[:3]]) if res else "empty"
    print(f"P{p}: {first_few}", flush=True)
