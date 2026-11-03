import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
import cv2
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2010年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)
engine = RapidOCR()

print("=== Scanning question occurrences by page ===")

def ocr_page(p):
    pix = doc[p].get_pixmap(dpi=110)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    res, _ = engine(img)
    lines = [r[1] for r in res] if res else []
    return "\n".join(lines)

# Scan Cloze pages: 6 to 14
print("--- Cloze Pages 6-14 ---")
cloze_map = {}
for p in range(6, 15):
    txt = ocr_page(p)
    found = re.findall(r'(?:^|\n)\s*(\d{1,2})\s*[\.．\、\-]\s*(?:本题考查|考点|【考点|［考点|第一步|第二步|［精准定位］|\[精准定位\])', txt)
    print(f"P{p}: {found}")

# Scan Reading pages: 20 to 54
print("--- Reading Pages 20-54 ---")
for p in [21, 22, 23, 24, 30, 31, 32, 33, 34, 40, 41, 42, 43, 44, 50, 51, 52, 53]:
    txt = ocr_page(p)
    found = re.findall(r'(?:^|\n)\s*(\d{2})\s*[\.．\、\-]\s*(?:本题考查|考点|【考点|［考点|第一步|第二步|［精准定位］|\[精准定位\]|In|According|What|The|Which|After)', txt)
    print(f"P{p}: {found}")

# Scan Part B pages: 56 to 59
print("--- Part B Pages 56-59 ---")
for p in range(56, 60):
    txt = ocr_page(p)
    found = re.findall(r'(?:^|\n)\s*(\d{2})\s*[\.．\、\-]\s*(?:本题考查|考点|【考点|［考点|Findings|The|Formation|It)', txt)
    print(f"P{p}: {found}")
