import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scratch_2004_decoded.txt', encoding='utf-8').read()
pages = content.split('<<<PAGE_')

def get_page_text(p_num):
    for p in pages:
        if p.startswith(str(p_num) + '>>>'):
            return p.split('>>>', 1)[1]
    return ""

print("=== Text 1 Pages (around P17-27) ===")
# Where does Text 1 passage appear?
for p in range(16, 28):
    t = get_page_text(p)
    if "Hunting for a job" in t or "CareerBuilder" in t:
        print(f"P{p}:")
        for line in t.split('\n'):
            if any(k in line for k in ["Hunting", "CareerBuilder", "Redman", "Zedmon", "agent"]):
                print("  ", line[:80])

print("\n=== Text 2 Pages (around P28-39) ===")
for p in range(28, 40):
    t = get_page_text(p)
    if any(k in t for k in ["alphabet", "Abbott", "Zodiac", "‘odiac"]):
        print(f"P{p}:")
        for line in t.split('\n'):
            if any(k in line for k in ["alphabet", "Abbott", "Zodiac", "‘odiac"]):
                print("  ", line[:80])

print("\n=== Text 3 Pages (around P40-48) ===")
for p in range(40, 49):
    t = get_page_text(p)
    if any(k in t for k in ["Ellen Spero", "biting her nails", "economic"]):
        print(f"P{p}:")
        for line in t.split('\n'):
            if any(k in line for k in ["Ellen Spero", "biting her nails", "economic"]):
                print("  ", line[:80])

print("\n=== Text 4 Pages (around P48-58) ===")
for p in range(48, 59):
    t = get_page_text(p)
    if any(k in t for k in ["intellect", "intelligence", "Hofstadter", "Ravitch"]):
        print(f"P{p}:")
        for line in t.split('\n'):
            if any(k in line for k in ["intellect", "intelligence", "Hofstadter", "Ravitch"]):
                print("  ", line[:80])
