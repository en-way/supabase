import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_questions_from_text(txt_path, target_qs):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"\n==================== Parsing {txt_path} ====================")
    for q in target_qs:
        # Search for pattern: "q. "
        # Find where question starts
        patterns = [
            rf'(?:^|\n)({q}\.\s+[^\n]+(?:\n(?!\d+\.)[^\n]+)+)',
            rf'(?:^|\n)({q}．\s+[^\n]+(?:\n(?!\d+．)[^\n]+)+)',
        ]
        found = False
        for pat in patterns:
            for m in re.finditer(pat, text):
                block = m.group(1)
                if any(k in block for k in ['［精准定位］', '【精准定位】', '［命题解密］', '【命题解密】', '[A]', '【A】', 'EA']):
                    print(f"\n--- Found Q{q} Block ({len(block)} chars) ---")
                    print(block[:600])
                    print("...\n" + block[-300:])
                    print('='*50)
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"Q{q} not found with strict pattern, searching looser...")
            pos = text.find(f"{q}.")
            if pos != -1:
                print(f"Snippet at {pos}:")
                print(text[pos:pos+500])
                print('='*50)

parse_questions_from_text('scripts/full_2015_reading_text.txt', [28, 34, 36, 37, 38])
parse_questions_from_text('scripts/full_2018_reading_text.txt', [31, 32, 35, 36, 37, 38])
