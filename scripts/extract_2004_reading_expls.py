import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

content = open('scratch_2004_clean_decoded.txt', encoding='utf-8').read()

# Let's write regex or slice locator for each Q21-40
questions = {}
for q in range(21, 41):
    next_q = q + 1
    # Search for question header in content
    # e.g. "21. How did" or "21.How did"
    pat = rf'(?:^|\n)\s*{q}\.\s*([^\n]+)'
    m = re.search(pat, content)
    if m:
        pos = m.start()
        # Find next question or end of text
        if q in [25, 30, 35, 40]:
            # Boundary could be next text or Translation section
            if q == 25:
                # Next is Text 2 (P27)
                next_marker = re.search(r'2aYy4\s*姓氏字母排序歧视现象|Text\s*2', content[pos:])
            elif q == 30:
                # Next is Text 3 (P38)
                next_marker = re.search(r'2aYyH\s*美国经济的疲软|Text\s*3', content[pos:])
            elif q == 35:
                # Next is Text 4 (P48)
                next_marker = re.search(r'36\.\s*What\s*do|Text\s*4', content[pos:])
            elif q == 40:
                # Next is Part B / Translation
                next_marker = re.search(r'Part\s*B|第三部分|英译汉|41\.', content[pos:])
            end_pos = pos + next_marker.start() if next_marker else pos + 4000
        else:
            pat_next = rf'(?:^|\n)\s*{next_q}\.\s*([^\n]+)'
            m_next = re.search(pat_next, content[pos+50:])
            end_pos = pos + 50 + m_next.start() if m_next else pos + 4000
        
        chunk = content[pos:end_pos].strip()
        questions[q] = chunk
        print(f"Q{q}: length={len(chunk)}, header={chunk.splitlines()[0][:60]}")
    else:
        print(f"FAILED to find Q{q}")

with open("scratch_2004_reading_expls_raw.json", "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in questions.items()}, f, ensure_ascii=False, indent=2)

print("Saved scratch_2004_reading_expls_raw.json with", len(questions), "questions!")
