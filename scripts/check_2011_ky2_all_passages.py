import json

with open('public/data/exams/53a52573-0afc-51a4-86b6-b2f321cbe6a8.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== 2011 ky2 Passages Overview ===")
for p in d['passages']:
    so = p.get('sort_order')
    title = p.get('title')
    content = p.get('content', '')
    paras = [x for x in content.split('\n\n') if x.strip()]
    words = len(content.split())
    print(f"\nPassage {so}: {title} | {len(paras)} paras | {words} words")
    print("Opening:", paras[0][:100] if paras else 'EMPTY')
    if len(paras) > 1:
        print("Second para:", paras[1][:80])
