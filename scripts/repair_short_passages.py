import os, sys, pymupdf, re, json

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_KY1 = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
EXAMS_DIR = os.path.join(ROOT_DIR, "public", "data", "exams")

def extract_english_from_pages(doc, page_start, page_end):
    paras = []
    current_para = []
    
    for pidx in range(page_start, page_end):
        if pidx >= len(doc):
            break
        page = doc[pidx]
        blocks = sorted(page.get_text("blocks"), key=lambda b: (b[1], b[0]))
        for b in blocks:
            x0, y0, x1, y1, text, bno, btype = b
            if btype != 0:
                continue
            txt = text.strip()
            # check if block contains substantial english
            eng_chars = sum(1 for c in txt if c.isascii() and c.isalpha())
            if len(txt) > 0 and eng_chars / len(txt) > 0.5:
                # filter out pure metadata
                if not any(k in txt for k in ["词汇注释", "真题精解", "语篇分析", "公众号", "解析及复习思路", "微信"]):
                    clean = re.sub(r'^[I|V|X]+\s*[❶❷❸❹❺❻❼❽❾❿]\s*', '', txt)
                    clean = re.sub(r'[❶❷❸❹❺❻❼❽❾❿⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽①②③④⑤⑥⑦⑧⑨⑩]', '', clean)
                    clean = re.sub(r'\s+', ' ', clean).strip()
                    if len(clean) > 20:
                        current_para.append(clean)
                        
    return "\n\n".join(current_para)

def repair_short_passages():
    print("=== REPAIRING SHORT PASSAGES ===")
    
    # 1. 2011 KY-1 Passage 6 (Part B) - baa66... or 111d6c78...
    f_2011 = "111d6c78-81a1-53dc-a039-dad4c94ebd35.json"
    p_2011 = os.path.join(EXAMS_DIR, f_2011)
    if os.path.exists(p_2011):
        doc = pymupdf.open(os.path.join(BASE_KY1, "2011黄皮书真题解析（英语一）.pdf"))
        content = extract_english_from_pages(doc, 44, 52)
        if len(content) > 300:
            d = json.load(open(p_2011, encoding='utf-8'))
            d['passages'][5]['content'] = content
            with open(p_2011, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Repaired 2011 KY-1 Passage 6 ({len(content)} chars)")
            
    # 2. 2013 KY-1 Passage 4 (Text 3) - 6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json
    f_2013 = "6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json"
    p_2013 = os.path.join(EXAMS_DIR, f_2013)
    if os.path.exists(p_2013):
        doc = pymupdf.open(os.path.join(BASE_KY1, "2013黄皮书真题解析（英语一）.pdf"))
        content = extract_english_from_pages(doc, 27, 36)
        if len(content) > 300:
            d = json.load(open(p_2013, encoding='utf-8'))
            d['passages'][3]['content'] = content
            with open(p_2013, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Repaired 2013 KY-1 Passage 4 ({len(content)} chars)")
            
    # 3. 2006 KY-1 Passage 6 (Part B) - c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json
    f_2006 = "c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json"
    p_2006 = os.path.join(EXAMS_DIR, f_2006)
    if os.path.exists(p_2006):
        doc = pymupdf.open(os.path.join(BASE_KY1, "2006年考研英语真题解析.pdf"))
        content = extract_english_from_pages(doc, 46, 54)
        if len(content) > 300:
            d = json.load(open(p_2006, encoding='utf-8'))
            d['passages'][5]['content'] = content
            with open(p_2006, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Repaired 2006 KY-1 Passage 6 ({len(content)} chars)")
            
    # 4. 2005 KY-1 Passage 6 (Part B) - d8ba7d14-5305-538d-b81b-f0f7ef3db461.json
    f_2005 = "d8ba7d14-5305-538d-b81b-f0f7ef3db461.json"
    p_2005 = os.path.join(EXAMS_DIR, f_2005)
    if os.path.exists(p_2005):
        doc = pymupdf.open(os.path.join(BASE_KY1, "2005年考研英语真题解析.pdf"))
        content = extract_english_from_pages(doc, 46, 54)
        if len(content) > 300:
            d = json.load(open(p_2005, encoding='utf-8'))
            d['passages'][5]['content'] = content
            with open(p_2005, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"  ✅ Repaired 2005 KY-1 Passage 6 ({len(content)} chars)")

if __name__ == "__main__":
    repair_short_passages()
