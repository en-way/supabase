import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
root = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"

for item in os.listdir(root):
    full = os.path.join(root, item)
    if os.path.isdir(full):
        files = os.listdir(full)
        pdf_count = len([x for x in files if x.endswith('.pdf')])
        print(f"[DIR] {item} ({len(files)} files, {pdf_count} PDFs)")
    else:
        print(f"[FILE] {item} ({os.path.getsize(full)} bytes)")
