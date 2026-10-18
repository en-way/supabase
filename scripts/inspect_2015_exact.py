import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/full_2015_reading_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for q in [28, 34, 36, 37, 38]:
    print(f"\n==================== 2015 ky1 Q{q} ====================")
    pos = text.find(f"{q}.")
    if pos != -1:
        print(text[pos:pos+1500])
        print('-'*40)
    else:
        print("Not found with dot")
