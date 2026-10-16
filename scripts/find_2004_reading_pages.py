import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

content = open('scratch_2004_decoded.txt', encoding='utf-8').read()

# Let's search for passages and questions across pages 15 to 65
pages = content.split('<<<PAGE_')

print(f"Total decoded pages: {len(pages)}")

for p in pages:
    if not p.strip(): continue
    p_num = p.split('>>>')[0]
    p_text = p.split('>>>')[1] if '>>>' in p else p
    
    # Check for text markers
    for q in [21, 25, 26, 30, 31, 35, 36, 40]:
        if f"{q}." in p_text:
            print(f"Page {p_num} contains {q}.")
            lines = [l for l in p_text.split('\n') if l.strip()]
            for idx, l in enumerate(lines):
                if f"{q}." in l:
                    print("  ", "\n   ".join(lines[max(0, idx):min(len(lines), idx+6)]))
                    break
