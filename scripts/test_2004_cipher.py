import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

# Cipher mapping
# Look at page 1 text
raw_page1 = doc[0].get_text()

# We know:
# Many theories concerning the causes of juvenile delinquency focus either on the individual or on society as the major contributing influence.
# Let's inspect raw_page1 lines
lines = raw_page1.split('\n')
for l in lines[:25]:
    print(repr(l))
