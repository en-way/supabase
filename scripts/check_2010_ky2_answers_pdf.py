import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
import cv2
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2010年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)
engine = RapidOCR()

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

# Check Page 0 or 1 for answer keys or Cloze answers
print("=== Cloze Q14-Q20 Pages 10-12 ===")
for p in range(10, 13):
    txt = ocr_page(p)
    for q in range(14, 21):
        m = re.findall(rf'{q}\s*[\.．\、\-]\s*(?:本题考查|［[A-D]］|\[[A-D]\]|[A-D])', txt)
        if m:
            print(f"P{p} Q{q}: {m}")
    # Also print lines matching [A-D]
    ans_lines = [l for l in txt.splitlines() if re.search(r'^\s*\d{1,2}\s*[\.．\、\-]\s*[\[［]?[A-D][\]］]?', l)]
    if ans_lines:
        print(f"P{p} ans_lines: {ans_lines}")
