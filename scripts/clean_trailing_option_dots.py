import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

print("Cleaning trailing middle dots (・, •, ·) from options across all exams...")
cleaned_count = 0
modified_files = set()

for f in sorted(glob.glob(os.path.join(exams_dir, "*.json"))):
    data = json.load(open(f, encoding="utf-8"))
    modified = False
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    
    for q in data["questions"]:
        so = q["sort_order"]
        for opt in q.get("options", []):
            t = opt.get("text", "")
            if t.endswith("・") or t.endswith("•") or t.endswith("·"):
                # strip trailing dots and replace with standard English period if sentence
                stripped = t.rstrip("・•· ").strip()
                # If the text was a full clause/sentence or originally ended with dot
                # In HuangPiShu, Reading options with full clauses end with period.
                new_t = stripped + "." if any(w in stripped for w in [" is ", " are ", " was ", " were ", " has ", " have ", " can ", " could ", " will ", " would ", " should ", " may "]) else stripped
                print(f"[{yr} {cat} Q{so} opt {opt['key']}]: {repr(t)} -> {repr(new_t)}")
                opt["text"] = new_t
                cleaned_count += 1
                modified = True
                
    if modified:
        with open(f, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
        modified_files.add(f)

print(f"\n✅ Cleaned {cleaned_count} trailing dots across {len(modified_files)} exam files.")
