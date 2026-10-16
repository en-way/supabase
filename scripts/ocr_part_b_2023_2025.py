import fitz
from rapidocr_onnxruntime import RapidOCR
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
ocr = RapidOCR()

pdf_files = {
    2023: (r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2023年英语一真题解析及复习思路.pdf", range(33, 40)),
    2024: (r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2024英语一真题解析及复习思路 .pdf", range(30, 40)),
    2025: (r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2025英语一真题解析及复习思路.pdf", range(32, 42)),
}

for yr, (path, p_range) in pdf_files.items():
    print(f"\n==========================================")
    print(f"YEAR {yr}: scanning pages {min(p_range)+1} to {max(p_range)+1}")
    print(f"==========================================")
    sys.stdout.flush()
    doc = fitz.open(path)
    
    for pno in p_range:
        if pno >= len(doc):
            continue
        pix = doc[pno].get_pixmap(dpi=120)
        res, _ = ocr(pix.tobytes("png"))
        lines = [line[1] for line in (res or [])]
        txt = "\n".join(lines)
        
        # Check if Q41-Q45 or answers appear
        answers = []
        for line in lines:
            m = re.findall(r'(?:4[1-5][\.\s、\)\]】]|正确答案|【答案|答案[：:])\s*([A-G])', line)
            if m:
                answers.extend(m)
        print(f"Year {yr} Page {pno+1}: lines={len(lines)}, detected_ans={answers}")
        for line in lines:
            if any(k in line for k in ["41", "42", "43", "44", "45", "正确答案", "【答案", "答案"]):
                print(f"  P{pno+1}: {line}")
        sys.stdout.flush()
