import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

broken_stems_to_inspect = [
    (2019, "ky1", 34),
    (2022, "ky1", 27),
    (2022, "ky1", 30),
    (2022, "ky1", 40),
    (2013, "ky1", 23),
    (2013, "ky1", 26),
    (2015, "ky1", 32),
    (2009, "ky1", 39),
    (2012, "ky1", 26),
    (2006, "ky1", 37),
    (2007, "ky1", 25),
    (2021, "ky1", 33),
    (2018, "ky1", 27),
    (2005, "ky1", 28),
]

for yr, cat, so in broken_stems_to_inspect:
    # find file
    found = False
    for f in glob.glob("public/data/exams/*.json"):
        d = json.load(open(f, encoding='utf-8'))
        if d["exam"]["year"] == yr and d["exam"]["category_id"] == cat:
            found = True
            for q in d["questions"]:
                if q["sort_order"] == so:
                    print(f"==================================================")
                    print(f"Exam: {yr} {cat} | Q{so}")
                    print(f"Current Stem: {repr(q['stem'])}")
                    print(f"Current Answer: {q['correct_answer']}")
                    print(f"Explanation Head:")
                    print(q['explanation'][:300])
                    break
            break
