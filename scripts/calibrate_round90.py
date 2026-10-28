import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 90 Calibrations ===")

# 1. 2022 ky1 Q38 & Q39
f2022 = "public/data/exams/6d676d85-a38a-5fe4-9506-31de03b648b6.json"
with open(f2022, "r", encoding="utf-8") as fp:
    d2022 = json.load(fp)

for q in d2022["questions"]:
    so = q.get("sort_order")
    if so == 38:
        for opt in q["options"]:
            if opt["key"] == "C":
                opt["text"] = "Limiting the powers of business owners."
                opt["content"] = "Limiting the powers of business owners."
                print("Calibrated 2022 ky1 Q38 Option C with terminal period.")
    elif so == 39:
        for opt in q["options"]:
            if opt["key"] == "C":
                opt["text"] = "Society sees a rise in overall well-being."
                opt["content"] = "Society sees a rise in overall well-being."
                print("Calibrated 2022 ky1 Q39 Option C with terminal period.")

with open(f2022, "w", encoding="utf-8") as fp:
    json.dump(d2022, fp, ensure_ascii=False, indent=2)

out2022 = "out/data/exams/6d676d85-a38a-5fe4-9506-31de03b648b6.json"
if os.path.exists(out2022):
    with open(out2022, "w", encoding="utf-8") as fp:
        json.dump(d2022, fp, ensure_ascii=False, indent=2)

# 2. 2018 ky1 Q22
f2018 = "public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json"
with open(f2018, "r", encoding="utf-8") as fp:
    d2018 = json.load(fp)

for q in d2018["questions"]:
    if q.get("sort_order") == 22:
        for opt in q["options"]:
            if opt["key"] == "B":
                opt["text"] = "Optimists' opinions on new tech find little support."
                opt["content"] = "Optimists' opinions on new tech find little support."
                print("Calibrated 2018 ky1 Q22 Option B with terminal period.")
            elif opt["key"] == "C":
                opt["text"] = "Issues arising from automation need to be tackled."
                opt["content"] = "Issues arising from automation need to be tackled."
                print("Calibrated 2018 ky1 Q22 Option C with terminal period.")

with open(f2018, "w", encoding="utf-8") as fp:
    json.dump(d2018, fp, ensure_ascii=False, indent=2)

out2018 = "out/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json"
if os.path.exists(out2018):
    with open(out2018, "w", encoding="utf-8") as fp:
        json.dump(d2018, fp, ensure_ascii=False, indent=2)

# 3. 2025 ky1 Q41-Q45
f2025 = "public/data/exams/c75ee9ef-ec21-5396-b3bf-4e30260d2918.json"
with open(f2025, "r", encoding="utf-8") as fp:
    d2025 = json.load(fp)

opt_f_text = "So what's the appeal of a long, sweaty day in pursuit of an elusive animal? 'It just feels bloody brilliant'..."
for q in d2025["questions"]:
    if 41 <= q.get("sort_order", 0) <= 45:
        for opt in q["options"]:
            if opt["key"] == "F":
                opt["text"] = opt_f_text
                opt["content"] = opt_f_text
                print(f"Calibrated 2025 ky1 Q{q['sort_order']} Option F with trailing ellipsis.")

with open(f2025, "w", encoding="utf-8") as fp:
    json.dump(d2025, fp, ensure_ascii=False, indent=2)

out2025 = "out/data/exams/c75ee9ef-ec21-5396-b3bf-4e30260d2918.json"
if os.path.exists(out2025):
    with open(out2025, "w", encoding="utf-8") as fp:
        json.dump(d2025, fp, ensure_ascii=False, indent=2)

print("=== Round 90 Local JSON Calibrations Complete ===")
