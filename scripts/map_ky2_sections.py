import pypdf
import re

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf"
reader = pypdf.PdfReader(pdf_path)

with open("scripts/ky2_sections_map.txt", "w", encoding="utf-8") as out:
    for idx, page in enumerate(reader.pages):
        text = page.extract_text()
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for line in lines[:5]:
            if any(k in line for k in ["Section", "Part", "Text", "真题精解", "参考答案", "总体分析", "答案速查", "试题精解"]):
                out.write(f"Page {idx+1}: {line}\n")
                break

print("Saved section map.")
