import pymupdf
import pathlib

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

for pdf_path in root.rglob("*.pdf"):
    if "2021" in pdf_path.name and ("英语（一）" in pdf_path.name or "英语一" in pdf_path.name):
        doc = pymupdf.open(pdf_path)
        with open("scripts/2021_q39_extracted.txt", "w", encoding="utf-8") as out:
            for i in range(35, 45): # pages around 40
                if i < len(doc):
                    out.write(f"\n--- PAGE {i+1} ---\n")
                    out.write(doc[i].get_text())
        print("Wrote pages 36-45 to scripts/2021_q39_extracted.txt")
        break
