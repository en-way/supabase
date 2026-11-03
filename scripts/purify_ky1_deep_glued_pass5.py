import json

# 1. 2003 Q22 in 91ff038a-e3f9-5b6d-82c5-1328735be1d1.json
f2003 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\91ff038a-e3f9-5b6d-82c5-1328735be1d1.json"
d2003 = json.load(open(f2003, encoding="utf-8"))
for q in d2003.get('questions', []):
    if q.get('question_number') == 22:
        q['explanation'] = q['explanation'].replace("vocationCspying）", "vocation (spying)）")
        print("Fixed 2003 Q22")
with open(f2003, "w", encoding="utf-8") as f:
    json.dump(d2003, f, ensure_ascii=False, indent=2)

# 2. 2002 Q26 in e1b9d134-9546-55ab-9a60-c7e5b04046a3.json
f2002 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\e1b9d134-9546-55ab-9a60-c7e5b04046a3.json"
d2002 = json.load(open(f2002, encoding="utf-8"))
for q in d2002.get('questions', []):
    if q.get('question_number') == 26:
        expl = q['explanation']
        expl = expl.replace("terminalC't3：mml］", "terminal ['t3:minl]")
        expl = expl.replace("miniaturizationEiminiatforal'zeiJan］", "miniaturization [,miniatʃərai'zeiʃn]")
        expl = expl.replace("submillimeterEsab'millimila]", "submillimeter [,sʌb'millimita]")
        q['explanation'] = expl
        print("Fixed 2002 Q26")
with open(f2002, "w", encoding="utf-8") as f:
    json.dump(d2002, f, ensure_ascii=False, indent=2)

# 3. 2021 Q11, Q23, Q26, Q28 in e7dfeb60-9e71-5912-8e2c-0828e345b98c.json
f2021 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
d2021 = json.load(open(f2021, encoding="utf-8"))
for q in d2021.get('questions', []):
    qn = q.get('question_number')
    expl = q.get('explanation', '')
    if qn == 11:
        expl = expl.replace("fluid intelligenceas the years", "fluid intelligence as the years")
        q['explanation'] = expl
        print("Fixed 2021 Q11")
    elif qn == 23:
        expl = expl.replace("crampedunreliable services>punctuated", "cramped, unreliable services, punctuated")
        q['explanation'] = expl
        print("Fixed 2021 Q23")
    elif qn == 26:
        expl = expl.replace("causalityCcausality 呼应②句", "causality（causality 呼应②句")
        q['explanation'] = expl
        print("Fixed 2021 Q26")
    elif qn == 28:
        expl = expl.replace("relationCCTsforest loss 分另I叔寸应文中的 is associated withpoverty-alleviation programAdeforestationo",
                            "relation (CCTs, forest loss) 分别对应文中的 is associated with, poverty-alleviation program, deforestation。")
        expl = expl.replace('rate of deforestation^年度）森林砍伐率”', 'rate of deforestation“（年度）森林砍伐率”')
        expl = expl.replace('[409 words]', '')
        q['explanation'] = expl
        print("Fixed 2021 Q28")
with open(f2021, "w", encoding="utf-8") as f:
    json.dump(d2021, f, ensure_ascii=False, indent=2)

print("Stage 5 fixes completed.")
