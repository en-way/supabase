import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

print("Auditing isolated number lines before cleaning...")

hits = []
for f in sorted(glob.glob(os.path.join(exams_dir, "*.json"))):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    for q in data["questions"]:
        so = q["sort_order"]
        e = q.get("explanation") or ""
        lines = e.split("\n")
        for i, l in enumerate(lines):
            stripped = l.strip()
            if re.match(r'^\d{1,3}$', stripped):
                prev_l = lines[i-1].strip() if i > 0 else "<START>"
                next_l = lines[i+1].strip() if i < len(lines)-1 else "<END>"
                hits.append({
                    "file": f,
                    "year": yr,
                    "cat": cat,
                    "so": so,
                    "num": int(stripped),
                    "prev": prev_l[-30:],
                    "next": next_l[:30]
                })

print(f"Total isolated number lines identified: {len(hits)}")
print("Sample 10 hits:")
for h in hits[:10]:
    print(f"  [{h['year']} {h['cat']} Q{h['so']}] {h['num']} | prev: {repr(h['prev'])} | next: {repr(h['next'])}")

# Now execute clean
cleaned_files = 0
total_removed = 0
for f in sorted(glob.glob(os.path.join(exams_dir, "*.json"))):
    data = json.load(open(f, encoding="utf-8"))
    file_modified = False
    for q in data["questions"]:
        e = q.get("explanation") or ""
        lines = e.split("\n")
        new_lines = []
        for l in lines:
            if re.match(r'^\s*\d{1,3}\s*$', l):
                total_removed += 1
                file_modified = True
            else:
                new_lines.append(l)
        if file_modified:
            # Clean consecutive empty lines created by removing the number
            clean_e = re.sub(r'\n{3,}', '\n\n', "\n".join(new_lines)).strip()
            q["explanation"] = clean_e
            
    if file_modified:
        with open(f, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
        cleaned_files += 1

print(f"\n✅ Cleaned {total_removed} isolated page number lines across {cleaned_files} exam files.")
