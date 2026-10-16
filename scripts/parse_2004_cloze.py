import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ocr_text = open(r'd:\A16pro\Aing\antigravity\supabase\scripts\2004_cloze_full_ocr.txt', encoding='utf-8').read()

# Question pattern: e.g. "1.[A]" or "13 [A]" or "3.[A]"
# Split by question numbers
q_indices = []
for q in range(1, 21):
    # Regex to find question start: e.g. "1.[A]" or "13 [A]" or "13A"
    pattern = rf'(?:^|\n)\s*{q}\s*[^a-zA-Z0-9\n]{{0,3}}[A-ZＡ-Ｚ]'
    m = re.search(pattern, ocr_text)
    if m:
        q_indices.append((q, m.start()))
    else:
        print(f"Warning: Q{q} not found with pattern")

q_indices.sort(key=lambda x: x[0])
print(f"Found {len(q_indices)} question boundaries.")

parsed_expls = {}
for i in range(len(q_indices)):
    qnum, start_pos = q_indices[i]
    if i + 1 < len(q_indices):
        end_pos = q_indices[i+1][1]
        raw_chunk = ocr_text[start_pos:end_pos].strip()
    else:
        # For Q20, find until "Section II" or next section
        end_match = re.search(r'Section\s*II|阅读理解|Text\s*1', ocr_text[start_pos:])
        if end_match:
            end_pos = start_pos + end_match.start()
            raw_chunk = ocr_text[start_pos:end_pos].strip()
        else:
            raw_chunk = ocr_text[start_pos:].strip()
    
    # Process raw_chunk into clean markdown explanation
    # Remove page number artifacts like "3", "4", "5", etc. standalone lines
    cleaned_lines = []
    for line in raw_chunk.split('\n'):
        line_s = line.strip()
        if re.match(r'^\d{1,2}$', line_s):
            continue # standalone page number
        if '语篇分析' in line_s or '真题精解' in line_s:
            continue
        cleaned_lines.append(line_s)
    
    clean_text = "\n".join(cleaned_lines).strip()
    
    # Format headers like [考点提炼], [精准定位], [空格设置], [错项排除], [干扰设置]
    clean_text = re.sub(r'[\[【]?(?:本题考核的知识点是|考点提炼)[：:\]】]?', '\n\n【考点提炼】', clean_text)
    clean_text = re.sub(r'[\[【]?(?:精准定位|解题思路)[：:\]】]?', '\n\n【解题思路】', clean_text)
    clean_text = re.sub(r'[\[【]?(?:错项排除|干扰设置)[：:\]】]?', '\n\n【错项排除】', clean_text)
    clean_text = re.sub(r'[\[【]?空格设置[：:\]】]?', '\n\n【空格设置】', clean_text)
    
    # Clean double spaces/newlines
    clean_text = re.sub(r'\n{3,}', '\n\n', clean_text).strip()
    
    parsed_expls[qnum] = clean_text

for q in range(1, 21):
    txt = parsed_expls.get(q, "")
    print(f"=== Q{q} (len={len(txt)}) ===")
    print(txt[:150] + ("..." if len(txt) > 150 else ""))
    print()

with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\2004_cloze_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_expls, f, ensure_ascii=False, indent=2)

print("Saved parsed explanations to scripts/2004_cloze_parsed.json")
