import json

with open('public/data/exams/307952b3-040c-5ab4-a893-687e97d737ec.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('scripts/ky2_passages_audit.txt', 'w', encoding='utf-8') as out:
    for idx, p in enumerate(d.get('passages', [])):
        content = p.get('content', '')
        paras = content.split('\n\n')
        out.write(f"\n{'='*40} PASSAGE {idx} (id: {p.get('id')}) {'='*40}\n")
        out.write(f"Title: {p.get('title')}, Type: {p.get('type')}, P_No: {p.get('passage_number')}\n")
        out.write(f"Total Words: {len(content.split())}, Total Paras: {len(paras)}\n\n")
        for p_idx, para in enumerate(paras):
            out.write(f"--- Para {p_idx+1} ({len(para.split())} words) ---\n")
            out.write(para.strip() + "\n\n")

print("Saved passages audit.")
