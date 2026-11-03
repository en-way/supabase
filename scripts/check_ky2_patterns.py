import json, glob

for p in sorted(glob.glob("public/data/exams/*.json")):
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    exam = d.get("exam", {})
    if exam.get("category_id") == "ky2" and exam.get("year") in [2010, 2011, 2012, 2013]:
        print(f"File: {p}")
        print(f"Title: {exam.get('title')}, Year: {exam.get('year')}")
        qs = d.get("questions", [])
        print(f"Questions: {len(qs)}, Q1 num={qs[0].get('question_number')}, pts={qs[0].get('points')}")
        print(f"Q1 expl: {qs[0].get('explanation')[:60]}")
        print(f"Q21 expl: {qs[20].get('explanation')[:60]}")
        print("-" * 50)
