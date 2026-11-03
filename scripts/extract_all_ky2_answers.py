# -*- coding: utf-8 -*-
import fitz
import re
from rapidocr_onnxruntime import RapidOCR

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print("Scanning for question answers from pages 1 to 54...")

detected_answers = {}

# Pages 1 to 54
for p in range(0, 54):
    pix = doc[p].get_pixmap(dpi=100)
    res, _ = ocr(pix.tobytes('png'))
    if not res: continue
    text = '\n'.join([r[1] for r in res])
    
    # Check for question answers
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Match pattern: e.g. "【答案B】" or "【答案】B" or "【答案 C】" or "【答案为D】"
        m = re.search(r'【答案\s*(?:为\s*)?([A-G])】', line)
        if m:
            ans = m.group(1)
            # Find closest question number before this line
            q_num = None
            for j in range(max(0, i-10), i+1):
                qm = re.search(r'(?:^|[^0-9])([1-9]|[1-4][0-9])\s*[\.、]\s*(?:本题考查|According|What|Which|The |By |In |It |Match |When )', lines[j])
                if qm:
                    q_num = int(qm.group(1))
            print(f"Page {p+1}: line '{line.strip()}' -> Q{q_num}: {ans}", flush=True)
            if q_num and q_num not in detected_answers:
                detected_answers[q_num] = (ans, p+1)

with open("scripts/ky2_detected_answers.txt", "w", encoding="utf-8") as out:
    for q in sorted(detected_answers.keys()):
        ans, page = detected_answers[q]
        out.write(f"Q{q}: {ans} (Page {page})\n")

print(f"Total detected answers: {len(detected_answers)}")
