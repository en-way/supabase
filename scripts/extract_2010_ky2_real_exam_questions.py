import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np, cv2
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题\【大间距】-英语二 （2010-2024）.pdf')
engine = RapidOCR()

print("=== Extracting 2010 ky2 Real Exam Questions (P4 to P19) ===")

exam_lines = []
for p in range(4, 20):
    pix = doc[p].get_pixmap(dpi=120)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4: img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    else: img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    res, _ = engine(img)
    lines = [r[1] for r in res] if res else []
    print(f"Page {p} extracted {len(lines)} lines")
    exam_lines.append(f"--- PAGE {p} ---")
    exam_lines.extend(lines)

with open('scripts/extracted_2010_ky2_real_reading.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(exam_lines))

print("Saved raw text to scripts/extracted_2010_ky2_real_reading.txt")
