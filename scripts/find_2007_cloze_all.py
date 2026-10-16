import re

with open('scripts/full_text_2007.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Pages 1-8 are typically Cloze
print("--- Searching Cloze Questions in 2007 Yellow Book ---")
for q in range(1, 21):
    # Find "q." or "q．" followed by options
    pos = text.find(f"\n{q}.\n")
    if pos == -1:
        pos = text.find(f"\n{q}. [")
    if pos == -1:
        pos = text.find(f"\n{q}. ")
    if pos != -1:
        snippet = text[pos:pos+250].replace('\n', ' ')
        print(f"Q{q}: {snippet}")
    else:
        print(f"Q{q}: Not found with simple search")
