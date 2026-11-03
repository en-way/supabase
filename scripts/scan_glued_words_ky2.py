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

# Let's inspect passages and questions of English 2:
# 1. Check for broken words like "rn" instead of "m", "cl" instead of "d", glued words like "in1998", "to2020", "andthe"
# 2. Check for Chinese OCR typos like "巳", "剌", "目", "日", "力", "［", "[AJ", "[BJ", etc.
# 3. Check for phonetic alphabet corruptions in explanations like "[diit3：mi'neifn]"
# 4. Check for broken markdown in explanations
# 5. Check for English typos in stems and options

glued_words_pattern = re.compile(r"\b([a-zA-Z]{3,})(the|and|that|with|for|from|this|these|their|which|about)\b")
unspaced_punct_pattern = re.compile(r"([a-zA-Z]{2,})([,\.?!;:])([a-zA-Z]{2,})")
letter_num_glued = re.compile(r"\b([a-zA-Z]{2,})(\d{1,4})\b|\b(\d{1,4})([a-zA-Z]{2,})\b")

findings = []

for meta in ky2_exams:
    year = meta.get("year")
    eid = meta.get("id")
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        exam = json.load(f)
        
    for p in exam.get("passages", []):
        content = p.get("content", "")
        # unspaced punctuation
        for m in unspaced_punct_pattern.finditer(content):
            # ignore e.g., i.e., etc., URLs
            w1, punct, w2 = m.groups()
            if w1.lower() in ("e", "i") and punct == ".": continue
            if "http" in content[max(0, m.start()-10):m.end()+10]: continue
            findings.append((year, p.get("title")[:25], "passage unspaced punct", m.group(0), content[max(0, m.start()-15):min(len(content), m.end()+15)]))
            
        for m in letter_num_glued.finditer(content):
            # ignore valid terms like 3D, G20, MP3, etc.
            tok = m.group(0)
            if tok.upper() in ("3D", "G20", "MP3", "B2B", "COVID19", "H1N1", "2D", "4G", "5G"): continue
            findings.append((year, p.get("title")[:25], "passage letter-num glued", tok, content[max(0, m.start()-15):min(len(content), m.end()+15)]))

    for q in exam.get("questions", []):
        qnum = q.get("question_number")
        stem = q.get("stem", "")
        expl = q.get("explanation", "")
        opts = [o.get("text", "") for o in q.get("options", []) if isinstance(o, dict)]
        
        for m in unspaced_punct_pattern.finditer(stem):
            findings.append((year, f"Q{qnum} stem", "stem unspaced punct", m.group(0), stem[max(0, m.start()-15):min(len(stem), m.end()+15)]))
            
        for opt in opts:
            for m in unspaced_punct_pattern.finditer(opt):
                findings.append((year, f"Q{qnum} opt", "opt unspaced punct", m.group(0), opt[max(0, m.start()-15):min(len(opt), m.end()+15)]))

print(f"Total glued/punctuation findings: {len(findings)}")
for f in findings[:30]:
    print(f"[{f[0]} {f[1]}] {f[2]} '{f[3]}': ...{f[4]}...")
if len(findings) > 30:
    print(f"... and {len(findings)-30} more")
