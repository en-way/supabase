import os
import sys
import json
import glob
import re

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def load_exam(year, cat):
    for f in glob.glob(os.path.join(exams_dir, "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        if d["exam"]["year"] == year and d["exam"]["category_id"] == cat:
            return f, d
    return None, None

print("=== Starting Round 8 Fixes Part 1 (Stems, Watermarks, 2014 Q8, 2009 Broken Spaces) ===")

# -------------------------------------------------------------
# 1. Target 1: Fix 2014 ky1 Cloze Q8 (Options, Answer, Explanation)
# -------------------------------------------------------------
f_2014, d_2014 = load_exam(2014, "ky1")
if d_2014:
    for q in d_2014["questions"]:
        if q["sort_order"] == 8:
            print("Fixing 2014 ky1 Q8...")
            q["options"] = [
                {"key": "A", "text": "genre", "value": "A"},
                {"key": "B", "text": "criterion", "value": "B"},
                {"key": "C", "text": "circumstances", "value": "C"},
                {"key": "D", "text": "functions", "value": "D"}
            ]
            q["correct_answer"] = "D"
            q["answer"] = "D"
            q["explanation"] = (
                "【考点提炼】上下文语义。\n\n"
                "【解题思路】空格句指出：适当的脑力训练（workouts）可以显著提高我们的基本认知______。由上文可知，"
                "大脑训练是应对大脑失焦的方式之一，而大脑失焦即是指大脑的退化（记忆力减退、头脑不清晰），"
                "而这些体现的都是大脑认知功能的衰退，因此脑力训练改善的应是大脑的认知功能，[D] functions符合文意。\n\n"
                "【错项排除】[A] genre指“（艺术、写作、音乐等的）类型，体裁”，不能与cognitive构成合理搭配，"
                "且“改善认知类型”不符合语义逻辑。[B] criterion与[C] circumstances分别表示“（判断、决定的）标准、准则”"
                "与“环境，情况”，但是“提高认知标准”或“改善认知环境”对大脑功能衰退均无实质帮助，故排除。"
            )
    with open(f_2014, "w", encoding="utf-8") as fp:
        json.dump(d_2014, fp, ensure_ascii=False, indent=2)
    print("✅ 2014 ky1 Q8 fixed successfully.")

# -------------------------------------------------------------
# 2. Target 2: Fix 21 Reading Stems Truncation
# -------------------------------------------------------------
stems_to_fix = {
    (2011, "ky1", 26): "When McGee announced his departure, his manner can best be described as being ________.",
    (2011, "ky1", 27): "According to Paragraph 2, senior executives' quitting may be spurred by ________.",
    (2011, "ky1", 33): "The author indicates in Paragraph 3 that earned media ________.",
    (2011, "ky1", 34): "Toyota Motor's experience is cited as an example of ________.",
    (2013, "ky1", 24): "Which of the following can be inferred from the last paragraph?",
    (2013, "ky1", 30): "The author's attitude towards what Brendon Lynch said in his blog is one of ________.",
    (2013, "ky1", 37): "On which of the following did the Justices agree, according to Paragraph 4?",
    (2013, "ky1", 38): "It can be inferred from Paragraph 5 that the Alien and Sedition Acts ________.",
    (2014, "ky1", 22): "The phrase \"to sign on\" (Line 2, Para. 2) most probably means ________.",
    (2014, "ky1", 25): "To which of the following would the author most probably agree?",
    (2014, "ky1", 32): "The critics think that the new awards will most benefit ________.",
    (2014, "ky1", 34): "According to Paragraph 4, which of the following is true of the Nobels?",
    (2014, "ky1", 36): "According to Paragraph 1, what is the author's attitude toward the AAAS's report?",
    (2015, "ky1", 23): "Which of the following is shown to be odd, according to Paragraph 4?",
    (2015, "ky1", 26): "The Supreme Court will work out whether, during an arrest, it is legitimate to ________.",
    (2015, "ky1", 27): "The author's attitude toward California's argument is one of ________.",
    (2015, "ky1", 29): "In Paragraphs 5 and 6, the author shows his concern that ________.",
    (2015, "ky1", 33): "Giovanni Parmigiani believes that the establishment of the SBoRE may ________.",
    (2015, "ky1", 34): "David Vaux holds that what Science is doing now ________.",
    (2015, "ky1", 38): "The author believes that Rebekah Brooks's defence ________.",
    (2015, "ky1", 39): "The author holds that the current collective doctrine shows ________."
}

updated_files = set()
for (yr, cat, so), canonical_stem in stems_to_fix.items():
    fpath, data = load_exam(yr, cat)
    if data:
        for q in data["questions"]:
            if q["sort_order"] == so:
                old_stem = q.get("stem")
                q["stem"] = canonical_stem
                print(f"Fixed Stem [{yr} {cat} Q{so}]: {repr(old_stem)} -> {repr(canonical_stem)}")
        with open(fpath, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
        updated_files.add(fpath)
print(f"✅ Fixed all {len(stems_to_fix)} truncated stems across {len(updated_files)} files.")

# -------------------------------------------------------------
# 3. Target 3: Clean Taobao Commercial Watermarks
# -------------------------------------------------------------
ad_pattern = re.compile(r'淘宝店铺：https://shop249445206\.taobao\.com/\s*旺旺：新一文化\s*')
for f in glob.glob(os.path.join(exams_dir, "*.json")):
    data = json.load(open(f, encoding="utf-8"))
    modified = False
    for q in data["questions"]:
        e = q.get("explanation") or ""
        if "shop249445206" in e or "淘宝" in e or "新一文化" in e:
            new_e = ad_pattern.sub("", e).strip()
            # Also clean individual watermark fragments if any
            for fragment in ["淘宝店铺：https://shop249445206.taobao.com/", "旺旺：新一文化"]:
                new_e = new_e.replace(fragment, "").strip()
            if new_e != e:
                q["explanation"] = new_e
                modified = True
                print(f"Cleaned watermark from {data['exam']['year']} {data['exam']['category_id']} Q{q['sort_order']}")
    if modified:
        with open(f, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
print("✅ Taobao watermarks cleaned from all questions.")

# -------------------------------------------------------------
# 4. Target 4: Fix 2009 ky1 Broken Space Words in Options and Stem
# -------------------------------------------------------------
f_2009, d_2009 = load_exam(2009, "ky1")
if d_2009:
    replacements = {
        "Ot h erwise": "Otherwise",
        "fundamenta l": "fundamental",
        "h ost ile": "hostile",
        "In tim e": "In time",
        "So fa r": "So far",
        "Better s ti ll": "Better still",
        "requires s ufficient": "requires sufficient",
        "libera l": "liberal"
    }
    for q in d_2009["questions"]:
        # check stem
        s = q.get("stem") or ""
        for bad, good in replacements.items():
            if bad in s:
                q["stem"] = s.replace(bad, good)
                print(f"Fixed 2009 Q{q['sort_order']} stem: {bad} -> {good}")
        # check options
        for opt in q.get("options", []):
            t = opt.get("text") or ""
            for bad, good in replacements.items():
                if bad in t:
                    opt["text"] = t.replace(bad, good)
                    print(f"Fixed 2009 Q{q['sort_order']} opt [{opt['key']}]: {bad} -> {good}")
    with open(f_2009, "w", encoding="utf-8") as fp:
        json.dump(d_2009, fp, ensure_ascii=False, indent=2)
    print("✅ 2009 ky1 broken spaces fixed.")

print("\n=== Part 1 fixes finished successfully! ===")
