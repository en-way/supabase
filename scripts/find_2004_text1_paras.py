import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
content = open('scratch_2004_decoded.txt', encoding='utf-8').read()

# Let's search for English paragraphs in decoded text
# Paragraphs in Huang Pi Shu 2004 start with markers like MM a, MM - a, MM v a, MMM a, etc.
# followed by English sentences.

# Let's inspect pages 16 to 27 for Text 1 English text
pages = content.split('<<<PAGE_')

print("=== Text 1 English paragraphs ===")
for p_num in range(16, 28):
    p_text = pages[p_num].split('>>>')[1] if len(pages) > p_num else ""
    # Find English text chunks with length > 100
    for line in p_text.split('\n'):
        if len(line) > 30 and re.match(r'^[A-Za-z0-9\s\.\,\-\'\"]+$', line):
            print(f"P{p_num}: {line}")
