import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
DATA_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def sanitize_all():
    print("=== Sanitizing OCR artifacts across all exams ===")
    count = 0
    for f in os.listdir(DATA_DIR):
        if not f.endswith('.json'):
            continue
        fp = os.path.join(DATA_DIR, f)
        with open(fp, 'r', encoding='utf-8') as fp_in:
            data = json.load(fp_in)
        
        changed = False
        for q in data.get('questions', []):
            exp = q.get('explanation')
            if exp:
                new_exp = exp
                if 'th&r' in new_exp:
                    new_exp = new_exp.replace('th&r', 'their')
                if 'o£' in new_exp:
                    new_exp = new_exp.replace('o£', 'of')
                # 44 followed by Chinese char -> “
                new_exp = re.sub(r'44([\u4e00-\u9fa5])', r'“\1', new_exp)
                if new_exp != exp:
                    q['explanation'] = new_exp
                    changed = True
                    count += 1
            # Also check options
            opts = q.get('options')
            if isinstance(opts, list):
                for o in opts:
                    txt = o.get('text', '')
                    if 'o£' in txt:
                        o['text'] = txt.replace('o£', 'of')
                        changed = True
                    if 'th&r' in txt:
                        o['text'] = txt.replace('th&r', 'their')
                        changed = True
        
        if changed:
            with open(fp, 'w', encoding='utf-8') as fp_out:
                json.dump(data, fp_out, ensure_ascii=False, indent=2)
            print(f"Sanitized: {f}")
            
    print(f"Sanitization complete! Updated {count} question explanations/options.")

if __name__ == '__main__':
    sanitize_all()
