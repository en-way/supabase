# -*- coding: utf-8 -*-
"""
purify_ky1_forensics_round97.py
Comprehensive forensic purification of English 1 (2001-2025: 25 exam sets).
"""

import json
import glob
import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=== STARTING ROUND 97: FORENSIC PURIFICATION OF ENGLISH 1 (2001-2025) ===")

exams = sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json"))

modified_files = set()
total_replacements = 0

for p in exams:
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    if d.get("exam", {}).get("category_id") != "ky1":
        continue
    yr = d.get("exam", {}).get("year")
    file_modified = False
    
    for q in d.get("questions", []):
        qn = q.get("question_number")
        expl = q.get("explanation", "")
        orig_expl = expl

        # ---------------------------------------------------------
        # 1. FIX [E] in Q1-Q40 (Cloze and Reading Part A)
        # ---------------------------------------------------------
        if 1 <= qn <= 40:
            if yr == 2003 and qn == 24:
                expl = expl.replace("表达过于绝对的［E］", "表达过于绝对的［B］")
            if yr == 2010 and qn == 21:
                expl = expl.replace("[E] English-language newspapers used to car", "[B] English-language newspapers used to car")
            if yr == 2010 and qn == 27:
                expl = expl.replace("[E] It involves a very big business transac", "[B] It involves a very big business transac")
            if yr == 2010 and qn == 37:
                expl = expl.replace("[E] the revival of the banking system", "[B] the revival of the banking system")
            if yr == 2012 and qn == 2:
                expl = expl.replace("[E] lest 唯恐；以免", "[B] lest 唯恐；以免")
            if yr == 2012 and qn == 3:
                expl = expl.replace("［E］ weakened （使）变弱；削弱", "［B］ weakened （使）变弱；削弱")
                expl = expl.replace("符合该逻辑的选项为［E］", "符合该逻辑的选项为［B］")
            if yr == 2015 and qn == 29:
                expl = expl.replace("［E］将第六段末句", "［B］将第六段末句")
            if yr == 2018 and qn == 23:
                expl = expl.replace("［E］对第四段①句job training断章取义", "［B］对第四段①句job training断章取义")
            if yr == 2018 and qn == 24:
                expl = expl.replace("［E］将①句所述调整税收政策的目的", "［B］将①句所述调整税收政策的目的")
            if yr == 2018 and qn == 29:
                expl = expl.replace("［E］由前  文第三段③句中bias", "［B］由前文第三段③句中bias")
                expl = expl.replace("［E］由前 文第三段③句中bias", "［B］由前文第三段③句中bias")
            if yr == 2020 and qn == 22:
                expl = expl.replace("正确项［E］是对 booby prize", "正确项［B］是对 booby prize")
                expl = expl.replace("正确项［E］是对", "正确项［B］是对")
            if yr == 2020 and qn == 29:
                expl = expl.replace("从选项［E］、［C］、［D］含有明确的方向性", "从选项［B］、［C］、［D］含有明确的方向性")
            if yr == 2021 and qn == 29:
                expl = expl.replace("［E］将第二段  ②句的reduce inequality", "［B］将第二段②句的reduce inequality")
                expl = expl.replace("［E］将第二段 ②句的reduce inequality", "［B］将第二段②句的reduce inequality")

        # ---------------------------------------------------------
        # 2. FIX 2004 CLOZE (Q1-Q20) OCR CHARACTER SHIFT & GLUED WORDS
        # ---------------------------------------------------------
        if yr == 2004 and 1 <= qn <= 20:
            replacements_2004 = [
                ("acting(on)", "acting on"),
                ("relying(on)", "relying on"),
                ("centering(on)", "centering on"),
                ("commenting(on)", "commenting on"),
                ("Many (heories", "Many theories"),
                ("focusonnT)eories1on(heindividualsuggestthatnTheoriesfocusingontheroleofsoci-",
                 "focus on... Theories [1] on the individual suggest that... Theories focusing on the role of society..."),
                ("focusonnT)eories", "focus on Theories"),
                ("Hernovelscen(eredont", "Her novel centered on"),
                ("Alcoholac(sont", "Alcohol acts on"),
                ("Sherelieson)erparentsfortuition", "She relies on her parents for tuition"),
                ("Hecommen(edonthebadweather", "He commented on the bad weather"),
                ("childrenengageincriminalbehavior", "children engage in criminal behavior"),
                ("theywerenotsufficientlypenalizedfor", "they were not sufficiently penalized for"),
                ("previousmisdeeds", "previous misdeeds"),
                ("learnedcriminalbehavior", "learned criminal behavior"),
                ("wi(hot)ers", "with others"),
                ("wi(hot", "without"),
                ("in(eractionwithot", "interaction with others"),
                ("(hroug)3", "through [3]"),
                ("(hroug)lackof", "through lack of"),
                ("heinteractionbetweenperformersandt)eiraudience", "the interaction between performers and their audience"),
                ("therapidassimilationofnewideas", "the rapid assimilation of new ideas"),
                ("hisassimila(ionintot", "his assimilation into the"),
                ("producedbythegovernmentincooperationwiththec", "produced by the government in cooperation with the"),
                ("Thedecisionwas(akena", "The decision was taken a"),
                ("tercloseconsultationwit)localresidents", "fter close consultation with local residents"),
                ("alargecollectionoftextsavailableforconsultation", "a large collection of texts available for consultation"),
                ("tin)re(urntfor)", "in return for"),
                ("tin)reply(to)", "in reply to"),
                ("tin)re“erence(to)", "in reference to"),
                ("tin)response(to)", "in response to"),
                ("in4(ot)eirfailure", "in [4] of their failure"),
                ("ot)eirfailure", "of their failure"),
                ("oulunchinre(urnforyour", "you lunch in return for your"),
                ("Iaskedheropinionybu(s", "I asked her opinion, but she"),
                ("Wi(hre", "With re"),
                ("urt)erdetails", "urther details"),
                ("Wecanno(a“fordtoignoret)eiradvice", "We cannot afford to ignore their advice"),
                ("Wecanno(a", "We cannot a"),
                ("fordtoignoret)eiradvice", "fford to ignore their advice"),
                ("Therepor(highlightedt)ema”orproblems“acingsocietytoday", "The report highlighted the major problems facing society today"),
                ("Therepor(highlightedt", "The report highlighted t"),
                ("[D] wit)", "[D] with"),
                ("On(heiradviceIappliedfort)ejob", "On their advice I applied for the job"),
                ("Thela(termaycommitcrimesinthattheylackadequate", "The latter may commit crimes in that they lack adequate"),
                ("a““ec(", "affect"),
                ("re“lec(", "reflect"),
                ("(oomuc)work", "too much work"),
                ("All(hesignspointtoasuccess", "All the signs point to a success"),
                ("ulyeara)ead", "ful year ahead"),
                ("[C] bycontras(", "[C] by contrast"),
                ("[D] a(lengt)", "[D] at length"),
                ("a(lengt", "at length"),
                ("changesintheeconomy(主语)make", "changes in the economy (主语) make"),
                ("(谓语)employment(宾语)difficulttoobtain(宾补)", "(谓语) employment (宾语) difficult to obtain (宾补)"),
                ("difficulttoobtain", "difficult to obtain"),
                ("Childreningeneralare“ondofcandy", "Children in general are fond of candy"),
                ("Onaveragewereceive5le(terseac)day", "On average we receive 5 letters each day"),
                ("r.Greenisa(aciturnperson.Bycontrastyhisbrotherwasmuc)moretalkative", "Mr. Green is a taciturn person. By contrast, his brother was much more talkative"),
                ("A(lengththeyreachedt)eirdestination", "At length they reached their destination"),
                ("Hequo(edatlengthfromt)ereport", "He quoted at length from the report"),
                ("undertake；", "undertake"),
                ("experiences(heseproblemsatsometimeint)eirlives", "experiences these problems at some time in their lives"),
                ("experiences(heseproblemsatsometimeint", "experiences these problems at some time in t"),
                ("Somes(rangecustoms", "Some strange customs"),
                ("anybirdsdidnv(survivet", "any birds didn't survive t"),
                ("accommoda(etto", "accommodate to"),
                ("(oexperiencepainrpleasure", "to experience pain or pleasure"),
                ("[A] contraril，", "[A] contrarily，"),
                ("[B] consequentl，", "[B] consequently，"),
                ("[C] similarl，", "[C] similarly，"),
                ("[D] simultaneousl，", "[D] simultaneously，"),
                ("Con(rarilyy)iswi“eisa", "Contrarily, his wife is a"),
                ("childrenarelikely(ohavelesssupervision", "children are likely to have less supervision"),
                ("at)ome", "at home"),
                ("siona(homenwhic", "sion at home, which"),
                ("hanw)at", "than what"),
                ("(hanwhat", "than what"),
                ("(hanisgoodforhishealth", "than is good for his health"),
                ("He(ookoverthegovernmentywhic", "He took over the government, which"),
                ("Sheusually(akesanapa", "She usually takes a nap a"),
                ("terlunchyasisher)abit", "fter lunch, as is her habit"),
                ("whic)", "which"),
                ("concep(", "concept"),
                ("one-paren(house)oldsortwoworkingparents", "one-parent households or two working parents"),
                ("one-paren(house)olds", "one-parent households"),
                ("(hecultural)eritageofItal，", "the cultural heritage of Italy，"),
                ("Only(hreepeopleinthephotograp)areidentifiable", "Only three people in the photograph are identifiable"),
                ("The“u(urepriceoft)e", "The future price of the"),
                ("u(urepriceoft", "uture price of the"),
                ("Zedecora(ingthe", "The decorating of the"),
                (")ousewillbeaconsiderableexpense", "house will be a considerable expense"),
                ("Thereisares(rictionagainst", "There is a restriction against"),
                ("smokinginsc)ools", "smoking in schools"),
                ("awareness)a", "awareness tha"),
                ("Agoodparliamen(arianmusthaveanawarenessofwhatthepeopleat", "A good parliamentarian must have an awareness of what the people at"),
                ("Exposureof(hebodytostrongsunlightmaybe", "Exposure of the body to strong sunlight may be"),
            ]
            for target, rep in replacements_2004:
                if target in expl:
                    expl = expl.replace(target, rep)

        # ---------------------------------------------------------
        # 3. FIX QUOTE OCR CORRUPTIONS ('w' -> '”')
        # ---------------------------------------------------------
        quote_repls = [
            ("anti-consumerismw", "anti-consumerism”"),
            ("robots)w", "robots)”"),
            ("minimum)w", "minimum)”"),
            ("began)w", "began)”"),
            ("encouraging)w", "encouraging)”"),
            ("detail)M", "detail)。”"),
            ("women)M", "women)。”"),
            ("capital)M", "capital)。”"),
            ("century)M", "century)。”"),
            ("ew ", "e” "),
            ("ow ", "o” "),
            ("aw ", "a” "),
            ("但w ", "但” "),
            ("现w ", "现” "),
            ("时w ", "时” "),
            ("以w ", "以” "),
            ("dw ", "d” "),
            ("mw ", "m” "),
            ("pw ", "p” "),
        ]
        # Only apply specific contextual quote replacements
        for qw, rep_qw in [("anti-consumerismw", "anti-consumerism”"), 
                           ("robots)w", "robots)”"), 
                           ("minimum)w", "minimum)”"), 
                           ("began)w", "began)”"), 
                           ("encouraging)w", "encouraging)”"),
                           ("detail)M", "detail)。”"),
                           ("women)M", "women)。”"),
                           ("capital)M", "capital)。”"),
                           ("century)M", "century)。”")]:
            if qw in expl:
                expl = expl.replace(qw, rep_qw)

        # ---------------------------------------------------------
        # 4. FIX CORRUPTED CIRCLED NUMBERS & WATERMARKS
        # ---------------------------------------------------------
        # Watermarks
        if "公众号：旗胜考研分享" in expl:
            expl = expl.replace("公众号：旗胜考研分享", "")
        if "公众号：旗胜考研" in expl:
            expl = expl.replace("公众号：旗胜考研", "")
            
        # Circled numbers
        if "ONeuroscientists" in expl:
            expl = expl.replace("ONeuroscientists", "② Neuroscientists")
        if "(Do" in expl:
            expl = expl.replace("(Do", "① o")
            
        # 2021 KY1 Q21 table and phonetic cleanups
        if yr == 2021 and qn == 21:
            expl = expl.replace("(Dsuccessive", "① successive")
            expl = expl.replace("©commute", "⑥ commute")
            expl = expl.replace(" [sak'sesiv] ", " [səkˈsesɪv] ")
            expl = expl.replace(" [kRmjurt] ", " [kəˈmjuːt] ")
            expl = expl.replace(" [graund] ", " [ɡraʊnd] ")
            expl = expl.replace(" nstokbraokaCr)] ", " [ˈstɒkbrəʊkə(r)] ")
            expl = expl.replace(" [bea(r)] ", " [beə(r)] ")
            expl = expl.replace(" ['iikwali] ", " [ˈiːkwəli] ")
            expl = expl.replace(" ['aigjumant] ", " [ˈɑːɡjumənt] ")
            expl = expl.replace(" ['traeveil] ", " [ˈtræveɪl] ")
            expl = expl.replace(" [,penfana(r)] ", " [ˈpenʃənə(r)] ")
            expl = expl.replace(" [in'djuaCr)] ", " [ɪnˈdjʊə(r)] ")
            expl = expl.replace(" ['sAbsidaiz] ", " [ˈsʌbsɪdaɪz] ")
            expl = expl.replace(" [1 infrastrAktJa(r)] ", " [ˈɪnfrəstrʌktʃə(r)] ")
            # strip border artifacts
            expl = expl.replace(" a.连续的；相继的 》 ", " a. 连续的；相继的\n")
            expl = expl.replace(" 根据 Z ⑧stockbroker", " 根据\n⑧ stockbroker")
            expl = expl.replace(" 承受；忍受 j ⑨equally", " 承受；忍受\n⑨ equally")
            expl = expl.replace(" 论据；理由 》 ⑩travail", " 论据；理由\n⑩ travail")
            expl = expl.replace(" 抚恤金)者 ? ⑪endure", " 抚恤金)者\n⑪ endure")
            expl = expl.replace(" 资助；补助 《 ⑫infrastructure", " 资助；补助\n⑫ infrastructure")
            expl = expl.replace("stockbrokerAcar-driving vs commuteLincolnshire vs Surrey", 
                                "stockbroker / car-driving vs commute / Lincolnshire vs Surrey")

        # ---------------------------------------------------------
        # 5. STRIP STANDALONE BOOK PAGE NUMBERS
        # ---------------------------------------------------------
        # 2011 Q1, 5, 8, 13, 14, 19
        if yr == 2011:
            if qn == 1: expl = re.sub(r'\n\s*1\s*\n\s*--- PAGE \d+ ---\s*', '', expl)
            if qn == 5: expl = re.sub(r'\n\s*2\s*\n\s*--- PAGE \d+ ---\s*', '', expl)
            if qn == 8: expl = re.sub(r'\n\s*3\s*\n\s*--- PAGE \d+ ---\s*', '', expl)
            if qn == 13: expl = re.sub(r'\n\s*4\s*\n\s*--- PAGE \d+ ---\s*', '', expl)
            if qn == 14: expl = re.sub(r'\n\s*5\s*\n\s*--- PAGE \d+ ---\s*', '', expl)
            if qn == 19: expl = re.sub(r'\n\s*6\s*$', '', expl.strip())

        # 2001 Q7, 11
        if yr == 2001 and qn in [7, 11]:
            expl = re.sub(r'\n\s*5\s*$', '', expl.strip())

        # 2002 Q23
        if yr == 2002 and qn == 23:
            expl = re.sub(r'\n\s*14\s*$', '', expl.strip())

        # 2004 Q15, 17
        if yr == 2004 and qn in [15, 17]:
            expl = re.sub(r'\n\s*1\s*\n', '\n', expl)

        # 2009 Q43
        if yr == 2009 and qn == 43:
            expl = re.sub(r'\n\s*52\s*\n', '\n', expl)

        # 2013 Q5, 8, 15, 19, 36, 37, 38, 40, 43
        if yr == 2013:
            if qn == 5: expl = re.sub(r'\n\s*2\s*\n\s*====================\s*\n', '\n', expl)
            if qn == 8: expl = re.sub(r'\n\s*3\s*\n\s*====================\s*\n', '\n', expl)
            if qn == 15: expl = re.sub(r'\n\s*5\s*\n\s*====================\s*\n', '\n', expl)
            if qn == 19: expl = re.sub(r'\n\s*6\s*\n\s*====================\s*\n', '\n', expl)
            if qn == 36: expl = re.sub(r'\n\s*40\s*\n+\s*====================\s*', '', expl)
            if qn == 37: expl = re.sub(r'\n\s*41\s*\n+\s*====================\s*', '', expl)
            if qn == 38: expl = re.sub(r'\n\s*42\s*\n+\s*====================\s*', '', expl)
            if qn == 40: expl = re.sub(r'\n\s*45\s*\n+\s*====================\s*\n7 Part B', '', expl)
            if qn == 43: expl = re.sub(r'\n\s*52\s*\n+\s*====================\s*', '', expl)

        # 2020 Q45
        if yr == 2020 and qn == 45:
            expl = re.sub(r'\n\s*48\s*$', '', expl.strip())

        # ---------------------------------------------------------
        # 6. FIX MISSING SPACES AFTER ENGLISH PUNCTUATION
        # ---------------------------------------------------------
        punct_missing_spaces = [
            ("r.Worse", "r. Worse"),
            ("r.Mc", "r. Mc"),
            ("l,social", "l, social"),
            ("s,that", "s, that"),
            ("t,leave", "t, leave"),
            ("k,disgraced", "k, disgraced"),
            ("w,This", "w, This"),
            ("o,similar", "o, similar"),
            ("e,related", "e, related"),
            ("d,publishing", "d, publishing"),
            ("s,keywords", "s, keywords"),
            ("a,the", "a, the"),
            ("d,computer", "d, computer"),
            ("w,weigh", "w, weigh"),
            ("o,also", "o, also"),
            ("w,accommodate", "w, accommodate"),
            ("s,student", "s, student"),
            ("k,sponsoring", "k, sponsoring"),
            ("e,nothing", "e, nothing"),
            ("s,friends", "s, friends"),
            ("s,middle", "s, middle"),
            ("e,news", "e, news"),
            ("s,historic", "s, historic"),
            ("t,not", "t, not"),
            ("d,a", "d, a"),
            ("e,as", "e, as"),
            ("e,appear", "e, appear"),
            ("r,no", "r, no"),
            ("s,to", "s, to"),
            ("c,c", "c, c")
        ]
        for p_old, p_new in punct_missing_spaces:
            if p_old in expl:
                expl = expl.replace(p_old, p_new)

        if expl != orig_expl:
            q["explanation"] = expl
            file_modified = True
            total_replacements += 1
            print(f"[{yr} KY1 Q{qn}]: Purified explanation.")

    if file_modified:
        modified_files.add(p)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

print(f"\nPurification complete! Modified {len(modified_files)} exam files, applied fixes across {total_replacements} questions.")
