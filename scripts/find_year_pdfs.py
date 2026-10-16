import glob
import os
import fitz

root = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"
pdfs = glob.glob(root + "/**/*.pdf", recursive=True)

print(f"Total PDFs found: {len(pdfs)}")

# Search for 2021 ky1 reading and cloze
targets = ['2021', '2007', '2006', '2008', '2009']
matched_files = {}

for p in pdfs:
    bname = os.path.basename(p)
    for t in targets:
        if t in bname:
            matched_files.setdefault(t, []).append(p)

for t, flist in matched_files.items():
    print(f"\nTarget {t}:")
    for f in flist:
        print(f"  {f}")
