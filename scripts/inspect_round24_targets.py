import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Inspecting Current State of Round 24 Target Questions ===")

# 1. 2021 ky1 Text 4 (Q36-40)
p2021 = 'public/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json'
d2021 = json.load(open(p2021, encoding='utf-8'))
print("\n--- 2021 ky1 Text 4 ---")
for q in d2021['questions']:
    so = q['sort_order']
    if so in range(36, 41):
        print(f"Q{so}: stem={repr(q['stem'])}")
        print(f"  options={[o['text'] for o in q['options']]}")
        print(f"  ans={q['correct_answer']}")
        print(f"  expl_preview={repr(q['explanation'][:100])}")

# 2. 2020 ky1 Text 4 (Q36-40)
p2020 = 'public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json'
d2020 = json.load(open(p2020, encoding='utf-8'))
print("\n--- 2020 ky1 Text 4 ---")
for q in d2020['questions']:
    so = q['sort_order']
    if so in range(36, 41):
        print(f"Q{so}: stem={repr(q['stem'])}")
        print(f"  options={[o['text'] for o in q['options']]}")
        print(f"  ans={q['correct_answer']}")
        print(f"  expl_preview={repr(q['explanation'][:100])}")

# 3. 2022 ky2 Text 4 (Q36-40)
p2022_ky2 = 'public/data/exams/cc4bf627-e456-538f-87e2-4a99ebb613ed.json'
d2022_ky2 = json.load(open(p2022_ky2, encoding='utf-8'))
print("\n--- 2022 ky2 Text 4 ---")
for q in d2022_ky2['questions']:
    so = q['sort_order']
    if so in range(36, 41):
        print(f"Q{so}: stem={repr(q['stem'])}")
        print(f"  options={[o['text'] for o in q['options']]}")
        print(f"  ans={q['correct_answer']}")
        print(f"  expl_preview={repr(q['explanation'][:100])}")

# 4. 2007 ky1 Text 3 (Q34-35)
p2007 = 'public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json'
d2007 = json.load(open(p2007, encoding='utf-8'))
print("\n--- 2007 ky1 Text 3 (Q34-35) ---")
for q in d2007['questions']:
    so = q['sort_order']
    if so in [34, 35]:
        print(f"Q{so}: stem={repr(q['stem'])}")
        print(f"  options={[o['text'] for o in q['options']]}")
        print(f"  ans={q['correct_answer']}")
        print(f"  expl={repr(q['explanation'])}")
