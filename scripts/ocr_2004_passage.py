import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

for p in [0, 5, 7, 10]:
    page = doc[p]
    # Pixmap with matrix 0.8
    pix = page.get_pixmap(matrix=fitz.Matrix(0.8, 0.8))
    res, _ = ocr(pix.tobytes("png"))
    lines = [r[1] for r in (res or [])]
    print(f"\n==================== Page {p+1} OCR ({len(lines)} lines) ====================")
    for l in lines:
        if any(w in l.lower() for w in ['theories', 'delinquency', 'children', 'society', 'crimes', 'family', 'parents', 'traditional', 'school', 'peer']):
            print(" ", l)
