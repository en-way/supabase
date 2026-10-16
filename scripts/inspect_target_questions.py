import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

targets = [
    ("public/data/exams/e5abf09b-e94d-5994-b944-7c5711cd4e4d.json", 26, "2010 ky1 Q26"),
    ("public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json", 40, "2012 ky1 Q40"),
    ("public/data/exams/666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json", 1, "2016 ky1 Q1"),
    ("public/data/exams/4fd42872-4822-5786-8d16-0317051bf03d.json", 14, "2017 ky1 Q14"),
    ("public/data/exams/6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json", 2, "2013 ky1 Q2"),
    ("public/data/exams/6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json", 10, "2013 ky1 Q10"),
    ("public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json", 7, "2020 ky1 Q7"),
    ("public/data/exams/2c892204-071f-5943-86be-d49bca93fe71.json", 5, "2001 ky1 Q5"),
    ("public/data/exams/d80926ab-1841-5d1f-a999-56773986c46d.json", 12, "2008 ky1 Q12"),
]

for path, qnum, label in targets:
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d.get('questions', []):
        if q.get('sort_order') == qnum:
            print(f"=== {label} (id: {q.get('id')}) ===")
            print(f"Stem: {q.get('stem')}")
            print(f"Options: {q.get('options')}")
            print(f"Correct Answer: {q.get('correct_answer')}, Answer: {q.get('answer')}")
            expl = str(q.get('explanation'))
            print(f"Expl: {expl[:180]}...\n")
