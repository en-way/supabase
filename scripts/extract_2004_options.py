import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect options for all 20 questions
for q in range(1, 21):
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*(.*?)(?=本题考核)', text, re.DOTALL)
    if m:
        opts_raw = m.group(1).strip()
        opts_clean = re.sub(r'e([A-D])o', r'[\1] ', opts_raw)
        opts_clean = re.sub(r'e([A-D])', r'[\1] ', opts_clean)
        # get English options by taking [A] ... [B] ... [C] ... [D]
        opts = {}
        for opt in ['A', 'B', 'C', 'D']:
            # look for [opt] English (Chinese)
            mo = re.search(rf'\[{opt}\]\s*([a-zA-Z\s\-]+(?:\([a-zA-Z\s\-]+\))?)', opts_clean)
            if mo:
                opts[opt] = mo.group(1).strip()
        print(f"Q{q}: {opts_clean[:120]}")
