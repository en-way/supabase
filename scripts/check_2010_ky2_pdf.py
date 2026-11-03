import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2010年真题解析及复习思路.pdf"
doc = fitz.open(pdf_path)

print(f"=== Checking 2010 ky2 PDF: {len(doc)} pages ===")

for p in range(len(doc)):
    text = doc[p].get_text()
    first_lines = [l.strip() for l in text.split('\n') if l.strip()][:3]
    # Check section keywords
    has_cloze = '完形' in text or 'Use of English' in text or '英语知识运用' in text or 'Section I' in text
    has_text1 = 'Text 1' in text
    has_text2 = 'Text 2' in text
    has_text3 = 'Text 3' in text
    has_text4 = 'Text 4' in text
    has_part_b = 'Part B' in text or '判断题' in text or '正误判断' in text
    has_part_c = 'Part C' in text or '翻译' in text or '英译汉' in text
    
    tags = []
    if has_cloze: tags.append('Cloze')
    if has_text1: tags.append('Text 1')
    if has_text2: tags.append('Text 2')
    if has_text3: tags.append('Text 3')
    if has_text4: tags.append('Text 4')
    if has_part_b: tags.append('Part B')
    if has_part_c: tags.append('Part C')
    
    if tags or p < 5 or p > len(doc) - 5:
        print(f"Page {p}: tags={tags} | first={first_lines}")
