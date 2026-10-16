import pymupdf
import pathlib
import re

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

years = {
    '2006': [26, 29, 34, 35],
    '2007': [23, 26, 27, 28, 29, 32, 37, 38, 40],
    '2008': [28, 29, 34, 40],
    '2009': [1, 3, 5, 9, 10, 17, 35]
}

# Find all PDFs for 2006, 2007, 2008, 2009
pdf_map = {}
for p in root.rglob("*.pdf"):
    for y in years.keys():
        if y in p.name and ("英语（一）" in p.name or "英语一" in p.name or "2001-2009" in p.name):
            pdf_map.setdefault(y, []).append(p)

print("Found PDFs:")
for y, flist in pdf_map.items():
    print(f"Year {y}: {[f.name for f in flist]}")

# Write extracted text for each year to scripts/extracted_{year}.txt
for y, q_nums in years.items():
    flist = pdf_map.get(y, [])
    if not flist:
        continue
    # Prefer year specific file
    target_pdf = flist[0]
    for f in flist:
        if f"{y}年" in f.name:
            target_pdf = f
            break
    print(f"Extracting {y} from {target_pdf.name}...")
    doc = pymupdf.open(target_pdf)
    out_file = f"scripts/extracted_{y}.txt"
    with open(out_file, "w", encoding="utf-8") as out:
        for page_idx, page in enumerate(doc):
            text = page.get_text()
            # check if any target question number is on this page
            for q_num in q_nums:
                if f"{q_num}." in text or f"{q_num}．" in text:
                    out.write(f"\n=== PAGE {page_idx+1} (matches Q{q_num}) ===\n")
                    out.write(text)
                    break
    print(f"Wrote {out_file}")
