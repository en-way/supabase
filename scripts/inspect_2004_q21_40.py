import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scratch_2004_decoded.txt', encoding='utf-8').read()

# Let's inspect where Q21 to Q40 are located in content
for q in range(21, 41):
    m = re.search(r'\n' + str(q) + r'\.([A-Za-z\u4e00-\u9fff\s\-\'\’\,\.\?\!]+)\n', content)
    if m:
        pos = m.start()
        print(f"=== Q{q} (pos {pos}) ===")
        chunk = content[pos:pos+1500]
        # Look for [A], [B], [C], [D] options
        lines = chunk.split('\n')
        header_lines = lines[:15]
        print("\n".join(header_lines))
        # Look for 正确 or 答案
        ans_match = re.search(r'(因此为正确[项|答案]|正确项[为是]|答案[为是]|故选|故[［\[]?[A-D][］\]]?为正确)[^A-D]*([A-D]|e[A-D]o)', chunk)
        if ans_match:
            print("  -> Answer hint:", ans_match.group(0))
        print("-" * 50)
