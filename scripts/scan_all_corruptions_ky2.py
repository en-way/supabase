import json
import glob
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams.json"
exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

with open(exams_file, "r", encoding="utf-8") as f:
    all_exams_meta = json.load(f)

ky2_exams = [e for e in all_exams_meta if e.get("category_id") == "ky2"]
ky2_exams.sort(key=lambda x: x.get("year", 0))

print("=== DEEP SCAN OF CORRUPTIONS IN ALL KY2 EXAMS (2010-2025) ===")

odd_chars_pattern = re.compile(r"[§©®±×÷µ¶\^\\|#~]")
corrupt_brackets_pattern = re.compile(r"[\[［【][A-Za-z0-9]+[JjLlI|]|[\[［【][A-Za-z0-9]+$|\]\]|］］")
garbled_chinese_pattern = re.compile(r"[\u4e00-\u9fa5][a-zA-Z]{1,2}[\u4e00-\u9fa5]|[\u4e00-\u9fa5][0-9][\u4e00-\u9fa5]")
corrupted_ocr_tokens = re.compile(r"Cr\b|C使|C指向|C踩|C适合|C轻率|C感到|C必要|巳|剌激|估价|！！|？？|，，|、、|【|】|“|”|‘|’")

corruptions_found = []

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
        
    # 1. Scan Passages
    for p in exam.get("passages", []):
        p_title = p.get("title", "")
        p_content = p.get("content", "")
        
        # Check odd characters
        for m in odd_chars_pattern.finditer(p_content):
            corruptions_found.append((year, p_title, "passage odd char", m.group(), p_content[max(0, m.start()-15):min(len(p_content), m.end()+15)]))
        for m in corrupt_brackets_pattern.finditer(p_content):
            corruptions_found.append((year, p_title, "passage bracket", m.group(), p_content[max(0, m.start()-15):min(len(p_content), m.end()+15)]))
            
    # 2. Scan Questions
    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        stem = q.get("stem", "")
        expl = q.get("explanation", "")
        opts = [o.get("text", "") for o in q.get("options", []) if isinstance(o, dict)]
        
        # In stem
        for m in odd_chars_pattern.finditer(stem):
            corruptions_found.append((year, f"Q{qnum} stem", "odd char", m.group(), stem[max(0, m.start()-15):min(len(stem), m.end()+15)]))
            
        # In options
        for opt_idx, opt_text in enumerate(opts):
            for m in odd_chars_pattern.finditer(opt_text):
                corruptions_found.append((year, f"Q{qnum} opt {opt_idx}", "odd char", m.group(), opt_text[max(0, m.start()-15):min(len(opt_text), m.end()+15)]))
                
        # In explanation
        for m in odd_chars_pattern.finditer(expl):
            corruptions_found.append((year, f"Q{qnum} expl", "odd char", m.group(), expl[max(0, m.start()-20):min(len(expl), m.end()+20)]))
        for m in corrupt_brackets_pattern.finditer(expl):
            corruptions_found.append((year, f"Q{qnum} expl", "corrupt bracket", m.group(), expl[max(0, m.start()-20):min(len(expl), m.end()+20)]))
        for m in re.finditer(r"\[sa'poitaCr|Cr\b|C使|C指向|C踩|C适合|C轻率|C感到|C必要|巳", expl):
            corruptions_found.append((year, f"Q{qnum} expl", "ocr token", m.group(), expl[max(0, m.start()-20):min(len(expl), m.end()+20)]))

print(f"Total corruptions found: {len(corruptions_found)}")
for item in corruptions_found:
    print(f"[{item[0]} {item[1]}] {item[2]} '{item[3]}': {item[4].replace(chr(10), ' ')}")
