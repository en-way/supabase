import fitz
from rapidocr_onnxruntime import RapidOCR
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_files = {
    2023: r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2023年英语一真题解析及复习思路.pdf",
    2024: r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2024英语一真题解析及复习思路 .pdf",
    2025: r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2025英语一真题解析及复习思路.pdf",
}

for yr, path in pdf_files.items():
    doc = fitz.open(path)
    print(f"\n==========================================")
    print(f"YEAR {yr}: total pages = {len(doc)}")
    print(f"==========================================")
    
    # Check page 1 and 2 for answer summary
    for pno in [0, 1, 2, 3]:
        pix = doc[pno].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes("png"))
        txt = "\n".join([line[1] for line in (res or [])])
        if any(k in txt for k in ["答案", "速查", "Part B", "41", "42", "43", "44", "45"]):
            print(f"--- Year {yr} Page {pno+1} ---")
            for line in txt.split("\n"):
                if any(k in line for k in ["Part B", "41", "42", "43", "44", "45", "答案", "速查"]):
                    print("  ", line)

