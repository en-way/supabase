# -*- coding: utf-8 -*-
import fitz
import re
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf')
ocr = RapidOCR()

def extract_bilingual_english(pages):
    english_paras = []
    current_para = []
    
    for p in pages:
        pix = doc[p-1].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes('png'))
        if not res:
            continue
        w, h = pix.width, pix.height
        
        # Filter left column
        lines = []
        for box, txt, score in res:
            xs = [pt[0] for pt in box]
            ys = [pt[1] for pt in box]
            if max(xs) < w * 0.56:
                lines.append((min(ys), txt))
        lines.sort(key=lambda x: x[0])
        
        for y, txt in lines:
            t = txt.strip()
            # If line is vocab / notes / questions, stop or skip
            if any(k in t for k in ['·真题精解·', '·语篇分析·', '经典搭配', '词汇注释', '长难句分析', '考题速览']):
                continue
            if re.match(r'^\d+\.\[[A-D]\]', t) or re.match(r'^\d+\.', t):
                continue
            if re.match(r'^\[[A-G]\]', t):
                continue
            if any(ord(c) > 0x4e00 and ord(c) < 0x9fff for c in t) and len([c for c in t if ord(c) > 0x4e00]) > 3:
                # Mostly Chinese
                continue
            
            # Check for Roman numeral start (new paragraph)
            m = re.match(r'^([I|V|X]+)\s*[①O0❶❷❸❹❺\d]?(.*)', t)
            if m:
                if current_para:
                    english_paras.append(' '.join(current_para))
                    current_para = []
                rest = m.group(2).strip()
                if rest:
                    current_para.append(rest)
            else:
                # Check if it looks like English text line
                words = re.findall(r'[a-zA-Z]+', t)
                if len(words) >= 2 or (current_para and len(words) >= 1):
                    # Clean out circled numbers
                    cleaned = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩❶❷❸❹❺❻❼❽❾❿]', '', t).strip()
                    if cleaned:
                        current_para.append(cleaned)
                        
    if current_para:
        english_paras.append(' '.join(current_para))
        
    return english_paras

print("=== Extracting Text 1 ===")
t1_paras = extract_bilingual_english([11, 12, 13, 14, 15, 16, 17])
print(f"Text 1 paras count: {len(t1_paras)}")
for i, p in enumerate(t1_paras):
    print(f"P{i+1} ({len(p.split())} words): {p[:100]}...")

print("\n=== Extracting Text 2 ===")
t2_paras = extract_bilingual_english([19, 20, 21, 22, 23, 24, 25])
print(f"Text 2 paras count: {len(t2_paras)}")
for i, p in enumerate(t2_paras):
    print(f"P{i+1} ({len(p.split())} words): {p[:100]}...")

print("\n=== Extracting Text 3 ===")
t3_paras = extract_bilingual_english([28, 29, 31, 33, 35])
print(f"Text 3 paras count: {len(t3_paras)}")
for i, p in enumerate(t3_paras):
    print(f"P{i+1} ({len(p.split())} words): {p[:100]}...")

print("\n=== Extracting Text 4 ===")
t4_paras = extract_bilingual_english([38, 39, 41, 43, 45])
print(f"Text 4 paras count: {len(t4_paras)}")
for i, p in enumerate(t4_paras):
    print(f"P{i+1} ({len(p.split())} words): {p[:100]}...")
