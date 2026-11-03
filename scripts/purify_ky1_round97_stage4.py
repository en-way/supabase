import json

# 1. Fix 2010 Q39
f2010 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\e5abf09b-e94d-5994-b944-7c5711cd4e4d.json"
d2010 = json.load(open(f2010, encoding="utf-8"))
for q in d2010['questions']:
    if q['question_number'] == 39:
        expl = q['explanation']
        expl = expl.replace("Mmisinterpreted", "“misinterpreted")
        expl = expl.replace("vastly overvaluedo", "vastly overvalued。")
        q['explanation'] = expl
        print("Fixed 2010 Q39")
with open(f2010, "w", encoding="utf-8") as f:
    json.dump(d2010, f, ensure_ascii=False, indent=2)

# 2. Fix 2020 Q22 & Q45
f2020 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\f56943c1-0ba8-58fe-b7d3-061352345067.json"
d2020 = json.load(open(f2020, encoding="utf-8"))
for q in d2020['questions']:
    if q['question_number'] == 22:
        expl = q['explanation']
        expl = expl.replace("prestigioussought-after", "prestigious, sought-after")
        q['explanation'] = expl
        print("Fixed 2020 Q22")
    if q['question_number'] == 45:
        expl = q['explanation']
        expl = expl.replace("self-consciousnessanxietynegative emotions", "self-consciousness, anxiety, negative emotions")
        q['explanation'] = expl
        print("Fixed 2020 Q45")
with open(f2020, "w", encoding="utf-8") as f:
    json.dump(d2020, f, ensure_ascii=False, indent=2)

print("Stage 4 updates saved successfully.")
