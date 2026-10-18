import os
import glob
import sys
import pypdf

sys.stdout.reconfigure(encoding='utf-8')
folder = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
files = glob.glob(os.path.join(folder, "*2003*.pdf"))
print("Files:", files)
if files:
    reader = pypdf.PdfReader(files[0])
    print("Num pages:", len(reader.pages))
    for idx, page in enumerate(reader.pages):
        txt = page.extract_text() or ""
        if "25." in txt and ("Straitford" in txt or "Stratfor" in txt or "proud of" in txt):
            print(f"Found on page {idx+1}")
            print(txt[:1000])
            print("="*40)
