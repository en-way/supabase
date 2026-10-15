import pypdf
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf'
reader = pypdf.PdfReader(pdf_path)

full_text = ""
for p in range(7):
    full_text += f"\n--- Page {p+1} ---\n" + reader.pages[p].extract_text()

# We know the positions of 1. through 20.
# Let's search each question start using a flexible regex:
# e.g. re.search(r'\n\s*(\d+)\s*\.\s*\[\s*[A-G]\s*\]', full_text)
matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\s*[\.、]\s*\[\s*[A-G]\s*\]', full_text))
print("Found question starts:", len(matches))

q_explanations_2005 = {}
for i, m in enumerate(matches):
    q_num = int(m.group(1))
    start_idx = m.start()
    if i + 1 < len(matches):
        end_idx = matches[i+1].start()
    else:
        # For Q20, stop before Section II / Part A
        end_idx = full_text.find("Section II", start_idx)
        if end_idx == -1:
            end_idx = full_text.find("Part A", start_idx)
        if end_idx == -1:
            end_idx = start_idx + 1500

    chunk = full_text[start_idx:end_idx].strip()
    # Strip any page headers like "--- Page X ---" or bilingual passage paragraphs before next question
    lines = chunk.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.startswith('--- Page') or re.match(r'^[①②③④⑤⑥⑦⑧⑨]\s*[A-Z\u4e00-\u9fa5]', line):
            # could be vocabulary notes or next paragraph of text, but let's check
            if '考点提炼' in line or '解题思路' in line or '错项排除' in line:
                cleaned_lines.append(line)
            elif any(k in line for k in ['[A]', '[B]', '[C]', '[D]', '[ A]', '[ B]', '[ C]', '[ D]', '[A］', '[B］', '[C］', '[D］']):
                cleaned_lines.append(line)
            elif len(cleaned_lines) > 0 and not any(k in line for k in ['真题精解', '语篇分析', '词汇注释', '总体分析']):
                cleaned_lines.append(line)
        else:
            if any(k in line for k in ['真题精解', '语篇分析', '词汇注释', '总体分析']) and len(cleaned_lines) > 5:
                break
            cleaned_lines.append(line)

    expl_text = "\n".join(cleaned_lines).strip()
    q_explanations_2005[q_num] = expl_text
    print(f"Q{q_num} len: {len(expl_text)} preview: {repr(expl_text[:80])}")

# Let's save to a json for inspect
with open('scripts/cloze_2005_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(q_explanations_2005, f, ensure_ascii=False, indent=2)
