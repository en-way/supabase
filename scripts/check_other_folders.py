import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"

for folder in ["2001-2025阅读真题", "2010-2025完型真题", "2010-2025新题型真题", "2010-2025翻译真题"]:
    full_folder = os.path.join(root, folder)
    print(f"\n=================== Checking {folder} ===================")
    for f in sorted(os.listdir(full_folder)):
        if f.endswith(".pdf"):
            path = os.path.join(full_folder, f)
            doc = pymupdf.open(path)
            total_pages = len(doc)
            total_chars = sum(len(p.get_text()) for p in doc)
            status = "SCANNED (IMAGE)" if total_chars < 1000 else f"TEXT ({total_chars} chars)"
            print(f"[{status}] {f} ({total_pages} pages, {total_chars} chars)")
