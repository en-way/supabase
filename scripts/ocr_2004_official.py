import fitz
from rapidocr_onnxruntime import RapidOCR
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()
doc = fitz.open(r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题\阅读真题（2001-2009年）.pdf')

pages_data = {}
for p_no in range(47, 63):
    page = doc[p_no]
    pix = page.get_pixmap(dpi=200)
    img_data = pix.tobytes('png')
    res, _ = ocr(img_data)
    lines = [item[1] for item in res] if res else []
    pages_data[p_no] = lines
    print(f"Page {p_no}: {len(lines)} lines")

with open("scratch_2004_ocr_raw.json", "w", encoding="utf-8") as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print("Saved scratch_2004_ocr_raw.json successfully!")
