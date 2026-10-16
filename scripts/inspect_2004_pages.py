import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect the exact passage text in scratch_2004_decoded.txt
p1 = text.split("<<<PAGE_1>>>")[1].split("<<<PAGE_2>>>")[0]
p2 = text.split("<<<PAGE_2>>>")[1].split("<<<PAGE_3>>>")[0]
p5 = text.split("<<<PAGE_5>>>")[1].split("<<<PAGE_6>>>")[0]
p6 = text.split("<<<PAGE_6>>>")[1].split("<<<PAGE_7>>>")[0]
p8 = text.split("<<<PAGE_8>>>")[1].split("<<<PAGE_9>>>")[0]
p11 = text.split("<<<PAGE_11>>>")[1].split("<<<PAGE_12>>>")[0]

print("=== P1 snippet ===")
print(p1[:500])
print("=== P6 snippet ===")
print(p6[:500])
print("=== P8 snippet ===")
print(p8[:500])
print("=== P11 snippet ===")
print(p11[:500])
