# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Round 26, 27, 28, 36, 37 where yr == 2013
import re
matches = re.findall(r'(\s*if yr == 2013 and cat == [\'"]ky1[\'"].*?)(?=\n\s*(?:if yr ==|passages =|total_passages|\Z))', text, re.DOTALL)
print(f"Found {len(matches)} historical 2013 ky1 check blocks:")
for idx, m in enumerate(matches):
    print(f"\n--- Block {idx+1} ---")
    print(m[:1200])
