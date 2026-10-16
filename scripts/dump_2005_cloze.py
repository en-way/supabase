# -*- coding: utf-8 -*-
import os, sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"
fpath = None
for root, dirs, files in os.walk(base):
    for f in files:
        if '2005' in f and f.endswith('.pdf') and '英语二' not in root and '题型' not in f:
            fpath = os.path.join(root, f)
            print(f"Matched: {fpath}")
            break
    if fpath: break

print(f"Found target PDF: {fpath}")
reader = pypdf.PdfReader(fpath)
out = []
for p in range(0, 8):
    out.append(f"=== PAGE {p+1} ===")
    out.append(reader.pages[p].extract_text() or '')

with open('scripts/2005_cloze_raw.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print(f"Dumped 8 pages of 2005 Cloze to scripts/2005_cloze_raw.txt")
