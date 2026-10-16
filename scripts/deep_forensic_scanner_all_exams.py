import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def scan_all():
    files = sorted([f for f in os.listdir(data_dir) if f.endswith('.json')])
    print(f"Total exam files to scan: {len(files)}")
    
    findings = []
    
    for f in files:
        fp = os.path.join(data_dir, f)
        with open(fp, 'r', encoding='utf-8') as fp_in:
            d = json.load(fp_in)
        
        exam = d.get('exam', d)
        cat = exam.get('category_id') or d.get('category_id')
        yr = exam.get('year') or d.get('year')
        exam_title = f"{yr} {cat}"
        
        questions = d.get('questions', [])
        
        # 1. Check duplicate options across questions
        opt_map = {}
        for q in questions:
            so = q.get('sort_order')
            opts = q.get('options')
            if isinstance(opts, list):
                # list of dicts with text
                opt_texts = tuple(sorted([str(o.get('text', '')).strip() for o in opts]))
            elif isinstance(opts, dict):
                opt_texts = tuple(sorted([str(v).strip() for v in opts.values()]))
            else:
                opt_texts = None
            
            if opt_texts and len(opt_texts) > 1 and all(len(t) > 3 for t in opt_texts):
                if opt_texts in opt_map:
                    prev_q = opt_map[opt_texts]
                    findings.append({
                        'exam': exam_title,
                        'file': f,
                        'type': 'DUPLICATE_OPTIONS',
                        'q': so,
                        'detail': f"Q{so} has exact duplicate options of Q{prev_q}: {opt_texts[:2]}..."
                    })
                else:
                    opt_map[opt_texts] = so

        # 2. Check each question for specific anomalies
        for q in questions:
            so = q.get('sort_order')
            stem = (q.get('stem') or '').strip()
            ans = q.get('correct_answer')
            alt_ans = q.get('answer')
            opts = q.get('options')
            exp = q.get('explanation') or ''
            
            # Answer consistency
            if ans and alt_ans and ans != alt_ans:
                findings.append({
                    'exam': exam_title,
                    'file': f,
                    'type': 'ANSWER_MISMATCH',
                    'q': so,
                    'detail': f"correct_answer='{ans}' != answer='{alt_ans}'"
                })
            
            # Suspicious stem ending (truncation)
            # e.g., ending with 'in', 'on', 'at', 'that', 'the', 'was', 'were', 'would', 'could', 'because', 'to'
            # Note: ignore standard Part B prompts like "fits into gap (41):"
            if so not in range(41, 46):
                words = re.findall(r'\b\w+\b', stem)
                if words:
                    last_word = words[-1].lower()
                    if last_word in ['in', 'the', 'that', 'was', 'were', 'would', 'could', 'because', 'with', 'about', 'from', 'of', 'and', 'or', 'to'] and not stem.endswith('.'):
                        findings.append({
                            'exam': exam_title,
                            'file': f,
                            'type': 'STEM_TRUNCATION',
                            'q': so,
                            'detail': f"Stem ends abruptly with '{words[-1]}': {repr(stem[-40:])}"
                        })

            # Check special OCR artifacts: o£, th&r, 44...
            all_text = stem + " " + exp
            if isinstance(opts, list):
                for o in opts:
                    all_text += " " + str(o.get('text', ''))
            elif isinstance(opts, dict):
                for v in opts.values():
                    all_text += " " + str(v)
            
            if 'o£' in all_text:
                findings.append({
                    'exam': exam_title,
                    'file': f,
                    'type': 'OCR_CORRUPTION',
                    'q': so,
                    'detail': "Contains 'o£' symbol (OCR error for 'of')"
                })
            
            if 'th&r' in all_text:
                findings.append({
                    'exam': exam_title,
                    'file': f,
                    'type': 'OCR_CORRUPTION',
                    'q': so,
                    'detail': "Contains 'th&r' (OCR error for 'their')"
                })
                
            if '44' in stem or (isinstance(opts, list) and any('44' in str(o.get('text', '')) for o in opts)):
                # Check if 44 is used as quote
                if re.search(r'44[a-zA-Z]', all_text) or re.search(r'\s44', all_text):
                    findings.append({
                        'exam': exam_title,
                        'file': f,
                        'type': 'OCR_QUOTE_CORRUPTION',
                        'q': so,
                        'detail': "Contains '44' used in place of quotation mark"
                    })

            # Watermark check
            wm = re.findall(r'(?:淘宝|旺旺|店主|微信|QQ|店铺|购买|正版|盗版)', all_text)
            if wm:
                findings.append({
                    'exam': exam_title,
                    'file': f,
                    'type': 'WATERMARK',
                    'q': so,
                    'detail': f"Contains watermark keywords: {set(wm)}"
                })

    print(f"\nScan complete! Found {len(findings)} anomalies across all exams:")
    for fn in findings:
        print(f"[{fn['type']}] {fn['exam']} Q{fn['q']}: {fn['detail']}")

    return findings

if __name__ == '__main__':
    scan_all()
