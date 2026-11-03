# -*- coding: utf-8 -*-
"""
purify_ky1_round97_stage3.py
Third stage purification for English 1: fix remaining commas, EB] in 2021 Q13, etc.
"""

import json
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== STARTING ROUND 97 STAGE 3: KY1 COMMAS & FINAL GLYPHS ===")

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

        # 2021 Q13: EB] -> [B]
        if yr == 2021 and qn == 13:
            expl = expl.replace("[A] restored,EB] isolated.[D] controlled", "[A] restored、[B] isolated、[D] controlled ")
            expl = expl.replace("restored,EB] isolated", "restored、[B] isolated")
            expl = expl.replace("EB]", "[B]")

        # 2003 Q19
        if yr == 2003 and qn == 19:
            expl = expl.replace("plan,organize\n\n（组织）", "plan, organize（组织）")
            expl = expl.replace("plan,organize", "plan, organize")

        # 2010 Q25
        if yr == 2010 and qn == 25:
            expl = expl.replace("arts criticism,newspaper reviews", "arts criticism, newspaper reviews")
            expl = expl.replace("criticism,music criticism", "criticism, music criticism")

        # 2010 Q33
        if yr == 2010 and qn == 33:
            expl = expl.replace("interactions,through the media,channels,media", "interactions, through the media, channels, media")
            expl = expl.replace("interactions,through the media", "interactions, through the media")
            expl = expl.replace("the media,channels", "the media, channels")

        # 2010 Q40
        if yr == 2010 and qn == 40:
            expl = expl.replace("wisely,exactly", "wisely, exactly")
            expl = expl.replace("must»may,should", "must, may, should")
            expl = expl.replace("may,should", "may, should")

        # 2021 Q26
        if yr == 2021 and qn == 26:
            expl = expl.replace("to,in order to", "to, in order to")
            expl = expl.replace("Paul Ferraro,an economist", "Paul Ferraro, an economist")

        # 2021 Q27
        if yr == 2021 and qn == 27:
            expl = expl.replace("traditional,be correlated with", "traditional, be correlated with")
            expl = expl.replace("often viewed,the traditional view", "often viewed, the traditional view")

        # 2021 Q28
        if yr == 2021 and qn == 28:
            expl = expl.replace("deforestation,this program", "deforestation, this program")

        # 2018 Q30
        if yr == 2018 and qn == 30:
            expl = expl.replace("news,skills", "news, skills")

        # 2018 Q43
        if yr == 2018 and qn == 43:
            expl = expl.replace("Construction,the building", "Construction, the building")
            expl = expl.replace("construction,a building", "construction, a building")

        if expl != orig_expl:
            q["explanation"] = expl
            file_modified = True
            print(f"[{yr} KY1 Q{qn}]: Stage 3 purified.")

    if file_modified:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

print("Stage 3 purification complete!")
