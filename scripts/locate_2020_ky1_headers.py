import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf"
doc = pymupdf.open(pdf_path)

for i, page in enumerate(doc):
    text = page.get_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for idx, l in enumerate(lines[:10]):
        if any(h in l for h in ["Text 1", "Text 2", "Text 3", "Text 4", "Part B", "Section I", "Section II"]):
            print(f"Page {i+1}: {l} -> {lines[idx+1] if idx+1 < len(lines) else ''}")
