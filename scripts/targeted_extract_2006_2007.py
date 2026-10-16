import re

with open('scripts/full_text_2007.txt', 'r', encoding='utf-8') as f:
    t2007 = f.read()

for q in [23, 26, 27, 28, 29]:
    print(f"\n================ 2007 Q{q} ================")
    # Look for "q. " or "[精准定位]"
    idx = 0
    while True:
        pos = t2007.find(f"{q}.", idx)
        if pos == -1:
            break
        print(t2007[pos:pos+400])
        print('-'*40)
        idx = pos + len(f"{q}.") + 10
        if idx >= len(t2007) or t2007.count(f"{q}.", 0, idx) > 3:
            break

with open('scripts/full_text_2006.txt', 'r', encoding='utf-8') as f:
    t2006 = f.read()

for q in [26, 29, 34, 35]:
    print(f"\n================ 2006 Q{q} ================")
    idx = 0
    while True:
        pos = t2006.find(f"{q}.", idx)
        if pos == -1:
            break
        print(t2006[pos:pos+400])
        print('-'*40)
        idx = pos + len(f"{q}.") + 10
        if idx >= len(t2006) or t2006.count(f"{q}.", 0, idx) > 3:
            break
