import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Loading 2015 text...")
with open('scripts/full_2015_reading_text.txt', 'r', encoding='utf-8') as f:
    t2015 = f.read()

for q in [28, 34, 36, 37, 38]:
    print(f"\n==================== 2015 ky1 Q{q} ====================")
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*', t2015)
    if m:
        start = m.start()
        print(t2015[start:start+1200])
    else:
        print(f"Pattern for Q{q} not found")

print("\n\nLoading 2018 text...")
with open('scripts/full_2018_reading_text.txt', 'r', encoding='utf-8') as f:
    t2018 = f.read()

for q in [31, 32, 35, 36, 37, 38]:
    print(f"\n==================== 2018 ky1 Q{q} ====================")
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*', t2018)
    if m:
        start = m.start()
        print(t2018[start:start+1200])
    else:
        print(f"Pattern for Q{q} not found")
