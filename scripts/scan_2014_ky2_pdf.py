import pypdf

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf"
reader = pypdf.PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

# Print first 5 pages to see table of contents or intro
with open("scripts/ky2_pdf_intro.txt", "w", encoding="utf-8") as out:
    for idx in range(min(10, len(reader.pages))):
        out.write(f"\n{'='*30} PAGE {idx+1} {'='*30}\n")
        out.write(reader.pages[idx].extract_text())

print("Saved first 10 pages to scripts/ky2_pdf_intro.txt")
