import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"

for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith(".pdf"):
            rel = os.path.relpath(os.path.join(root, f), base)
            print(rel)
