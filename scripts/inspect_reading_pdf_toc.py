import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题\阅读真题（2001-2009年）.pdf"
doc = pymupdf.open(pdf_path)

print(f"Total pages: {len(doc)}")
toc = doc.get_toc()
print(f"TOC entries: {len(toc)}")
for item in toc:
    print(item)

if not toc:
    print("No TOC. Checking page headers...")
