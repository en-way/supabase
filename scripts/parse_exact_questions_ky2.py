# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/2020_ky2_full_book.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages_raw = text.split('=== Page ')
pages = {}
for p in pages_raw[1:]:
    p_num = int(p.split(' ===')[0])
    p_text = p[len(str(p_num)) + 4:]
    pages[p_num] = p_text

# Map question to its source page(s)
q_pages = {
    1: [1], 2: [2], 3: [2], 4: [2], 5: [2, 3], 6: [3], 7: [3],
    8: [4], 9: [5], 10: [5], 11: [5, 6], 12: [6], 13: [6], 14: [6, 7],
    15: [7], 16: [8], 17: [8], 18: [9], 19: [9], 20: [9],
    21: [11, 12], 22: [13, 14], 23: [15, 16], 24: [17, 18], 25: [18],
    26: [21, 22], 27: [23, 24], 28: [24, 25], 29: [26], 30: [27],
    31: [30, 31], 32: [32, 33], 33: [34, 35], 34: [36, 37], 35: [37],
    36: [40, 41], 37: [42], 38: [42, 43], 39: [44, 45], 40: [46],
    41: [53], 42: [53], 43: [53], 44: [53], 45: [53]
}

results = {}

for q, p_list in q_pages.items():
    combined = "\n".join(pages[p] for p in p_list)
    
    # In reading questions, find the question block
    # Pattern: q. Stem... [A] ... [B] ... [C] ... [D] ... [精准定位]...
    if q <= 20:
        # Cloze: find q.[A] ... [D]
        m = re.search(rf'(?:^|\n){q}\.\s*\[A\]([\s\S]*?)(?=(?:^|\n)\d{{1,2}}\.\s*\[A\]|\Z)', combined)
        target = m.group(0) if m else combined
    elif q <= 40:
        # Reading
        m = re.search(rf'(?:^|\n){q}\.\s*([A-Z][\s\S]*?)(?=(?:^|\n)\d{{1,2}}\.\s*[A-Z]|\Z)', combined)
        target = m.group(0) if m else combined
    else:
        # Part B
        m = re.search(rf'(?:^|\n){q}\.\s*([\s\S]*?)(?=(?:^|\n)\d{{1,2}}\.|\Z)', combined)
        target = m.group(0) if m else combined
    
    # Find answer
    ans = None
    m_ans = re.findall(r'(?:\[答案\]|【答案】|［答案］)\s*([A-G])', target)
    if m_ans:
        ans = m_ans[0]
    else:
        m_ans2 = re.findall(r'\[([A-D])\](?:正确|为正确|为本题正确|最贴合|符合|契合)', target)
        if m_ans2:
            ans = m_ans2[-1]
    
    print(f"Q{q:02d}: ans={ans} | target_len={len(target)}")
    if not ans:
        print("  TARGET SNIPPET:", repr(target[:200]))
