import fitz

doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf')
print("Total pages:", len(doc))
# Check if there are other PDFs in this folder!
import os, glob
pdf_dir = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）'
files = glob.glob(pdf_dir + "/**/*.pdf", recursive=True)
ky2_2014 = [f for f in files if "2014" in f and ("二" in f or "ky2" in f.lower() or "英语二" in f)]
for f in ky2_2014:
    print("Found PDF:", f)
