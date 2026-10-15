import json
import glob
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Round 3 Comprehensive Calibration (Explanations, Options Sorting, and Parity)...")

# Exact extracted Huangpi text for the 4 severely corrupted questions:

EXPL_2021_KY1_Q18 = """18. [A] well-being 健康；福祉 
[B] process 过程；进展
[C] formation 形成；构造 
[D] coordination 协作；配合
[考点提炼]句内因果逻辑链+上下文语义+固定搭配。
[解题思路]空格句中以to... in order to...构建因果目的链：采取措施→减少腹部脂肪，保持肌肉量→维护自身的身心______ 。联系贯穿全文的主旨“减少腹部脂肪、增加肌肉量可延缓流体智力衰退”，可知空格词意在说明“采取措施”的根本目的(维护身心健康：减少脂肪，保持肌肉，延缓流体智力衰退)。physical and mental health/well-being 为固定搭配，表示"身心健康",[A] well-being 正确。
[错项排除][B] process与[C] formation分别指向事物的“发展”和“形成”过程，而文中的建议对象为“中老年人”，身心状态已趋向成熟和稳定，且“形成”“发展”等变化过程通常不与protect以及physical and mental搭配。[D] coordination强调"各部分形成一个整体共同运作"，而文中both"两者都"表明此处仍将“生理的______”和“心理的______ "看作彼此独立的部分，且上下文中并未涉及“身心的协调”。"""

EXPL_2002_KY1_Q9 = """9. [A] indeed实际上，确实 [B] hence因此，所以 [C] however然而 [D] therefore因此
[试题考点]逻辑关系
[解题思路]上段⑤⑥句指出，并非所有人都能正确看待16-19世纪通信革命发展的情况。本句指出，人们普遍认同20世纪初计算机的出现极大地改变了该进程。Not everyone see... in perspective VS It is generally recognized that... 20th century形成鲜明反差；同时，空格句说明，20世纪计算机的出现从根本上改变了 19世纪通信革命的进程，暗示虽然19世纪传媒革命加速发展，但其影响力都不及 20世纪的计算机，其出现体现了通信手段革命性的转折。因此，空格处只能填入转折逻辑词，[C] however符合题意。
[错项排除][A] indeed传达“递进”逻辑，强调与上文之间的统一顺承关系，不符合题意。[B] hence与[D] therefore均表示因果关系，区别是hence除了表示“因此”还有“此后”的意思，并且hence前后一般不用逗号隔开。
[技巧补充]当逻辑关系词以插入形式进行考查时，应注意许多逻辑词较少以插入语形式出现，因此正确项常出自however和therefore两词，两者既可位于句首，也可位于句中或句尾，必须重点关注。"""

EXPL_2003_KY1_Q2 = """2. 
[A] strengthen 加强，巩固 
[B] accommodate 适应，顺应
[C] stimulate 刺激，激励，激发 
[D] enhance 提高，增强，增进
[试题考点]动宾搭配
[解题思路]空格处主语线索为they,指代“青少年”，宾语线索为such changes,指代①句“青少年身心变化"，空格处表示青少年对这些变化所做出的动作。从①②句need to,also need to传递出的"建议基调”可知，空格处应为积极、正面的动作。另外从下文④句可知这些变化实际上对于青少年而言是“全新而艰巨的挑战”，而这些挑战又是必须经历的客观事实，所以青少年只能调整自身去“适应、顺应",accommodate在此意为“改变自身行为以更好地应对新情况”，符合文意，[B]项为正确答案。
[错项排除]strengthen意为“增强、加固”(感情、联系、实力等);stimulate意为“刺激、促进”，宾语通常为“经济增长”等；enhance意为“提高、增加”，通常与reputation、value等抽象概念搭配，均不符合“顺应生理与身心变化”的语境，故排除。"""

EXPL_2022_KY1_Q34 = """34. What does the author say about CAVS?
34.关于高级视觉研究中心，作者说了什么？
[A] It was headed alternately by artists and scientists.
[A]它由艺术家和科学家交替负责。
[B] It exemplified valuable art-science alliances.
[B]它体现了有价值的艺术和科学联盟。
[C] Its projects aimed at advancing visual studies.
[C]它的项目旨在推动视觉研究的发展。
[D] Its founders sought to raise the status of artists.
[D]它的创始人试图提高艺术家的地位。

【答案锁定】B
1. 定位：由题干信息CAVS可定位至第五段(CAVS)。
2. 分析：第五段①句点明麻省理工学院设立高级视觉研究中心(CAVS)的初衷“探索科技在人文艺术中的作用”，②③句揭示该中心促成科艺合作的关键因素“以双方的兴趣/利益共同点为基础”，④句补充指出该中心一直坚持与时俱进，谋求科学与艺术的深度融合。结合第四段末两句“最有价值的科艺合作是双方都有共同的利益关系，能够共同参与项目设计并评判彼此成果”可判断,作者高度认可CAVS的做法，认为它是有价值的科艺联盟之典范。
3. 确定：选项 It exemplified valuable art-science alliances 既体现了作者对 CAVS 的高度认可，又明确了第五段与第四段末两句之间的“观点/论点一例子/论据”关联，[B]正确。

【排除干扰】
[A] 定位至第五段④句，选项将该句所述“一流的科学家和艺术家突破各自专业边界，成为复合型人才”曲解为“艺术家和科学家轮流接管项目”。
[C] 定位至第五段②句，选项将该句所述“项目组有意将光作为研究重点”断章取义为“旨在推动视觉研究的发展”，而下文明确其意在促成科艺合作。
[D] 定位至第五段②③句，选项利用段中个别词汇捏造出“创始人试图提高艺术家的地位”，文中并未提及相关信息。

【技巧总结】本题针对事例细节设题，解题关键在于抓住段中的关键信息，结合上下文明确事例的论点，能与之对应的选项即为正确项。综上可知，该段重在展现CAVS是如何促成科学与艺术达成合作共赢的，为“有价值的科艺联盟”的正面例证，B项与之对应。"""

def get_option_sort_key(opt_key, total_count):
    if total_count == 2 and opt_key in ('T', 'F'):
        return 0 if opt_key == 'T' else 1
    alpha_order = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    return alpha_order.get(opt_key, 99)

exams_dir = 'public/data/exams'
total_opts_sorted = 0
total_expls_fixed = 0
unclosed_bolds_fixed = 0
files_modified = 0

for filepath in sorted(glob.glob(os.path.join(exams_dir, '*.json'))):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    exam = data.get('exam', {})
    yr = exam.get('year')
    cat = exam.get('category_id')
    file_changed = False
    
    for q in data.get('questions', []):
        so = q.get('sort_order')
        
        # 1. Normalize and sort options
        opts = q.get('options', [])
        if opts:
            keys = [o.get('key') for o in opts]
            sorted_opts = sorted(opts, key=lambda o: get_option_sort_key(o.get('key', ''), len(opts)))
            sorted_keys = [o.get('key') for o in sorted_opts]
            if keys != sorted_keys:
                q['options'] = sorted_opts
                file_changed = True
                total_opts_sorted += 1
                print(f"[{yr} {cat} Q{so}] Sorted options: {keys} -> {sorted_keys}")
                
        # 2. Targeted Explanation fixes
        expl = q.get('explanation', '')
        old_expl = expl
        
        if yr == 2021 and cat == 'ky1' and so == 18:
            expl = EXPL_2021_KY1_Q18
        elif yr == 2002 and cat == 'ky1' and so == 9:
            expl = EXPL_2002_KY1_Q9
        elif yr == 2003 and cat == 'ky1' and so == 2:
            expl = EXPL_2003_KY1_Q2
        elif yr == 2022 and cat == 'ky1' and so == 34:
            expl = EXPL_2022_KY1_Q34
        elif yr == 2021 and cat == 'ky2' and so == 36:
            # Cut bleed into 37
            for marker in ['\n•真题精解•', '\n\n37 ・ In Ambady', '37 ・ In Ambady']:
                idx = expl.find(marker)
                if idx != -1:
                    expl = expl[:idx].strip()
                    break
        elif yr == 2019 and cat == 'ky1' and so == 32:
            # Cut bleed into 33
            for marker in ['33・ The solution', '\n33・']:
                idx = expl.find(marker)
                if idx != -1:
                    expl = expl[:idx].strip()
                    break
        elif yr == 2019 and cat == 'ky1' and so == 36:
            # Cut bleed into 37
            for marker in ['\n•真题精解•\n\n37・', '\n•真题精解•\n\n37']:
                idx = expl.find(marker)
                if idx != -1:
                    expl = expl[:idx].strip()
                    break
        elif yr == 2019 and cat == 'ky1' and so == 39:
            # Cut bleed of Q40 explanation
            marker = '•真题精解\n\n【精准定位】本文首段概述事件'
            idx = expl.find(marker)
            if idx != -1:
                expl = expl[:idx].strip()
        elif yr == 2013 and cat == 'ky1' and so == 32:
            # Cut bleed into 33
            for marker in ['•真题精解\n\n33・', '•真题精解\n33・']:
                idx = expl.find(marker)
                if idx != -1:
                    expl = expl[:idx].strip()
                    break
        elif yr == 2018 and cat == 'ky1' and so == 32:
            # Cut bleed into 33
            idx = expl.find('33 ・ The author argues in Paragraph 2 that')
            if idx != -1:
                expl = expl[:idx].strip()
        elif yr == 2001 and cat == 'ky1' and so == 29:
            # Cut appendix of Text 4
            for marker in ['\n\n知识补充', '\n知识补充']:
                idx = expl.find(marker)
                if idx != -1:
                    expl = expl[:idx].strip()
                    break
        elif yr == 2017 and cat == 'ky1' and so == 32:
            # Cut appendix margin
            for marker in ['•词汇注释与难句分析', '•语篇分析']:
                idx = expl.find(marker)
                if idx != -1 and idx > 800:
                    expl = expl[:idx].strip()
                    break

        # 3. Clean up unclosed bold tags (odd count of **)
        if expl.count("**") % 2 != 0:
            # If an unclosed ** exists, remove stray single ** or append closing **
            # Typically a stray leading **
            parts = expl.split("**")
            if len(parts) % 2 == 0: # means odd count of **
                # Replace the isolated **
                expl = expl.replace("**", "")
                unclosed_bolds_fixed += 1
                
        if expl != old_expl:
            q['explanation'] = expl
            file_changed = True
            total_expls_fixed += 1
            print(f"[{yr} {cat} Q{so}] Explanation cleaned: len {len(old_expl)} -> {len(expl)}")
            
    if file_changed:
        files_modified += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print("\n--- Calibration Complete ---")
print(f"Files modified: {files_modified}")
print(f"Options arrays sorted: {total_opts_sorted}")
print(f"Explanations cleaned: {total_expls_fixed}")
print(f"Unclosed bold markers cleaned: {unclosed_bolds_fixed}")
