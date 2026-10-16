import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

agent_dirs = {
    '2001-2005': 'C:/Users/57867/.gemini/antigravity/brain/5d33c28a-5549-47f0-bd22-1b9cb339848f/scratch',
    '2006-2010': 'C:/Users/57867/.gemini/antigravity/brain/ec10f8d3-6e9f-421b-a9be-72a82dd5de9b/scratch',
    '2011-2015': 'C:/Users/57867/.gemini/antigravity/brain/bff42094-214a-421b-9c4b-ebcabd69b641/scratch'
}

def load_raw_text(year):
    if 2001 <= year <= 2005:
        p = os.path.join(agent_dirs['2001-2005'], f'dump_{year}_all_exp.txt')
        if not os.path.exists(p):
            p = os.path.join(agent_dirs['2001-2005'], f'pdf_text_{year}.txt')
    elif 2006 <= year <= 2010:
        p = os.path.join(agent_dirs['2006-2010'], f'{year}_cloze_raw_pdf.txt')
    else:
        p = os.path.join(agent_dirs['2011-2015'], f'{year}_cloze_raw_pdf.txt')
    
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def extract_questions_from_text(year, text):
    # Locate where 真题精解 begins
    # Cut off translation/vocabulary section if present
    patterns = [
        r'(?:Section\s+I|一、总体分析).*?(?:二[、\.]\s*试[题題]精解|•\s*真题精解\s*•|试题精解)',
        r'二[、\.]\s*试[题題]精解',
        r'•\s*真题精解\s*•'
    ]
    
    # Try finding the start of explanation
    start_pos = -1
    for pat in patterns:
        m = re.search(pat, text, re.DOTALL)
        if m:
            start_pos = m.end()
            break
            
    if start_pos != -1:
        exp_text = text[start_pos:]
    else:
        exp_text = text
        
    # Cut off at Reading comprehension
    end_m = re.search(r'(?:Section\s+II|Reading\s+Comprehension|Text\s+1)', exp_text, re.IGNORECASE)
    if end_m and end_m.start() > 2000:
        exp_text = exp_text[:end_m.start()]
        
    # Find all question blocks
    # A question block usually starts with a number 1..20 followed by dot/paren/bracket
    # e.g., "1.", "1 ", "1. [A]", "[1]", "10.", "20."
    # Let's find matches for all numbers 1..20
    q_dict = {}
    
    # Pattern to find question headers
    # We look for lines starting with number 1..20, or preceded by newline
    # Also handle OCR noise like "& [A]" for 8
    clean_lines = exp_text.split('\n')
    
    # Let's inspect where 考点提炼 occurs
    kdtl_indices = []
    for idx, l in enumerate(clean_lines):
        if re.search(r'[\[［]考点提炼[\]］]|1：考点提炼］|【考点提炼】', l):
            kdtl_indices.append(idx)
            
    return len(clean_lines), len(kdtl_indices), kdtl_indices

print("Testing raw text availability and 考点提炼 counts:")
for y in range(2001, 2016):
    t = load_raw_text(y)
    if not t:
        print(f'{y}: NOT FOUND')
        continue
    lines_cnt, kdtl_cnt, indices = extract_questions_from_text(y, t)
    print(f'{y}: total chars={len(t)}, lines={lines_cnt}, 考点提炼 count={kdtl_cnt}')
