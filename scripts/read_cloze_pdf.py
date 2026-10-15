import os
import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"

target = None
for root, dirs, files in os.walk(base):
    for f in files:
        if "完形填空-英语（一）" in f and f.endswith(".pdf"):
            target = os.path.join(root, f)
            break

print("Found Cloze PDF:", target)
reader = pypdf.PdfReader(target)
print("Page count:", len(reader.pages))

# Search for 2005 and 2007 cloze
for i in range(len(reader.pages)):
    txt = reader.pages[i].extract_text()
    if "2005" in txt and ("smell" in txt or "nose" in txt):
        print(f"2005 Cloze on Page {i+1}")
        print(txt[:600])
        break

for i in range(len(reader.pages)):
    txt = reader.pages[i].extract_text()
    if "2007" in txt and ("colonial" in txt or "Spain" in txt or "colonies" in txt):
        print(f"2007 Cloze on Page {i+1}")
        print(txt[:600])
        break
