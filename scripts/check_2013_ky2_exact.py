import fitz, sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)

for pno in [53, 54]:
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes("png"))
    print(f"\n=== 2013 ky2 Page {pno+1} ===")
    for r in (res or []):
        print("  ", r[1])
