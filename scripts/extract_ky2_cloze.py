import fitz
from rapidocr_onnxruntime import RapidOCR

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

with open("scripts/ky2_cloze_raw.txt", "w", encoding="utf-8") as out:
    for p in [1, 2, 3]:
        out.write(f"\n--- Page {p} ---\n")
        pix = doc[p-1].get_pixmap(dpi=130)
        res, _ = ocr(pix.tobytes('png'))
        if res:
            text = '\n'.join([r[1] for r in res])
            out.write(text + "\n")

print("Extracted pages 1-3.")
