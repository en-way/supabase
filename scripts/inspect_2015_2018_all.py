import json
import pymupdf
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Compare 2015 ky1 questions in DB vs official answer key
f2015 = 'public/data/exams/865e5af8-24a4-58e1-bc9e-640f32d8e946.json'
d2015 = json.load(open(f2015, encoding='utf-8'))

print("=== 2015 ky1 Questions (21-40) ===")
for q in d2015['questions']:
    if 21 <= q['sort_order'] <= 40:
        so = q['sort_order']
        ans = q['correct_answer']
        expl = q['explanation']
        first_line = expl.splitlines()[0] if expl else ''
        print(f"Q{so} (Ans: {ans}): Stem: {q['stem'][:40]} | Expl len: {len(expl)} | First line: {first_line[:40]}")

f2018 = 'public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json'
d2018 = json.load(open(f2018, encoding='utf-8'))

print("\n=== 2018 ky1 Questions (21-40) ===")
for q in d2018['questions']:
    if 21 <= q['sort_order'] <= 40:
        so = q['sort_order']
        ans = q['correct_answer']
        expl = q['explanation']
        first_line = expl.splitlines()[0] if expl else ''
        print(f"Q{so} (Ans: {ans}): Stem: {q['stem'][:40]} | Expl len: {len(expl)} | First line: {first_line[:40]}")
