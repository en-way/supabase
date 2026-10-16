import pymupdf
import pathlib

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")
pdf_path = None
for p in root.rglob("*.pdf"):
    if "2001-2009" in p.name:
        pdf_path = p
        break

print(f"Reading aggregated PDF: {pdf_path}")
doc = pymupdf.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Look for 2007, 2006, 2008 sections
# Let's search TOC or page headings
sections = {}
for i in range(len(doc)):
    text = doc[i].get_text()
    for y in ['2006', '2007', '2008']:
        if f"{y}年" in text or f"{y} 年" in text:
            sections.setdefault(y, []).append(i + 1)

for y, pgs in sections.items():
    print(f"Year {y} found on pages: {pgs[:10]} ... total {len(pgs)} pages")
