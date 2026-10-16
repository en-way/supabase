with open('scripts/full_text_2007.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "careers" or "talent" or "open (to"
pos = text.find("careers")
if pos != -1:
    print(text[pos-100:pos+300])

pos2 = text.find("open")
print("--- Search for talent / open ---")
for m in re.finditer(r'\[[A-D]\]\s*(?:open|close|related|devoted)', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 200)
    print(text[start:end])
    print('='*40)
