# -*- coding: utf-8 -*-
import pymupdf
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf")

with open(r"d:\A16pro\Aing\antigravity\supabase\scripts\2020_ky1_dump.txt", "w", encoding="utf-8") as out:
    for i, page in enumerate(doc[:48]):
        out.write(f"--- PAGE {i+1} ---\n")
        out.write(page.get_text())
        out.write("\n\n")

print("Dumped pages 1-48 to scripts/2020_ky1_dump.txt")
