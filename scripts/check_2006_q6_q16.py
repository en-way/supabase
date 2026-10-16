with open('scripts/full_text_2006.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for q in [6, 16]:
    print(f"\n--- 2006 Q{q} in Yellow Book ---")
    pos = 0
    while True:
        idx = text.find(f"{q}.", pos)
        if idx == -1:
            break
        print(text[idx:idx+300])
        print('-'*30)
        pos = idx + len(f"{q}.") + 10
        if text.count(f"{q}.", 0, pos) > 3:
            break
