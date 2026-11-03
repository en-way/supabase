import fitz

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")
for i in range(min(5, len(doc))):
    page = doc[i]
    text = page.get_text()
    images = page.get_images()
    print(f"Page {i+1}: text length = {len(text)}, images count = {len(images)}")
