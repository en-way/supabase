# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
p = Path(r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2008年考研英语真题解析.pdf')
doc = fitz.open(str(p))
for i in range(12):
    t = doc[i].get_text()
    if any(k in t for k in ['paradoxical', 'attaining', 'scoring']):
        print(f"=== Page {i+1} ===")
        for l in t.split('\n'):
            if any(k in l for k in ['19.', '20.', 'paradoxical', 'attaining', 'scoring']):
                print(' ', l)
