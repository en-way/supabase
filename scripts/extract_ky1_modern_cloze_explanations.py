#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_ky1_modern_cloze_explanations.py
精准提取 2016-2022 年考研英语一真题精解中的缺陷题目：
- 2022 ky1: Q1 - Q20 全量 20 题（解决 Ampersand 8. 映射，注入黄皮书三步分析法精解，精确切除尾部语篇分析与双语文本）
- 2017 ky1: Q14, Q17, Q18（解决 Ampersand 18. 映射，注入黄皮书精解）
- 2016 ky1: Q1, Q19（剥离双语篇章倒灌，闭合跨页截断）
- 2018 ky1: Q10（修复逗号序号，剥离词汇分析尾巴）
"""

import os
import sys
import json
import re
import fitz

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'ky1_modern_cloze_restored.json')

def clean_page_artifacts(text):
    text = text.replace('44尽管如', '“尽管如')
    text = re.sub(r'([a-zA-Z\s])44([\u4e00-\u9fa5])', r'\1“\2', text)
    lines = []
    for line in text.split('\n'):
        l = line.strip()
        if re.match(r'^\d+$', l): # standalone page number
            continue
        if l.startswith('=== Page'):
            continue
        lines.append(line)
    return '\n'.join(lines).strip()

def clean_tail_passage_analysis(txt):
    idx_d = txt.rfind('[D]')
    if idx_d == -1:
        idx_d = txt.rfind('［D］')
    if idx_d == -1:
        return txt
    d_part = txt[idx_d:]
    lines = d_part.split('\n')
    kept = []
    for l in lines:
        s = l.strip()
        if any(marker in s for marker in ['语篇分析', '甌分杭', '全文总结', '•真题精解', '「•真题精解']):
            break
        if re.match(r'^(?:[I|V|X]+|\d+)\s+[❶❷❸❹❺❻O\u2776-\u277f]', s):
            break
        if 'Taiz said' in s or 'the authors wrote' in s or 'according to the article' in s:
            break
        kept.append(l)
    return (txt[:idx_d] + '\n'.join(kept)).strip()

def extract_2022(doc):
    raw = ''
    for i in range(15):
        raw += f"\n=== Page {i+1} ===\n" + doc[i].get_text()
    
    txt = raw.replace('&.本题考查', '8.本题考查').replace('&本题考查', '8.本题考查')
    pattern = r'(?:^|\n)\s*(\d{1,2})\s*[\.、]\s*本题考查'
    matches = list(re.finditer(pattern, txt))
    
    res = {}
    for i, m in enumerate(matches):
        qnum = int(m.group(1))
        start_pos = m.start()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(txt)
        q_txt = txt[start_pos:end_pos].strip()
        if '词汇注释与难句分析' in q_txt:
            q_txt = q_txt.split('词汇注释与难句分析')[0].strip()
        if '全文翻译' in q_txt:
            q_txt = q_txt.split('全文翻译')[0].strip()
        cleaned = clean_page_artifacts(q_txt)
        cleaned = clean_tail_passage_analysis(cleaned)
        res[str(qnum)] = cleaned
    return res

def extract_2017(doc):
    txt = ''
    for i in range(12):
        txt += f"\n=== Page {i+1} ===\n" + doc[i].get_text()
    
    txt = re.sub(r'1&(?=[\s\.\,、\[［])', '18.', txt)
    txt = re.sub(r'(?<!\d)&(?=[\s\.\,、\[［])', '8.', txt)
    
    res = {}
    for q in [14, 17, 18]:
        m = re.search(rf'(?:^|\n)\s*{q}\s*[\.、]\s*([\[［][A-D][\]］].*?)(?=(?:\n\s*(?:{q+1}\s*[\.、]|Text|Section|\[•词汇注释|词汇注释)|$))', txt, re.DOTALL)
        if m:
            content = m.group(0).strip()
            # Clean EC] -> [C]
            content = re.sub(r'E([A-D])[］\]]', r'[\1]', content)
            cleaned = clean_page_artifacts(content)
            res[str(q)] = cleaned
    return res

def extract_2016(doc):
    txt = ''
    for i in range(10):
        txt += f"\n=== Page {i+1} ===\n" + doc[i].get_text()
    
    res = {}
    # Q1
    m1 = re.search(r'(?:^|\n)\s*1\s*[\.、]\s*(\[Aj.*?)((?:\n\s*2\s*[\.、]|$))', txt, re.DOTALL)
    if m1:
        q1_raw = m1.group(1).replace('[Aj', '[A]').strip()
        res['1'] = '1. ' + clean_page_artifacts(q1_raw)
    
    # Q19
    m19 = re.search(r'(?:^|\n)\s*19\s*[\.、]\s*(.*?)(?=(?:\n\s*20\s*[\.、]|$))', txt, re.DOTALL)
    if m19:
        q19_raw = m19.group(1).strip()
        res['19'] = '19. ' + clean_page_artifacts(q19_raw)
    return res

def extract_2018(doc):
    txt = ''
    for i in range(10):
        txt += f"\n=== Page {i+1} ===\n" + doc[i].get_text()
    
    res = {}
    m10 = re.search(r'(?:^|\n)\s*10\s*[\,\.、]\s*(\[A\].*?)(?=(?:\n\s*(?:11\s*[\.、]|\[•词汇注释|「•词汇注释|词汇注释)|$))', txt, re.DOTALL)
    if m10:
        q10_raw = m10.group(1).strip()
        if '「•词汇注释' in q10_raw:
            q10_raw = q10_raw.split('「•词汇注释')[0].strip()
        if '[•词汇注释' in q10_raw:
            q10_raw = q10_raw.split('[•词汇注释')[0].strip()
        res['10'] = '10. ' + clean_page_artifacts(q10_raw)
    return res

def main():
    payload = {}
    
    # 2022
    p22 = os.path.join(BASE_DIR, "2022黄皮书真题解析（英语一）.pdf")
    doc22 = fitz.open(p22)
    payload['2022'] = extract_2022(doc22)
    print(f"2022 ky1 extracted: {len(payload['2022'])} questions")

    # 2017
    p17 = os.path.join(BASE_DIR, "2017黄皮书真题解析（英语一）.pdf")
    doc17 = fitz.open(p17)
    payload['2017'] = extract_2017(doc17)
    print(f"2017 ky1 extracted: {len(payload['2017'])} questions")

    # 2016
    p16 = os.path.join(BASE_DIR, "2016黄皮书真题解析（英语一）.pdf")
    doc16 = fitz.open(p16)
    payload['2016'] = extract_2016(doc16)
    print(f"2016 ky1 extracted: {len(payload['2016'])} questions")

    # 2018
    p18 = os.path.join(BASE_DIR, "2018黄皮书真题解析（英语一）.pdf")
    doc18 = fitz.open(p18)
    payload['2018'] = extract_2018(doc18)
    print(f"2018 ky1 extracted: {len(payload['2018'])} questions")

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Saved payload to: {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
