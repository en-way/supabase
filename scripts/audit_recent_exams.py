import glob
import json
import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_pdf(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

# Check 2023, 2024, 2025 ky1 and ky2
for yr in [2023, 2024, 2025]:
    for cat in ['ky1', 'ky2']:
        doc = get_pdf(yr, cat)
        print(f"\n=================== {yr} {cat} (PDF pages: {len(doc) if doc else 'None'}) ===================")
        # Find exam JSON
        exam_json = None
        for ef in glob.glob('public/data/exams/*.json'):
            d = json.load(open(ef, encoding='utf-8'))
            if d['exam']['year'] == yr and d['exam']['category_id'] == cat:
                exam_json = d
                break
        
        if not exam_json:
            print("Exam JSON not found!")
            continue
        
        # Check explanation lengths for Q1-20, Q21-40, Q41-45
        cloze_lens = [len(q.get('explanation') or '') for q in exam_json['questions'] if 1 <= q['sort_order'] <= 20]
        read_lens = [len(q.get('explanation') or '') for q in exam_json['questions'] if 21 <= q['sort_order'] <= 40]
        partb_lens = [len(q.get('explanation') or '') for q in exam_json['questions'] if 41 <= q['sort_order'] <= 45]
        
        avg_cloze = sum(cloze_lens) / len(cloze_lens) if cloze_lens else 0
        avg_read = sum(read_lens) / len(read_lens) if read_lens else 0
        avg_partb = sum(partb_lens) / len(partb_lens) if partb_lens else 0
        
        print(f"Cloze avg length: {avg_cloze:.1f}, min: {min(cloze_lens)}, max: {max(cloze_lens)}")
        print(f"Reading avg length: {avg_read:.1f}, min: {min(read_lens)}, max: {max(read_lens)}")
        print(f"Part B avg length: {avg_partb:.1f}, min: {min(partb_lens)}, max: {max(partb_lens)}")
        
        # Print a sample reading explanation from JSON
        sample_q = next((q for q in exam_json['questions'] if q['sort_order'] == 21), None)
        if sample_q:
            print(f"Sample Q21 expl (len={len(sample_q.get('explanation',''))}):")
            print((sample_q.get('explanation') or '')[:150].replace('\n', ' '))
