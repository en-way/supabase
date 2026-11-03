import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Update 2022 KY2
p2022 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\cc4bf627-e456-538f-87e2-4a99ebb613ed.json"
with open(p2022, "r", encoding="utf-8") as f:
    d2022 = json.load(f)

for q in d2022["questions"]:
    qn = q["question_number"]
    expl = q.get("explanation", "")
    
    if qn == 8:
        expl = expl.replace("“这(让)”", "“这(it)”")
        expl = expl.replace("代n段", "代II段")
        expl = expl.replace("明u段", "明II段")
        expl = expl.replace("it( U段所述问题)", "it(II段所述问题)")
        print("2022 Q8: fixed Roman numerals and (让) -> (it)")
        
    if qn == 9:
        expl = expl.replace('"日常活动(day-to-day activities) w和', '"日常活动(day-to-day activities)”和')
        expl = re.sub(r'\n\s*4\s*\n', '\n', expl)
        print("2022 Q9: fixed w和 and removed page 4")
        
    if qn == 14:
        expl = expl.replace("activityC偶尔", "activity（偶尔")
        expl = expl.replace("间的______ o 取舍结构", "间的______。取舍结构")
        expl = re.sub(r'\n\s*5\s*\n', '\n', expl)
        print("2022 Q14: fixed activityC, period o, and removed page 5")
        
    if qn == 15:
        expl = expl.replace("have to sacrifice,have to cut down on", "have to sacrifice, have to cut down on")
        print("2022 Q15: fixed comma space")
        
    if qn == 20:
        expl = expl.replace("prioritising,spend most time on", "prioritising, spend most time on")
        expl = re.sub(r'\n\s*7\s*\n', '\n', expl)
        print("2022 Q20: fixed comma space and removed page 7")
        
    if qn == 34:
        expl = expl.replace("ensure,will not be confused or", "ensure, will not be confused or")
        print("2022 Q34: fixed comma space")
        
    q["explanation"] = expl

with open(p2022, "w", encoding="utf-8") as f:
    json.dump(d2022, f, ensure_ascii=False, indent=2)

print("Saved 2022 KY2 updates.")

# 2. Update 2020 KY2
p2020 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json"
with open(p2020, "r", encoding="utf-8") as f:
    d2020 = json.load(f)

for q in d2020["questions"]:
    qn = q["question_number"]
    expl = q.get("explanation", "")
    
    # Clean standalone page numbers
    if qn == 14:
        expl = re.sub(r'\n\s*6\s*\n+', '\n\n', expl)
    if qn == 22:
        expl = re.sub(r'\n\s*13\s*\n+', '\n\n', expl)
    if qn == 23:
        expl = re.sub(r'\n\s*15\s*\n+', '\n\n', expl)
    if qn == 24:
        expl = re.sub(r'\n\s*17\s*\n+', '\n\n', expl)
    if qn == 26:
        expl = re.sub(r'\n\s*21\s*\n+', '\n\n', expl)
    if qn == 33:
        expl = re.sub(r'\n\s*34\s*\n+', '\n\n', expl)
    if qn == 34:
        expl = re.sub(r'\n\s*36\s*\n+', '\n\n', expl)
    if qn == 38:
        expl = re.sub(r'\n\s*42\s*\n+', '\n\n', expl)

    # Specific phrase cleanups
    repls = [
        ("say somethingthat", "say something that"),
        ("oneofthemost important of alllife's", "one of the most important of all life's"),
        ("oneofthemost", "one of the most"),
        ("alllife's", "all life's"),
        (".OWe are all becoming", ". ② We are all becoming"),
        ("allthroughout life.In fact", "all throughout life. In fact"),
        ("allthroughout life", "all throughout life"),
        ("life.In fact", "life. In fact"),
        ("However,even though it's common,it's important tokeep", "However, even though it's common, it's important to keep"),
        ("However,even though", "However, even though"),
        ("common,it's", "common, it's"),
        ("tokeep in mind", "to keep in mind"),
        ("kids,then you are inadvertently", "kids, then you are inadvertently"),
        ("days.The robot rats were quite", "days. The robot rats were quite"),
        ("days.The", "days. The"),
        ("During the experiment,the social robot rat", "During the experiment, the social robot rat"),
        ("experiment,the", "experiment, the"),
        ("theasocial robot", "the asocial robot"),
        ("theasocial", "the asocial"),
        ("by pressing a lever.Across 18 trials each,the living", "by pressing a lever. Across 18 trials each, the living"),
        ("lever.Across", "lever. Across"),
        ("trials each,the", "trials each, the"),
        ("trialseach", "trials each"),
        ("than the asocial one.This suggests", "than the asocial one. This suggests"),
        ("asocial one.This", "asocial one. This"),
        ("earlier,and", "earlier, and"),
        ("trapped,she says", "trapped, she says"),
        ("says Quinn.The rats may have", "says Quinn. The rats may have"),
        ("Quinn.The", "Quinn. The"),
        ("exploring and playing.This could lead", "exploring and playing. This could lead"),
        ("playing.This", "playing. This"),
        ("given its minimal design.The", "given its minimal design. The"),
        ("design.The", "design. The"),
        ("itsminimal", "its minimal"),
        ("tail,facial features,and", "tail, facial features, and"),
        ("tail,facial", "tail, facial"),
        ("features,and", "features, and"),
        ("realrat,but that", "real rat, but that"),
        ("realrat", "real rat"),
        ("says Wiles.Similarly,children tend to", "says Wiles. Similarly, children tend to"),
        ("Wiles.Similarly", "Wiles. Similarly"),
        ("Similarly,children", "Similarly, children"),
        ("fellow beings,even when they display", "fellow beings, even when they display"),
        ("beings,even", "beings, even"),
        ("fascinatedby robots", "fascinated by robots"),
        ("fascinatedby", "fascinated by"),
        ("We'dassumed...butthatwasn'tnecessary", "We'd assumed... but that wasn't necessary"),
        ("butthatwasn'tnecessary", "but that wasn't necessary"),
        ("can be significant.Thenthere'sthefactthat", "can be significant. Then there's the fact that"),
        ("significant.Then there", "significant. Then there"),
        ("Thenthere'sthefactthat", "Then there's the fact that"),
        ("number of countries.To lead in that system requires", "number of countries. To lead in that system requires"),
        ("countries.To lead", "countries. To lead"),
        ("fairly mind-boggling.Plus,", "fairly mind-boggling. Plus,"),
        ("mind-boggling.Plus", "mind-boggling. Plus"),
        ("ever before,with supply chains spread", "ever before, with supply chains spread"),
        ("before,with", "before, with"),
        ("one way or another.Beyond this, major", "one way or another. Beyond this, major"),
        ("another.Beyond", "another. Beyond"),
        ("companies,one way or another", "companies, one way or another"),
        ("tradeinthem.They also need", "trade in them. They also need"),
        ("tradeinthem", "trade in them"),
        ("thecosts ofcleaningthe air on toindividual drivers", "the costs of cleaning the air on to individual drivers"),
        ("ofcleaningthe", "of cleaning the"),
        ("toindividual", "to individual"),
        ("Among other weaknesses,the measures", "Among other weaknesses, the measures"),
        ("weaknesses,the", "weaknesses, the"),
        ("practical and cautious.According to the", "practical and cautious. According to the"),
        ("cautious.According", "cautious. According"),
        ("tothe career", "to the career"),
        ("economic pragmatists.Despite", "economic pragmatists. Despite"),
        ("pragmatists.Despite", "pragmatists. Despite"),
        ("savings or both.They aren't", "savings or both. They aren't"),
        ("both.They", "both. They"),
        ("any chances.The booming economy", "any chances. The booming economy"),
        ("chances.The", "chances. The"),
        ("who study them,Generation Zs", "who study them, Generation Zs"),
        ("them,Generation", "them, Generation"),
        ("of anxious urgency,especially for those", "of anxious urgency, especially for those"),
        ("urgency,especially", "urgency, especially"),
        ("$1.5trillion,according to the Federal", "$1.5 trillion, according to the Federal"),
        ("$1.5trillion", "$1.5 trillion"),
        ("trillion,according", "trillion, according"),
        ("balancesin the U.S.", "balances in the U.S."),
        ("balancesin", "balances in"),
        ("sense of being dedicatedto a cause", "sense of being dedicated to a cause"),
        ("dedicatedto", "dedicated to"),
        ("Just as important asbeinghonest is", "Just as important as being honest is"),
        ("asbeinghonest", "as being honest"),
    ]
    
    for old_s, new_s in repls:
        if old_s in expl:
            expl = expl.replace(old_s, new_s)
            
    q["explanation"] = expl

with open(p2020, "w", encoding="utf-8") as f:
    json.dump(d2020, f, ensure_ascii=False, indent=2)

print("Saved 2020 KY2 updates Stage 2.")
