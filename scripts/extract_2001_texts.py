import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2001年真题解析及复习思路.pdf')

def extract_range(start_p, end_p, label):
    print(f"=== {label} (Pages {start_p}-{end_p}) ===")
    for p in range(start_p - 1, end_p):
        txt = doc[p].get_text()
        lines = txt.split('\n')
        for i, l in enumerate(lines):
            if any(l.strip().startswith(x) for x in ['I ', 'II ', 'III ', 'IV ', 'V ', 'VI ', 'VII ']):
                print(f"P{p+1} [{l[:40]}]")
                for k in range(1, 15):
                    if i + k < len(lines):
                        print("   ", lines[i+k])

extract_range(15, 20, "2001 Text 2")
extract_range(20, 27, "2001 Text 3")
extract_range(27, 34, "2001 Text 4")
extract_range(34, 40, "2001 Text 5")
