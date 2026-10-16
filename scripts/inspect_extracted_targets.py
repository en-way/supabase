import re

def search_questions(txt_file, q_nums):
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()

    results = {}
    for q in q_nums:
        # Match e.g. "29. According to..." or "29. "
        patterns = [
            rf"(?:^|\n)({q}\.\s+[^\n]+(?:\n(?!\d+\.)[^\n]+){{1,25}})",
            rf"(?:^|\n)({q}．\s+[^\n]+(?:\n(?!\d+．)[^\n]+){{1,25}})"
        ]
        found = []
        for pat in patterns:
            matches = re.findall(pat, content)
            if matches:
                found.extend(matches)
        results[q] = found
    return results

print("=== 2006 ky1 ===")
res2006 = search_questions('scripts/full_text_2006.txt', [26, 29, 34, 35])
for q, matches in res2006.items():
    print(f"\n--- Q{q} (Found {len(matches)} matches) ---")
    for m in matches[:2]:
        print(m.strip())
        print('-'*30)

print("\n=== 2007 ky1 ===")
res2007 = search_questions('scripts/full_text_2007.txt', [23, 26, 27, 28, 29, 32, 37, 38, 40])
for q, matches in res2007.items():
    print(f"\n--- Q{q} (Found {len(matches)} matches) ---")
    for m in matches[:2]:
        print(m.strip())
        print('-'*30)

print("\n=== 2008 ky1 ===")
res2008 = search_questions('scripts/full_text_2008.txt', [28, 29, 34, 40])
for q, matches in res2008.items():
    print(f"\n--- Q{q} (Found {len(matches)} matches) ---")
    for m in matches[:2]:
        print(m.strip())
        print('-'*30)
