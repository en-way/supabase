import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

targets = [
    ("2011", 3, "public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json"),
    ("2011", 7, "public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json"),
    ("2011", 11, "public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json"),
    ("2011", 40, "public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json"),
    ("2003", 25, "public/data/exams/91ff038a-e3f9-5b6d-82c5-1328735be1d1.json"),
    ("2009", 11, "public/data/exams/9369aa41-c91e-548c-bf99-1ad46a07ac25.json"),
]

for year, qnum, path in targets:
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    for q in d.get("questions", []):
        if q.get("sort_order") == qnum:
            print(f"==================== {year} Q{qnum} ====================")
            print(f"Stem: {q.get('stem')}")
            print(f"Options: {q.get('options')}")
            print(f"Correct Ans: {q.get('correct_answer')}, Ans: {q.get('answer')}")
            print("Expl:")
            print(str(q.get("explanation"))[:600])
            print("...")
