import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"
parsed_expls = json.load(open(r"d:\A16pro\Aing\antigravity\supabase\scripts\2004_cloze_parsed.json", encoding="utf-8"))

target_file = None
target_data = None
for f in glob.glob(os.path.join(exams_dir, "*.json")):
    d = json.load(open(f, encoding="utf-8"))
    if d["exam"]["year"] == 2004 and d["exam"]["category_id"] == "ky1":
        target_file = f
        target_data = d
        break

assert target_data is not None, "2004 ky1 exam file not found!"

print(f"Injecting 2004 Cloze explanations into {os.path.basename(target_file)}...")
injected_count = 0
for q in target_data["questions"]:
    so = q["sort_order"]
    if str(so) in parsed_expls:
        old_expl = q.get("explanation") or ""
        new_expl = parsed_expls[str(so)].strip()
        q["explanation"] = new_expl
        injected_count += 1
        print(f"  Q{so}: replaced placeholder ({len(old_expl)} chars) -> authentic HuangPiShu ({len(new_expl)} chars)")

with open(target_file, "w", encoding="utf-8") as fp:
    json.dump(target_data, fp, ensure_ascii=False, indent=2)

print(f"✅ Successfully injected {injected_count}/20 authentic Cloze explanations into 2004 ky1!")
