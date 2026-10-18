import pymupdf
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

def check_pdf(year, q_nums):
    print(f"\n==================== Checking {year} ====================")
    target_pdfs = []
    for p in root.rglob("*.pdf"):
        if str(year) in p.name and ("英语一" in p.name or "英语（一）" in p.name or "英语一" in p.parent.name):
            target_pdfs.append(p)
    print(f"Found {len(target_pdfs)} PDFs for {year}: {[p.name for p in target_pdfs]}")
    for p in target_pdfs:
        doc = pymupdf.open(p)
        for i, page in enumerate(doc):
            text = page.get_text()
            for q in q_nums:
                if f"{q}." in text and ("［精准定位］" in text or "【精准定位】" in text or "［命题解密］" in text or "[A]" in text):
                    print(f"\n--- {p.name} Page {i+1} for Q{q} ---")
                    lines = text.splitlines()
                    for idx, line in enumerate(lines):
                        if f"{q}." in line:
                            print('\n'.join(lines[max(0, idx-2):min(len(lines), idx+15)]))
                            print('-'*30)

check_pdf(2015, [36, 37])
check_pdf(2018, [31, 32])
