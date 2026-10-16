with open('scripts/full_text_2007.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for q in [4, 5, 8, 9, 10, 11, 14]:
    print(f"\n--- 2007 Q{q} in Yellow Book ---")
    pos = 0
    while True:
        idx = text.find(f"{q}.", pos)
        if idx == -1:
            break
        print(text[idx:idx+250])
        print('-'*30)
        pos = idx + len(f"{q}.") + 10
        if text.count(f"{q}.", 0, pos) > 2:
            break
