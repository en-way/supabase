import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

# Page 3 has Q1
t3 = doc[2].get_text()
print("Raw characters around Q1:")
for l in t3.split('\n')[:35]:
    print(repr(l))
