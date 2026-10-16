import sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scratch_2004_decoded.txt', encoding='utf-8').read()

# Search for answer key table or '21—25' or '21-25' or '21.'
for kw in ['21—25', '21-25', '21～25', '21~25', '26—30', '31—35', '36—40', '【答案】', '［答案］', '答案速查']:
    pos = 0
    while True:
        pos = content.find(kw, pos)
        if pos == -1: break
        print(f"Found '{kw}' at {pos}:")
        print(content[max(0, pos-40):min(len(content), pos+150)].replace('\n', ' '))
        pos += len(kw)
