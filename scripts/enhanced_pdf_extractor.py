import os, sys, pymupdf, re, json, glob

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_KY1 = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
BASE_KY2 = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_pdf_path(year, cat):
    base = BASE_KY1 if cat == 'ky1' else BASE_KY2
    for f in os.listdir(base):
        if str(year) in f and f.endswith('.pdf'):
            return os.path.join(base, f)
    return None

def normalize_text(text):
    # Fullwidth brackets
    text = text.replace('［', '[').replace('］', ']').replace('〔', '[').replace('〕', ']')
    text = text.replace('【', '[').replace('】', ']')
    
    # Common OCR bracket glitches: [AJ, [BJ, [CJ, [DJ
    text = re.sub(r'\[\s*([A-Ga-g])\s*[Jj\]\)]', r'[\1]', text)
    text = re.sub(r'(?:C|\:|\bE)A\]', '[A]', text)
    text = re.sub(r'\[因', '[B]', text)
    text = re.sub(r'\[I3\]', '[B]', text)
    text = re.sub(r'\[\:B\]', '[B]', text)
    text = re.sub(r'(?<=\n)\s*:B\]', '[B]', text)
    text = re.sub(r'\[E\](?=[\s\S]{1,300}?\[C\])', '[B]', text)
    text = re.sub(r'(?:E|C)C\]', '[C]', text)
    text = re.sub(r'(?<=\n)\s*LC\]', '[C]', text)
    text = re.sub(r'(?<=\n)\s*:C\]', '[C]', text)
    text = re.sub(r'\[DJ', '[D]', text)
    text = re.sub(r'ED\]', '[D]', text)
    
    # Numbers with ampersands / OCR typos
    text = re.sub(r'(?<=\n)\s*2&\s*[\.、]?', '\n28. ', text)
    text = re.sub(r'(?<=\n)\s*1&\s*[\.、]?', '\n18. ', text)
    text = re.sub(r'(?<=\n)\s*3&\s*[\.、]?', '\n38. ', text)
    text = re.sub(r'(?<=\n)\s*&\s*[\.、]?', '\n8. ', text)
    text = re.sub(r'(?<=\n)\s*\'L\s*', '\n4. ', text)
    text = re.sub(r'(?<=\n)\s*(\d+)[\・\·]\s*', r'\n\1. ', text)
    
    return text

def clean_opt_text(t):
    t = re.sub(r'[\r\n]+', ' ', t).strip()
    t = re.sub(r'^[A-Ga-g][\.\:、\s\-]+', '', t).strip()
    # remove trailing Chinese if starts with English
    m = re.match(r'^([A-Za-z0-9\s\-\,\.\'\’\”\“\:\;\?\!\(\)\/\$\%\&]+?)(?:[\u4e00-\u9fa5]|$)', t)
    if m and len(m.group(1).strip()) > 1:
        eng = m.group(1).strip()
        eng = re.sub(r'[\,\:\;]+$', '', eng).strip()
        # Clean kerning spaces inside single words e.g. "confused l y" -> "confusedly"
        if re.search(r'\b[a-z]\s+[a-z]\b', eng):
            parts = eng.split()
            reassembled = []
            buf = ""
            for p in parts:
                if len(p) <= 2 and p.isalpha():
                    buf += p
                else:
                    if buf:
                        reassembled.append(buf)
                        buf = ""
                    reassembled.append(p)
            if buf:
                reassembled.append(buf)
            eng = " ".join(reassembled)
        if len(eng) > 1:
            return eng
    return t.strip()

def extract_cloze(text, qnum):
    # Pattern to find qnum in Cloze: search all occurrences of qnum followed by [A]
    # Because 2-column layout places [考点提炼] between [A]/[C] and [B]/[D], we look ahead until [解题思路] or next question
    patterns = [
        rf'(?:^|\n)\s*{qnum}\s*[\.、\:]\s*(.*?)(?=(?:\n\s*(?:{qnum+1}|\d{{1,2}})\s*[\.、\:]\s*\[A\]|\n\s*\[(?:解题思路|试题精解|试题点评)\]|\Z))',
        rf'(?:^|\n)\s*{qnum}\s*[\.、\:\s](.*?)(?=(?:\n\s*(?:{qnum+1}|\d+)\s*[\.、]|\n\s*\[(?:精准定位|解题思路)\]|\Z))'
    ]
    for pattern in patterns:
        for m in re.finditer(pattern, text, re.DOTALL):
            block = m.group(1)
            if '[A]' not in block:
                continue
            opts = {}
            for om in re.finditer(r'\[([A-D])\]\s*([^\[\n\r]+)', block):
                k = om.group(1).upper()
                val = clean_opt_text(om.group(2))
                if val and any(c.isascii() and c.isalpha() for c in val):
                    if k not in opts or len(val) > len(opts[k]):
                        opts[k] = val
            if len(opts) == 4:
                return [{"key": k, "text": opts[k]} for k in ['A', 'B', 'C', 'D']]
    return None

def extract_reading(text, qnum):
    # Search all occurrences of qnum
    pattern = rf'(?:^|\n)\s*(?:{qnum}|2&|3&)\s*[\.、](.*?)(?=(?:\n\s*(?:{qnum+1}|\d{{1,2}})\s*[\.、]|\n\s*\[(?:精准定位|命题解密|解题思路)\]|\Z))'
    for m in re.finditer(pattern, text, re.DOTALL):
        block = m.group(1)
        if '[A]' not in block:
            continue
        opts = {}
        for om in re.finditer(r'\[([A-D])\]\s*([^\[\n\r]+)', block):
            k = om.group(1).upper()
            val = clean_opt_text(om.group(2))
            if val and any(c.isascii() and c.isalpha() for c in val):
                if k not in opts or len(val) > len(opts[k]):
                    opts[k] = val
        if len(opts) == 4:
            return [{"key": k, "text": opts[k]} for k in ['A', 'B', 'C', 'D']]
    return None

def run_test():
    import sys, os
    sys.path.insert(0, ROOT_DIR)
    import scripts.audit_synthetic_details as audit
    print("Testing Enhanced PDF Extractor across all exams...")
    
    extracted_total = 0
    missing_total = 0
    
    for (year, cat), (title, qnums, fname) in audit.exam_missing.items():
        pdf_path = get_pdf_path(year, cat)
        if not pdf_path:
            continue
        doc = pymupdf.open(pdf_path)
        text = normalize_text("\n".join([page.get_text() for page in doc]))
        
        exam_success = []
        exam_fail = []
        
        for q in qnums:
            if q > 40:
                exam_fail.append(q)
                continue
                
            res = extract_cloze(text, q) if q <= 20 else extract_reading(text, q)
            if res:
                exam_success.append((q, res))
                extracted_total += 1
            else:
                exam_fail.append(q)
                missing_total += 1
                
        total_cr = len(qnums) - sum(1 for q in qnums if q > 40)
        print(f"{year} {cat}: {len(exam_success)}/{total_cr} Cloze/Reading extracted. Fails: {exam_fail}")
        
    print(f"\nTOTAL EXTRACTED: {extracted_total}, STILL MISSING: {missing_total}")

if __name__ == "__main__":
    run_test()
