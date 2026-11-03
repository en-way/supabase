# -*- coding: utf-8 -*-
import sys
import pymupdf
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2022年真题解析及复习思路.pdf"
doc = pymupdf.open(pdf_path)

def get_text_in_range(start_page, end_page):
    blocks_collected = []
    for p_no in range(start_page, end_page + 1):
        page = doc[p_no - 1]
        blocks = page.get_text("blocks")
        for b in blocks:
            x0, y0, x1, y1, text, b_no, b_type = b
            t = text.strip()
            # Left column English passage
            if x0 < 90 and x1 < 290:
                # filter out footnote vocabulary definitions
                lines = [l.strip() for l in t.split("\n") if l.strip()]
                # if primarily english and not commentary
                for l in lines:
                    if any(c in l for c in ["词汇注释", "难句分析", "语篇分析", "真题精解", "错项排除", "经典搭配", "考点提炼", "小标题分析", "备选段落分析"]):
                        continue
                    if re.match(r"^[①-⑩\d]\s*[a-zA-Z\s\-\'\:]+\[", l) or re.match(r"^[①-⑩\d][a-zA-Z\s\-\'\:]+\[", l):
                        continue
                    eng_chars = len(re.findall(r"[a-zA-Z]", l))
                    if eng_chars > len(l) * 0.4 or any(c in l for c in ["❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾", "❿", "①", "②", "③"]):
                        blocks_collected.append((p_no, b_no, l))
    return blocks_collected

for sec, start, end in [
    ("cloze", 1, 7),
    ("text1", 8, 18),
    ("text2", 19, 27),
    ("text3", 28, 36),
    ("text4", 37, 45),
    ("partb", 46, 54)
]:
    lines = get_text_in_range(start, end)
    with open(f"scripts/gold_2022_ky2_{sec}.txt", "w", encoding="utf-8") as f:
        for p_no, b_no, l in lines:
            f.write(f"{l}\n")
    print(f"{sec}: {len(lines)} lines extracted.")
