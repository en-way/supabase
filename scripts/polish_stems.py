import os, sys, pymupdf, re, json, uuid

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXAMS_DIR = os.path.join(ROOT_DIR, "public", "data", "exams")

def fix_all_stems_and_polish():
    import glob
    files = glob.glob(os.path.join(EXAMS_DIR, "*.json"))
    for fp in files:
        with open(fp, 'r', encoding='utf-8') as f:
            d = json.load(f)
            
        modified = False
        year = d['exam'].get('year')
        cat = d['exam'].get('category_id')
        
        for q in d.get('questions', []):
            qnum = q['sort_order']
            stem = q.get('stem', '').strip()
            
            # 1. Part B standard stem
            if qnum >= 41 and (len(stem) < 10 or re.match(r'^[\(\[\{]?\d+[\)\]\}]?$', stem)):
                q['stem'] = f"Choose the most suitable heading or paragraph for blank [{qnum}]:"
                modified = True
                
            # 2. 2006 Q21 fix
            if year == 2006 and cat == 'ky1' and qnum == 21:
                q['stem'] = 'The word "homogenizing" (Line 2, Paragraph 1) most probably means'
                modified = True
                
            # 3. Cloze standard stems
            if qnum <= 20 and (not stem or len(stem) < 10 or stem.startswith("Question")):
                q['stem'] = f"Choose the best option for blank ({qnum}) in the passage:"
                modified = True
                
        if modified:
            with open(fp, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
                
    print("✨ All stems and Part B headings successfully polished!")

if __name__ == "__main__":
    fix_all_stems_and_polish()
