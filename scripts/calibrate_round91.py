import json
import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 91 Calibrations ===")

# Passages needing taxonomy normalization
# Target rules:
# so == 1: type = 'cloze', section_type = 'cloze'
# 2 <= so <= 5: type = 'reading', section_type = 'reading'
# so == 6:
#   if yr == 2001: type = 'reading', section_type = 'reading'
#   else: type = 'reading_part_b', section_type = 'reading'

exam_files = sorted(glob.glob("public/data/exams/*.json"))
calibrated_count = 0

for ef in exam_files:
    with open(ef, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    yr = d["exam"]["year"]
    cat = d["exam"]["category_id"]
    file_modified = False
    
    for p in d.get("passages", []):
        so = p.get("sort_order")
        pt = p.get("type")
        st = p.get("section_type")
        
        if so == 1:
            exp_pt = "cloze"
            exp_st = "cloze"
        elif 2 <= so <= 5:
            exp_pt = "reading"
            exp_st = "reading"
        elif so == 6:
            if yr == 2001:
                exp_pt = "reading"
                exp_st = "reading"
            else:
                exp_pt = "reading_part_b"
                exp_st = "reading"
        else:
            exp_pt = "reading"
            exp_st = "reading"
            
        if pt != exp_pt or st != exp_st:
            p["type"] = exp_pt
            p["section_type"] = exp_st
            file_modified = True
            calibrated_count += 1
            print(f"Calibrated [{yr} {cat} P{so}] id: {p['id']} -> type: '{exp_pt}', section_type: '{exp_st}'")
            
    if file_modified:
        with open(ef, "w", encoding="utf-8") as fp:
            json.dump(d, fp, ensure_ascii=False, indent=2)
            
        # Also sync to out/ if exists
        out_f = os.path.join("out", ef)
        if os.path.exists(out_f):
            with open(out_f, "w", encoding="utf-8") as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)

print(f"=== Round 91 Calibrations Complete: {calibrated_count} passages normalized ===")
