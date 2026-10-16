import glob
import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'
out_dir = 'C:/Users/57867/.gemini/antigravity/brain/ec10f8d3-6e9f-421b-a9be-72a82dd5de9b/scratch'

for y in [2006, 2007, 2008, 2009, 2010]:
    matches = glob.glob(f'{pdf_dir}/*{y}*.pdf')
    if not matches:
        print(f'Error: no PDF found for {y}')
        continue
    pdf_path = matches[0]
    doc = fitz.open(pdf_path)
    
    cloze_text = []
    for p_idx in range(min(12, len(doc))):
        text = doc[p_idx].get_text()
        # Stop if we hit Reading section
        if ('Section II Reading Comprehension' in text or 'Text 1' in text) and p_idx > 2:
            # We take up to Text 1
            t_split = text.split('Text 1')[0]
            cloze_text.append(f'=== PAGE {p_idx+1} ===\n' + t_split)
            break
        cloze_text.append(f'=== PAGE {p_idx+1} ===\n' + text)
        
    full_text = '\n'.join(cloze_text)
    out_file = os.path.join(out_dir, f'{y}_cloze_raw_pdf.txt')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f'Wrote {y} cloze text to {out_file}, size={len(full_text)} chars')
