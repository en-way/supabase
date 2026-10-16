# -*- coding: utf-8 -*-
"""
parse_2022_ky2_cloze.py
Extract cleanly formatted explanations for 2022 ky2 Q1-Q20 from scripts/2022_ky2_cloze_raw.txt
"""

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

raw = open('scripts/2022_ky2_cloze_raw.txt', encoding='utf-8').read()

# Let's locate the start of each question in raw text
pattern = r'(?m)^\s*(?:1[0-9]|20|[1-9]|1\&)\s*[\.・]?\s*(?:\[|［)'

matches = list(re.finditer(pattern, raw))
print(f"Found {len(matches)} question markers")

questions_text = {}
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i + 1 < len(matches) else len(raw)
    chunk = raw[start:end].strip()
    
    # Identify question number
    m_num = re.match(r'^\s*(1\&|\d+)', chunk)
    if m_num:
        num_str = m_num.group(1)
        q_num = 18 if num_str == '1&' else int(num_str)
        
        # Clean chunk from page headers/footers
        cleaned = re.sub(r'=+\s*Page \d+\s*=+', '', chunk)
        cleaned = re.sub(r'•词汇注释与难句分析.*?(?=［|\[|\Z)', '', cleaned, flags=re.S)
        cleaned = re.sub(r'•语篇分析.*?(?=［|\[|\d+\.|\Z)', '', cleaned, flags=re.S)
        cleaned = re.sub(r'第[一二三四五]段.*?(?=［|\[|\d+\.|\Z)', '', cleaned, flags=re.S)
        cleaned = re.sub(r'[IVXLCDM]+\s*❶.*?(?=［|\[|\d+\.|\Z)', '', cleaned, flags=re.S)
        if q_num == 20:
            cleaned = re.sub(r':\[\'fainaitZ\].*', '', cleaned, flags=re.S)
            cleaned = re.sub(r'\[总体分析\].*', '', cleaned, flags=re.S)
        cleaned = re.sub(r'44([\u4e00-\u9fa5])', r'“\1', cleaned)
        cleaned = cleaned.replace('・', '·')
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned).strip()
        
        questions_text[q_num] = cleaned
        print(f"Q{q_num:02d}: length {len(cleaned)} | head: {cleaned[:40]!r}")

print(f"\nTotal parsed questions: {len(questions_text)}/20")
