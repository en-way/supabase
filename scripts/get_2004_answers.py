import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scratch_2004_decoded.txt', encoding='utf-8').read()

print("=== Extracting answers for 2004 Q21-40 from explanation text ===")

cipher_map_rev = {'eAo': '[A]', 'eBo': '[B]', 'eCo': '[C]', 'eDo': '[D]'}

for q in range(21, 41):
    m = re.search(r'\n' + str(q) + r'\.([A-Za-z\u4e00-\u9fff\s\-\'\’\,\.\?\!]+)\n', content)
    if not m:
        # try without leading newline
        m = re.search(str(q) + r'\.([A-Za-z\u4e00-\u9fff\s\-\'\’\,\.\?\!]+)\n', content)
    if m:
        pos = m.start()
        # Find next question or end
        next_q = q + 1
        m_next = re.search(str(next_q) + r'\.([A-Za-z\u4e00-\u9fff\s\-\'\’\,\.\?\!]+)\n', content[pos+50:])
        end_pos = pos + 50 + m_next.start() if m_next else pos + 3000
        chunk = content[pos:end_pos]
        
        # Search for answer indicators:
        # e.g. 因此为正确项, 故...为正确, 正确答案为, 答案是
        ans_patterns = [
            r'因此[，,]?[^A-D\n]*([A-D]|e[A-D]o)[^A-D\n]*(?:为正确[项答案]|正确)',
            r'正确[项答案][为是][^A-D\n]*([A-D]|e[A-D]o)',
            r'故选[^A-D\n]*([A-D]|e[A-D]o)',
            r'故[^A-D\n]*([A-D]|e[A-D]o)[^A-D\n]*为正确',
            r'答案[为是][^A-D\n]*([A-D]|e[A-D]o)',
            r'［?([A-D])］?[是对同义改写]',
            r'([A-D]|e[A-D]o)[项]?[是对同义改写]',
            r'为本题答案[^A-D\n]*([A-D]|e[A-D]o)?',
            r'敲定[^A-D\n]*([A-D]|e[A-D]o)[^A-D\n]*为答案'
        ]
        found_ans = None
        for pat in ans_patterns:
            hit = re.search(pat, chunk)
            if hit:
                found_ans = hit.group(0)
                break
        
        print(f"Q{q}: {found_ans}")
        # also print first 300 chars of chunk
        first_lines = [l for l in chunk.split('\n') if l.strip()][:4]
        print("   " + " | ".join(first_lines))
