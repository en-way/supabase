import fitz
import sys
import re
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf'
doc = fitz.open(pdf_path)

print("Extracting 2004 Cloze pages 3 to 11 via RapidOCR...")
all_lines = []

for pno in range(2, 11):
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes('png'))
    lines = [r[1] for r in (res or [])]
    print(f"Page {pno+1}: {len(lines)} lines")
    all_lines.extend(lines)

with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\2004_cloze_raw_ocr.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(all_lines))

print("Raw OCR written to scripts/2004_cloze_raw_ocr.txt")
