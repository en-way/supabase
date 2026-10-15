import pypdf
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def extract_cloze(pdf_path, year):
    reader = pypdf.PdfReader(pdf_path)
    print(f"=== Extracting {year} Cloze Explanations from {pdf_path} ===")
    full_cloze_text = ""
    # Cloze is typically in the first 8 pages
    for p in range(min(8, len(reader.pages))):
        full_cloze_text += f"\n--- Page {p+1} ---\n" + reader.pages[p].extract_text()
    
    # Let's search for question numbers 1. to 20.
    q_map = {}
    for q_num in range(1, 21):
        # find pattern
        m = re.search(rf'(?:^|\n)\s*{q_num}\s*[\.、]\s*(\[[A-G]\].*?)(?=(?:^|\n)\s*{q_num+1}\s*[\.、]|\n•词|\n•语篇|\n\n\n|$)', full_cloze_text, re.DOTALL)
        if m:
            q_map[q_num] = m.group(1).strip()
            print(f"Q{q_num}: extracted ({len(q_map[q_num])} chars)")
        else:
            print(f"Q{q_num}: NOT found!")
    return q_map

q2005 = extract_cloze(r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf', 2005)
q2007 = extract_cloze(r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2007年考研英语真题解析.pdf', 2007)
