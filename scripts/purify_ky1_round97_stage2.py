# -*- coding: utf-8 -*-
"""
purify_ky1_round97_stage2.py
Second stage purification for English 1 (remaining [E] in Q29, commas, 2004 Q14, and OCR glyphs).
"""

import json
import glob
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== STARTING ROUND 97 STAGE 2: KY1 REFINEMENT ===")

for p in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    if d.get("exam", {}).get("category_id") != "ky1":
        continue
    yr = d.get("exam", {}).get("year")
    file_modified = False

    for q in d.get("questions", []):
        qn = q.get("question_number")
        expl = q.get("explanation", "")
        orig_expl = expl

        # 1. 2021 Q29 and 2018 Q29 [E] -> [B]
        if yr == 2021 and qn == 29:
            expl = re.sub(r'［E］\s*将第二段', '［B］将第二段', expl)
        if yr == 2018 and qn == 29:
            expl = re.sub(r'［E］\s*由前', '［B］由前', expl)

        # 2. 2004 Q14 dot-glued and words
        if yr == 2004 and qn == 14:
            expl = expl.replace("Bobisaliberal.Contrarily, his wife is a", "Bob is a liberal. Contrarily, his wife is a")
            expl = expl.replace("Bobisaliberal.", "Bob is a liberal. ")
            expl = expl.replace("stweara”acketandtie.", "st wear a jacket and tie. ")
            expl = expl.replace("stweara”acketandtie", "st wear a jacket and tie")
            expl = expl.replace("Simi-\nlarlyywomenmustwearaskir", "Similarly, women must wear a skirt")
            expl = expl.replace("Simi-\nlarlyy", "Similarly, ")
            expl = expl.replace("womenmustwearaskir", "women must wear a skirt")

        # 3. Comma missing spaces and OCR typos
        if yr == 2001 and qn == 25:
            expl = expl.replace("digital divide,BP世界上", "digital divide，即世界上")
            expl = expl.replace("[,juiu,v3S31aiz]", "[ˌjuːnɪvɜːˈsælaɪz]")
        if yr == 2001 and qn == 37:
            expl = expl.replace("disgraced,cover等", "disgraced, cover 等")
        if yr == 2022 and qn == 19:
            expl = expl.replace("A represents B,A与B为", "A represents B, A 与 B 为")
        if yr == 2003 and qn == 19:
            expl = expl.replace("plan,organize  （组织）", "plan, organize（组织）")
        if yr == 2003 and qn == 30:
            expl = expl.replace("personalities,courageous", "personalities, courageous")
        if yr == 2003 and qn == 31:
            expl = expl.replace("believe,hold,think,support等", "believe, hold, think, support 等")
        if yr == 2002 and qn == 32:
            expl = expl.replace("pump price,price of petrol", "pump price, price of petrol")
        if yr == 2002 and qn == 35:
            expl = expl.replace("effect,less dependent", "effect, less dependent")
        if yr == 2010 and qn == 6:
            expl = expl.replace("有所变化M,matter常用于it doesn't matter", "有所变化”。matter 常用于 it doesn't matter")
        if yr == 2010 and qn == 23:
            expl = expl.replace("believes,con^nds等", "believes, contends 等")

        # 4. Check any other Caret ^
        if "^" in expl:
            expl = expl.replace("con^nds", "contends")
            expl = expl.replace("feel ^Feeling", "feel / feeling")

        if expl != orig_expl:
            q["explanation"] = expl
            file_modified = True
            print(f"[{yr} KY1 Q{qn}]: Stage 2 purified.")

    if file_modified:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

print("Stage 2 purification complete!")
