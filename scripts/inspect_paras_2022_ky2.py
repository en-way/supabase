# -*- coding: utf-8 -*-
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

for sec in ["cloze", "text1", "text2", "text3", "text4", "partb"]:
    with open(f"scripts/2022_ky2_{sec}_lines.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"\n==================== {sec.upper()} ====================")
    for l in lines:
        l = l.strip()
        if re.search(r"(?:^P\d+\s+B\d+:\s*)?[I|V|X]+(?:\s+[❶①]|\b)", l) or "words" in l or "wordsj" in l:
            print("  PARAGRAPH:", l[:90])
