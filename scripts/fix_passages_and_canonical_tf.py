import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
DATA_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def fix_all():
    print("=== Fixing 5 passages with 'th&r' ===")
    
    for f in os.listdir(DATA_DIR):
        if not f.endswith('.json'):
            continue
        fp = os.path.join(DATA_DIR, f)
        with open(fp, 'r', encoding='utf-8') as fp_in:
            data = json.load(fp_in)
            
        changed = False
        for p in data.get('passages', []):
            c = p.get('content', '')
            if 'th&r' in c:
                new_c = c.replace('th&r', 'their')
                # Also clean duplicate phrase in 2018 ky1 Text 1 if present
                if 'for their jobs? robots come for their jobs?' in new_c:
                    new_c = new_c.replace('for their jobs? robots come for their jobs?', 'for their jobs?')
                p['content'] = new_c
                changed = True
                print(f"Fixed passage in {f} ({p.get('title')})")
                
        if changed:
            with open(fp, 'w', encoding='utf-8') as fp_out:
                json.dump(data, fp_out, ensure_ascii=False, indent=2)
                
    print("Passages fixed.")

if __name__ == '__main__':
    fix_all()
