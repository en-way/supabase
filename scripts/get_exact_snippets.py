# -*- coding: utf-8 -*-
import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2019 ky1 Text 1 end & Text 2 start
doc19 = pymupdf.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2019黄皮书真题解析（英语一）.pdf")

print("=== 2019 Text 1 End ===")
for p in range(12, 18):
    t = doc19[p].get_text()
    if 'society has an interest' in t:
        print(f"Page {p+1}:")
        lines = t.splitlines()
        for idx, l in enumerate(lines):
            if 'society has an interest' in l or 'reminder to bankers' in l:
                print("\n".join(lines[max(0, idx-5):min(len(lines), idx+10)]))

print("\n=== 2019 Text 2 Start ===")
for p in range(16, 22):
    t = doc19[p].get_text()
    if 'Grade inflation' in t:
        print(f"Page {p+1}:")
        lines = t.splitlines()
        for idx, l in enumerate(lines):
            if 'Grade inflation' in l:
                print("\n".join(lines[max(0, idx):min(len(lines), idx+15)]))

print("\n=== 2019 Text 4 End ===")
for p in range(30, 38):
    t = doc19[p].get_text()
    if 'Small Business & Entrepreneurship' in t:
        print(f"Page {p+1}:")
        lines = t.splitlines()
        for idx, l in enumerate(lines):
            if 'Small Business & Entrepreneurship' in l:
                print("\n".join(lines[max(0, idx-5):min(len(lines), idx+10)]))

# 2. 2008 ky1 Text 3 End
doc08 = pymupdf.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2008年考研英语真题解析.pdf")
print("\n=== 2008 Text 3 End ===")
for p in range(len(doc08)):
    t = doc08[p].get_text()
    if 'Gordon says' in t and 'confident' in t:
        print(f"Page {p+1}:")
        lines = t.splitlines()
        for idx, l in enumerate(lines):
            if 'Gordon says' in l:
                print("\n".join(lines[max(0, idx-6):min(len(lines), idx+10)]))
