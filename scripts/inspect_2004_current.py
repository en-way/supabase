import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("public/data/exams/47036de0-e57d-5ccb-9bc8-b3f86d4e6457.json", "r", encoding="utf-8") as f:
    d = json.load(f)

pas = d.get('passages', [])
print("Passages count:", len(pas))
if pas:
    p0 = pas[0]
    print(f"Passage 0 id: {p0.get('id')}, type: {p0.get('passage_type')}")
    print("Content:")
    print(p0.get('content'))

print("\n--- Questions 1 to 20 ---")
for q in d.get('questions', []):
    order = q.get('sort_order')
    if order <= 20:
        print(f"Q{order}: stem={q.get('stem')[:40]}, ans={q.get('correct_answer')}, opts={[o['text'] for o in q.get('options', [])]}")
