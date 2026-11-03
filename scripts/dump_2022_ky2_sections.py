# -*- coding: utf-8 -*-
import sys
import pymupdf
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2022年真题解析及复习思路.pdf"
doc = pymupdf.open(pdf_path)

def extract_section(start_page, end_page, sec_name):
    print(f"\n==================== {sec_name} (Pages {start_page}-{end_page}) ====================")
    lines_found = []
    for p_no in range(start_page, end_page + 1):
        page = doc[p_no - 1]
        blocks = page.get_text("blocks")
        for b in blocks:
            x0, y0, x1, y1, text, b_no, b_type = b
            t = text.strip()
            # English passage is in left column (x1 < 290)
            if x0 < 90 and x1 < 290:
                lines = [l.strip() for l in t.split("\n") if l.strip()]
                for l in lines:
                    if any(c in l for c in ["词汇注释", "难句分析", "语篇分析", "真题精解", "错项排除", "经典搭配", "考点提炼", "小标题分析", "备选段落分析"]):
                        continue
                    if re.match(r"^[①-⑩\d]\s*[a-zA-Z\s\-\'\:]+\[", l) or re.match(r"^[①-⑩\d][a-zA-Z\s\-\'\:]+\[", l):
                        continue
                    eng_chars = len(re.findall(r"[a-zA-Z]", l))
                    if eng_chars > len(l) * 0.4 or any(c in l for c in ["❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾", "❿", "①", "②", "③"]):
                        lines_found.append((p_no, b_no, l))
    return lines_found

for sec, start, end in [
    ("cloze", 1, 7),
    ("text1", 8, 18),
    ("text2", 19, 27),
    ("text3", 28, 36),
    ("text4", 37, 45),
    ("partb", 46, 54)
]:
    res = extract_section(start, end, sec)
    with open(f"scripts/2022_ky2_{sec}_lines.txt", "w", encoding="utf-8") as f:
        for p_no, b_no, l in res:
            f.write(f"P{p_no} B{b_no}: {l}\n")
    print(f"Saved {len(res)} lines for {sec}.")
