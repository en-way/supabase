import pypdf
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2007年考研英语真题解析.pdf'
reader = pypdf.PdfReader(pdf_path)

full_text = ""
for p in range(7):
    full_text += f"\n--- Page {p+1} ---\n" + reader.pages[p].extract_text()

# Replace the OCR typo 'L with 4.
full_text = full_text.replace("'L [A]", "4. [A]")

matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*[\.、]\s*\[\s*[A-G]\s*\]', full_text))
print("Found question starts in 2007:", len(matches))

q_explanations_2007 = {}
for i, m in enumerate(matches):
    q_num = int(m.group(1))
    start_idx = m.start()
    if i + 1 < len(matches):
        end_idx = matches[i+1].start()
    else:
        end_idx = full_text.find("Section II", start_idx)
        if end_idx == -1:
            end_idx = full_text.find("Part A", start_idx)
        if end_idx == -1:
            end_idx = start_idx + 1500

    chunk = full_text[start_idx:end_idx].strip()
    lines = chunk.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.startswith('--- Page'):
            continue
        if any(k in line for k in ['真题精解', '语篇分析', '词汇注释', '总体分析']) and len(cleaned_lines) > 5:
            break
        cleaned_lines.append(line)

    expl_text = "\n".join(cleaned_lines).strip()
    q_explanations_2007[q_num] = expl_text
    print(f"Q{q_num} len: {len(expl_text)} preview: {repr(expl_text[:80])}")

with open('scripts/cloze_2007_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(q_explanations_2007, f, ensure_ascii=False, indent=2)
