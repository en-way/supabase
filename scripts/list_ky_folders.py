import pymupdf
import pathlib
import sys

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

# Find the ky1 directory
ky1_dir = None
for p in root.iterdir():
    if p.is_dir() and "2001-2025" in p.name:
        # Check if it has 2006
        if any("2006" in f.name for f in p.glob("*.pdf")):
            # Distinguish ky1 vs ky2: ky2 was only introduced in 2010! But folder might be named ky1
            # Let's check subfolders
            print(f"Candidate folder: {repr(p.name)}")

# Let's inspect all subfolders and their pdfs
for p in root.iterdir():
    if p.is_dir():
        pdfs = list(p.glob("*.pdf"))
        print(f"Folder '{p.name}' has {len(pdfs)} PDFs: {[f.name for f in pdfs[:5]]}")
