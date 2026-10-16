import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scratch_2004_decoded.txt', encoding='utf-8').read()

for q in [23, 26, 33, 35]:
    m = re.search(str(q) + r'\.([A-Za-z\u4e00-\u9fff\s\-\'\’\,\.\?\!]+)\n', content)
    if m:
        pos = m.start()
        print(f"=================== Q{q} ===================")
        print(content[pos:pos+1500])
