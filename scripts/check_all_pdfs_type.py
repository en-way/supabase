import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def check_folder(base, name):
    print(f"\n=================== Checking {name} ===================")
    for f in sorted(os.listdir(base)):
        if f.endswith(".pdf"):
            path = os.path.join(base, f)
            doc = pymupdf.open(path)
            total_pages = len(doc)
            # count text chars across all pages
            total_chars = sum(len(page.get_text()) for page in doc)
            sample_page_images = len(doc[0].get_images()) if total_pages > 0 else 0
            is_scanned = (total_chars < 1000)
            status = "SCANNED (IMAGE)" if is_scanned else f"TEXT ({total_chars} chars)"
            print(f"[{status}] {f} ({total_pages} pages, {total_chars} chars)")

check_folder(pdf_base_ky1, "英语一")
check_folder(pdf_base_ky2, "英语二")
