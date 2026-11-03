import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf"
doc = pymupdf.open(pdf_path)

print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    text = page.get_text()
    for kw in ["Use of English", "Text 1", "Text 2", "Text 3", "Text 4", "Part B", "Section III"]:
        if kw in text:
            first_few = [l.strip() for l in text.splitlines() if l.strip()][:3]
            print(f"Page {i+1}: [{kw}] -> {' | '.join(first_few)}")
            break
