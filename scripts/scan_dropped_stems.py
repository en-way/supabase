import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Forensic Scan: Detecting Multi-line Stems Dropped by Scrapers ===")

exam_files = sorted(glob.glob("public/data/exams/*.json"))

multi_line_stem_drops = []

for fpath in exam_files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    title = data["exam"]["title"]
    year = data["exam"]["year"]
    cat = data["exam"]["category_id"]

    for q in data["questions"]:
        so = q.get("sort_order")
        stem = q.get("stem", "").strip()
        expl = q.get("explanation", "").strip()

        if so <= 20: # cloze standard stems
            continue

        # Look in expl header (first 300 chars) for lines matching question number: e.g. "^27\." or "\n27\."
        # Extract the English stem text from expl before Chinese translation or options
        m = re.search(rf'(?:^|\n)\s*{so}\s*[\.・\、\:]\s*([^\n]+(?:\n[^\n]+){{1,4}})', expl)
        if m:
            expl_header = m.group(1).strip()
            # Clean Chinese, brackets, etc.
            lines = expl_header.split('\n')
            eng_lines = []
            for line in lines:
                l_strip = line.strip()
                # Stop if it starts with Chinese, [A], 【A】, or is just a bullet
                if re.match(r'^[\[【［]?[A-G][\]】］\.]', l_strip):
                    break
                if re.match(r'^[0-9]+\s*[\.、]', l_strip) and not l_strip.startswith(str(so)):
                    break
                # If line is mostly English
                zh_chars = len(re.findall(r'[\u4e00-\u9fa5]', l_strip))
                en_chars = len(re.findall(r'[a-zA-Z]', l_strip))
                if en_chars > 5 and zh_chars == 0:
                    eng_lines.append(l_strip)
                elif l_strip in ['・', '.', '•', '']:
                    continue
                else:
                    break
            
            full_expl_stem = " ".join(eng_lines).strip()
            # Normalize spaces
            full_expl_stem = re.sub(r'\s+', ' ', full_expl_stem)
            
            # Compare with stem
            norm_stem = re.sub(r'\s+', ' ', stem).strip()
            # Remove trailing blanks like ______ or .
            norm_stem_core = re.sub(r'[\s_\.\?]+$', '', norm_stem).strip()
            full_expl_core = re.sub(r'[\s_\.\?]+$', '', full_expl_stem).strip()

            if len(full_expl_core) > len(norm_stem_core) + 5 and norm_stem_core in full_expl_core:
                multi_line_stem_drops.append({
                    "year": year,
                    "cat": cat,
                    "so": so,
                    "current_stem": stem,
                    "recovered_stem": full_expl_stem
                })

print(f"Total dropped multi-line stems found: {len(multi_line_stem_drops)}")
for item in multi_line_stem_drops:
    print(f"[{item['year']} {item['cat']} Q{item['so']}]")
    print(f"   Current:   {repr(item['current_stem'])}")
    print(f"   Recovered: {repr(item['recovered_stem'])}")
