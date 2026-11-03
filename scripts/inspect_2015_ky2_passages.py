import json

path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\17ca33c3-66f2-5ae0-a1ba-847f507dd6e4.json'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

passages = d.get('passages', [])
for i, p in enumerate(passages):
    c = p.get('content', '')
    paras = [para.strip() for para in c.split('\n\n') if para.strip()]
    print(f"=== Passage {i}: {p.get('title')} ===")
    print(f"ID: {p.get('id')}")
    print(f"Length: {len(c)}, Paragraphs count: {len(paras)}")
    print(f"Start: {c[:150]}...")
    print(f"End: ...{c[-150:]}")
    print()
