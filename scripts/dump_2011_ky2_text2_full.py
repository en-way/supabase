import pymupdf
from rapidocr_onnxruntime import RapidOCR

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2011年真题解析及复习思路.pdf"
doc = pymupdf.open(pdf_path)
ocr = RapidOCR()

for pno in [23, 24, 25]:
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=200)
    img_bytes = pix.tobytes("png")
    result, _ = ocr(img_bytes)
    print(f"\n==================== PAGE {pno} ====================")
    if result:
        for line in result:
            print(line[1])
