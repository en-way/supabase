import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = {
    2016: '666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json',
    2017: '4fd42872-4822-5786-8d16-0317051bf03d.json',
    2018: 'e95fe05a-07f4-53d1-a11f-9b636acc6469.json',
    2019: '5bcba462-0a1e-59b2-9fcb-c171d242db3b.json',
    2020: 'f56943c1-0ba8-58fe-b7d3-061352345067.json',
    2021: 'e7dfeb60-9e71-5912-8e2c-0828e345b98c.json',
    2022: '6d676d85-a38a-5fe4-9506-31de03b648b6.json',
    2023: 'b5992dc7-d0ac-56ce-8845-aa2c58675802.json',
    2024: 'f303f3fb-abfe-477f-a2e5-8dcd1ba78ef0.json',
    2025: 'c75ee9ef-ec21-5396-b3bf-4e30260d2918.json'
}
data_dir = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams'

for y in range(2016, 2026):
    fp = os.path.join(data_dir, files[y])
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f'******************** YEAR {y} ********************')
    qs = [q for q in d.get('questions', []) if q.get('sort_order') in range(41, 46)]
    p_ids = set(q.get('passage_id') for q in qs)
    print(f'Passage IDs for Q41-45: {p_ids}')
    for p in d.get('passages', []):
        if p['id'] in p_ids:
            p_title = p.get('title', '')
            p_text = p.get('text', '')
            print(f'Passage title: {p_title}, text len: {len(p_text)}')
            print('Passage preview (first 200 chars):')
            print(p_text[:200].replace('\n', ' '))
            print('Passage ending (last 150 chars):')
            print(p_text[-150:].replace('\n', ' '))
    for q in qs:
        so = q.get('sort_order')
        ans = q.get('correct_answer')
        opts = q.get('options')
        print(f'--- Q{so} (ans: {ans}) ---')
        print(f'Stem: {q.get("stem")}')
        if isinstance(opts, list):
            print(f'Options count: {len(opts)}')
            for o in opts:
                txt = o.get('text', '') if isinstance(o, dict) else str(o)
                k = o.get('key', '') if isinstance(o, dict) else ''
                print(f'  [{k}] ({len(txt)} chars): {txt[:60]}...')
        elif isinstance(opts, dict):
            print(f'Options dict keys: {list(opts.keys())}')
            for k, v in opts.items():
                print(f'  [{k}] ({len(v)} chars): {v[:60]}...')
