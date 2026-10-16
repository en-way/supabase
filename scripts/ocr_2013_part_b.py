import fitz, sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}", flush=True)

for pno in [51, 52, 53, 54]:
    page = doc[pno]
    pix = page.get_pixmap(dpi=120)
    res, _ = ocr(pix.tobytes("png"))
    lines = [r[1] for r in (res or [])]
    print(f"\n=== Page {pno+1} ({len(lines)} lines) ===", flush=True)
    for l in lines:
        if any(w in l for w in ["41", "42", "43", "44", "45", "Skint", "Foodie", "Tony", "Directions", "[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]"]):
            print("  ", l, flush=True)
