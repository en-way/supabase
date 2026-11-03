# -*- coding: utf-8 -*-
import json
import re

with open("scripts/target_pages_ocr.txt", "r", encoding="utf-8") as f:
    target_ocr = f.read()

with open("scripts/ky2_reading_passages_raw.txt", "r", encoding="utf-8") as f:
    reading_raw = f.read()

with open("scripts/specific_pages_ocr.txt", "r", encoding="utf-8") as f:
    specific_ocr = f.read()

print("All OCR sources loaded.")
print(f"target_ocr length: {len(target_ocr)}")
print(f"reading_raw length: {len(reading_raw)}")
print(f"specific_ocr length: {len(specific_ocr)}")
