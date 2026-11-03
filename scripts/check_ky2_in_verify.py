import sys

with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("if yr == 2013 and cat == 'ky2':")
sys.stdout.buffer.write(text[pos:pos+2500].encode('utf-8'))
