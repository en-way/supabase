import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
base = r"C:\Users\57867\Desktop\WYJ"
for root, dirs, files in os.walk(base):
    for f in files:
        if "2004" in f and f.endswith(".pdf"):
            full = os.path.join(root, f)
            print("Found PDF:", full)
