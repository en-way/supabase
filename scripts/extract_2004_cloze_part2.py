import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf'
doc = fitz.open(pdf_path)

print("Extracting 2004 Cloze pages 12 to 15 (indices 11 to 14)...")
lines_part2 = []

for pno in range(11, 15):
    page = doc[pno]
    pix = page.get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes('png'))
    lines = [r[1] for r in (res or [])]
    print(f"Page {pno+1}: {len(lines)} lines")
    lines_part2.extend(lines)

with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\2004_cloze_raw_ocr_part2.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines_part2))

print("Part 2 written to scripts/2004_cloze_raw_ocr_part2.txt")
