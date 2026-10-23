import json
import sys

json_path = 'public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json'
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('scripts/2013_ky2_current_summary.txt', 'w', encoding='utf-8') as out:
    out.write(f"Exam Title: {data['exam'].get('title')}\n")
    out.write(f"Exam Total Score: {data['exam'].get('total_score')}\n")
    out.write(f"Passages count: {len(data['passages'])}\n")
    for idx, p in enumerate(data['passages']):
        text = p.get('content') or p.get('text', '')
        paras = [para.strip() for para in text.split('\n\n') if para.strip()]
        words = len(text.split())
        out.write(f"\n--- Passage {idx} (ID: {p.get('id')}, Type: {p.get('section_type')}, Title: {p.get('title')}) ---\n")
        out.write(f"Paras count: {len(paras)}, Words count: {words}, Total chars: {len(text)}\n")
        for p_idx, para in enumerate(paras):
            out.write(f"  [Para {p_idx+1}] ({len(para.split())} words): {para[:80]!r} ... {para[-60:]!r}\n")

    out.write('\n' + '='*50 + '\n')
    out.write(f"Questions count: {len(data['questions'])}\n")
    for idx, q in enumerate(data['questions']):
        q_num = q.get('question_number')
        so = q.get('sort_order')
        q_type = q.get('question_type')
        stem = q.get('stem', '')
        ans = q.get('answer')
        pts = q.get('points')
        opts = q.get('options', {})
        expl = q.get('explanation') or ''
        out.write(f"\nQ[{idx+1}] so={so} num={q_num} type={q_type} pts={pts} ans={ans} expl_len={len(expl)}\n")
        out.write(f"   Stem: {stem}\n")
        if isinstance(opts, dict):
            for k, v in opts.items():
                out.write(f"     [{k}] {v}\n")
        elif isinstance(opts, list):
            for item in opts:
                out.write(f"     [{item.get('key')}] {item.get('value')}\n")
        out.write(f"   Expl: {expl[:120]}...\n")

print("Done writing scripts/2013_ky2_current_summary.txt")
