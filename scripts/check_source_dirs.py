import fitz
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_dir_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"
cloze_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2010-2025完型真题"
reading_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题"

print("Checking available source directories and files...")
print("ky1 pdfs:", len(os.listdir(pdf_dir_ky1)))
print("ky2 pdfs:", len(os.listdir(pdf_dir_ky2)))
print("cloze dir:", os.listdir(cloze_dir))
print("reading dir:", os.listdir(reading_dir))
