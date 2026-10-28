import json
import glob
import os

print("=== Starting Round 87 Local JSON Calibrations ===")

# 1. Calibrate 2021 ky1 Q35
f2021 = "public/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
with open(f2021, "r", encoding="utf-8") as f:
    d2021 = json.load(f)

for q in d2021.get("questions", []):
    if q.get("question_number") == 35 or q.get("sort_order") == 35:
        for opt in q.get("options", []):
            if opt.get("key") == "C":
                opt["text"] = "What made photography develop in the Victorian period?"
                opt["content"] = "What made photography develop in the Victorian period?"
            elif opt.get("key") == "D":
                opt["text"] = "How did smiling in photographs become a post-Victorian norm?"
                opt["content"] = "How did smiling in photographs become a post-Victorian norm?"
        print("Calibrated 2021 ky1 Q35 options C and D")

with open(f2021, "w", encoding="utf-8") as f:
    json.dump(d2021, f, ensure_ascii=False, indent=2)

# Also update in out/data/exams if exists
out2021 = "out/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
if os.path.exists(out2021):
    with open(out2021, "w", encoding="utf-8") as f:
        json.dump(d2021, f, ensure_ascii=False, indent=2)

# 2. Calibrate 2017 ky1 Part B Q41-Q45 options
f2017 = "public/data/exams/4fd42872-4822-5786-8d16-0317051bf03d.json"
with open(f2017, "r", encoding="utf-8") as f:
    d2017 = json.load(f)

dickens_options = [
    {
        "key": "A",
        "value": "A",
        "text": 'The first published sketch, "A Dinner at Poplar Walk", brought tears to Dickens\'s eyes when he discovered it in the pages of The Monthly Magazine.',
        "content": 'The first published sketch, "A Dinner at Poplar Walk", brought tears to Dickens\'s eyes when he discovered it in the pages of The Monthly Magazine.'
    },
    {
        "key": "B",
        "value": "B",
        "text": 'The runaway success of The Pickwick Papers, as it is generally known today, secured Dickens\'s fame.',
        "content": 'The runaway success of The Pickwick Papers, as it is generally known today, secured Dickens\'s fame.'
    },
    {
        "key": "C",
        "value": "C",
        "text": 'Soon after Sketches by Boz appeared, a publisher invited Dickens to write a story in monthly installments, as a backdrop for a series of woodcuts by the then-famous artist Robert Seymour, who had originated the idea for the story.',
        "content": 'Soon after Sketches by Boz appeared, a publisher invited Dickens to write a story in monthly installments, as a backdrop for a series of woodcuts by the then-famous artist Robert Seymour, who had originated the idea for the story.'
    },
    {
        "key": "D",
        "value": "D",
        "text": 'Charles Dickens is probably the best-known and, to many people, the greatest English novelist of the 19th century.',
        "content": 'Charles Dickens is probably the best-known and, to many people, the greatest English novelist of the 19th century.'
    },
    {
        "key": "E",
        "value": "E",
        "text": 'Soon after his father\'s release from debtor\'s prison, young Charles got a better job as an errand boy in the office of an attorney.',
        "content": 'Soon after his father\'s release from debtor\'s prison, young Charles got a better job as an errand boy in the office of an attorney.'
    },
    {
        "key": "F",
        "value": "F",
        "text": 'Dickens was born in Portsmouth, on England\'s southern coast, in 1812.',
        "content": 'Dickens was born in Portsmouth, on England\'s southern coast, in 1812.'
    },
    {
        "key": "G",
        "value": "G",
        "text": 'After Pickwick, Dickens plunged into a bleaker world.',
        "content": 'After Pickwick, Dickens plunged into a bleaker world.'
    }
]

for q in d2017.get("questions", []):
    qn = q.get("question_number") or q.get("sort_order")
    if qn and qn >= 41:
        q["options"] = [dict(opt) for opt in dickens_options]
        print(f"Calibrated 2017 ky1 Q{qn} options with Dickens paragraph summaries")

with open(f2017, "w", encoding="utf-8") as f:
    json.dump(d2017, f, ensure_ascii=False, indent=2)

out2017 = "out/data/exams/4fd42872-4822-5786-8d16-0317051bf03d.json"
if os.path.exists(out2017):
    with open(out2017, "w", encoding="utf-8") as f:
        json.dump(d2017, f, ensure_ascii=False, indent=2)

# 3. Synchronize score = points across all exams in public and out
all_files = sorted(glob.glob("public/data/exams/*.json"))
synchronized_count = 0

for ef in all_files:
    with open(ef, "r", encoding="utf-8") as f:
        data = json.load(f)
    changed = False
    for q in data.get("questions", []):
        pts = q.get("points")
        sc = q.get("score")
        if sc is None and pts is not None:
            q["score"] = pts
            changed = True
            synchronized_count += 1
        elif pts is None and sc is not None:
            q["points"] = sc
            changed = True
            synchronized_count += 1
    if changed:
        with open(ef, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        out_ef = os.path.join("out/data/exams", os.path.basename(ef))
        if os.path.exists(out_ef):
            with open(out_ef, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Synchronized score and points across {synchronized_count} questions.")
print("=== Local JSON Calibrations Complete ===")
