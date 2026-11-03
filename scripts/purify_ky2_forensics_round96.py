import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams.json"
exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

with open(exams_file, "r", encoding="utf-8") as f:
    all_exams_meta = json.load(f)

ky2_map = {e.get("year"): e.get("id") for e in all_exams_meta if e.get("category_id") == "ky2"}

print("=== STARTING ROUND 96 KY2 PURIFICATION ===")

total_fixed = 0
modified_files = set()

for year, eid in sorted(ky2_map.items()):
    fpath = os.path.join(exams_dir, f"{eid}.json")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    file_modified = False
    
    # 1. Clean Questions
    for q in data.get("questions", []):
        qnum = q.get("question_number")
        old_expl = q.get("explanation", "")
        new_expl = old_expl
        
        # ---- 2021 Ky2 fixes ----
        if year == 2021:
            if qnum == 1:
                # [E] however -> [B] however
                new_expl = new_expl.replace("[E] however", "[B] however")
            elif qnum == 8:
                # [E] trained -> [B] trained
                new_expl = new_expl.replace("[E] trained", "[B] trained")
            elif qnum == 9:
                # hit® -> hit, ©If -> If
                new_expl = new_expl.replace("hit®", "hit")
                new_expl = new_expl.replace("©If", "If")
                
        # ---- 2022 Ky2 fixes ----
        if year == 2022:
            if qnum == 1:
                new_expl = new_expl.replace("［E］ normal", "［B］ normal")
            elif qnum == 4:
                new_expl = new_expl.replace("[E] strange奇怪的；异常的", "[B] strange奇怪的；异常的")
                new_expl = new_expl.replace("[E] strangewrong填入文中表示", "[B] strange / [C] wrong 填入文中表示")
            elif qnum == 7:
                # [diit3：mi'neifn] n.决心 § ②single-mindedness [isitlgl 'maindidnas]兀•专注力 〔
                new_expl = re.sub(
                    r"\[diit3：mi'neifn\]\s*n\.决心\s*§\s*②single-mindedness\s*\[isitlgl\s*'maindidnas\]兀•专注力\s*〔",
                    "[ˌdɪtɜːmɪˈneɪʃn] n. 决心；② single-mindedness [ˌsɪŋɡl ˈmaɪndɪdnəs] n. 专注力",
                    new_expl
                )
            elif qnum == 9:
                new_expl = new_expl.replace("[E]sacrifice正确", "[B] sacrifice 正确")
            elif qnum == 17:
                # :-词汇注释与难句分析•:/ © time-consuming ［'taim kan'sju：mi!］］ a.费时的 § ② supporter ［sa'poitaCr)］ n.支撑物 [398 words]
                new_expl = re.sub(
                    r":-词汇注释与难句分析•:/\s*©\s*time-consuming\s*［'taim kan'sju：mi!］］\s*a\.费时的\s*§\s*②\s*supporter\s*［sa'poitaCr\)\］\s*n\.支撑物\s*\[398 words\]",
                    "【词汇注释与难句分析】① time-consuming [ˈtaɪm kənsjuːmɪŋ] adj. 费时的；② supporter [səˈpɔːtə(r)] n. 支持者，支撑物",
                    new_expl
                )
            elif qnum == 18:
                new_expl = new_expl.replace("1& [A] duller更乏味地 [E] harder更困难地", "18. [A] duller更乏味地 [B] harder更困难地")
            elif qnum == 20:
                new_expl = new_expl.replace("[E] m turn利用中文表达", "[B] in turn 利用中文表达")
            elif qnum == 31:
                new_expl = new_expl.replace("［E］由第五段data privacy rights", "［B］由第五段 data privacy rights")
            elif qnum == 32:
                new_expl = new_expl.replace("[E] their complex designs\n［B］其复杂设计", "[B] their complex designs\n［B］其复杂设计")
                new_expl = new_expl.replace("[E] their complex designs", "[B] their complex designs")
            elif qnum == 42:
                new_expl = new_expl.replace("feel ^Feeling", "feel / feeling")
                
        # ---- 2020 Ky2 fixes ----
        if year == 2020:
            if qnum == 4:
                new_expl = new_expl.replace("[解题思路］", "［解题思路］")
            elif qnum == 11:
                new_expl = new_expl.replace("[错项排除］", "［错项排除］")
            elif qnum == 17:
                new_expl = new_expl.replace("[解题思路］", "［解题思路］")
            elif qnum == 26:
                new_expl = new_expl.replace("[命题解密］题干十正确项", "［命题解密］题干+正确项")
            elif qnum == 31:
                new_expl = new_expl.replace("[B将反对“清洁空气区”的主体", "[B] 将反对“清洁空气区”的主体")
            elif qnum == 32:
                new_expl = new_expl.replace("[命题解密］", "［命题解密］")
            elif qnum == 34:
                new_expl = new_expl.replace("[精准定位］", "［精准定位］")
            elif qnum == 39:
                new_expl = new_expl.replace("[精准定位］", "［精准定位］")
                new_expl = new_expl.replace("乙世代", "Z世代")
            elif qnum == 40:
                new_expl = new_expl.replace("[精准定位］", "［精准定位］")
            elif qnum == 43:
                new_expl = new_expl.replace("[答案］D［精解］", "［答案］D ［精解］")
            elif qnum == 45:
                new_expl = new_expl.replace("[C“调整你的互动方式”", "[C] “调整你的互动方式”")
                new_expl = new_expl.replace("［答案]", "［答案］")

        # ---- 2010 Ky2 fixes ----
        if year == 2010:
            if qnum in (41, 43, 45):
                # Ensure ［False］ is fully closed
                new_expl = new_expl.replace("故判断为［Fal", "故判断为［False］。")
                
        if new_expl != old_expl:
            q["explanation"] = new_expl
            file_modified = True
            total_fixed += 1
            print(f"Fixed {year} Q{qnum} explanation.")

    if file_modified:
        modified_files.add(fpath)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nTotal fixes applied: {total_fixed} across {len(modified_files)} exam files.")
