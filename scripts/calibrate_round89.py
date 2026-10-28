import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 89 Calibrations ===")

# 1. 2018 ky1 Q8
f2018 = "public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json"
with open(f2018, "r", encoding="utf-8") as fp:
    d2018 = json.load(fp)

q8 = next(q for q in d2018["questions"] if q.get("sort_order") == 8)
for opt in q8["options"]:
    if opt["key"] == "C":
        opt["text"] = "of"
        opt["content"] = "of"
        print("Calibrated 2018 ky1 Q8 Option C text and content to 'of'")

expl = q8["explanation"]
expl = expl.replace("[C] of......... 的", "[C] of 的")
expl = expl.replace("[C] of.........:", "[C] of:")
expl = expl.replace("in£ormation", "information")
q8["explanation"] = expl
print("Calibrated 2018 ky1 Q8 explanation (fixed of......... and information).")

with open(f2018, "w", encoding="utf-8") as fp:
    json.dump(d2018, fp, ensure_ascii=False, indent=2)

out2018 = "out/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json"
if os.path.exists(out2018):
    with open(out2018, "w", encoding="utf-8") as fp:
        json.dump(d2018, fp, ensure_ascii=False, indent=2)

# 2. 2021 ky1 Q23, Q26, Q28
f2021 = "public/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
with open(f2021, "r", encoding="utf-8") as fp:
    d2021 = json.load(fp)

for q in d2021["questions"]:
    so = q.get("sort_order")
    if so == 23:
        q["explanation"] = q["explanation"].replace("•词汇注释与难句分析・］£", "［•词汇注释与难句分析•］")
        print("Calibrated 2021 ky1 Q23 explanation header.")
    elif so == 26:
        q["explanation"] = q["explanation"].replace("ef£ect", "effect")
        print("Calibrated 2021 ky1 Q26 explanation effect.")
    elif so == 28:
        q["explanation"] = q["explanation"].replace("•词汇注释与难句分析・£", "［•词汇注释与难句分析•］")
        print("Calibrated 2021 ky1 Q28 explanation header.")

with open(f2021, "w", encoding="utf-8") as fp:
    json.dump(d2021, fp, ensure_ascii=False, indent=2)

out2021 = "out/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
if os.path.exists(out2021):
    with open(out2021, "w", encoding="utf-8") as fp:
        json.dump(d2021, fp, ensure_ascii=False, indent=2)

print("=== Round 89 Local JSON Calibrations Complete ===")
