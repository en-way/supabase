import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

fpath = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json"
with open(fpath, "r", encoding="utf-8") as f:
    d = json.load(f)

vocab_replacements = {
    # Q7
    "①parenting['perantrn]n.养育，抚养\nS\n③sibling[siblin]n.兄弟姐妹\n②rule-following[rulfolaun]a.遵守规则的\nS\n④composed[kampauzd]a.镇静的，平静的，沉着的":
        "① parenting [ˈpeərəntɪŋ] n. 养育，抚养\n② rule-following [ruːl ˈfɒləʊɪŋ] adj. 遵守规则的\n③ sibling [ˈsɪblɪŋ] n. 兄弟姐妹\n④ composed [kəmˈpəʊzd] adj. 镇静的，平静的，沉着的",
    
    # Q11
    "①pushsbtoofar逼人太甚（第8题）\n④dosbgood对某人有好处\n②loseone'spatience失去耐心\nstartover从头开始\nS\n③screamatsb朝某人吼叫\nS":
        "① push sb. too far 逼人太甚\n② lose one's patience 失去耐心\n③ scream at sb. 朝某人吼叫\n④ do sb. good 对某人有好处\n• start over 从头开始",

    # Q14
    "①keepinmind记住\nS\n③self-esteem[iself1'stim]n.自尊\n②fatigue[fatig]n.疲劳，疲乏\nS":
        "① keep in mind 记住\n② fatigue [fəˈtiːɡ] n. 疲劳，疲乏\n③ self-esteem [ˌself ɪˈstiːm] n. 自尊",

    # Q17
    "①consistently[kan'sistantli]ad.一贯地；始终\nS\n③model[mbd1]o.塑造\n②inadvertently[inadv3:tntli]ad.无意地，不经意地\n④regulate[regjulet]o.调节，规定；控制":
        "① consistently [kənˈsɪstəntli] adv. 一贯地；始终\n② inadvertently [ˌɪnədˈvɜːtəntli] adv. 无意地，不经意地\n③ model [ˈmɒdl] v. 塑造\n④ regulate [ˈreɡjuleɪt] v. 调节，规定；控制",

    # Q20
    "①incredibly[inkredabli]ad.难以置信地；极其\nS\n④composed[kampauzd]a.镇静的；沉着的\n②practical['prektikl]a.实际的，务实的\nbefacedwith面对；面临\n③tothebest尽全力\nasaresultof由于；作为....的结果":
        "① incredibly [ɪnˈkredəbli] adv. 难以置信地；极其\n② practical [ˈpræktɪkl] adj. 实际的，务实的\n③ to the best 尽全力\n④ composed [kəmˈpəʊzd] adj. 镇静的；沉着的\n• be faced with 面对；面临\n• as a result of 由于；作为……的结果"
}

for q in d["questions"]:
    expl = q.get("explanation", "")
    for target, rep in vocab_replacements.items():
        if target in expl:
            q["explanation"] = expl.replace(target, rep)
            print(f"Purified vocab block in 2020 Q{q['question_number']}")

# Also clean up OCR table fragments in Q14:
# "结构切分：\n让步状\n语从句\nit's\nimportant\ntokeep inmind\nHowever,even thoughit's common,\n形式主语+系动词表语\n真正主语\nina singlemoment of fatigue\nthat youmayregretfora long time\n状语\n定语"
for q in d["questions"]:
    if q["question_number"] == 14:
        expl = q["explanation"]
        expl = re.sub(
            r"结构切分：\s*让步状\s*语从句\s*it's\s*important\s*tokeep inmind\s*However,even thoughit's common,\s*形式主语\+系动词表语\s*真正主语\s*ina singlemoment of fatigue\s*that youmayregretfora long time\s*状语\s*定语",
            "【结构切分】[However, even though it's common]（让步状语从句）, it's important to keep in mind（形式主语+系表结构，真正主语为不定式）[that in a single moment of fatigue, you can say something to your child that you may regret for a long time]（宾语从句及定语从句）。",
            expl
        )
        q["explanation"] = expl
        print("Cleaned Q14 table fragment.")

with open(fpath, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Saved 2020 vocab cleanup.")
