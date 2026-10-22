import sys
import fitz
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2010黄皮书真题解析（英语一）.pdf"
doc = fitz.open(pdf_path)

print("=== 2010 ky1 Gold Extraction Engine v4 Started ===")

def clean_txt(t):
    t = re.sub(r'公众号：研友加油站\s*', '', t)
    t = re.sub(r'高清PDF任你选\s*', '', t)
    t = re.sub(r'-2010年全真试题精解\s*', '', t)
    t = re.sub(r'外教朗读\s*', '', t)
    t = re.sub(r'§总体分析\s*', '', t)
    t = re.sub(r'§二•语篇分析及试题精解\s*', '', t)
    # Remove standalone page numbers
    t = re.sub(r'(?:^|\n)\s*\d{1,2}\s*(?:\n|$)', '\n', t)
    return t

# -------------------------------------------------------------
# Part 1: Cloze Q1 - Q20
# -------------------------------------------------------------
cloze_text = clean_txt("\n".join(doc[p].get_text() for p in range(0, 7)))
cloze_text = re.sub(r'\n&\s*\n\s*［A］\s*awareness', '\n8.\n［A］ awareness', cloze_text)

cloze_exps = {}
for qnum in range(1, 21):
    next_qnum = qnum + 1
    pattern = rf'(?:^|\n)\s*{qnum}\s*[\.．\、\-]\s*(.*?)(?=(?:^|\n)\s*{next_qnum}\s*[\.．\、\-]\s*|\nSection II|\nText 1|$)'
    m = re.search(pattern, cloze_text, re.DOTALL)
    if m:
        block = m.group(1).strip()
        pos = block.find('[考点提炼]')
        if pos == -1:
            pos = block.find('［考点提炼］')
        if pos != -1:
            exp = block[pos:].strip()
            exp = exp.replace('[考点提炼]', '［考点提炼］')
            for rep in ['[解题思路]', '〔解题思路〕', 'L解题思路」', '[解题思路〕']:
                exp = exp.replace(rep, '\n\n［解题思路］')
            for rep in ['[错项排除]', '〔错项排除]', '［错项排除J', '[错项排除〕']:
                exp = exp.replace(rep, '\n\n［错项排除］')
            for cutoff in ['•真题精解', '「•真题精解', '解V幺', 'Section H', 'Section II', 'Text 1']:
                if cutoff in exp:
                    exp = exp.split(cutoff)[0].strip()
            # Clean OCR artifacts
            exp = exp.replace('o£', 'of')
            exp = exp.replace('£', 'f')
            exp = re.sub(r'\n{3,}', '\n\n', exp)
            cloze_exps[qnum] = exp.strip()
        else:
            print(f"Error: Cloze Q{qnum} missing ［考点提炼］")
    else:
        print(f"Error: Cloze Q{qnum} block not found")

print(f"Extracted {len(cloze_exps)} / 20 Cloze explanations.")

# -------------------------------------------------------------
# Part 2: Reading Q21 - Q40
# -------------------------------------------------------------
reading_text = clean_txt("\n".join(doc[p].get_text() for p in range(7, 45)))
reading_text = reading_text.replace('［命题解密」', '［命题解密］')
reading_text = reading_text.replace('[命题解密]', '［命题解密］')
reading_text = reading_text.replace('［命题解£\'］', '［命题解密］')
reading_text = reading_text.replace('［命题解密J', '［命题解密］')
reading_text = reading_text.replace('\'技"总结」', '［技巧总结］')
reading_text = reading_text.replace('[技巧总结]', '［技巧总结］')

pos_matches = list(re.finditer(r'［精准定位］', reading_text))
print(f"Found {len(pos_matches)} ［精准定位］ in Reading.")

reading_exps = {}
cutoff_markers = [
    '•语篇分析', '•词汇注释', '•经典搭配', '【深层解读】', '§总体分析', '§二•语篇分析',
    'I ❶', 'II ❶', 'III ❶', 'IV ❶', 'V ❶', 'VI ❶',
    'I O', 'II O', 'III O', 'IV O', 'V O', 'VI O',
    'ID ❶', 'ID O', '1\\ ❶', '1\\ O', 'D ❶', 'D O',
    '1 ❶', '2 ❶', '3 ❶', '4 ❶', '5 ❶',
    'Text ', 'Section II', 'Part C', '英译汉',
    '•真题精解', '•全局真题精解', 'Part B', '文章总体分析', '一.文章总体分析', '扌一.文章总体分析'
]

for idx, match in enumerate(pos_matches):
    qnum = idx + 21
    start = match.start()
    end = pos_matches[idx + 1].start() if idx + 1 < len(pos_matches) else len(reading_text)
    block = reading_text[start:end].strip()
    
    m_dec = re.search(r'［命题解密］', block)
    if not m_dec:
        print(f"Error: Q{qnum} missing ［命题解密］")
        continue
    
    pos_part_raw = block[:m_dec.start()].strip()
    pos_lines = [l.strip() for l in pos_part_raw.split('\n') if l.strip()]
    cleaned_pos_lines = []
    for l in pos_lines:
        if re.search(r'^(?:\d{2}\s*[\.・\、\-]|\b[A-D]\b|[\[［][A-D][\]］])\s*[A-Za-z]', l):
            continue
        if re.search(r'^[\[［][A-D][\]］]\s*[\u4e00-\u9fa5]', l):
            continue
        if re.search(r'^\d{2}\s*[\.・\、\-]\s*[\u4e00-\u9fa5]', l):
            continue
        if any(h in l for h in ['•真题精解', '•全局真题精解', '外教朗读', '总体分析']):
            continue
        cleaned_pos_lines.append(l)
    pos_part = '\n'.join(cleaned_pos_lines).strip()
    
    rest_raw = block[m_dec.start():].strip()
    earliest_cutoff = len(rest_raw)
    for c in cutoff_markers:
        cpos = rest_raw.find(c)
        if cpos != -1 and cpos < earliest_cutoff:
            earliest_cutoff = cpos
            
    rest_clean = rest_raw[:earliest_cutoff].strip()
    combined = f'{pos_part}\n\n{rest_clean}'
    combined = combined.replace('o£', 'of').replace('£', 'f')
    combined = re.sub(r'\n{3,}', '\n\n', combined.strip())
    reading_exps[qnum] = combined
    print(f"Extracted Reading Q{qnum}: {len(combined)} chars | pos_len={len(pos_part)}")

print(f"\nExtracted {len(reading_exps)} / 20 Reading explanations.")

# -------------------------------------------------------------
# Part 3: Part B Q41 - Q45
# -------------------------------------------------------------
p50_text = clean_txt(doc[50].get_text())
p51_text = clean_txt(doc[51].get_text())
part_b_combined = p50_text + '\n' + p51_text

part_b_exps = {}

# 41:
m41 = re.search(r'41\.\s*本题考核的知识点是：.*?(?=\n\s*45\.\s*本题考核的知识点是)', part_b_combined, re.DOTALL)
if m41:
    part_b_exps[41] = m41.group(0).strip()

# 42:
m42 = re.search(r'42\.\s*本题考核的知识点是.*?：.*?(?=\n\s*43\.\s*本题考核的知识点是)', part_b_combined, re.DOTALL)
if m42:
    part_b_exps[42] = m42.group(0).strip()

# 43:
m43 = re.search(r'43\.\s*本题考核的知识点是.*?：.*?(?=\n\s*44\.\s*本题考核的知识点是)', part_b_combined, re.DOTALL)
if m43:
    part_b_exps[43] = m43.group(0).strip()

# 44:
m44 = re.search(r'44\.\s*本题考核的知识点是.*?：.*?(?=\n\s*至此，全文顺序确定为)', part_b_combined, re.DOTALL)
if m44:
    part_b_exps[44] = m44.group(0).strip()

# 45:
m45 = re.search(r'45\.\s*本题考核的知识点是：.*?(?=\n\s*（三）\s*借助路标词)', part_b_combined, re.DOTALL)
if m45:
    part_b_exps[45] = m45.group(0).strip()

for q in [41, 42, 43, 44, 45]:
    if q in part_b_exps:
        exp = part_b_exps[q]
        exp = exp.replace('o£', 'of').replace('£', 'f')
        exp = re.sub(r'\n{3,}', '\n\n', exp).strip()
        part_b_exps[q] = exp
        print(f"Extracted Part B Q{q}: {len(exp)} chars")
    else:
        print(f"Error: Part B Q{q} not found!")

# Save all
all_exps = {}
for k, v in cloze_exps.items():
    all_exps[k] = v
for k, v in reading_exps.items():
    all_exps[k] = v
for k, v in part_b_exps.items():
    all_exps[k] = v

with open('scripts/extracted_2010_all_gold.json', 'w', encoding='utf-8') as f:
    json.dump(all_exps, f, ensure_ascii=False, indent=2)

print(f"\nSaved all {len(all_exps)} explanations to scripts/extracted_2010_all_gold.json!")
