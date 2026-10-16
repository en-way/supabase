import fitz
from rapidocr_onnxruntime import RapidOCR
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_files = {
    2023: (r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2023年英语一真题解析及复习思路.pdf", range(30, 48)),
    2024: (r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2024英语一真题解析及复习思路 .pdf", range(28, 44)),
    2025: (r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2025英语一真题解析及复习思路.pdf", range(30, 48)),
}

for yr, (path, p_range) in pdf_files.items():
    doc = fitz.open(path)
    print(f"\n==========================================")
    print(f"YEAR {yr}: scanning pages {min(p_range)+1} to {max(p_range)+1}")
    print(f"==========================================")
    
    for pno in p_range:
        if pno >= len(doc):
            continue
        pix = doc[pno].get_pixmap(dpi=100)
        res, _ = ocr(pix.tobytes("png"))
        txt = "\n".join([line[1] for line in (res or [])])
        # Check if Part B or 41 is in txt
        has_part_b = "Part B" in txt or "新题型" in txt or "七选五" in txt or "排序" in txt or "41." in txt or "41题" in txt or "41】" in txt or "【41" in txt or "【42" in txt
        has_trans = "Part C" in txt or "翻译" in txt or "46." in txt or "46题" in txt
        if has_part_b or any(f"{q}" in txt for q in [41, 42, 43, 44, 45]):
            # Check for answers
            ans_matches = re.findall(r'(?:正确答案|答案)[:：]?\s*\[?([A-G])\]?', txt)
            q_matches = re.findall(r'(?:4[1-5])', txt)
            print(f"Year {yr} Page {pno+1}: Q_nums={set(q_matches)}, Ans={ans_matches}")
            for l in txt.split("\n"):
                if any(k in l for k in ["Part B", "正确答案", "【答案", "41", "42", "43", "44", "45", "排序"]):
                    print("   ", l[:80])
