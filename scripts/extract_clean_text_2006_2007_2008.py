import pymupdf
import pathlib
import json

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

# Find all PDFs under folders with 25 files (the 2001-2025 single-year folders)
target_files = {}
for p in root.rglob("*.pdf"):
    for y in ['2006', '2007', '2008']:
        if y in p.name and len(p.name) < 25: # e.g. 2007年考研英语.pdf
            # check if it has text layer
            try:
                d = pymupdf.open(p)
                tlen = sum(len(d[i].get_text()) for i in range(min(5, len(d))))
                if tlen > 1000:
                    target_files[f"{y}_{p.parent.name[:4]}"] = (y, p)
            except Exception as e:
                pass

print("Found candidate text PDFs:")
for k, (y, p) in target_files.items():
    print(f"  {y}: {p}")

# For each target year, search for the questions
for k, (y, p) in target_files.items():
    doc = pymupdf.open(p)
    out_name = f"scripts/full_text_{y}.txt"
    with open(out_name, "w", encoding="utf-8") as out:
        for idx, page in enumerate(doc):
            t = page.get_text()
            out.write(f"\n--- PAGE {idx+1} ---\n{t}\n")
    print(f"Saved full text of {y} ({len(doc)} pages) to {out_name}")
