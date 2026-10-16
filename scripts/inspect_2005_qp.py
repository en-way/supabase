# -*- coding: utf-8 -*-
import os, sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"
for root, dirs, files in os.walk(base):
    for f in files:
        if '2005' in f and '真题.pdf' in f and '解析' not in f:
            p = os.path.join(root, f)
            print(f"Reading question paper: {p}")
            reader = pypdf.PdfReader(p)
            for idx in range(min(5, len(reader.pages))):
                txt = reader.pages[idx].extract_text() or ''
                print(f"--- Page {idx+1} ---")
                print(txt[:1500])
