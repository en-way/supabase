import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Applying Round 6 Cloze & Explanation Enrichment (2020 Q8, 2005 Q1-20, 2007 Q1-20) ===")

exam_files = {}
for f in glob.glob("public/data/exams/*.json"):
    with open(f, "r", encoding="utf-8") as jf:
        data = json.load(jf)
        yr = data["exam"]["year"]
        cat = data["exam"]["category_id"]
        exam_files[(yr, cat)] = f

def get_exam(yr, cat):
    fpath = exam_files[(yr, cat)]
    with open(fpath, "r", encoding="utf-8") as f:
        return fpath, json.load(f)

def save_exam(fpath, data):
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 1. 2020 ky1 Q8 Cloze Explanation
fpath_2020, d_2020 = get_exam(2020, "ky1")
expl_2020_q8 = """8. [A] partially不完全地，部分地 [B] regularly定期地；常常地；匀称地，整齐地
[C] easily简单地；很可能；动不动 [D] initially 最初；首先
[考点提炼]句内语义+副词辨析。
[解题思路]空格所在部分and only_____ toast their bread与前两项建议并行.only暗示应控制面包加热的程度，而空格副词修饰动词toast,选项中只有副词partially能弱化"动作（toast）"的程度，表示“不完全地、在一定程度上”，[A]正确。
[错项排除][B] regularly 一方面表"频率"，另一方面表"排列整齐、美观（evenly arranged or shaped）”;[C] easily表示做某事的难易程度，两项均与“食物是否高温烹制”无关。[D] initially是时间副词，表示“在某事的最初阶段（而非中间或其他阶段）”，而先烤还是什么时候烤，均与温度高低无关。"""

for q in d_2020["questions"]:
    if q["sort_order"] == 8:
        q["explanation"] = expl_2020_q8
save_exam(fpath_2020, d_2020)
print("Updated 2020 ky1 Q8 Cloze explanation.")

# 2. 2005 ky1 Q1-20 Cloze Explanations
fpath_2005, d_2005 = get_exam(2005, "ky1")
with open("scripts/cloze_2005_extracted.json", "r", encoding="utf-8") as f:
    cloze_2005 = json.load(f)

for q in d_2005["questions"][:20]:
    so = str(q["sort_order"])
    if so in cloze_2005:
        q["explanation"] = cloze_2005[so]
save_exam(fpath_2005, d_2005)
print("Updated 2005 ky1 all 20 Cloze explanations with complete authentic Yellow Book text.")

# 3. 2007 ky1 Q1-20 Cloze Explanations
fpath_2007, d_2007 = get_exam(2007, "ky1")
with open("scripts/cloze_2007_extracted.json", "r", encoding="utf-8") as f:
    cloze_2007 = json.load(f)

for q in d_2007["questions"][:20]:
    so = str(q["sort_order"])
    if so in cloze_2007:
        q["explanation"] = cloze_2007[so]
save_exam(fpath_2007, d_2007)
print("Updated 2007 ky1 all 20 Cloze explanations with complete authentic Yellow Book text.")

print("\n--- All Cloze Enrichments Successfully Applied! ---")
