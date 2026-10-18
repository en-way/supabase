import pymupdf
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")
p2015 = list(root.rglob("*2015黄皮书真题解析（英语一）*.pdf"))[0]
doc = pymupdf.open(p2015)

for p_no in range(len(doc)):
    txt = doc[p_no].get_text()
    if '38.' in txt or '34.' in txt or '28.' in txt:
        print(f"Page {p_no+1} matches:")
        for line in txt.splitlines():
            if any(k in line for k in ['38.', '34.', '28.', 'Rebekah Brooks', 'David Vaux', 'exploring']):
                print("  ", line.strip())
