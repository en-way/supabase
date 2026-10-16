import glob
import json
import os

exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"
for f in sorted(glob.glob(os.path.join(exams_dir, "*.json"))):
    data = json.load(open(f, encoding="utf-8"))
    mod = False
    for q in data["questions"]:
        for opt in q.get("options", []):
            t = opt.get("text", "")
            if "Companies1 financial" in t:
                opt["text"] = t.replace("Companies1 financial", "Companies' financial")
                mod = True
                print("Fixed Companies1 financial in", os.path.basename(f))
            if "Optimists, opinions" in t:
                opt["text"] = t.replace("Optimists, opinions", "Optimists' opinions")
                mod = True
                print("Fixed Optimists, opinions in", os.path.basename(f))
    if mod:
        with open(f, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
print("Done fixing Companies1 and Optimists,.")
