import pymupdf
import pathlib

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

for pdf_path in root.rglob("*.pdf"):
    if "2021" in pdf_path.name and ("英语（一）" in pdf_path.name or "英语一" in pdf_path.name or "ky1" in pdf_path.name.lower()):
        print(f"Found target PDF: {pdf_path}")
        doc = pymupdf.open(pdf_path)
        print(f"Total pages: {len(doc)}")
        for i, page in enumerate(doc):
            text = page.get_text()
            if 'well-being' in text or '18.' in text:
                for line in text.splitlines():
                    if any(w in line for w in ['well-being', '[A]', '[B]', '[C]', '[D]', '18.']):
                        print(f"P{i+1}: {line.strip()}")
            if 'Patricia Millett' in text or 'trivialities' in text or '39.' in text:
                for line in text.splitlines():
                    if any(w in line for w in ['Patricia Millett', 'trivialities', 'ambiguous', 'reality', 'odds', '39.']):
                        print(f"P{i+1}: {line.strip()}")
