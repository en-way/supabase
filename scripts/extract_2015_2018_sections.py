import pymupdf
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

p2015 = list(root.rglob("*2015黄皮书真题解析（英语一）*.pdf"))[0]
doc2015 = pymupdf.open(p2015)
with open("scripts/full_2015_reading_text.txt", "w", encoding="utf-8") as out:
    for i in range(25, 48):
        if i < len(doc2015):
            out.write(f"\n=== PAGE {i+1} ===\n")
            out.write(doc2015[i].get_text())
print("Saved 2015 reading text to scripts/full_2015_reading_text.txt")

p2018 = list(root.rglob("*2018黄皮书真题解析（英语一）*.pdf"))[0]
doc2018 = pymupdf.open(p2018)
with open("scripts/full_2018_reading_text.txt", "w", encoding="utf-8") as out:
    for i in range(25, 46):
        if i < len(doc2018):
            out.write(f"\n=== PAGE {i+1} ===\n")
            out.write(doc2018[i].get_text())
print("Saved 2018 reading text to scripts/full_2018_reading_text.txt")
