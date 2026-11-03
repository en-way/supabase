import json
import glob
import os
import re
import sys
import io

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams.json"
exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

with open(exams_file, "r", encoding="utf-8") as f:
    all_exams_meta = json.load(f)

ky2_exams = [e for e in all_exams_meta if e.get("category_id") == "ky2"]
ky2_exams.sort(key=lambda x: x.get("year", 0))

print(f"Total English 2 exams: {len(ky2_exams)}")

findings = {
    "invisible_chars": [],
    "bracket_glitches": [],
    "ocr_latin_greek_symbols": [],
    "ocr_chinese_typos": [],
    "double_punctuation": [],
    "unspaced_punctuation": [],
    "cloze_blank_missing": [],
    "stem_glitches": [],
    "option_glitches": [],
    "answer_conflicts": [],
    "short_or_placeholder_expls": [],
    "hyphen_break_words": [],
    "passage_tail_leak": [],
}

# Regexes
re_invisible = re.compile(r"[\u00a0\u00ad\u200b\u200e\u200f\ufeff\u3000]")
re_bad_brackets = re.compile(r"[\[［【][A-Ga-g][JjLlI|]|[\[［【][A-Ga-g]$")
re_odd_symbols = re.compile(r"[£§¤¥©®±×÷µ¶·•\^~_|\\]")
re_ocr_cn = re.compile(r"巳[a-zA-Z]|[a-zA-Z]巳|剌激|估价|，，|、、|！！|？？")
re_answer_mention = re.compile(r"(?:故选|答案为|正确答案是|答案是|【答案】|［答案］|\[答案\])\s*[:：]?\s*([A-Ga-gTF])\b")

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        exam_data = json.load(f)
    
    passages = exam_data.get("passages", [])
    questions = exam_data.get("questions", [])
    
    # 1. Passage checks
    for p_idx, p in enumerate(passages):
        pid = p.get("id", f"p_{p_idx}")
        title = p.get("title", "")
        content = p.get("content", "")
        stype = p.get("type") or p.get("section_type", "")
        
        # Check invisibles
        invis = re_invisible.findall(content)
        if invis:
            findings["invisible_chars"].append((year, title, f"passage {pid}", [hex(ord(c)) for c in set(invis)]))
            
        # Check odd symbols
        odds = re_odd_symbols.findall(content)
        if odds:
            findings["ocr_latin_greek_symbols"].append((year, title, f"passage {pid}", set(odds)))
            
        # Check cloze blanks
        if stype == "cloze":
            # Blanks should be [1] to [20] or similar
            for b_num in range(1, 21):
                b_pat = f"[{b_num}]"
                if b_pat not in content and f"［{b_num}］" not in content and f"_{b_num}_" not in content:
                    findings["cloze_blank_missing"].append((year, title, b_pat))
                    
        # Check hyphen wrap breaks e.g. "someth- ing"
        hyphen_wraps = re.findall(r"\b([a-zA-Z]{3,})-\s+([a-zA-Z]{3,})\b", content)
        if hyphen_wraps:
            findings["hyphen_break_words"].append((year, title, f"passage {pid}", hyphen_wraps[:5]))
            
        # Check passage tail leaks (words like "Word count: 420", or options leaked)
        if re.search(r"word count|\b\d{3}\s*words|\bText \d\b", content[-100:], re.IGNORECASE):
            findings["passage_tail_leak"].append((year, title, content[-80:]))

    # 2. Questions checks
    for q in questions:
        qnum = q.get("question_number")
        stem = q.get("stem", "")
        opts = q.get("options", [])
        ans = q.get("answer") or q.get("correct_answer") or ""
        expl = q.get("explanation", "")
        
        full_q_text = stem + " " + expl + " " + " ".join(o.get("text", "") for o in opts if isinstance(o, dict))
        
        # Check invisibles
        invis = re_invisible.findall(full_q_text)
        if invis:
            findings["invisible_chars"].append((year, f"Q{qnum}", "question", [hex(ord(c)) for c in set(invis)]))
            
        # Check bad brackets
        bad_b = re_bad_brackets.findall(full_q_text)
        if bad_b:
            findings["bracket_glitches"].append((year, f"Q{qnum}", bad_b))
            
        # Check odd symbols in stem or options
        odds = re_odd_symbols.findall(stem + " " + " ".join(o.get("text", "") for o in opts if isinstance(o, dict)))
        if odds:
            findings["ocr_latin_greek_symbols"].append((year, f"Q{qnum}", "stem/opts", set(odds)))
            
        # Check double punctuation
        dp = re.findall(r"[，,]{2,}|[。.]{2,}(?!\.)|[；;]{2,}|[！!]{2,}", full_q_text)
        if dp:
            findings["double_punctuation"].append((year, f"Q{qnum}", dp))
            
        # Check OCR CN typos
        cn_typos = re_ocr_cn.findall(full_q_text)
        if cn_typos:
            findings["ocr_chinese_typos"].append((year, f"Q{qnum}", cn_typos))
            
        # Check answer conflicts in explanation
        ans_mentions = re_answer_mention.findall(expl)
        if ans_mentions:
            for m in ans_mentions:
                if m.upper() != ans.upper():
                    findings["answer_conflicts"].append((year, f"Q{qnum}", f"Official ans: {ans}, expl mentions: {m}"))
                    
        # Check short or placeholder explanations
        if not expl or len(expl.strip()) < 30 or "暂无解析" in expl or "待补充" in expl:
            findings["short_or_placeholder_expls"].append((year, f"Q{qnum}", len(expl.strip())))
            
        # Check options count and format
        if 1 <= qnum <= 40:
            if len(opts) != 4:
                findings["option_glitches"].append((year, f"Q{qnum}", f"Expected 4 options, got {len(opts)}"))
            keys = [o.get("key") for o in opts if isinstance(o, dict)]
            if keys != ["A", "B", "C", "D"]:
                findings["option_glitches"].append((year, f"Q{qnum}", f"Keys not A-D: {keys}"))
        elif 41 <= qnum <= 45:
            # English 2 Part B
            if year == 2010:
                # 2010 is True/False
                keys = [o.get("key") for o in opts if isinstance(o, dict)]
                if keys != ["T", "F"] and keys != ["True", "False"]:
                    findings["option_glitches"].append((year, f"Q{qnum}", f"2010 Part B keys: {keys}"))
            else:
                # [A]-[G] or [A]-[E]
                keys = [o.get("key") for o in opts if isinstance(o, dict)]
                if len(opts) < 5:
                    findings["option_glitches"].append((year, f"Q{qnum}", f"Part B options count: {len(opts)}, keys: {keys}"))

print("\n=== SCAN SUMMARY ===")
for cat, items in findings.items():
    print(f"{cat}: {len(items)} items")
    if items:
        for it in items[:10]:
            print(f"   {it}")
        if len(items) > 10:
            print(f"   ... and {len(items) - 10} more")
