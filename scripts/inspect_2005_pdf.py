# -*- coding: utf-8 -*-
import os, sys, pypdf
sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"
for root, dirs, files in os.walk(base):
    for f in files:
        if '2005' in f and f.endswith('.pdf'):
            fpath = os.path.join(root, f)
            print(f"Checking: {fpath}")
            reader = pypdf.PdfReader(fpath)
            for idx, p in enumerate(reader.pages[:10]):
                txt = p.extract_text() or ''
                if 'Section I' in txt or 'Use of English' in txt or 'The nose is' in txt:
                    print(f"  Page {idx+1} has Cloze!")
                    print(txt[:1000])
                    print("-" * 50)
