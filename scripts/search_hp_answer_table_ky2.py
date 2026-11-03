import fitz
from rapidocr_onnxruntime import RapidOCR
import sys

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()
pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2017年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)

# Let's check pages 54 to 69
for pno in range(54, len(doc) + 1):
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=70)
    img_bytes = pix.tobytes("png")
    res, _ = ocr(img_bytes)
    text = " ".join([r[1] for r in (res or [])])
    if any(k in text for k in ["答案速查", "参考答案", "1~5", "1-5", "21~25", "21-25"]):
        print(f"FOUND ANSWER TABLE ON PAGE {pno}!", flush=True)
        for r in res:
            print("  ", r[1], flush=True)
    else:
        # print first line
        first = res[0][1] if res else "EMPTY"
        print(f"P{pno}: {first[:60]}", flush=True)
