#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_deep_text_calibration.py
法医级全库文本校对与做题适配断言验证脚本。
27 项核心断言指标必须 100% PASS。
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import glob
import re
from collections import Counter

LEGIT_NUM_WORDS = {
    '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s',
    '3d', 'mp3', 'h1n1', 'covid19', 'g7', 'g20', '4g', '5g', 'k12', 'wto', 'who'
}

ABBREVIATIONS = {
    'e.g.', 'i.e.', 'etc.', 'u.s.', 'al.', 'vs.', 'mr.', 'mrs.', 'ms.',
    'dr.', 'prof.', 'no.', 'vol.', 'pp.', 'ed.', 'inc.', 'ltd.', 'corp.',
    'co.', 'dept.', 'gov.', 'univ.', 'am.', 'pm.', 'a.m.', 'p.m.'
}

def main():
    exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'exams'))
    exam_files = sorted(glob.glob(os.path.join(exams_dir, '*.json')))

    print(f"=== 考研英语全库真题法医级文本校对与适配断言 (Round 8 终极版) ===")
    print(f"扫描目录: {exams_dir}")
    print(f"试卷文件数: {len(exam_files)}")

    results = {
        "1. 试卷总量 41 套": len(exam_files) == 41,
        "2. 篇章总量 243 篇": False,
        "3. 试题总量 1,825 题": False,
        "4. 试题答案 100% 对齐 (correct_answer == answer)": True,
        "5. 试题题干 0 处序号冗余前缀": True,
        "6. 完型小题 820 题题干 100% 格式统一": True,
        "7. Part A 篇章 0 处残存选项代号": True,
        "8. 篇章 0 处生词音标侧栏注解残留": True,
        "9. 篇章 0 处词尾角标漂移数字": True,
        "10. 篇章 0 处段首伪数字标记": True,
        "11. 篇章 0 处英文逗号/句号黏连": True,
        "12. 试题解析 0 处假模版占位符": True,
        "13. 试题解析 0 处答案描述冲突": True,
        "14. 试题解析 0 处短文本或残片乱码": True,
        "15. 试题题干 0 处 OCR 异形字符与双空格": True,
        "16. 选项文本 0 处冗余代号前缀与尾部杂字": True,
        "17. 篇章正文 0 处词内非法数字与非标准黏连": True,
        "18. 选项字典键顺序 100% 符合 A-B-C-D 规范": True,
        "19. 试题解析 0 处跨题渗透与外泄解析污染": True,
        "20. 试题解析 0 处未闭合 Markdown 加粗标识 (**)": True,
        "21. 篇章与试题拓扑关联 100% 紧密绑定": True,
        "22. 篇章篇首篇尾 0 处伪题干、截断与跨篇串文污染": True,
        "23. 试题题干 0 处断裂、截断与多行丢失": True,
        "24. 全库试题与选项 0 处解析语义冲突、重复选项与空选项": True,
        "25. 全库完型与阅读 0 处选项跨题覆盖与重复": True,
        "26. 全库试题与篇章 0 处 o£、th&r 异形字符与 44 伪双引号残留": True,
        "27. 全库新题型 Part B 41-45 题答案与题干 100% 官方黄金吻合": True,
        "28. 全库试题与篇章 0 处商业广告与淘宝水印残留": True,
        "29. 选项文本 0 处日文中黑点 (・) 伪符号残留": True,
        "30. 2004 年完型填空 20 题 100% 具备黄皮书真题精解": True,
        "31. 2014 年完型第 8 题选项与答案 100% 为 functions (D)": True,
        "32. 2010 Q26 / 2012 Q40 / 2016 Q1 / 2017 Q14 / 2013 Q2 官方答案 100% 黄金校准": True,
        "33. 2011 完型第 7/8 题及阅读 40 题选项与答案 100% 官方黄金校准": True,
        "34. 2004 完型篇章正文与 20 题选项 100% 官方黄金还原": True,
        "35. 2002/2009/2010/2016/2017/2020/2021/2022 等25题官方精解与完整选项 100% 黄金还原": True,
        "36. 2004 年阅读理解 4 篇官方黄金篇章与 20 道试题及黄皮书精解 100% 黄金还原": True,
        "37. 全库 0 处章节末题译文倒灌、0 处掌柜水印、2005 Q25 题干选项答案 100% 黄金校准": True,
        "38. 全库 0 处占位符选项，2002/2003/2006/2008/2010/2012/2017/2018/2020/2021/2022 核心题项 100% 黄金校准": True,
        "39. 2005 完型 20 题官方黄金还原、4 处截断题干与残损选项 100% 官方黄金校准": True,
        "40. 2011/2014/2001 年阅读理解 13 道被篡改试题官方真实选项、答案与题解 100% 黄金纠偏": True,
        "41. 全库 243 篇篇章末尾 0 处字数泄露、0 处跨篇截断与倒灌，2019/2021/2022/2014/2008/2010 篇章 100% 黄金校准": True,
        "42. 2006/2007/2008/2009/2014/2021 年完型与阅读 61 道题选项截断、碎词与题干 100% 官方黄金校准": True,
    }

    total_passages = 0
    total_questions = 0

    mismatched_answers = []
    stems_with_prefix = []
    non_standard_cloze_stems = []
    part_a_leaked_options = []
    gloss_phonetics_found = []
    trailing_digit_words = []
    paragraph_start_digits = []
    glued_punctuations = []
    raw_placeholders = []
    explanation_conflicts = []
    short_or_garbage_expls = []
    stem_ocr_anomalies = []
    opt_prefix_anomalies = []
    passage_word_anomalies = []
    non_canonical_option_orders = []
    explanation_bleeding_found = []
    unclosed_markdown_bolds = []
    orphan_questions = []
    passage_boundary_anomalies = []
    truncated_stems_found = []
    semantic_conflicts = []
    duplicate_cloze_reading_options = []
    ocr_corruptions_found = []
    part_b_anomalies = []
    watermark_hits = []
    trailing_dot_opts = []
    cloze_2004_placeholders = []
    cloze_2014_q8_anomalies = []
    round12_core_anomalies = []
    round13_anomalies = []
    round14_2004_reading_anomalies = []
    round15_anomalies = []
    round16_anomalies = []
    round17_anomalies = []
    round18_anomalies = []
    round19_anomalies = []
    round20_anomalies = []
    round21_anomalies = []
    round22_anomalies = []
    round23_anomalies = []
    round24_anomalies = []
    round25_anomalies = []
    round26_anomalies = []
    round27_anomalies = []
    round28_anomalies = []
    round29_anomalies = []
    round30_anomalies = []
    round31_anomalies = []
    round32_anomalies = []
    round33_anomalies = []
    round34_anomalies = []
    round35_anomalies = []
    round36_anomalies = []
    round37_anomalies = []
    round38_anomalies = []
    round39_anomalies = []
    round40_anomalies = []
    round41_anomalies = []
    round42_anomalies = []
    round43_anomalies = []
    round44_anomalies = []
    round45_anomalies = []
    round46_anomalies = []
    round47_anomalies = []
    round48_anomalies = []
    round49_anomalies = []
    round50_anomalies = []
    round51_anomalies = []
    round52_anomalies = []
    round53_anomalies = []
    round54_anomalies = []
    round55_anomalies = []
    round56_anomalies = []
    round57_anomalies = []
    round58_anomalies = []
    round59_anomalies = []
    round60_anomalies = []
    round61_anomalies = []
    round62_anomalies = []
    round63_anomalies = []
    round64_anomalies = []
    round65_anomalies = []
    round66_anomalies = []
    round67_anomalies = []
    round68_anomalies = []
    round69_anomalies = []
    for fpath in exam_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        title = data['exam'].get('title', '')
        yr = data['exam'].get('year')
        cat = data['exam'].get('category_id')

        if yr == 2010 and cat == 'ky1':
            if title != '2010年全国硕士研究生入学统一考试英语（一）真题':
                round52_anomalies.append(('2010_ky1_title', title))
        if yr == 2010 and cat == 'ky2':
            if title != '2010年全国硕士研究生入学统一考试英语（二）真题':
                round53_anomalies.append(('2010_ky2_title', title))
        if yr == 2011 and cat == 'ky1':
            if title != '2011年全国硕士研究生入学统一考试英语（一）真题':
                round54_anomalies.append(('2011_ky1_title', title))
        if yr == 2011 and cat == 'ky2':
            if title != '2011年全国硕士研究生入学统一考试英语（二）真题':
                round55_anomalies.append(('2011_ky2_title', title))
        if yr == 2012 and cat == 'ky1':
            if title != '2012年全国硕士研究生入学统一考试英语（一）真题':
                round56_anomalies.append(('2012_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round56_anomalies.append(('2012_ky1_total_score', data['exam'].get('total_score')))
        if yr == 2012 and cat == 'ky2':
            if title != '2012年全国硕士研究生入学统一考试英语（二）真题':
                round57_anomalies.append(('2012_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round57_anomalies.append(('2012_ky2_total_score', data['exam'].get('total_score')))
        if yr == 2013 and cat == 'ky1':
            if title != '2013年全国硕士研究生入学统一考试英语（一）真题':
                round58_anomalies.append(('2013_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round58_anomalies.append(('2013_ky1_total_score', data['exam'].get('total_score')))
            
            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round58_anomalies.append(('2013_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round58_anomalies.append(('2013_ky1_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("People are, on the whole, poor at considering"):
                    round58_anomalies.append(('2013_ky1_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 6:
                    round58_anomalies.append(('2013_ky1_t1_paras', len(t1_paras)))
                if "The victims of this revolution, of course, are not limited to designers" not in t1.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t1_p3', 'corrupted'))
                if "Overdressed is the fashion world's answer" not in t1.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t1_p4', 'missing'))
                if "better clothes is good for both the planet" in t1.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t1_external_junk', 'present'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 7:
                    round58_anomalies.append(('2013_ky1_t2_paras', len(t2_paras)))
                if "It is suggested in Paragraph 1" in t2.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t2_stem_pollution', 'present'))
                if "hoirified" in t2.get("content", "") or "Microsoffs" in t2.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t2_ocr_errors', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 7:
                    round58_anomalies.append(('2013_ky1_t3_paras', len(t3_paras)))
                if "the past holds the key to the future" not in t3.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t3_p6', 'missing'))
                if "This long perspective makes the pessimistic view of our prospects" not in t3.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t3_p7', 'missing'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 7:
                    round58_anomalies.append(('2013_ky1_t4_paras', len(t4_paras)))
                if "to holds the key to" in t4.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t4_inverted_residue', 'present'))
                if "In Arizona v. United States" not in t4.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t4_p2', 'corrupted'))
                if "Two of the three objecting Justices—" not in t4.get("content", ""):
                    round58_anomalies.append(('2013_ky1_t4_p5', 'missing_header'))

                pb = p_list[5]
                if "[A] The idea is to force social scientists" not in pb.get("content", "") or "[B] The solution is to change the mindset" not in pb.get("content", ""):
                    round58_anomalies.append(('2013_ky1_pb_options', 'missing_A_or_B'))
                if "[41] ____________" not in pb.get("content", "") or "[45] ____________" not in pb.get("content", ""):
                    round58_anomalies.append(('2013_ky1_pb_gaps', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round58_anomalies.append(('2013_ky1_questions_count', len(q_list)))
            else:
                total_pts = sum(q.get("points", 0) for q in q_list)
                if abs(total_pts - 60.0) > 1e-4:
                    round58_anomalies.append(('2013_ky1_total_points', total_pts))

                q22 = next((q for q in q_list if q.get("sort_order") == 22), None)
                if not q22 or q22.get("correct_answer") != "B":
                    round58_anomalies.append(('2013_ky1_q22_ans', 'not_B'))
                else:
                    opt_b = next((it["text"] for it in q22.get("options", []) if it["key"] == "B"), "")
                    if "shop for their garments more frequently" not in opt_b:
                        round58_anomalies.append(('2013_ky1_q22_opt_b', opt_b))

                q23 = next((q for q in q_list if q.get("sort_order") == 23), None)
                if not q23 or q23.get("correct_answer") != "D":
                    round58_anomalies.append(('2013_ky1_q23_ans', 'not_D'))
                else:
                    opt_d = next((it["text"] for it in q23.get("options", []) if it["key"] == "D"), "")
                    if opt_d != "accusation":
                        round58_anomalies.append(('2013_ky1_q23_opt_d', opt_d))

                pb_ans_map = {41: 'E', 42: 'F', 43: 'D', 44: 'G', 45: 'A'}
                for qn, exp_a in pb_ans_map.items():
                    q_obj = next((q for q in q_list if q.get("sort_order") == qn), None)
                    if not q_obj or q_obj.get("correct_answer") != exp_a:
                        round58_anomalies.append((f'2013_ky1_q{qn}_ans', q_obj.get('correct_answer') if q_obj else None))

        if yr == 2013 and cat == 'ky2':
            if title != '2013年全国硕士研究生入学统一考试英语（二）真题':
                round59_anomalies.append(('2013_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round59_anomalies.append(('2013_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round59_anomalies.append(('2013_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round59_anomalies.append(('2013_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("Given the advantages of electronic money"):
                    round59_anomalies.append(('2013_ky2_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 6:
                    round59_anomalies.append(('2013_ky2_t1_paras', len(t1_paras)))
                if "Davidson relates a joke from cotton country" not in t1.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t1_header', 'corrupted'))
                if "G.I. Bill" not in t1.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t1_gi_bill', 'missing'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 5:
                    round59_anomalies.append(('2013_ky2_t2_paras', len(t2_paras)))
                if "A century ago, the immigrants from across the Atlantic" not in t2.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t2_header', 'corrupted'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 6:
                    round59_anomalies.append(('2013_ky2_t3_paras', len(t3_paras)))
                if "Scientists have found that although we are prone" not in t3.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t3_header', 'corrupted'))
                if "John Gottman" not in t3.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t3_gottman', 'missing'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 7:
                    round59_anomalies.append(('2013_ky2_t4_paras', len(t4_paras)))
                if "Do we need quotas" not in t4.get("content", ""):
                    round59_anomalies.append(('2013_ky2_t4_p3_quota', 'missing'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 6:
                    round59_anomalies.append(('2013_ky2_pb_paras', len(pb_paras)))
                if "[41]" not in pb.get("content", "") or "[45]" not in pb.get("content", ""):
                    round59_anomalies.append(('2013_ky2_pb_labels', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round59_anomalies.append(('2013_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round59_anomalies.append((f'2013_ky2_q{i}_number', q.get('question_number')))
                    if q.get('question_type') != 'multiple_choice':
                        round59_anomalies.append((f'2013_ky2_q{i}_type', q.get('question_type')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round59_anomalies.append((f'2013_ky2_q{i}_points', q_pts))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round59_anomalies.append((f'2013_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or ('【精准定位】' not in expl and '【命题解密】' not in expl and '【错项排除】' not in expl):
                        round59_anomalies.append((f'2013_ky2_q{i}_explanation_structure', 'incomplete'))

                gold_ans = {
                    1:'B', 2:'D', 3:'B', 4:'A', 5:'C', 6:'B', 7:'A', 8:'D', 9:'C', 10:'A',
                    11:'A', 12:'C', 13:'B', 14:'D', 15:'C', 16:'D', 17:'A', 18:'B', 19:'D', 20:'C',
                    21:'A', 22:'D', 23:'B', 24:'B', 25:'C',
                    26:'A', 27:'C', 28:'C', 29:'B', 30:'D',
                    31:'D', 32:'A', 33:'B', 34:'C', 35:'B',
                    36:'B', 37:'C', 38:'A', 39:'D', 40:'C',
                    41:'F', 42:'C', 43:'G', 44:'A', 45:'B'
                }
                for q_no, exp_a in gold_ans.items():
                    act_a = q_list[q_no-1].get('answer')
                    if act_a != exp_a:
                        round59_anomalies.append((f'2013_ky2_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))

        if yr == 2014 and cat == 'ky1':
            if title != '2014年全国硕士研究生入学统一考试英语（一）真题':
                round60_anomalies.append(('2014_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round60_anomalies.append(('2014_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round60_anomalies.append(('2014_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round60_anomalies.append(('2014_ky1_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("As many people hit middle age"):
                    round60_anomalies.append(('2014_ky1_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 4:
                    round60_anomalies.append(('2014_ky1_t1_paras', len(t1_paras)))
                if "George Osborne introduced a new requirement" not in t1.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t1_header', 'corrupted'))
                if "least generous in the EU." not in t1.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t1_tail', 'corrupted'))
                if "icipants" in t1.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t1_pollution', 'present'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 6:
                    round60_anomalies.append(('2014_ky1_t2_paras', len(t2_paras)))
                if "All around the world, lawyers generate more hostility" not in t2.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t2_header', 'corrupted'))
                if "Which of the following adds to the costs" in t2.get("content", "") or "A lot of students take up law" in t2.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t2_stem_pollution', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 5:
                    round60_anomalies.append(('2014_ky1_t3_paras', len(t3_paras)))
                if "Fundamental Physics Prize" not in t3.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t3_header', 'corrupted'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 6:
                    round60_anomalies.append(('2014_ky1_t4_paras', len(t4_paras)))
                if "The Heart of the Matter" not in t4.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t4_header', 'corrupted'))
                if "Influential figures in the Congress required" in t4.get("content", ""):
                    round60_anomalies.append(('2014_ky1_t4_stem_pollution', 'present'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 8:
                    round60_anomalies.append(('2014_ky1_pb_paras', len(pb_paras)))
                for lbl in ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]']:
                    if lbl not in pb.get("content", ""):
                        round60_anomalies.append((f'2014_ky1_pb_{lbl}', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round60_anomalies.append(('2014_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round60_anomalies.append((f'2014_ky1_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round60_anomalies.append((f'2014_ky1_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round60_anomalies.append((f'2014_ky1_q{i}_q_type', q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round60_anomalies.append((f'2014_ky1_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or ('考点提炼' not in expl and '精准定位' not in expl and '选项推测' not in expl and '答案敲定' not in expl):
                        round60_anomalies.append((f'2014_ky1_q{i}_explanation_structure', 'incomplete'))

                gold_ans = {
                    1: 'D', 2: 'A', 3: 'B', 4: 'A', 5: 'C', 6: 'D', 7: 'C', 8: 'D', 9: 'B', 10: 'C',
                    11: 'A', 12: 'A', 13: 'B', 14: 'D', 15: 'C', 16: 'B', 17: 'A', 18: 'B', 19: 'C', 20: 'D',
                    21: 'A', 22: 'C', 23: 'D', 24: 'A', 25: 'A',
                    26: 'D', 27: 'D', 28: 'A', 29: 'B', 30: 'B',
                    31: 'B', 32: 'C', 33: 'C', 34: 'B', 35: 'D',
                    36: 'A', 37: 'D', 38: 'C', 39: 'C', 40: 'B',
                    41: 'C', 42: 'F', 43: 'G', 44: 'D', 45: 'B'
                }
                for q_no, exp_a in gold_ans.items():
                    act_a = q_list[q_no-1].get('answer')
                    if act_a != exp_a:
                        round60_anomalies.append((f'2014_ky1_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))

        if yr == 2014 and cat == 'ky2':
            if title != '2014年全国硕士研究生招生考试英语（二）真题':
                round61_anomalies.append(('2014_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round61_anomalies.append(('2014_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round61_anomalies.append(('2014_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 5:
                    round61_anomalies.append(('2014_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("Thinner isn't always better."):
                    round61_anomalies.append(('2014_ky2_cloze_header', 'corrupted'))
                if "matter of weight than body fat. Some people with a high BMI are in fact extremely fit," not in cloze.get("content", ""):
                    round61_anomalies.append(('2014_ky2_cloze_missing_sentence', 'not found'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 4:
                    round61_anomalies.append(('2014_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("What would you do with $590m?"):
                    round61_anomalies.append(('2014_ky2_t1_header', 'corrupted'))
                if "Money may not quite buy happiness, but people in wealthier countries are generally happier than those in poor ones." not in t1.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t1_missing_sentence', 'not found'))
                if "seemsmostpeoplewouldbebetter" in t1.get("content", "") or "theycouldshortentheir" in t1.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t1_concatenation', 'present'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 5:
                    round61_anomalies.append(('2014_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("An article in Scientific American has pointed out"):
                    round61_anomalies.append(('2014_ky2_t2_header', 'corrupted'))
                if "Social psychologists have amassed oceans of research into what they call the \"above average effect\"" not in t2.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t2_missing_sentence', 'not found'))
                if "I don't think the findings that we have are any evidence of personal delusion" not in t2.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t2_epley_quote', 'truncated'))
                if "statisticalimpossibilities" in t2.get("content", "") or "wasreallyhowtheylooked" in t2.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t2_concatenation', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 4:
                    round61_anomalies.append(('2014_ky2_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("The concept of man versus machine is at least as old"):
                    round61_anomalies.append(('2014_ky2_t3_header', 'corrupted'))
                if "these are the types of jobs that machines can perform much better at than human beings." not in t3.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t3_missing_sentence', 'not found'))
                if 'how do we innovate our institutions and our work practices?' not in t3.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t3_tail', 'corrupted'))
                if "weinnovate ourinstitutions" in t3.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t3_concatenation', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) not in [6, 7]:
                    round61_anomalies.append(('2014_ky2_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith("When the government talks about infrastructure"):
                    round61_anomalies.append(('2014_ky2_t4_header', 'corrupted'))
                if "offers an opportunity for the government to help rectify this." not in t4.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t4_missing_sentence', 'not found'))
                if "The Labour party has recently announced that it will retain a large part of the coalition's spending plans" not in t4.get("content", ""):
                    round61_anomalies.append(('2014_ky2_t4_missing_spending_plans', 'not found'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 8:
                    round61_anomalies.append(('2014_ky2_pb_paras', len(pb_paras)))
                if "range of new forms, including Body Art, Performance Art, Action Art and Installation Art, which pushed art beyond" not in pb.get("content", ""):
                    round61_anomalies.append(('2014_ky2_pb_intro', 'truncated'))
                if "Samuel 9 Palmer" in pb.get("content", ""):
                    round61_anomalies.append(('2014_ky2_pb_ocr_noise', 'present'))
                if "Towards Avebury" not in pb.get("content", ""):
                    round61_anomalies.append(('2014_ky2_pb_artwork', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round61_anomalies.append(('2014_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round61_anomalies.append((f'2014_ky2_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round61_anomalies.append((f'2014_ky2_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round61_anomalies.append((f'2014_ky2_q{i}_q_type', q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round61_anomalies.append((f'2014_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl:
                        round61_anomalies.append((f'2014_ky2_q{i}_explanation', 'missing'))

                gold_ans_ky2 = {
                    1: 'B', 2: 'A', 3: 'C', 4: 'A', 5: 'D', 6: 'A', 7: 'C', 8: 'C', 9: 'D', 10: 'B',
                    11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'B', 16: 'D', 17: 'A', 18: 'D', 19: 'C', 20: 'B',
                    21: 'B', 22: 'A', 23: 'D', 24: 'B', 25: 'C',
                    26: 'A', 27: 'C', 28: 'B', 29: 'A', 30: 'D',
                    31: 'B', 32: 'A', 33: 'D', 34: 'D', 35: 'C',
                    36: 'B', 37: 'C', 38: 'A', 39: 'C', 40: 'D',
                    41: 'D', 42: 'E', 43: 'G', 44: 'C', 45: 'A'
                }
                for q_no, exp_a in gold_ans_ky2.items():
                    act_a = q_list[q_no-1].get('answer')
                    if act_a != exp_a:
                        round61_anomalies.append((f'2014_ky2_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))

        if yr == 2015 and cat == 'ky1':
            if title != '2015年全国硕士研究生招生考试英语（一）真题':
                round62_anomalies.append(('2015_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round62_anomalies.append(('2015_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round62_anomalies.append(('2015_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 5:
                    round62_anomalies.append(('2015_ky1_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith('Though not biologically related, friends are as "related" as fourth cousins'):
                    round62_anomalies.append(('2015_ky1_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 7:
                    round62_anomalies.append(('2015_ky1_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("King Juan Carlos of Spain once insisted that \"kings don't abdicate, they die in their sleep.\""):
                    round62_anomalies.append(('2015_ky1_t1_header', 'corrupted'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 7:
                    round62_anomalies.append(('2015_ky1_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("Just how much does the Constitution protect your digital data?"):
                    round62_anomalies.append(('2015_ky1_t2_header', 'corrupted'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 6:
                    round62_anomalies.append(('2015_ky1_t3_paras', len(t3_paras)))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 6:
                    round62_anomalies.append(('2015_ky1_t4_paras', len(t4_paras)))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 5:
                    round62_anomalies.append(('2015_ky1_pb_paras', len(pb_paras)))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round62_anomalies.append(('2015_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round62_anomalies.append((f'2015_ky1_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round62_anomalies.append((f'2015_ky1_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round62_anomalies.append((f'2015_ky1_q{i}_q_type', q.get('q_type')))

                gold_ans_ky1 = {
                    1: 'D', 2: 'B', 3: 'C', 4: 'A', 5: 'C', 6: 'A', 7: 'D', 8: 'A', 9: 'B', 10: 'D',
                    11: 'B', 12: 'A', 13: 'B', 14: 'D', 15: 'C', 16: 'C', 17: 'B', 18: 'D', 19: 'C', 20: 'A',
                    21: 'D', 22: 'C', 23: 'B', 24: 'A', 25: 'C',
                    26: 'C', 27: 'A', 28: 'D', 29: 'D', 30: 'D',
                    31: 'B', 32: 'C', 33: 'D', 34: 'C', 35: 'A',
                    36: 'A', 37: 'B', 38: 'A', 39: 'C', 40: 'B',
                    41: 'C', 42: 'E', 43: 'G', 44: 'B', 45: 'A'
                }
                for q_idx, exp_ans in gold_ans_ky1.items():
                    act_ans = q_list[q_idx-1].get('answer') or q_list[q_idx-1].get('correct_answer')
                    if act_ans != exp_ans:
                        round62_anomalies.append((f'2015_ky1_q{q_idx}_answer_mismatch', f'expected {exp_ans}, got {act_ans}'))

        if yr == 2015 and cat == 'ky2':
            if title != '2015年全国硕士研究生招生考试英语（二）真题':
                round63_anomalies.append(('2015_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round63_anomalies.append(('2015_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round63_anomalies.append(('2015_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round63_anomalies.append(('2015_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith('In our contemporary culture, the prospect of communicating with'):
                    round63_anomalies.append(('2015_ky2_cloze_header', 'corrupted'))
                if "_:" in cloze.get("content", ""):
                    round63_anomalies.append(('2015_ky2_cloze_placeholder_corruption', 'present'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 6:
                    round63_anomalies.append(('2015_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("A new study suggests that contrary to most surveys"):
                    round63_anomalies.append(('2015_ky2_t1_header', 'corrupted'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 5:
                    round63_anomalies.append(('2015_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("For years, studies have found that first-generation college students"):
                    round63_anomalies.append(('2015_ky2_t2_header', 'corrupted'))
                if "‘like them’" in t2.get("content", "") or "\ufffd" in t2.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t2_corrupted_quotes', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 5:
                    round63_anomalies.append(('2015_ky2_t3_paras', len(t3_paras)))
                if "much more right-brained than it was 20 years ago, says Harvard Business School historian Nancy Koehn." not in t3.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t3_missing_right_brained', 'not found'))
                if "very \"team\"-oriented - and that is not by coincidence." not in t3.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t3_missing_team_oriented', 'not found'))
                if "andhow" in t3.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t3_concatenation', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 6:
                    round63_anomalies.append(('2015_ky2_t4_paras', len(t4_paras)))
                if "arenowfinallymovingforward" in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_concatenation', 'present'))
                if "evidence of weakness in the labor market and it means that many" not in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_missing_weakness', 'not found'))
                if "before Obamacare the only way to get insurance was through a job that provided health insurance." not in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_missing_obamacare_way', 'not found'))
                if "These are people who may previously have felt the need to get a full-time job that provided insurance in order to cover themselves and their families." not in t4.get("content", ""):
                    round63_anomalies.append(('2015_ky2_t4_missing_full_time_need', 'not found'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) < 7:
                    round63_anomalies.append(('2015_ky2_pb_paras', len(pb_paras)))
                if "n sn s n" in pb.get("content", ""):
                    round63_anomalies.append(('2015_ky2_pb_ocr_noise', 'present'))
                if "Fear is both useful and harmful." not in pb.get("content", ""):
                    round63_anomalies.append(('2015_ky2_pb_fear_useful', 'missing'))
                if "companionship. If you have no friends or relatives, try to participate in several online communities" not in pb.get("content", ""):
                    round63_anomalies.append(('2015_ky2_pb_missing_companionship', 'not found'))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"[{gap_num}]" not in pb.get("content", ""):
                        round63_anomalies.append((f'2015_ky2_pb_gap_{gap_num}', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round63_anomalies.append(('2015_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round63_anomalies.append((f'2015_ky2_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round63_anomalies.append((f'2015_ky2_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('q_type') != exp_type:
                        round63_anomalies.append((f'2015_ky2_q{i}_q_type', q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round63_anomalies.append((f'2015_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round63_anomalies.append((f'2015_ky2_q{i}_explanation', 'insufficient'))

                gold_ans_ky2 = {
                    1: 'A', 2: 'D', 3: 'B', 4: 'A', 5: 'C', 6: 'B', 7: 'A', 8: 'D', 9: 'C', 10: 'B',
                    11: 'A', 12: 'C', 13: 'C', 14: 'D', 15: 'C', 16: 'D', 17: 'A', 18: 'B', 19: 'D', 20: 'B',
                    21: 'A', 22: 'B', 23: 'A', 24: 'C', 25: 'D',
                    26: 'C', 27: 'C', 28: 'C', 29: 'B', 30: 'D',
                    31: 'D', 32: 'A', 33: 'D', 34: 'A', 35: 'B',
                    36: 'B', 37: 'C', 38: 'A', 39: 'D', 40: 'A',
                    41: 'D', 42: 'E', 43: 'G', 44: 'A', 45: 'C'
                }
                for q_idx, exp_ans in gold_ans_ky2.items():
                    act_ans = q_list[q_idx-1].get('answer') or q_list[q_idx-1].get('correct_answer')
                    if act_ans != exp_ans:
                        round63_anomalies.append((f'2015_ky2_q{q_idx}_answer_mismatch', f'expected {exp_ans}, got {act_ans}'))

        if yr == 2016 and cat == 'ky1':
            if title != '2016年全国硕士研究生招生考试英语（一）真题':
                round64_anomalies.append(('2016_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round64_anomalies.append(('2016_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round64_anomalies.append(('2016_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 3:
                    round64_anomalies.append(('2016_ky1_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith('In Cambodia, the choice of a spouse is a complex one for the young male.'):
                    round64_anomalies.append(('2016_ky1_cloze_header', 'corrupted'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 7:
                    round64_anomalies.append(('2016_ky1_t1_paras', len(t1_paras)))
                if "France 9 which" in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_ocr_noise', 'France 9 which'))
                if "a couple of uplifting motiveso" in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_duplicate_phrase', 'uplifting motiveso'))
                if "The bans, if fully enforced, would suggest to women" not in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_missing_bans_sentence', 'not found'))
                if "Relying on ethical persuasion rather than law to address the misuse of body ideals" not in t1.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t1_missing_para7', 'not found'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 6:
                    round64_anomalies.append(('2016_ky1_t2_paras', len(t2_paras)))
                if "showT" in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_ocr_showT', 'present'))
                if "At the next election none of the big parties seem likely to endorse this sentiment." not in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_missing_para3_start', 'not found'))
                if "struck terror into many local Conservative parties." not in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_missing_para3_end', 'not found'))
                if "concreted meadows n" in t2.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t2_corrupted_quotes', 'present'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 6:
                    round64_anomalies.append(('2016_ky1_t3_paras', len(t3_paras)))
                if "others. causes it helps." in t3.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t3_duplicated_phrase', 'causes it helps.'))
                if ":Companies did not receive lower fines." in t3.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t3_duplicated_fines', 'present'))
                if "We estimate < record in CSRO" in t3.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t3_ocr_leak', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 7:
                    round64_anomalies.append(('2016_ky1_t4_paras', len(t4_paras)))
                if "There will eventually come a day when The New York Times ceases to publish" not in t4.get("content", ""):
                    round64_anomalies.append(('2016_ky1_t4_header', 'corrupted'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 8:
                    round64_anomalies.append(('2016_ky1_pb_paras', len(pb_paras)))
                if "Directions:" in pb.get("content", ""):
                    round64_anomalies.append(('2016_ky1_pb_directions_leaked', 'present'))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"[{gap_num}] _________________________________" not in pb.get("content", ""):
                        round64_anomalies.append((f'2016_ky1_pb_gap_{gap_num}', 'missing'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round64_anomalies.append(('2016_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round64_anomalies.append((f'2016_ky1_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round64_anomalies.append((f'2016_ky1_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round64_anomalies.append((f'2016_ky1_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round64_anomalies.append((f'2016_ky1_q{i}_placeholder_opt', opt_k))
                        if "once.... ..." in opt_v:
                            round64_anomalies.append(('2016_ky1_q20_corrupted_once', opt_v))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round64_anomalies.append((f'2016_ky1_q{i}_explanation', 'insufficient'))

                gold_ans_ky1_2016 = {
                    1: 'A', 2: 'D', 3: 'C', 4: 'A', 5: 'C', 6: 'B', 7: 'D', 8: 'B', 9: 'D', 10: 'A',
                    11: 'D', 12: 'C', 13: 'B', 14: 'B', 15: 'C', 16: 'A', 17: 'B', 18: 'D', 19: 'B', 20: 'A',
                    21: 'A', 22: 'D', 23: 'D', 24: 'C', 25: 'D',
                    26: 'A', 27: 'D', 28: 'C', 29: 'A', 30: 'C',
                    31: 'B', 32: 'C', 33: 'D', 34: 'A', 35: 'B',
                    36: 'A', 37: 'B', 38: 'B', 39: 'C', 40: 'B',
                    41: 'C', 42: 'F', 43: 'D', 44: 'E', 45: 'G'
                }
                for q_idx, exp_ans in gold_ans_ky1_2016.items():
                    act_ans = q_list[q_idx - 1].get('correct_answer') or q_list[q_idx - 1].get('answer')
                    if act_ans != exp_ans:
                        round64_anomalies.append((f'2016_ky1_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))

        if yr == 2016 and cat == 'ky2':
            if title != '2016年全国硕士研究生招生考试英语（二）真题':
                round65_anomalies.append(('2016_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round65_anomalies.append(('2016_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round65_anomalies.append(('2016_ky2_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round65_anomalies.append(('2016_ky2_cloze_paras', len(c_paras)))
                if "averagehappiness" in cloze.get("content", ""):
                    round65_anomalies.append(('2016_ky2_cloze_ocr_noise', 'averagehappiness'))
                if "The correlation between happiness and investment was particularly strong for younger" not in cloze.get("content", ""):
                    round65_anomalies.append(('2016_ky2_cloze_missing_text', 'younger firms'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 6:
                    round65_anomalies.append(('2016_ky2_t1_paras', len(t1_paras)))
                if "computer-science TOT classes" in t1.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t1_ocr_noise', 'computer-science TOT classes'))
                if "Programming languages have a short shelf life, and the ones Flatiron teaches may not even be relevant" not in t1.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t1_missing_shelf_life', 'not found'))
                if "learnthat" in t1.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t1_typo_learnthat', 'present'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 4:
                    round65_anomalies.append(('2016_ky2_t2_paras', len(t2_paras)))
                if "withfederal" in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_typo_withfederal', 'present'))
                if "privatelandowners" in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_typo_privatelandowners', 'present'))
                if "as part of their operations to pay into a fund to replace every acre of destroyed habitat with 2 new acres of suitable habitat." not in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_missing_fund_sentence', 'not found'))
                if "says Jay Lininger, a senior scientist at the Center for Biological Diversity." not in t2.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t2_cut_off_ending', 'not found'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 4:
                    round65_anomalies.append(('2016_ky2_t3_paras', len(t3_paras)))
                if "theproblem" in t3.get("content", "") or "isthat" in t3.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t3_typo_squashed', 'present'))
                if "writes Gary Eberle in Sacred Time, “and we feel a pressure to fill these different-sized bottles" not in t3.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t3_missing_eberle_quote', 'not found'))
                if "helps us “step outside time's flow” into “soul time.” You might also consider reading only physical books" not in t3.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t3_missing_soul_time', 'not found'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 6:
                    round65_anomalies.append(('2016_ky2_t4_paras', len(t4_paras)))
                if "preferencestohousingpatternstopolitics" in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_typo_squashed', 'present'))
                if "affordablehousing" in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_typo_affordablehousing', 'present'))
                if "says he struggled to find a job after graduating from college." not in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_missing_schneider_struggle', 'not found'))
                if "to rent rooms out to people to make that happen.” Looking back, he is struck that his parents could provide a comfortable life" not in t4.get("content", ""):
                    round65_anomalies.append(('2016_ky2_t4_missing_schneider_parents', 'not found'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 7:
                    round65_anomalies.append(('2016_ky2_pb_paras', len(pb_paras)))
                for gap_num in [41, 42, 43, 44, 45]:
                    if f"[{gap_num}] _________________________________" not in pb.get("content", ""):
                        round65_anomalies.append((f'2016_ky2_pb_gap_{gap_num}', 'missing'))
                if "- n s move on" in pb.get("content", ""):
                    round65_anomalies.append(('2016_ky2_pb_mangled_ns', 'present'))
                if "What we need to do is find a way to acknowledge and express what we feel appropriately, and then move on." not in pb.get("content", ""):
                    round65_anomalies.append(('2016_ky2_pb_missing_express_sentence', 'not found'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round65_anomalies.append(('2016_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round65_anomalies.append((f'2016_ky2_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round65_anomalies.append((f'2016_ky2_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round65_anomalies.append((f'2016_ky2_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round65_anomalies.append((f'2016_ky2_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round65_anomalies.append((f'2016_ky2_q{i}_explanation', 'insufficient'))

                gold_ans_ky2_2016 = {
                    1: 'B', 2: 'B', 3: 'A', 4: 'C', 5: 'D', 6: 'B', 7: 'A', 8: 'D', 9: 'C', 10: 'A',
                    11: 'A', 12: 'C', 13: 'B', 14: 'D', 15: 'C', 16: 'D', 17: 'A', 18: 'C', 19: 'D', 20: 'B',
                    21: 'B', 22: 'B', 23: 'A', 24: 'C', 25: 'A',
                    26: 'A', 27: 'C', 28: 'A', 29: 'D', 30: 'C',
                    31: 'D', 32: 'B', 33: 'D', 34: 'A', 35: 'B',
                    36: 'B', 37: 'C', 38: 'D', 39: 'D', 40: 'C',
                    41: 'D', 42: 'F', 43: 'A', 44: 'B', 45: 'E'
                }
                for q_idx, exp_ans in gold_ans_ky2_2016.items():
                    act_ans = q_list[q_idx - 1].get('correct_answer') or q_list[q_idx - 1].get('answer')
                    if act_ans != exp_ans:
                        round65_anomalies.append((f'2016_ky2_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))

        if yr == 2017 and cat == 'ky1':
            if title != '2017年全国硕士研究生招生考试英语（一）真题':
                round66_anomalies.append(('2017_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round66_anomalies.append(('2017_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round66_anomalies.append(('2017_ky1_passages_count', len(p_list)))
            else:
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round66_anomalies.append(('2017_ky1_cloze_paras', len(c_paras)))
                if "resounding ayes!" in cloze.get("content", ""):
                    round66_anomalies.append(('2017_ky1_cloze_typo_ayes', 'resounding ayes!'))
                if "oxytocin, often called “the bonding hormone”" not in cloze.get("content", ""):
                    round66_anomalies.append(('2017_ky1_cloze_oxytocin_text', 'missing'))

                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 7:
                    round66_anomalies.append(('2017_ky1_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("First two hours, now three hours"):
                    round66_anomalies.append(('2017_ky1_t1_start', t1.get("content", "")[:50]))
                if "EgyptAir Flight 804" not in t1.get("content", "") or "underused PreCheck lanes" not in t1.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t1_required_phrases', 'missing'))

                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 6:
                    round66_anomalies.append(('2017_ky1_t2_paras', len(t2_paras)))
                if "“The ancient Hawaiians were astronomers,” wrote Queen Liliuokalani" not in t2.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t2_missing_queen_liliuokalani', 'not found'))
                if "Thirty Meter Telescope (TMT)" not in t2.get("content", "") or "dormant volcano worshiped by some Hawaiians as the piko" not in t2.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t2_content_phrases', 'missing'))

                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 7:
                    round66_anomalies.append(('2017_ky1_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("Robert F. Kennedy once said that a country's GDP measures"):
                    round66_anomalies.append(('2017_ky1_t3_start', t3.get("content", "")[:60]))
                if "Across the 163 countries measured, the UK is one of the poorest performers" not in t3.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t3_gdp_study_text', 'missing'))
                if "Robert McDonnell" in t3.get("content", "") or "Supreme Court" in t3.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t3_inversion_contamination', 'McDonnell present in T3'))
                if "[452 words]" in t3.get("content", "") or "452 words" in t3.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t3_word_count_leakage', 'present'))

                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 8:
                    round66_anomalies.append(('2017_ky1_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith('In a rare unanimous ruling, the US Supreme Court has overturned the corruption conviction of a former Virginia governor, Robert McDonnell.'):
                    round66_anomalies.append(('2017_ky1_t4_start', t4.get("content", "")[:60]))
                if "The court's ruling is a step forward in the struggle against both corruption and official favoritism." not in t4.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t4_ending', 'missing'))
                if "When GDP is no longer regarded as the sole measure" in t4.get("content", "") or "Brexit" in t4.get("content", ""):
                    round66_anomalies.append(('2017_ky1_t4_inversion_contamination', 'GDP present in T4'))

                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 7:
                    round66_anomalies.append(('2017_ky1_pb_paras', len(pb_paras)))
                if "Directions:" in pb.get("content", "") or "[D] -> [41]" in pb.get("content", ""):
                    round66_anomalies.append(('2017_ky1_pb_directions_leak', 'present'))
                if not pb.get("content", "").startswith('[A] The first published sketch'):
                    round66_anomalies.append(('2017_ky1_pb_start', pb.get("content", "")[:50]))
                if "A Dinner at Poplar Walk" not in pb.get("content", "") or "The Pickwick Papers" not in pb.get("content", ""):
                    round66_anomalies.append(('2017_ky1_pb_content', 'missing Dickens work'))

            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round66_anomalies.append(('2017_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i:
                        round66_anomalies.append((f'2017_ky1_q{i}_number', q.get('question_number')))
                    exp_score = 0.5 if i <= 20 else 2.0
                    q_pts = q.get('points') if q.get('points') is not None else q.get('score')
                    if float(q_pts or 0) != exp_score:
                        round66_anomalies.append((f'2017_ky1_q{i}_points', q_pts))
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round66_anomalies.append((f'2017_ky1_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    opts = q.get('options', [])
                    for opt_item in opts:
                        opt_k = opt_item.get('key', '')
                        opt_v = opt_item.get('text', '')
                        if opt_v.strip() == opt_k:
                            round66_anomalies.append((f'2017_ky1_q{i}_placeholder_opt', opt_k))
                    expl = q.get('explanation', '')
                    if not expl or len(expl) < 100:
                        round66_anomalies.append((f'2017_ky1_q{i}_explanation', 'insufficient'))

                gold_ans_ky1_2017 = {
                    1: 'B', 2: 'A', 3: 'D', 4: 'C', 5: 'B', 6: 'D', 7: 'B', 8: 'C', 9: 'A', 10: 'D',
                    11: 'A', 12: 'B', 13: 'D', 14: 'B', 15: 'C', 16: 'A', 17: 'C', 18: 'A', 19: 'C', 20: 'D',
                    21: 'A', 22: 'C', 23: 'D', 24: 'D', 25: 'C',
                    26: 'B', 27: 'A', 28: 'B', 29: 'A', 30: 'D',
                    31: 'D', 32: 'B', 33: 'D', 34: 'C', 35: 'A',
                    36: 'C', 37: 'C', 38: 'A', 39: 'B', 40: 'D',
                    41: 'F', 42: 'E', 43: 'A', 44: 'C', 45: 'G'
                }
                for q_idx, exp_ans in gold_ans_ky1_2017.items():
                    act_ans = q_list[q_idx - 1].get('correct_answer') or q_list[q_idx - 1].get('answer')
                    if act_ans != exp_ans:
                        round66_anomalies.append((f'2017_ky1_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))

        if yr == 2017 and cat == 'ky2':
            if title != '2017年全国硕士研究生招生考试英语（二）真题':
                round67_anomalies.append(('2017_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round67_anomalies.append(('2017_ky2_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round67_anomalies.append(('2017_ky2_passages_count', len(p_list)))
            else:
                # Cloze
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round67_anomalies.append(('2017_ky2_cloze_paras', len(c_paras)))
                if "reservedfor" in cloze.get("content", ""):
                    round67_anomalies.append(('2017_ky2_cloze_concats_reservedfor', 'present'))
                if not cloze.get("content", "").startswith("People have speculated for centuries about a future without work."):
                    round67_anomalies.append(('2017_ky2_cloze_start', cloze.get("content", "")[:50]))

                # Text 1 (Parkrun)
                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 4:
                    round67_anomalies.append(('2017_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("Every Saturday morning, at 9 am"):
                    round67_anomalies.append(('2017_ky2_t1_start', t1.get("content", "")[:50]))
                if "toprovidethe" in t1.get("content", ""):
                    round67_anomalies.append(('2017_ky2_t1_concats', 'toprovidethe present'))
                if "Andrew Baddeley" not in t1.get("content", ""):
                    round67_anomalies.append(('2017_ky2_t1_baddeley_text', 'missing'))

                # Text 2 (Screens & Mealtimes)
                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 4:
                    round67_anomalies.append(('2017_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("With so much focus on children's use of screens"):
                    round67_anomalies.append(('2017_ky2_t2_start', t2.get("content", "")[:50]))
                if "therest ofthe" in t2.get("content", ""):
                    round67_anomalies.append(('2017_ky2_t2_concats', 'therest ofthe present'))
                if "still face experiment" not in t2.get("content", "") or "Edward Tronick" not in t2.get("content", ""):
                    round67_anomalies.append(('2017_ky2_t2_content_phrases', 'missing'))

                # Text 3 (Gap Year)
                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 4:
                    round67_anomalies.append(('2017_ky2_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("Today, widespread social pressure to immediately go to college"):
                    round67_anomalies.append(('2017_ky2_t3_start', t3.get("content", "")[:60]))
                if "acclimation blunders" not in t3.get("content", ""):
                    round67_anomalies.append(('2017_ky2_t3_acclimation_text', 'missing'))

                # Text 4 (Wildfires)
                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 10:
                    round67_anomalies.append(('2017_ky2_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith("Though often viewed as a problem for western states"):
                    round67_anomalies.append(('2017_ky2_t4_start', t4.get("content", "")[:60]))
                if "take a magnifying glass to where we spend funds" not in t4.get("content", ""):
                    round67_anomalies.append(('2017_ky2_t4_magnifying_glass', 'missing'))

                # Part B (American Manufacturing)
                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 6:
                    round67_anomalies.append(('2017_ky2_pb_paras', len(pb_paras)))
                if not pb.get("content", "").startswith("The decline in American manufacturing is a common refrain"):
                    round67_anomalies.append(('2017_ky2_pb_start', pb.get("content", "")[:50]))
                if "Jay Dunwell" not in pb.get("content", "") or "Jason Stenquist" not in pb.get("content", "") or "Birgit Klohs" not in pb.get("content", ""):
                    round67_anomalies.append(('2017_ky2_pb_content', 'missing matching figures'))

            # Questions verification
            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round67_anomalies.append(('2017_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i or q.get('sort_order') != i:
                        round67_anomalies.append((f'2017_ky2_q{i}_number', q.get('question_number')))
                    
                    exp_pts = 0.5 if i <= 20 else 2.0
                    q_pts = float(q.get('score') or q.get('points') or 0)
                    if abs(q_pts - exp_pts) > 1e-4:
                        round67_anomalies.append((f'2017_ky2_q{i}_points', q_pts))
                    
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round67_anomalies.append((f'2017_ky2_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    
                    opts = q.get('options', [])
                    for opt in opts:
                        opt_k = opt.get('key', '')
                        opt_t = opt.get('text', '')
                        if opt_t in ['[A]', '[B]', '[C]', '[D]', 'A', 'B', 'C', 'D', ''] or len(opt_t.strip()) == 0:
                            round67_anomalies.append((f'2017_ky2_q{i}_placeholder_opt', opt_k))
                    
                    exp = q.get('explanation') or q.get('analysis') or ''
                    if len(exp.strip()) < 15:
                        round67_anomalies.append((f'2017_ky2_q{i}_explanation', 'insufficient'))

                # Official answers verification
                official_answers_ky2 = {
                    1: 'C', 2: 'A', 3: 'D', 4: 'A', 5: 'B',
                    6: 'B', 7: 'C', 8: 'A', 9: 'D', 10: 'C',
                    11: 'C', 12: 'B', 13: 'A', 14: 'D', 15: 'C',
                    16: 'D', 17: 'A', 18: 'B', 19: 'D', 20: 'B',
                    21: 'B', 22: 'D', 23: 'C', 24: 'B', 25: 'A',
                    26: 'A', 27: 'D', 28: 'C', 29: 'D', 30: 'B',
                    31: 'C', 32: 'A', 33: 'D', 34: 'B', 35: 'A',
                    36: 'A', 37: 'D', 38: 'C', 39: 'C', 40: 'B',
                    41: 'E', 42: 'A', 43: 'G', 44: 'B', 45: 'F'
                }
                for q_idx, exp_ans in official_answers_ky2.items():
                    act_ans = q_list[q_idx - 1].get('answer') or q_list[q_idx - 1].get('correct_answer')
                    if act_ans != exp_ans:
                        round67_anomalies.append((f'2017_ky2_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))

        if yr == 2018 and cat == 'ky1':
            if title != '2018年全国硕士研究生招生考试英语（一）真题':
                round68_anomalies.append(('2018_ky1_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round68_anomalies.append(('2018_ky1_total_score', data['exam'].get('total_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round68_anomalies.append(('2018_ky1_passages_count', len(p_list)))
            else:
                # Cloze
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 4:
                    round68_anomalies.append(('2018_ky1_cloze_paras', len(c_paras)))
                if "[1] for" in cloze.get("content", ""):
                    round68_anomalies.append(('2018_ky1_cloze_leaked_ans', 'present'))
                if not cloze.get("content", "").startswith("Trust is a tricky business."):
                    round68_anomalies.append(('2018_ky1_cloze_start', cloze.get("content", "")[:50]))

                # Text 1 (Automation & Middle Class)
                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 7:
                    round68_anomalies.append(('2018_ky1_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("Among the annoying challenges facing the middle class"):
                    round68_anomalies.append(('2018_ky1_t1_start', t1.get("content", "")[:50]))
                if re.search(r"\bon't dismiss\b", t1.get("content", "")) or "\\ The first step" in t1.get("content", ""):
                    round68_anomalies.append(('2018_ky1_t1_broken_text', 'present'))
                if "The Second Machine Age" not in t1.get("content", ""):
                    round68_anomalies.append(('2018_ky1_t1_second_machine_age', 'missing'))

                # Text 2 (Social Media & Media Literacy)
                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 6:
                    round68_anomalies.append(('2018_ky1_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("A new survey by Harvard University finds"):
                    round68_anomalies.append(('2018_ky1_t2_start', t2.get("content", "")[:50]))
                if re.search(r"\bniversity of Oxford\b", t2.get("content", "")) or re.search(r"\bnited States\b", t2.get("content", "")):
                    round68_anomalies.append(('2018_ky1_t2_broken_words', 'present'))
                if ". The phrase “beef up”" in t2.get("content", "") or ". The Barna survey found" in t2.get("content", ""):
                    round68_anomalies.append(('2018_ky1_t2_leaked_stems', 'present'))

                # Text 3 (NHS & DeepMind)
                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 4:
                    round68_anomalies.append(('2018_ky1_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("Any fair-minded assessment of the dangers of the deal between Britain's National Health Service (NHS) and DeepMind"):
                    round68_anomalies.append(('2018_ky1_t3_start', t3.get("content", "")[:60]))
                if "Social media allows users" in t3.get("content", ""):
                    round68_anomalies.append(('2018_ky1_t3_cross_contamination', 'present'))
                if "digital feudalism" not in t3.get("content", ""):
                    round68_anomalies.append(('2018_ky1_t3_digital_feudalism', 'missing'))

                # Text 4 (USPS Reform)
                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 4:
                    round68_anomalies.append(('2018_ky1_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith("The U. S. Postal Service (USPS) continues to bleed red ink."):
                    round68_anomalies.append(('2018_ky1_t4_start', t4.get("content", "")[:60]))
                if "unfunded liabilities" not in t4.get("content", "") or "Medicare" not in t4.get("content", ""):
                    round68_anomalies.append(('2018_ky1_t4_core_text', 'missing'))

                # Part B (EEOB)
                pb = p_list[5]
                pb_paras = [p for p in pb.get("content", "").split("\n\n") if p.strip()]
                if len(pb_paras) != 7:
                    round68_anomalies.append(('2018_ky1_pb_paras', len(pb_paras)))
                if not pb.get("content", "").startswith("[A] In December of 1869, Congress appointed a commission"):
                    round68_anomalies.append(('2018_ky1_pb_start', pb.get("content", "")[:50]))
                if "Directions:" in pb.get("content", "") or "[41] -> [C]" in pb.get("content", ""):
                    round68_anomalies.append(('2018_ky1_pb_directions_leak', 'present'))

            # Questions verification
            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round68_anomalies.append(('2018_ky1_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i or q.get('sort_order') != i:
                        round68_anomalies.append((f'2018_ky1_q{i}_number', q.get('question_number')))
                    
                    exp_pts = 0.5 if i <= 20 else 2.0
                    q_pts = float(q.get('score') or q.get('points') or 0)
                    if abs(q_pts - exp_pts) > 1e-4:
                        round68_anomalies.append((f'2018_ky1_q{i}_points', q_pts))
                    
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round68_anomalies.append((f'2018_ky1_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    
                    opts = q.get('options', [])
                    for opt in opts:
                        opt_k = opt.get('key', '')
                        opt_t = opt.get('text', '')
                        if opt_t in ['[A]', '[B]', '[C]', '[D]', 'A', 'B', 'C', 'D', ''] or len(opt_t.strip()) == 0:
                            round68_anomalies.append((f'2018_ky1_q{i}_placeholder_opt', opt_k))
                        if 41 <= i <= 45 and 'playhouse' in opt_t.lower():
                            round68_anomalies.append((f'2018_ky1_q{i}_hallucinated_part_b', opt_k))
                    
                    exp = q.get('explanation') or q.get('analysis') or ''
                    if len(exp.strip()) < 15:
                        round68_anomalies.append((f'2018_ky1_q{i}_explanation', 'insufficient'))

                # Official answers verification
                official_answers_2018_ky1 = {
                    1: 'C', 2: 'A', 3: 'D', 4: 'B', 5: 'D',
                    6: 'B', 7: 'C', 8: 'D', 9: 'B', 10: 'A',
                    11: 'B', 12: 'B', 13: 'A', 14: 'C', 15: 'D',
                    16: 'A', 17: 'C', 18: 'B', 19: 'A', 20: 'C',
                    21: 'D', 22: 'C', 23: 'A', 24: 'D', 25: 'B',
                    26: 'D', 27: 'A', 28: 'B', 29: 'C', 30: 'A',
                    31: 'B', 32: 'C', 33: 'D', 34: 'D', 35: 'B',
                    36: 'B', 37: 'A', 38: 'A', 39: 'C', 40: 'D',
                    41: 'E', 42: 'G', 43: 'A', 44: 'B', 45: 'D'
                }
                for q_idx, exp_ans in official_answers_2018_ky1.items():
                    act_ans = q_list[q_idx - 1].get('answer') or q_list[q_idx - 1].get('correct_answer')
                    if act_ans != exp_ans:
                        round68_anomalies.append((f'2018_ky1_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))

        if yr == 2018 and cat == 'ky2':
            if title != '2018年全国硕士研究生招生考试英语（二）真题':
                round69_anomalies.append(('2018_ky2_title', title))
            if float(data['exam'].get('total_score', 0)) != 60.0:
                round69_anomalies.append(('2018_ky2_total_score', data['exam'].get('total_score')))
            if float(data['exam'].get('pass_score', 0)) != 36.0:
                round69_anomalies.append(('2018_ky2_pass_score', data['exam'].get('pass_score')))

            p_list = data.get("passages", [])
            if len(p_list) != 6:
                round69_anomalies.append(('2018_ky2_passages_count', len(p_list)))
            else:
                # Cloze (5 paras, 350 words)
                cloze = p_list[0]
                c_paras = [p for p in cloze.get("content", "").split("\n\n") if p.strip()]
                if len(c_paras) != 5:
                    round69_anomalies.append(('2018_ky2_cloze_paras', len(c_paras)))
                if not cloze.get("content", "").startswith("Why do people read negative Internet comments"):
                    round69_anomalies.append(('2018_ky2_cloze_start', cloze.get("content", "")[:50]))
                if "each participant were shown 10 pens" in cloze.get("content", ""):
                    round69_anomalies.append(('2018_ky2_cloze_hallucination', 'present'))

                # Text 1 (Vocational Ed / Koziatek, 8 paras, 370 words)
                t1 = p_list[1]
                t1_paras = [p for p in t1.get("content", "").split("\n\n") if p.strip()]
                if len(t1_paras) != 8:
                    round69_anomalies.append(('2018_ky2_t1_paras', len(t1_paras)))
                if not t1.get("content", "").startswith("It is curious that Stephen Koziatek feels almost as though"):
                    round69_anomalies.append(('2018_ky2_t1_start', t1.get("content", "")[:50]))
                if len(t1_paras) >= 5 and "On one hand, that viewpoint is a logical product of America's evolution" not in t1_paras[4]:
                    round69_anomalies.append(('2018_ky2_t1_para5_q23_alignment', 'missing'))

                # Text 2 (Renewable Energy, 7 paras, 416 words)
                t2 = p_list[2]
                t2_paras = [p for p in t2.get("content", "").split("\n\n") if p.strip()]
                if len(t2_paras) != 7:
                    round69_anomalies.append(('2018_ky2_t2_paras', len(t2_paras)))
                if not t2.get("content", "").startswith("While fossil fuels - coal, oil, gas - still generate roughly 85 percent"):
                    round69_anomalies.append(('2018_ky2_t2_start', t2.get("content", "")[:50]))
                if "plummeting prices of renewables" not in t2.get("content", ""):
                    round69_anomalies.append(('2018_ky2_t2_plummeting', 'missing'))

                # Text 3 (Digital Giants, 4 paras, 412 words)
                t3 = p_list[3]
                t3_paras = [p for p in t3.get("content", "").split("\n\n") if p.strip()]
                if len(t3_paras) != 4:
                    round69_anomalies.append(('2018_ky2_t3_paras', len(t3_paras)))
                if not t3.get("content", "").startswith("The power and ambition of the giants of the digital economy is astonishing"):
                    round69_anomalies.append(('2018_ky2_t3_start', t3.get("content", "")[:50]))
                if "very slow compared to the pace of change within the digital economy. By the time a problem has been addressed" not in t3.get("content", ""):
                    round69_anomalies.append(('2018_ky2_t3_truncated_clause', 'missing'))
                if "notlink" in t3.get("content", "") or "toFacebook" in t3.get("content", ""):
                    round69_anomalies.append(('2018_ky2_t3_glued_words', 'present'))

                # Text 4 (Deep Work, 7 paras, 439 words)
                t4 = p_list[4]
                t4_paras = [p for p in t4.get("content", "").split("\n\n") if p.strip()]
                if len(t4_paras) != 7:
                    round69_anomalies.append(('2018_ky2_t4_paras', len(t4_paras)))
                if not t4.get("content", "").startswith("To combat the trap of putting a premium on being busy, Cal Newport"):
                    round69_anomalies.append(('2018_ky2_t4_start', t4.get("content", "")[:50]))
                if 'Newport also recommends "deep scheduling" to combat constant interruptions' not in t4.get("content", ""):
                    round69_anomalies.append(('2018_ky2_t4_deep_scheduling', 'missing'))
                if "rethink Tim Harford" in t4.get("content", ""):
                    round69_anomalies.append(('2018_ky2_t4_rethink_truncation', 'present'))

                # Part B (Five Ways to Make Conversation, 584 words)
                pb = p_list[5]
                if not pb.get("content", "").startswith("Five Ways to Make Conversation with Anyone"):
                    round69_anomalies.append(('2018_ky2_pb_start', pb.get("content", "")[:50]))
                if "Directions:" in pb.get("content", "") or "10 points" in pb.get("content", ""):
                    round69_anomalies.append(('2018_ky2_pb_directions_leak', 'present'))

            # Questions verification
            q_list = data.get("questions", [])
            if len(q_list) != 45:
                round69_anomalies.append(('2018_ky2_questions_count', len(q_list)))
            else:
                for i, q in enumerate(q_list, 1):
                    if q.get('question_number') != i or q.get('sort_order') != i:
                        round69_anomalies.append((f'2018_ky2_q{i}_number', q.get('question_number')))
                    
                    exp_pts = 0.5 if i <= 20 else 2.0
                    q_pts = float(q.get('score') or q.get('points') or 0)
                    if abs(q_pts - exp_pts) > 1e-4:
                        round69_anomalies.append((f'2018_ky2_q{i}_points', q_pts))
                    
                    exp_type = 'cloze_item' if i <= 20 else 'reading_item'
                    if q.get('question_type') != exp_type and q.get('q_type') != exp_type:
                        round69_anomalies.append((f'2018_ky2_q{i}_q_type', q.get('question_type') or q.get('q_type')))
                    
                    opts = q.get('options', [])
                    for opt in opts:
                        opt_k = opt.get('key', '')
                        opt_t = opt.get('text', '')
                        if opt_t in ['[A]', '[B]', '[C]', '[D]', 'A', 'B', 'C', 'D', ''] or len(opt_t.strip()) == 0:
                            round69_anomalies.append((f'2018_ky2_q{i}_placeholder_opt', opt_k))
                    
                    exp = q.get('explanation') or q.get('analysis') or ''
                    if len(exp.strip()) < 15:
                        round69_anomalies.append((f'2018_ky2_q{i}_explanation', 'insufficient'))

                # Official answers verification
                official_answers_2018_ky2 = {
                    1: 'C', 2: 'A', 3: 'B', 4: 'A', 5: 'D',
                    6: 'A', 7: 'B', 8: 'C', 9: 'D', 10: 'B',
                    11: 'A', 12: 'B', 13: 'D', 14: 'C', 15: 'C',
                    16: 'C', 17: 'D', 18: 'A', 19: 'C', 20: 'B',
                    21: 'A', 22: 'C', 23: 'B', 24: 'D', 25: 'A',
                    26: 'B', 27: 'B', 28: 'D', 29: 'C', 30: 'A',
                    31: 'D', 32: 'C', 33: 'C', 34: 'B', 35: 'D',
                    36: 'C', 37: 'C', 38: 'A', 39: 'B', 40: 'D',
                    41: 'A', 42: 'C', 43: 'E', 44: 'B', 45: 'F'
                }
                for q_idx, exp_ans in official_answers_2018_ky2.items():
                    act_ans = q_list[q_idx - 1].get('answer') or q_list[q_idx - 1].get('correct_answer')
                    if act_ans != exp_ans:
                        round69_anomalies.append((f'2018_ky2_q{q_idx}_answer', f"Expected {exp_ans}, got {act_ans}"))


        passages = data.get('passages', [])
        questions = data.get('questions', [])

        total_passages += len(passages)
        total_questions += len(questions)

        # Audit Passages
        for p in passages:
            pt = p.get('title', '')
            c = p.get('content', '')

            # 7. Leaked options in Part A
            if 'Part A' in pt:
                leaks = re.findall(r'\[[A-G][\]J]|\([A-G]\)', c)
                if leaks:
                    part_a_leaked_options.append((title, pt, leaks))

            # 8. Leaked phonetics / glosses
            ph = re.findall(r'(\([a-z]+\s*\[[^\]]+\]\s*[a-z]\.?\)?|\[[’\'][^\]]+\]\s*[a-z]\.?|\[[a-z\s\:\,\'\-]{4,}\]\s*[a-z]\.?)', c)
            if ph:
                gloss_phonetics_found.append((title, pt, ph))

            # Check 26 in passages: o£, th&r, 44...
            if 'o£' in c or 'th&r' in c or 's e n no os' in c:
                ocr_corruptions_found.append((title, pt, 'corrupted_string_in_passage'))

        # Check 25: Duplicate options in Q1-Q40
        opt_history = {}
        for q in questions:
            so = q.get('sort_order')
            opts = q.get('options')
            if so in range(1, 41) and isinstance(opts, list):
                opt_texts = tuple(sorted([str(o.get('text', '')).strip().lower() for o in opts]))
                if opt_texts in opt_history and len(opt_texts) > 1:
                    duplicate_cloze_reading_options.append((title, so, opt_history[opt_texts], opt_texts))
                else:
                    opt_history[opt_texts] = so

        p_ids = {p['id'] for p in passages}
        for q in questions:
            so = q.get('sort_order')
            stem = (q.get('stem') or '').strip()
            ans = q.get('correct_answer')
            expl = q.get('explanation') or ''
            opts = q.get('options') or []

            # 4. correct_answer == answer
            if ans != q.get('answer'):
                mismatched_answers.append((title, so, ans, q.get('answer')))

            # 5. Redundant prefix
            if re.match(r'^(?:\d+[\.\、\s]|第\d+题|Q\d+)', stem):
                stems_with_prefix.append((title, so, stem[:30]))

            # 6. Cloze stem standard
            if so in range(1, 21):
                if not re.match(r'^Choose the best option for blank \[\d+\] in the passage:$', stem):
                    non_standard_cloze_stems.append((title, so, stem))

            # 18. Canonical option order
            if isinstance(opts, list):
                keys = [o.get('key') for o in opts if 'key' in o]
                if keys != sorted(keys) and keys != ['T', 'F']:
                    non_canonical_option_orders.append((title, so, keys))

            # 21. Topology
            if q.get('passage_id') not in p_ids:
                orphan_questions.append((title, so, q.get('passage_id')))

            # 23. Truncated stems
            if so > 20:
                if stem.endswith('-') or stem.endswith('—') or stem.endswith('/'):
                    truncated_stems_found.append((title, so, 'ends_with_hyphen', stem))
                elif stem.endswith('closest to') or stem.endswith('closest in') or stem.endswith('mean by') or stem.endswith('smiling for') or stem.endswith('Generation'):
                    truncated_stems_found.append((title, so, 'cut_off_phrase', stem))

            # 24. Option sanity
            texts = [o.get('text', '').strip() for o in opts]
            if len(texts) != len(set(texts)) and len(texts) > 0:
                semantic_conflicts.append((title, so, 'duplicate_options', texts))
            if any(len(t) == 0 for t in texts):
                semantic_conflicts.append((title, so, 'empty_option', texts))

            # 26. Check o£, th&r, 44 quote
            all_q_text = stem + " " + expl + " " + " ".join(texts)
            if 'o£' in all_q_text or 'th&r' in all_q_text:
                ocr_corruptions_found.append((title, so, 'o£_or_th&r_found'))
            if re.search(r'44[\u4e00-\u9fa5a-zA-Z]', all_q_text):
                ocr_corruptions_found.append((title, so, '44_quote_found'))

            # 27. Part B check
            if so in range(41, 46):
                # Verify specific gold-standard Part B answers
                if yr == 2013 and cat == 'ky1':
                    expected = {41: 'E', 42: 'F', 43: 'D', 44: 'G', 45: 'A'}
                    if ans != expected[so]:
                        part_b_anomalies.append((title, so, ans, expected[so]))
                if yr == 2014 and cat == 'ky1':
                    expected = {41: 'C', 42: 'F', 43: 'G', 44: 'D', 45: 'B'}
                    if ans != expected[so]:
                        part_b_anomalies.append((title, so, ans, expected[so]))
                if yr == 2013 and cat == 'ky2':
                    expected = {41: 'F', 42: 'C', 43: 'G', 44: 'A', 45: 'B'}
                    if ans != expected[so]:
                        part_b_anomalies.append((title, so, ans, expected[so]))
                    if 'regarding' in stem:
                        part_b_anomalies.append((title, so, 'spoiler_in_stem', stem))

            # 28. Commercial watermarks
            if 'shop249445206' in expl or 'taobao.com' in expl or '新一文化' in expl:
                watermark_hits.append((title, so, 'watermark_in_explanation'))

            # 29. Trailing middle dots
            for opt in opts:
                ot = opt.get('text', '')
                if ot.endswith('・') or ot.endswith('•') or ot.endswith('·'):
                    trailing_dot_opts.append((title, so, opt.get('key'), ot))

            # 30. 2004 Cloze real explanation
            if yr == 2004 and cat == 'ky1' and so in range(1, 21):
                if '精确契合语境' in expl or len(expl) < 200:
                    cloze_2004_placeholders.append((title, so, expl))

            # 31. 2014 Cloze Q8 check
            if yr == 2014 and cat == 'ky1' and so == 8:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'D' or 'functions' not in opt_texts or 'rigid bodies' in expl:
                    cloze_2014_q8_anomalies.append((title, so, ans, opt_texts, expl[:50]))

            # 32. Key official answers gold standard
            if yr == 2010 and cat == 'ky1' and so == 26:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'C' or 'the possible restriction on their granting' not in opt_texts:
                    round12_core_anomalies.append(('2010_q26', ans, opt_texts))
            if yr == 2012 and cat == 'ky1' and so == 40:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'A' or 'disapproval' not in opt_texts:
                    round12_core_anomalies.append(('2012_q40', ans, opt_texts))
            if yr == 2016 and cat == 'ky1' and so == 1 and ans != 'A':
                round12_core_anomalies.append(('2016_q1', ans))
            if yr == 2017 and cat == 'ky1' and so == 14 and ans != 'B':
                round12_core_anomalies.append(('2017_q14', ans))
            if yr == 2013 and cat == 'ky1' and so == 2 and ans != 'B':
                round12_core_anomalies.append(('2013_q2', ans))

            # 33. 2011 cloze & reading calibration
            if yr == 2011 and cat == 'ky1' and so == 7:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'A' or 'opposite' not in opt_texts:
                    round12_core_anomalies.append(('2011_q7', ans, opt_texts))
            if yr == 2011 and cat == 'ky1' and so == 8:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'D' or 'relaxes' not in opt_texts:
                    round12_core_anomalies.append(('2011_q8', ans, opt_texts))
            if yr == 2011 and cat == 'ky1' and so == 40:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'B' or 'Celebrity moms have influenced our attitude towards child rearing.' not in opt_texts:
                    round12_core_anomalies.append(('2011_q40', ans, opt_texts))

            # 34. 2004 cloze 20 questions gold standard
            if yr == 2004 and cat == 'ky1' and so == 1:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'C' or 'centering' not in opt_texts:
                    round12_core_anomalies.append(('2004_q1', ans, opt_texts))
            if yr == 2004 and cat == 'ky1' and so == 13:
                opt_texts = [o.get('text') for o in opts]
                if ans != 'D' or 'experienced' not in opt_texts:
                    round12_core_anomalies.append(('2004_q13', ans, opt_texts))

            # 35. Round 13 25 questions calibration check
            if yr == 2017 and cat == 'ky1' and so == 38:
                if len(opts) != 4 or ans != 'A' or len(expl) < 500 or not any('justified in addressing' in o.get('text', '') for o in opts):
                    round13_anomalies.append(('2017_q38', ans, len(expl)))
            if yr == 2016 and cat == 'ky1' and so == 45:
                if len(expl) < 300 or 'Make it efficient' not in expl:
                    round13_anomalies.append(('2016_q45', len(expl)))
            if yr == 2002 and cat == 'ky1' and so == 30:
                if len(opts) != 4 or ans != 'C' or len(expl) < 400 or ('far from reaching human mental standards' not in [o.get('text') for o in opts] and 'far less able than human brain in focusing on relevant information' not in [o.get('text') for o in opts]):
                    round13_anomalies.append(('2002_q30', ans, len(expl)))
            if yr == 2010 and cat == 'ky1' and so == 25:
                if len(opts) != 4 or ans != 'B' or len(expl) < 400 or 'The Lost Horizon in Newspapers' not in [o.get('text') for o in opts]:
                    round13_anomalies.append(('2010_q25', ans, len(expl)))
            if yr == 2009 and cat == 'ky1' and so in [43, 44]:
                if len(expl) < 300 or expl.endswith('、'):
                    round13_anomalies.append((f'2009_q{so}', len(expl)))
            if yr == 2020 and cat == 'ky1' and so == 29:
                if len(expl) < 600 or '开放获取模式实质上还是出版商的盈利工具' not in expl:
                    round13_anomalies.append(('2020_q29', len(expl)))
            if yr == 2021 and cat == 'ky2' and so in [21, 23, 24, 25]:
                if len(expl) < 400 or '事实细节:' in expl:
                    round13_anomalies.append((f'2021_ky2_q{so}', len(expl)))
            if yr == 2022 and cat == 'ky1' and so in [27, 32, 36, 37, 38, 39]:
                if len(expl) < 400 or '段落主旨\n' in expl or '写作目的\n' in expl:
                    round13_anomalies.append((f'2022_ky1_q{so}', len(expl)))
            if yr == 2022 and cat == 'ky2' and so in [21, 22, 23, 24, 26, 27, 28, 29]:
                if len(expl) < 250 or '事实细节:' in expl:
                    round13_anomalies.append((f'2022_ky2_q{so}', len(expl)))

            # Check Round 14: 2004 Reading Q21-Q40
            if yr == 2004 and cat == 'ky1' and so in range(21, 41):
                expected_ans_2004 = {
                    21: 'C', 22: 'A', 23: 'D', 24: 'B', 25: 'C',
                    26: 'A', 27: 'D', 28: 'C', 29: 'B', 30: 'D',
                    31: 'D', 32: 'A', 33: 'B', 34: 'A', 35: 'C',
                    36: 'C', 37: 'A', 38: 'D', 39: 'B', 40: 'C'
                }
                if ans != expected_ans_2004.get(so):
                    round14_2004_reading_anomalies.append((f'2004_q{so}_ans', ans, expected_ans_2004.get(so)))
                if len(expl) < 300 or '【精准定位】' not in expl:
                    round14_2004_reading_anomalies.append((f'2004_q{so}_expl_len', len(expl)))
                if '⿼㡿' in expl or '⿼' in expl:
                    round14_2004_reading_anomalies.append((f'2004_q{so}_garbage', 'found'))

            # Check Round 15: Zero leaked translations, zero commerce watermarks, authentic 2005 Q25
            bad_patterns_round15 = ['掌柜', '旺旺', '淘宝', '店铺', '新一文化', '全文翻译', '长难句分析', '核心词与超纲词', '核心词汇与超纲词汇', '文章题材结构分析', '【翻译】', '【长难句分析】']
            for bp in bad_patterns_round15:
                if bp in expl:
                    round15_anomalies.append((f"{yr}_{cat}_q{so}", f"bad_pattern_{bp}"))

            if yr == 2005 and cat == 'ky1' and so == 25:
                if stem != "What can we infer from the last paragraph?" or ans != 'B':
                    round15_anomalies.append(('2005_q25_stem_or_ans', stem, ans))
                if len(expl) < 400 or '【精准定位】' not in expl:
                    round15_anomalies.append(('2005_q25_expl', len(expl)))
            if yr == 2004 and cat == 'ky1' and so == 20:
                if not expl.endswith('假如下雨，你会怎么办呢？'):
                    round15_anomalies.append(('2004_q20_not_truncated', expl[-50:]))
            if yr == 2004 and cat == 'ky1' and so == 40:
                if not expl.endswith('捏造它们与才智之间的关系（evolves from 和 underlies）。'):
                    round15_anomalies.append(('2004_q40_not_truncated', expl[-50:]))
            if yr == 2007 and cat == 'ky1' and so == 45:
                expl_norm = re.sub(r'\s+', '', expl)
                if not expl_norm.endswith('最后要教会孩子在面对挫折和失败时如何解决问题（E）。'):
                    round15_anomalies.append(('2007_q45_not_truncated', expl[-50:]))
            if yr == 2008 and cat == 'ky1' and so == 43:
                if '掌柜' in expl:
                    round15_anomalies.append(('2008_q43_watermark', expl[-30:]))
            if yr == 2008 and cat == 'ky1' and so == 45:
                expl_norm = re.sub(r'\s+', '', expl)
                if not (expl.startswith('［精准定位］') or expl_norm.endswith('确定答案E后，我们马上可以排除F。')):
                    round15_anomalies.append(('2008_q45_not_truncated', expl[-50:]))
            if yr == 2009 and cat == 'ky1' and so == 41:
                if '【空格推测】' not in expl or '【答案敲定】' not in expl or len(expl) < 200:
                    round15_anomalies.append(('2009_q41_expl_incomplete', len(expl)))
            if yr == 2012 and cat == 'ky1' and so == 25:
                expl_norm = re.sub(r'\s+', '', expl)
                if not expl_norm.endswith('由此可以看出，作者对于peerpressure的影响持质疑态度，故答案选D。'):
                    round15_anomalies.append(('2012_q25_not_truncated', expl[-50:]))
            if yr == 2012 and cat == 'ky1' and so in range(41, 46):
                if '【空格推测】' not in expl or '【答案敲定】' not in expl or len(expl) < 150:
                    round15_anomalies.append((f'2012_q{so}_expl_incomplete', len(expl)))

            # Check Round 16: Zero placeholders and authentic options/answers
            opt_map = {o.get('key'): o.get('text', '').strip() for o in opts if isinstance(o, dict)}
            for ok, ov in opt_map.items():
                if 'Verified standard' in ov or '占位' in ov:
                    round16_anomalies.append((f"{yr}_{cat}_q{so}", f"placeholder_opt_{ok}"))

            if yr == 2017 and cat == 'ky1' and so == 39:
                if not stem.endswith('________.') or ans != 'B' or 'fair play in official access' not in opt_map.get('B', ''):
                    round16_anomalies.append(('2017_q39_stem_or_ans', stem, ans, opt_map.get('B')))
                if 'In the year and a half' in expl or 'Text 4' in expl:
                    round16_anomalies.append(('2017_q39_expl_bleeding', expl[-100:]))
            if yr == 2017 and cat == 'ky1' and so == 40:
                if not stem.endswith('________.') or ans != 'D' or opt_map.get('D') != 'supportive':
                    round16_anomalies.append(('2017_q40_stem_or_ans', stem, ans, opt_map.get('D')))
            if yr == 2006 and cat == 'ky1' and so == 20:
                if ans != 'D' or opt_map.get('D') != 'coordination':
                    round16_anomalies.append(('2006_q20_ans_or_opts', ans, opt_map))
            if yr == 2008 and cat == 'ky1' and so == 20:
                if ans != 'A' or opt_map.get('A') != 'paradoxical':
                    round16_anomalies.append(('2008_q20_ans_or_opts', ans, opt_map))
            if yr == 2003 and cat == 'ky1' and so == 2:
                if ans != 'B' or opt_map.get('B') != 'accommodate':
                    round16_anomalies.append(('2003_q2_ans_or_opts', ans, opt_map))
            if yr == 2003 and cat == 'ky1' and so == 9:
                if ans != 'A' or opt_map.get('A') != 'displaying':
                    round16_anomalies.append(('2003_q9_ans_or_opts', ans, opt_map))
            if yr == 2020 and cat == 'ky1' and so == 23:
                if ans != 'D' or 'commits to its long-term growth' not in opt_map.get('D', ''):
                    round16_anomalies.append(('2020_q23_ans_or_opts', ans, opt_map.get('D')))
            if yr == 2020 and cat == 'ky1' and so == 25:
                if ans != 'C' or opt_map.get('C') != 'Favourable':
                    round16_anomalies.append(('2020_q25_ans_or_opts', ans, opt_map.get('C')))
            if yr == 2020 and cat == 'ky1' and so == 28:
                if ans != 'C' or opt_map.get('C') != 'Concerned.':
                    round16_anomalies.append(('2020_q28_ans_or_opts', ans, opt_map.get('C')))
            if yr == 2018 and cat == 'ky1':
                if so == 24 and ans != 'D': round16_anomalies.append(('2018_q24_ans', ans))
                if so == 27 and ans != 'A': round16_anomalies.append(('2018_q27_ans', ans))
                if so == 30 and ans != 'A': round16_anomalies.append(('2018_q30_ans', ans))
                if so == 34 and ans != 'D': round16_anomalies.append(('2018_q34_ans', ans))
                if so == 40 and ans != 'D': round16_anomalies.append(('2018_q40_ans', ans))
            if yr == 2002 and cat == 'ky1':
                if so == 31 and ans != 'B': round16_anomalies.append(('2002_q31_ans', ans))
                if so == 32 and ans != 'D': round16_anomalies.append(('2002_q32_ans', ans))
                if so == 38 and ans != 'B': round16_anomalies.append(('2002_q38_ans', ans))
            if yr == 2010 and cat == 'ky1' and so == 27 and ans != 'D':
                round16_anomalies.append(('2010_q27_ans', ans))
            if yr == 2021 and cat == 'ky1' and so == 24 and ans != 'D':
                round16_anomalies.append(('2021_q24_ans', ans))
            if yr == 2012 and cat == 'ky1':
                if so == 33 and ans != 'B': round16_anomalies.append(('2012_q33_ans', ans))
                if so == 35 and ans != 'C': round16_anomalies.append(('2012_q35_ans', ans))
            if yr == 2022 and cat == 'ky2':
                if so in range(1, 21):
                    if len(expl) < 100 or '事实细节:' in expl:
                        round16_anomalies.append((f'2022_ky2_cloze_q{so}', len(expl)))
                if so == 32 and ans != 'D': round16_anomalies.append(('2022_ky2_q32_ans', ans))
                if so == 38 and ans != 'D': round16_anomalies.append(('2022_ky2_q38_ans', ans))
                if so == 40 and ans != 'C': round16_anomalies.append(('2022_ky2_q40_ans', ans))

            # Check Round 17: 2005 cloze authentic options, un-truncated stems
            if yr == 2005 and cat == 'ky1':
                if so == 4 and (ans != 'C' or opt_map.get('C') != 'missing'):
                    round17_anomalies.append(('2005_q4_ans_or_opts', ans, opt_map))
                if so == 5 and (ans != 'B' or opt_map.get('B') != 'though'):
                    round17_anomalies.append(('2005_q5_ans_or_opts', ans, opt_map))
                if so == 9 and (ans != 'D' or opt_map.get('D') != 'whereas'):
                    round17_anomalies.append(('2005_q9_ans_or_opts', ans, opt_map))
                if so == 11 and (ans != 'C' or opt_map.get('C') != 'messages' or not expl.startswith('11.')):
                    round17_anomalies.append(('2005_q11_ans_or_opts_or_expl', ans, opt_map.get('C'), expl[:30]))
                if so == 12 and (ans != 'A' or opt_map.get('A') != 'at first' or not expl.startswith('12.')):
                    round17_anomalies.append(('2005_q12_ans_or_opts_or_expl', ans, opt_map.get('A'), expl[:30]))
                if so == 13 and (ans != 'D' or opt_map.get('D') != 'exposed'):
                    round17_anomalies.append(('2005_q13_ans_or_opts', ans, opt_map))
                if so == 14 and (ans != 'C' or opt_map.get('C') != 'inefficient'):
                    round17_anomalies.append(('2005_q14_ans_or_opts', ans, opt_map))
                if so == 15 and (ans != 'D' or opt_map.get('D') != 'create'):
                    round17_anomalies.append(('2005_q15_ans_or_opts', ans, opt_map))
                if so == 16 and (ans != 'B' or opt_map.get('B') != 'also'):
                    round17_anomalies.append(('2005_q16_ans_or_opts', ans, opt_map))
                if so == 17 and (ans != 'C' or opt_map.get('C') != 'aware'):
                    round17_anomalies.append(('2005_q17_ans_or_opts', ans, opt_map))
                if so == 18 and (ans != 'D' or opt_map.get('D') != 'notice'):
                    round17_anomalies.append(('2005_q18_ans_or_opts', ans, opt_map))
                if so == 19 and (ans != 'A' or opt_map.get('A') != 'available'):
                    round17_anomalies.append(('2005_q19_ans_or_opts', ans, opt_map))
                if so == 20 and (ans != 'B' or opt_map.get('B') != 'such as'):
                    round17_anomalies.append(('2005_q20_ans_or_opts', ans, opt_map))
                if so == 22:
                    if not stem.endswith('________.') or 'it is all too monkey' not in stem or ans != 'B':
                        round17_anomalies.append(('2005_q22_stem_or_ans', stem, ans))
                    if opt_map.get('A') != 'monkeys are also outraged by slack rivals' or opt_map.get('B') != "resenting unfairness is also monkeys' nature":
                        round17_anomalies.append(('2005_q22_opts', opt_map))
            if yr == 2003 and cat == 'ky1' and so == 23:
                if stem != 'The phrase "making the biggest splash" (Line 1, Paragraph 3) most probably means ________.':
                    round17_anomalies.append(('2003_q23_stem', stem))
            if yr == 2006 and cat == 'ky1' and so == 28:
                if stem != 'By saying "Stratford cries poor traditionally" (Line 2, Paragraph 4), the author implies that ________.':
                    round17_anomalies.append(('2006_q28_stem', stem))
                if opt_map.get('A') != 'Stratford cannot afford the expansion projects':
                    round17_anomalies.append(('2006_q28_opt_A', opt_map.get('A')))
            if yr == 2006 and cat == 'ky1' and so == 33:
                if stem != 'By saying "these figures are conservative" (Line 1, Paragraph 3), Dr. Worm means that ________.':
                    round17_anomalies.append(('2006_q33_stem', stem))
                if opt_map.get('D') != 'the data collected so far are out of date':
                    round17_anomalies.append(('2006_q33_opt_D', opt_map.get('D')))

            # Check Round 18: 2011 ky1, 2014 ky1, 2001 ky1 authentic options & answers
            if yr == 2011 and cat == 'ky1':
                if so == 21 and (ans != 'C' or opt_map.get('C') != 'received acclaim'):
                    round18_anomalies.append(('2011_q21', ans, opt_map))
                if so == 22 and (ans != 'B' or opt_map.get('B') != 'modest'):
                    round18_anomalies.append(('2011_q22', ans, opt_map))
                if so == 23 and (ans != 'D' or opt_map.get('D') != 'overestimate the value of live performances'):
                    round18_anomalies.append(('2011_q23', ans, opt_map))
                if so == 32 and (ans != 'C' or opt_map.get('C') != 'strong user traffic'):
                    round18_anomalies.append(('2011_q32', ans, opt_map))
                if so == 33 and (ans != 'B' or opt_map.get('B') != 'can be used to produce negative effects in marketing'):
                    round18_anomalies.append(('2011_q33', ans, opt_map))
                if so == 35 and (ans != 'A' or opt_map.get('A') != 'Alternatives to conventional paid media.'):
                    round18_anomalies.append(('2011_q35', ans, opt_map))
            if yr == 2014 and cat == 'ky1':
                if so == 31 and (ans != 'B' or opt_map.get('B') != 'a handsome reward for researchers'):
                    round18_anomalies.append(('2014_q31', ans, opt_map))
                if so == 32 and (ans != 'C' or opt_map.get('C') != 'the founders of the new awards'):
                    round18_anomalies.append(('2014_q32', ans, opt_map))
                if so == 33 and (ans != 'C' or opt_map.get('C') != 'the joint effort of modern researchers'):
                    round18_anomalies.append(('2014_q33', ans, opt_map))
                if so == 39 and (ans != 'C' or opt_map.get('C') != 'biased against classical liberal ideas' or not (expl.startswith('［精准定位］') or expl.startswith('【精准定位】'))):
                    round18_anomalies.append(('2014_q39', ans, opt_map, expl[:30]))
                if so == 40 and (ans != 'B' or opt_map.get('B') != 'Illiberal Education and "The Heart of the Matter"' or not (expl.startswith('［精准定位］') or expl.startswith('【精准定位】'))):
                    round18_anomalies.append(('2014_q40', ans, opt_map, expl[:30]))
            if yr == 2001 and cat == 'ky1':
                if so == 32 and (ans != 'A' or opt_map.get('A') != 'failure to realize its real problem'):
                    round18_anomalies.append(('2001_q32', ans, opt_map))
                if so == 40 and (ans != 'D' or opt_map.get('D') != 'the economic situation'):
                    round18_anomalies.append(('2001_q40', ans, opt_map))

            # Check Round 20: 2006/2007/2008/2009/2014/2021 option truncations, stems & OCR repairs
            if yr == 2007 and cat == 'ky1':
                if so == 4 and opt_map.get('C') != 'open (to)':
                    round20_anomalies.append(('2007_q4_opt_C', opt_map.get('C')))
                if so == 8 and (ans != 'A' or opt_map.get('A') != 'freedom' or opt_map.get('D') != 'reform'):
                    round20_anomalies.append(('2007_q8_ans_or_opts', ans, opt_map))
                if so == 15 and (ans != 'B' or opt_map.get('B') != 'cry' or opt_map.get('A') != 'support'):
                    round20_anomalies.append(('2007_q15_ans_or_opts', ans, opt_map))
                if so == 23 and opt_map.get('C') != 'is determined by genetic rather than psychological factors':
                    round20_anomalies.append(('2007_q23_opt_C', opt_map.get('C')))
                if so == 26 and opt_map.get('C') != 'Telling the differences between certain concepts.':
                    round20_anomalies.append(('2007_q26_opt_C', opt_map.get('C')))
                if so == 27 and (stem != 'What can be inferred about intelligence testing from Paragraph 3?' or opt_map.get('D') != 'Scientists have defined the important elements of human intelligence.'):
                    round20_anomalies.append(('2007_q27', stem, opt_map.get('D')))
                if so == 28 and (not stem.endswith('________.') or not opt_map.get('A', '').endswith('computational procedures') or not opt_map.get('B', '').endswith('emphasized now')):
                    round20_anomalies.append(('2007_q28', stem, opt_map))
                if so == 29 and (not stem.endswith('________.') or opt_map.get('A') != "test scores may not be reliable indicators of one's ability" or opt_map.get('B') != 'IQ scores and SAT results are highly correlated'):
                    round20_anomalies.append(('2007_q29', stem, opt_map))
                if so == 32 and (opt_map.get('C') != 'less chance to invest' or not stem.endswith('________.')):
                    round20_anomalies.append(('2007_q32', stem, opt_map.get('C')))
                if so == 37 and (not stem.endswith('________.') or opt_map.get('A') != 'whether there is any weak point' or opt_map.get('D') != 'how the potential spies can be located'):
                    round20_anomalies.append(('2007_q37', stem, opt_map))
                if so == 40 and (opt_map.get('A') != 'data leakage is more severe in Europe' or opt_map.get('B') != "FTC's decision is essential to data security"):
                    round20_anomalies.append(('2007_q40', opt_map))
            if yr == 2006 and cat == 'ky1':
                if so == 6 and opt_map.get('B') != 'change':
                    round20_anomalies.append(('2006_q6_opt_B', opt_map.get('B')))
                if so == 9 and (ans != 'A' or opt_map.get('A') != 'predicts' or opt_map.get('D') != 'discovers'):
                    round20_anomalies.append(('2006_q9_ans_or_opts', ans, opt_map))
                if so == 16 and opt_map.get('B') not in ['(turn) over', 'over']:
                    round20_anomalies.append(('2006_q16_opt_B', opt_map.get('B')))
                if so == 26 and opt_map.get('B') != 'the actors of the RSC imitate Shakespeare on and off stage':
                    round20_anomalies.append(('2006_q26_opt_B', opt_map.get('B')))
                if so == 29 and opt_map.get('A') != 'ticket prices can be raised to cover the spending':
                    round20_anomalies.append(('2006_q29_opt_A', opt_map.get('A')))
                if so == 34 and (opt_map.get('B') != 'fisheries should keep their yields below 50% of the biomass' or opt_map.get('D') != 'people should adjust the fishing baseline to the changing situation'):
                    round20_anomalies.append(('2006_q34_opts', opt_map))
                if so == 35 and (opt_map.get('A') != 'management efficiency' or opt_map.get('B') != 'biomass level'):
                    round20_anomalies.append(('2006_q35_opts', opt_map))
            if yr == 2008 and cat == 'ky1':
                if so == 1 and opt_map.get('A') != '(be) selected (to do)':
                    round20_anomalies.append(('2008_q1_opt_A', opt_map.get('A')))
                if so == 6 and opt_map.get('A') != '(at the) thought (of)':
                    round20_anomalies.append(('2008_q6_opt_A', opt_map.get('A')))
                if so == 9 and opt_map.get('B') != 'scoring':
                    round20_anomalies.append(('2008_q9_opt_B', opt_map.get('B')))
                if so == 10 and opt_map.get('C') != 'mean':
                    round20_anomalies.append(('2008_q10_opt_C', opt_map.get('C')))
                if so == 15 and (opt_map.get('A') != 'given up (to sb/sth)' or opt_map.get('D') != 'put down (to sth)'):
                    round20_anomalies.append(('2008_q15_opts', opt_map))
                if so == 18 and (opt_map.get('B') != 'integrated' or opt_map.get('C') != 'woven'):
                    round20_anomalies.append(('2008_q18_opts', opt_map))
                if so == 28 and opt_map.get('A') != 'it provides an easier access to scientific results':
                    round20_anomalies.append(('2008_q28_opt_A', opt_map.get('A')))
                if so == 29 and opt_map.get('B') != 'subscribe to the journal publishing it':
                    round20_anomalies.append(('2008_q29_opt_B', opt_map.get('B')))
                if so == 34 and (opt_map.get('B') != 'the design of military uniforms will remain unchanged' or opt_map.get('D') != 'the existing data of human height will still be applicable'):
                    round20_anomalies.append(('2008_q34_opts', opt_map))
                if so == 40 and (opt_map.get('B') != 'military experience' or opt_map.get('D') != 'political stand'):
                    round20_anomalies.append(('2008_q40_opts', opt_map))
            if yr == 2009 and cat == 'ky1':
                if so == 1 and opt_map.get('C') != 'Observe':
                    round20_anomalies.append(('2009_q1_opt_C', opt_map.get('C')))
                if so == 3 and (opt_map.get('A') != 'thinner' or opt_map.get('B') != 'stabler'):
                    round20_anomalies.append(('2009_q3_opts', opt_map))
                if so == 10 and (opt_map.get('B') != 'forward' or opt_map.get('C') != 'afterward' or opt_map.get('D') != 'backward'):
                    round20_anomalies.append(('2009_q10_opts', opt_map))
                if so == 35 and not opt_map.get('A', '').startswith('results directly from competitive'):
                    round20_anomalies.append(('2009_q35_opt_A', opt_map.get('A')))
            if yr == 2014 and cat == 'ky1' and so == 9:
                if opt_map.get('A') != 'channel':
                    round20_anomalies.append(('2014_q9_opt_A', opt_map.get('A')))
            if yr == 2021 and cat == 'ky1':
                if so == 18 and opt_map.get('B') != 'process':
                    round20_anomalies.append(('2021_q18_opt_B', opt_map.get('B')))
                if so == 39 and opt_map.get('C') != 'is at odds with its earlier rulings':
                    round20_anomalies.append(('2021_q39_opt_C', opt_map.get('C')))

            # Check Round 21: Official Answer Rectification & Bleeding Cut
            if yr == 2001 and cat == 'ky1' and so == 7:
                if ans != 'D':
                    round21_anomalies.append(('2001_ky1_q7_ans', ans))
            if yr == 2003 and cat == 'ky1':
                if so == 24:
                    if opt_map.get('B') != 'Straitford guarantees the truthfulness of its information' or opt_map.get('C') != "Straitford's business is characterized by unpredictability":
                        round21_anomalies.append(('2003_ky1_q24_opts', opt_map))
                if so == 25:
                    if expl.startswith('25.') or 'nonconformist image' not in expl or '【命题解七' in expl:
                        round21_anomalies.append(('2003_ky1_q25_expl', expl[:50]))
            if yr == 2015 and cat == 'ky1':
                if so == 28 and ('entering his or her home' not in expl or len(expl) < 300):
                    round21_anomalies.append(('2015_ky1_q28_expl', len(expl)))
                if so == 34 and ('has room for further improvement' not in expl or len(expl) < 300):
                    round21_anomalies.append(('2015_ky1_q34_expl', len(expl)))
                if so == 36:
                    if ans != 'A' or 'Others await trial' in expl or len(expl) > 2500:
                        round21_anomalies.append(('2015_ky1_q36', ans, len(expl)))
                if so == 37 and ('Rebekah Brooks' in expl or len(expl) > 2500):
                    round21_anomalies.append(('2015_ky1_q37', len(expl)))
                if so == 38 and ('astonishing' not in expl or len(expl) < 300):
                    round21_anomalies.append(('2015_ky1_q38_expl', len(expl)))
            if yr == 2018 and cat == 'ky1':
                if so == 31:
                    if opt_map.get('B') != "It failed to pay due attention to patients' rights." or '【C】正确' in expl:
                        round21_anomalies.append(('2018_ky1_q31', opt_map.get('B'), 'bleeding' in expl))
                if so == 32 and 'Q33' in expl:
                    round21_anomalies.append(('2018_ky1_q32_expl', expl[:50]))
                if so == 35 and (expl.startswith('done.❻') or '谨慎' not in expl):
                    round21_anomalies.append(('2018_ky1_q35_expl', expl[:50]))
                if so in [36, 37, 38] and len(expl) > 2500:
                    round21_anomalies.append((f'2018_ky1_q{so}_len', len(expl)))

            # Check Round 22: 2008 Text 4 (Q36-40), 2009 Text 2 (Q29-30), 2010 Q45
            if yr == 2008 and cat == 'ky1':
                if so == 36:
                    if not (stem.endswith('to') or stem.endswith('to ________.')) or ans != 'D' or opt_map.get('C') != 'stress the role of slaves in the U.S. history' or '乔治”大为不同' in expl or len(expl) < 400:
                        round22_anomalies.append(('2008_ky1_q36', stem, ans, opt_map.get('C'), len(expl)))
                elif so == 37:
                    if ans != 'B' or opt_map.get('B') != 'in its early days the U.S. was confronted with delicate situations' or '大众生活中存在的记忆资料' in expl:
                        round22_anomalies.append(('2008_ky1_q37', ans, opt_map.get('B')))
                elif so == 38:
                    if stem != 'What do we learn about Thomas Jefferson?' or ans != 'C' or opt_map.get('C') != 'His attitude towards slavery was complex.' or '实施细节' in expl or len(expl) < 400:
                        round22_anomalies.append(('2008_ky1_q38', stem, ans, opt_map.get('C'), len(expl)))
                elif so == 39:
                    if ans != 'A' or expl.startswith('旺。Mo r e than anything') or '【深层解读】' in expl:
                        round22_anomalies.append(('2008_ky1_q39', ans, expl[:40]))
                elif so == 40:
                    if ans != 'B' or expl.startswith('矛盾态度') or '【深层解读】' in expl:
                        round22_anomalies.append(('2008_ky1_q40', ans, expl[:40]))
            if yr == 2009 and cat == 'ky1':
                if so == 29:
                    if stem not in ['In the last paragraph, a problem commercial genetic testing faces is', 'In the last paragraph, a problem commercial genetic testing faces is ________.'] or ans != 'A' or expl.startswith('29.'):
                        round22_anomalies.append(('2009_ky1_q29', stem, ans, expl[:30]))
                elif so == 30:
                    if stem not in ['An appropriate title for the text is most likely to be', 'An appropriate title for the text is most likely to be ________.'] or ans != 'B' or expl.startswith('30 . . .'):
                        round22_anomalies.append(('2009_ky1_q30', stem, ans, expl[:30]))
            if yr == 2010 and cat == 'ky1' and so == 45:
                if '42. 本题考核的知识点是' in expl:
                    round22_anomalies.append(('2010_ky1_q45_bleeding', 'leaked Q42 in explanation'))

            # Check Round 23: 2008 Q35 / 2006 Q22,25,31,32,36,38,39 / 2005 Reading 16 checks / 2001 Q28 / Cloze OCR
            if yr == 2008 and cat == 'ky1' and so == 35:
                if opt_map.get('C') != 'Americans have reached their genetic growth limit' or ans != 'C' or len(expl) < 400:
                    round23_anomalies.append(('2008_ky1_q35', ans, opt_map.get('C'), len(expl)))
            if yr == 2006 and cat == 'ky1':
                if so == 22:
                    if stem not in ['According to the author, the department stores of the 19th century', 'According to the author, the department stores of the 19th century ________.'] or ans != 'A' or opt_map.get('A') != 'played a role in the spread of popular culture' or opt_map.get('D') != 'owed its emergence to the culture of consumption':
                        round23_anomalies.append(('2006_ky1_q22', stem, ans, opt_map))
                elif so == 25 and opt_map.get('B') != 'successful':
                    round23_anomalies.append(('2006_ky1_q25_opt_B', opt_map.get('B')))
                elif so == 31 and (opt_map.get('A') not in ['large animals were vulnerable to the changing', 'large animals were vulnerable to the changing environment'] or opt_map.get('D') != 'slow-growing fish outlive fast-growing ones'):
                    round23_anomalies.append(('2006_ky1_q31_opts', opt_map))
                elif so == 32:
                    if (not stem.startswith("We can infer from Dr. Myers and Dr. Worm")) or ans != 'A' or opt_map.get('A') != 'the stock of large predators in some old fisheries has reduced by 90%' or opt_map.get('C') != 'the catch sizes in new fisheries are only 20% of the original amount':
                        round23_anomalies.append(('2006_ky1_q32', stem, ans, opt_map))
                elif so == 36:
                    if stem not in ['By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that', 'By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that ________.'] or ans != 'D' or opt_map.get('D') != 'artists have changed their focus of interest' or expl.startswith('情况并非总是如此'):
                        round23_anomalies.append(('2006_ky1_q36', stem, ans, opt_map.get('D'), expl[:50]))
                elif so == 38 and opt_map.get('A') != 'emerges in the wake of the anti-happy art':
                    round23_anomalies.append(('2006_ky1_q38_opt_A', opt_map.get('A')))
                elif so == 39:
                    if stem not in ['We can learn from the last paragraph that the author believes', 'We can learn from the last paragraph that the author believes ________.'] or opt_map.get('D') != 'the anti-happy art flourishes when economy booms' or opt_map.get('B') != 'the anti-happy art is distasteful but refreshing':
                        round23_anomalies.append(('2006_ky1_q39', stem, opt_map))
            if yr == 2005 and cat == 'ky1':
                if so == 4 and (ans != 'C' or opt_map.get('C') != 'missing'):
                    round17_anomalies.append(('2005_q4_ans_or_opts', ans, opt_map))
                if so == 5 and (ans != 'B' or opt_map.get('B') != 'though'):
                    round17_anomalies.append(('2005_q5_ans_or_opts', ans, opt_map))
                if so == 9 and (ans != 'D' or opt_map.get('D') != 'whereas'):
                    round17_anomalies.append(('2005_q9_ans_or_opts', ans, opt_map))
                if so == 11 and (ans != 'C' or opt_map.get('C') != 'messages' or not expl.startswith('11.')):
                    round17_anomalies.append(('2005_q11_ans_or_opts_or_expl', ans, opt_map.get('C'), expl[:30]))
                if so == 12 and (ans != 'A' or opt_map.get('A') != 'at first' or not expl.startswith('12.')):
                    round17_anomalies.append(('2005_q12_ans_or_opts_or_expl', ans, opt_map.get('A'), expl[:30]))
                if so == 13 and (ans != 'D' or opt_map.get('D') != 'exposed'):
                    round17_anomalies.append(('2005_q13_ans_or_opts', ans, opt_map))
                if so == 14 and (ans != 'C' or opt_map.get('C') != 'inefficient'):
                    round17_anomalies.append(('2005_q14_ans_or_opts', ans, opt_map))
                if so == 15 and (ans != 'D' or opt_map.get('D') != 'create'):
                    round17_anomalies.append(('2005_q15_ans_or_opts', ans, opt_map))
                if so == 16 and (ans != 'B' or opt_map.get('B') != 'also'):
                    round17_anomalies.append(('2005_q16_ans_or_opts', ans, opt_map))
                if so == 17 and (ans != 'C' or opt_map.get('C') != 'aware'):
                    round17_anomalies.append(('2005_q17_ans_or_opts', ans, opt_map))
                if so == 18 and (ans != 'D' or opt_map.get('D') != 'notice'):
                    round17_anomalies.append(('2005_q18_ans_or_opts', ans, opt_map))
                if so == 19 and (ans != 'A' or opt_map.get('A') != 'available'):
                    round17_anomalies.append(('2005_q19_ans_or_opts', ans, opt_map))
                if so == 20 and (ans != 'B' or opt_map.get('B') != 'such as'):
                    round17_anomalies.append(('2005_q20_ans_or_opts', ans, opt_map))
                if so == 22:
                    if not stem.endswith('________.') or 'it is all too monkey' not in stem or ans != 'B':
                        round17_anomalies.append(('2005_q22_stem_or_ans', stem, ans))
                    if opt_map.get('A') != 'monkeys are also outraged by slack rivals' or opt_map.get('B') != "resenting unfairness is also monkeys' nature":
                        round17_anomalies.append(('2005_q22_opts', opt_map))
            if yr == 2003 and cat == 'ky1' and so == 23:
                if stem != 'The phrase "making the biggest splash" (Line 1, Paragraph 3) most probably means ________.':
                    round17_anomalies.append(('2003_q23_stem', stem))
            if yr == 2006 and cat == 'ky1' and so == 28:
                if stem != 'By saying "Stratford cries poor traditionally" (Line 2, Paragraph 4), the author implies that ________.':
                    round17_anomalies.append(('2006_q28_stem', stem))
                if opt_map.get('A') != 'Stratford cannot afford the expansion projects':
                    round17_anomalies.append(('2006_q28_opt_A', opt_map.get('A')))
            if yr == 2006 and cat == 'ky1' and so == 33:
                if stem != 'By saying "these figures are conservative" (Line 1, Paragraph 3), Dr. Worm means that ________.':
                    round17_anomalies.append(('2006_q33_stem', stem))
                if opt_map.get('D') != 'the data collected so far are out of date':
                    round17_anomalies.append(('2006_q33_opt_D', opt_map.get('D')))

            # Check Round 18: 2011 ky1, 2014 ky1, 2001 ky1 authentic options & answers
            if yr == 2011 and cat == 'ky1':
                if so == 21 and (ans != 'C' or opt_map.get('C') != 'received acclaim'):
                    round18_anomalies.append(('2011_q21', ans, opt_map))
                if so == 22 and (ans != 'B' or opt_map.get('B') != 'modest'):
                    round18_anomalies.append(('2011_q22', ans, opt_map))
                if so == 23 and (ans != 'D' or opt_map.get('D') != 'overestimate the value of live performances'):
                    round18_anomalies.append(('2011_q23', ans, opt_map))
                if so == 32 and (ans != 'C' or opt_map.get('C') != 'strong user traffic'):
                    round18_anomalies.append(('2011_q32', ans, opt_map))
                if so == 33 and (ans != 'B' or opt_map.get('B') != 'can be used to produce negative effects in marketing'):
                    round18_anomalies.append(('2011_q33', ans, opt_map))
                if so == 35 and (ans != 'A' or opt_map.get('A') != 'Alternatives to conventional paid media.'):
                    round18_anomalies.append(('2011_q35', ans, opt_map))
            if yr == 2014 and cat == 'ky1':
                if so == 31 and (ans != 'B' or opt_map.get('B') != 'a handsome reward for researchers'):
                    round18_anomalies.append(('2014_q31', ans, opt_map))
                if so == 32 and (ans != 'C' or opt_map.get('C') != 'the founders of the new awards'):
                    round18_anomalies.append(('2014_q32', ans, opt_map))
                if so == 33 and (ans != 'C' or opt_map.get('C') != 'the joint effort of modern researchers'):
                    round18_anomalies.append(('2014_q33', ans, opt_map))
                if so == 39 and (ans != 'C' or opt_map.get('C') != 'biased against classical liberal ideas' or not (expl.startswith('［精准定位］') or expl.startswith('【精准定位】'))):
                    round18_anomalies.append(('2014_q39', ans, opt_map, expl[:30]))
                if so == 40 and (ans != 'B' or opt_map.get('B') != 'Illiberal Education and "The Heart of the Matter"' or not (expl.startswith('［精准定位］') or expl.startswith('【精准定位】'))):
                    round18_anomalies.append(('2014_q40', ans, opt_map, expl[:30]))
            if yr == 2001 and cat == 'ky1':
                if so == 32 and (ans != 'A' or opt_map.get('A') != 'failure to realize its real problem'):
                    round18_anomalies.append(('2001_q32', ans, opt_map))
                if so == 40 and (ans != 'D' or opt_map.get('D') != 'the economic situation'):
                    round18_anomalies.append(('2001_q40', ans, opt_map))

            # Check Round 20: 2006/2007/2008/2009/2014/2021 option truncations, stems & OCR repairs
            if yr == 2007 and cat == 'ky1':
                if so == 4 and opt_map.get('C') != 'open (to)':
                    round20_anomalies.append(('2007_q4_opt_C', opt_map.get('C')))
                if so == 8 and (ans != 'A' or opt_map.get('A') != 'freedom' or opt_map.get('D') != 'reform'):
                    round20_anomalies.append(('2007_q8_ans_or_opts', ans, opt_map))
                if so == 15 and (ans != 'B' or opt_map.get('B') != 'cry' or opt_map.get('A') != 'support'):
                    round20_anomalies.append(('2007_q15_ans_or_opts', ans, opt_map))
                if so == 23 and opt_map.get('C') != 'is determined by genetic rather than psychological factors':
                    round20_anomalies.append(('2007_q23_opt_C', opt_map.get('C')))
                if so == 26 and opt_map.get('C') != 'Telling the differences between certain concepts.':
                    round20_anomalies.append(('2007_q26_opt_C', opt_map.get('C')))
                if so == 27 and (stem != 'What can be inferred about intelligence testing from Paragraph 3?' or opt_map.get('D') != 'Scientists have defined the important elements of human intelligence.'):
                    round20_anomalies.append(('2007_q27', stem, opt_map.get('D')))
                if so == 28 and (not stem.endswith('________.') or not opt_map.get('A', '').endswith('computational procedures') or not opt_map.get('B', '').endswith('emphasized now')):
                    round20_anomalies.append(('2007_q28', stem, opt_map))
                if so == 29 and (not stem.endswith('________.') or opt_map.get('A') != "test scores may not be reliable indicators of one's ability" or opt_map.get('B') != 'IQ scores and SAT results are highly correlated'):
                    round20_anomalies.append(('2007_q29', stem, opt_map))
                if so == 32 and (opt_map.get('C') != 'less chance to invest' or not stem.endswith('________.')):
                    round20_anomalies.append(('2007_q32', stem, opt_map.get('C')))
                if so == 37 and (not stem.endswith('________.') or opt_map.get('A') != 'whether there is any weak point' or opt_map.get('D') != 'how the potential spies can be located'):
                    round20_anomalies.append(('2007_q37', stem, opt_map))
                if so == 40 and (opt_map.get('A') != 'data leakage is more severe in Europe' or opt_map.get('B') != "FTC's decision is essential to data security"):
                    round20_anomalies.append(('2007_q40', opt_map))
            if yr == 2006 and cat == 'ky1':
                if so == 6 and opt_map.get('B') != 'change':
                    round20_anomalies.append(('2006_q6_opt_B', opt_map.get('B')))
                if so == 9 and (ans != 'A' or opt_map.get('A') != 'predicts' or opt_map.get('D') != 'discovers'):
                    round20_anomalies.append(('2006_q9_ans_or_opts', ans, opt_map))
                if so == 16 and opt_map.get('B') not in ['(turn) over', 'over']:
                    round20_anomalies.append(('2006_q16_opt_B', opt_map.get('B')))
                if so == 26 and opt_map.get('B') != 'the actors of the RSC imitate Shakespeare on and off stage':
                    round20_anomalies.append(('2006_q26_opt_B', opt_map.get('B')))
                if so == 29 and opt_map.get('A') != 'ticket prices can be raised to cover the spending':
                    round20_anomalies.append(('2006_q29_opt_A', opt_map.get('A')))
                if so == 34 and (opt_map.get('B') != 'fisheries should keep their yields below 50% of the biomass' or opt_map.get('D') != 'people should adjust the fishing baseline to the changing situation'):
                    round20_anomalies.append(('2006_q34_opts', opt_map))
                if so == 35 and (opt_map.get('A') != 'management efficiency' or opt_map.get('B') != 'biomass level'):
                    round20_anomalies.append(('2006_q35_opts', opt_map))
            if yr == 2008 and cat == 'ky1':
                if so == 1 and opt_map.get('A') != '(be) selected (to do)':
                    round20_anomalies.append(('2008_q1_opt_A', opt_map.get('A')))
                if so == 6 and opt_map.get('A') != '(at the) thought (of)':
                    round20_anomalies.append(('2008_q6_opt_A', opt_map.get('A')))
                if so == 9 and opt_map.get('B') != 'scoring':
                    round20_anomalies.append(('2008_q9_opt_B', opt_map.get('B')))
                if so == 10 and opt_map.get('C') != 'mean':
                    round20_anomalies.append(('2008_q10_opt_C', opt_map.get('C')))
                if so == 15 and (opt_map.get('A') != 'given up (to sb/sth)' or opt_map.get('D') != 'put down (to sth)'):
                    round20_anomalies.append(('2008_q15_opts', opt_map))
                if so == 18 and (opt_map.get('B') != 'integrated' or opt_map.get('C') != 'woven'):
                    round20_anomalies.append(('2008_q18_opts', opt_map))
                if so == 28 and opt_map.get('A') != 'it provides an easier access to scientific results':
                    round20_anomalies.append(('2008_q28_opt_A', opt_map.get('A')))
                if so == 29 and opt_map.get('B') != 'subscribe to the journal publishing it':
                    round20_anomalies.append(('2008_q29_opt_B', opt_map.get('B')))
                if so == 34 and (opt_map.get('B') != 'the design of military uniforms will remain unchanged' or opt_map.get('D') != 'the existing data of human height will still be applicable'):
                    round20_anomalies.append(('2008_q34_opts', opt_map))
                if so == 40 and (opt_map.get('B') != 'military experience' or opt_map.get('D') != 'political stand'):
                    round20_anomalies.append(('2008_q40_opts', opt_map))
            if yr == 2009 and cat == 'ky1':
                if so == 1 and opt_map.get('C') != 'Observe':
                    round20_anomalies.append(('2009_q1_opt_C', opt_map.get('C')))
                if so == 3 and (opt_map.get('A') != 'thinner' or opt_map.get('B') != 'stabler'):
                    round20_anomalies.append(('2009_q3_opts', opt_map))
                if so == 10 and (opt_map.get('B') != 'forward' or opt_map.get('C') != 'afterward' or opt_map.get('D') != 'backward'):
                    round20_anomalies.append(('2009_q10_opts', opt_map))
                if so == 35 and not opt_map.get('A', '').startswith('results directly from competitive'):
                    round20_anomalies.append(('2009_q35_opt_A', opt_map.get('A')))
            if yr == 2014 and cat == 'ky1' and so == 9:
                if opt_map.get('A') != 'channel':
                    round20_anomalies.append(('2014_q9_opt_A', opt_map.get('A')))
            if yr == 2021 and cat == 'ky1':
                if so == 18 and opt_map.get('B') != 'process':
                    round20_anomalies.append(('2021_q18_opt_B', opt_map.get('B')))
                if so == 39 and opt_map.get('C') != 'is at odds with its earlier rulings':
                    round20_anomalies.append(('2021_q39_opt_C', opt_map.get('C')))

            # Check Round 21: Official Answer Rectification & Bleeding Cut
            if yr == 2001 and cat == 'ky1' and so == 7:
                if ans != 'D':
                    round21_anomalies.append(('2001_ky1_q7_ans', ans))
            if yr == 2003 and cat == 'ky1':
                if so == 24:
                    if opt_map.get('B') != 'Straitford guarantees the truthfulness of its information' or opt_map.get('C') != "Straitford's business is characterized by unpredictability":
                        round21_anomalies.append(('2003_ky1_q24_opts', opt_map))
                if so == 25:
                    if expl.startswith('25.') or 'nonconformist image' not in expl or '【命题解七' in expl:
                        round21_anomalies.append(('2003_ky1_q25_expl', expl[:50]))
            if yr == 2015 and cat == 'ky1':
                if so == 28 and ('entering his or her home' not in expl or len(expl) < 300):
                    round21_anomalies.append(('2015_ky1_q28_expl', len(expl)))
                if so == 34 and ('has room for further improvement' not in expl or len(expl) < 300):
                    round21_anomalies.append(('2015_ky1_q34_expl', len(expl)))
                if so == 36:
                    if ans != 'A' or 'Others await trial' in expl or len(expl) > 2500:
                        round21_anomalies.append(('2015_ky1_q36', ans, len(expl)))
                if so == 37 and ('Rebekah Brooks' in expl or len(expl) > 2500):
                    round21_anomalies.append(('2015_ky1_q37', len(expl)))
                if so == 38 and ('astonishing' not in expl or len(expl) < 300):
                    round21_anomalies.append(('2015_ky1_q38_expl', len(expl)))
            if yr == 2018 and cat == 'ky1':
                if so == 31:
                    if opt_map.get('B') != "It failed to pay due attention to patients' rights." or '【C】正确' in expl:
                        round21_anomalies.append(('2018_ky1_q31', opt_map.get('B'), 'bleeding' in expl))
                if so == 32 and 'Q33' in expl:
                    round21_anomalies.append(('2018_ky1_q32_expl', expl[:50]))
                if so == 35 and (expl.startswith('done.❻') or '谨慎' not in expl):
                    round21_anomalies.append(('2018_ky1_q35_expl', expl[:50]))
                if so in [36, 37, 38] and len(expl) > 2500:
                    round21_anomalies.append((f'2018_ky1_q{so}_len', len(expl)))

            # Check Round 22: 2008 Text 4 (Q36-40), 2009 Text 2 (Q29-30), 2010 Q45
            if yr == 2008 and cat == 'ky1':
                if so == 36:
                    if not (stem.endswith('to') or stem.endswith('to ________.')) or ans != 'D' or opt_map.get('C') != 'stress the role of slaves in the U.S. history' or '乔治”大为不同' in expl or len(expl) < 400:
                        round22_anomalies.append(('2008_ky1_q36', stem, ans, opt_map.get('C'), len(expl)))
                elif so == 37:
                    if ans != 'B' or opt_map.get('B') != 'in its early days the U.S. was confronted with delicate situations' or '大众生活中存在的记忆资料' in expl:
                        round22_anomalies.append(('2008_ky1_q37', ans, opt_map.get('B')))
                elif so == 38:
                    if stem != 'What do we learn about Thomas Jefferson?' or ans != 'C' or opt_map.get('C') != 'His attitude towards slavery was complex.' or '实施细节' in expl or len(expl) < 400:
                        round22_anomalies.append(('2008_ky1_q38', stem, ans, opt_map.get('C'), len(expl)))
                elif so == 39:
                    if ans != 'A' or expl.startswith('旺。Mo r e than anything') or '【深层解读】' in expl:
                        round22_anomalies.append(('2008_ky1_q39', ans, expl[:40]))
                elif so == 40:
                    if ans != 'B' or expl.startswith('矛盾态度') or '【深层解读】' in expl:
                        round22_anomalies.append(('2008_ky1_q40', ans, expl[:40]))
            if yr == 2009 and cat == 'ky1':
                if so == 29:
                    if stem not in ['In the last paragraph, a problem commercial genetic testing faces is', 'In the last paragraph, a problem commercial genetic testing faces is ________.'] or ans != 'A' or expl.startswith('29.'):
                        round22_anomalies.append(('2009_ky1_q29', stem, ans, expl[:30]))
                elif so == 30:
                    if stem not in ['An appropriate title for the text is most likely to be', 'An appropriate title for the text is most likely to be ________.'] or ans != 'B' or expl.startswith('30 . . .'):
                        round22_anomalies.append(('2009_ky1_q30', stem, ans, expl[:30]))
            if yr == 2010 and cat == 'ky1' and so == 45:
                if '42. 本题考核的知识点是' in expl:
                    round22_anomalies.append(('2010_ky1_q45_bleeding', 'leaked Q42 in explanation'))

            # Check Round 23: 2008 Q35 / 2006 Q22,25,31,32,36,38,39 / 2005 Reading 16 checks / 2001 Q28 / Cloze OCR
            if yr == 2008 and cat == 'ky1' and so == 35:
                if opt_map.get('C') != 'Americans have reached their genetic growth limit' or ans != 'C' or len(expl) < 400:
                    round23_anomalies.append(('2008_ky1_q35', ans, opt_map.get('C'), len(expl)))
            if yr == 2006 and cat == 'ky1':
                if so == 22:
                    if stem not in ['According to the author, the department stores of the 19th century', 'According to the author, the department stores of the 19th century ________.'] or ans != 'A' or opt_map.get('A') != 'played a role in the spread of popular culture' or opt_map.get('D') != 'owed its emergence to the culture of consumption':
                        round23_anomalies.append(('2006_ky1_q22', stem, ans, opt_map))
                elif so == 25 and opt_map.get('B') != 'successful':
                    round23_anomalies.append(('2006_ky1_q25_opt_B', opt_map.get('B')))
                elif so == 31 and (opt_map.get('A') not in ['large animals were vulnerable to the changing', 'large animals were vulnerable to the changing environment'] or opt_map.get('D') != 'slow-growing fish outlive fast-growing ones'):
                    round23_anomalies.append(('2006_ky1_q31_opts', opt_map))
                elif so == 32:
                    if (not stem.startswith("We can infer from Dr. Myers and Dr. Worm")) or ans != 'A' or opt_map.get('A') != 'the stock of large predators in some old fisheries has reduced by 90%' or opt_map.get('C') != 'the catch sizes in new fisheries are only 20% of the original amount':
                        round23_anomalies.append(('2006_ky1_q32', stem, ans, opt_map))
                elif so == 36:
                    if stem not in ['By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that', 'By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that ________.'] or ans != 'D' or opt_map.get('D') != 'artists have changed their focus of interest' or expl.startswith('情况并非总是如此'):
                        round23_anomalies.append(('2006_ky1_q36', stem, ans, opt_map.get('D'), expl[:50]))
                elif so == 38 and opt_map.get('A') != 'emerges in the wake of the anti-happy art':
                    round23_anomalies.append(('2006_ky1_q38_opt_A', opt_map.get('A')))
                elif so == 39:
                    if stem not in ['We can learn from the last paragraph that the author believes', 'We can learn from the last paragraph that the author believes ________.'] or opt_map.get('D') != 'the anti-happy art flourishes when economy booms' or opt_map.get('B') != 'the anti-happy art is distasteful but refreshing':
                        round23_anomalies.append(('2006_ky1_q39', stem, opt_map))
            if yr == 2005 and cat == 'ky1':
                if so == 21 and stem != 'In the opening paragraph, the author introduces his topic by':
                    round23_anomalies.append(('2005_ky1_q21_stem', stem))
                elif so == 23 and stem != 'Female capuchin monkeys were chosen for the research most probably because they are':
                    round23_anomalies.append(('2005_ky1_q23_stem', stem))
                elif so == 24 and (stem != 'Dr. Brosnan and Dr. de Waal have eventually found in their study that the monkeys' or opt_map.get('C') != 'will not be cooperative if feeling cheated'):
                    round23_anomalies.append(('2005_ky1_q24', stem, opt_map.get('C')))
                elif so == 26:
                    if opt_map.get('A') != 'there was no scientific evidence of the correlation between smoking and death' or opt_map.get('B') != 'the number of early deaths of smokers in the past decades was insignificant' or opt_map.get('C') != 'people had the freedom to choose their own way of life':
                        round23_anomalies.append(('2005_ky1_q26_opts', opt_map))
                elif so == 27 and opt_map.get('D') != 'a guide':
                    round23_anomalies.append(('2005_ky1_q27_opt_D', opt_map.get('D')))
                elif so == 28 and opt_map.get('A') != 'Endless studies kill action.':
                    round23_anomalies.append(('2005_ky1_q28_opt_A', opt_map.get('A')))
                elif so == 29:
                    if stem != 'According to the author, what should the Administration do about global warming?' or opt_map.get('A') != 'Offer aid to build cleaner power plants.':
                        round23_anomalies.append(('2005_ky1_q29', stem, opt_map.get('A')))
                elif so == 30:
                    if stem != 'The author associates the issue of global warming with that of smoking because' or opt_map.get('B') != 'a lesson from the latter is applicable to the former' or opt_map.get('C') != 'the outcome of the latter aggravates the former':
                        round23_anomalies.append(('2005_ky1_q30', stem, opt_map))
                elif so == 32 and stem != 'By referring to the limbic system, the author intends to show':
                    round23_anomalies.append(('2005_ky1_q32_stem', stem))
                elif so == 33 and (opt_map.get('A') != 'aggravate in our unconscious mind' or opt_map.get('C') != 'persist till the time we fall asleep' or opt_map.get('D') != 'show up in dreams early at night'):
                    round23_anomalies.append(('2005_ky1_q33_opts', opt_map))
                elif so == 35 and stem != 'What advice might Cartwright give to those who sometimes have bad dreams?':
                    round23_anomalies.append(('2005_ky1_q35_stem', stem))
                elif so == 36 and (opt_map.get('C') != 'has caused the controversy over the counter-culture' or opt_map.get('D') != 'brought about changes in public attitudes in the 1960s'):
                    round23_anomalies.append(('2005_ky1_q36_opts', opt_map))
                elif so == 38 and opt_map.get('D') != 'Of all the varieties standard English can best convey complex ideas.':
                    round23_anomalies.append(('2005_ky1_q38_opt_D', opt_map.get('D')))
                elif so == 39 and (opt_map.get('C') != 'admiration for their memory' or opt_map.get('D') != 'contempt for their old-fashionedness'):
                    round23_anomalies.append(('2005_ky1_q39_opts', opt_map))
            if yr == 2001 and cat == 'ky1' and so == 28:
                if stem not in ["It seems that now a country's economy depends much on", "It seems that now a country's economy depends much on ________."] or opt_map.get('D') != 'how much control it has over foreign corporations' or '2&现在看来' in expl:
                    round23_anomalies.append(('2001_ky1_q28', stem, opt_map.get('D'), expl[:40]))
            if yr == 2007 and cat == 'ky1':
                if so == 1 and (opt_map.get('C') != 'peoples' or opt_map.get('D') != 'individuals'):
                    round23_anomalies.append(('2007_ky1_q1_opts', opt_map))
                elif so == 2 and (opt_map.get('A') != 'confusedly' or opt_map.get('B') != 'cheerfully' or opt_map.get('C') != 'worriedly' or opt_map.get('D') != 'hopefully'):
                    round23_anomalies.append(('2007_ky1_q2_opts', opt_map))
                elif so == 6 and (opt_map.get('A') != 'Presumably' or opt_map.get('B') != 'Incidentally' or opt_map.get('C') != 'Obviously' or opt_map.get('D') != 'Generally'):
                    round23_anomalies.append(('2007_ky1_q6_opts', opt_map))
                elif so == 9 and (opt_map.get('A') != 'therefore' or opt_map.get('B') != 'however' or opt_map.get('C') != 'indeed' or opt_map.get('D') != 'moreover'):
                    round23_anomalies.append(('2007_ky1_q9_opts', opt_map))
                elif so == 12 and (opt_map.get('C') != 'Unless' or opt_map.get('D') != 'While'):
                    round23_anomalies.append(('2007_ky1_q12_opts', opt_map))
                elif so == 13 and opt_map.get('B') != 'for':
                    round23_anomalies.append(('2007_ky1_q13_opt_B', opt_map.get('B')))
                elif so == 25 and opt_map.get('A') != '“Faith will move mountains.”':
                    round23_anomalies.append(('2007_ky1_q25_opt_A', opt_map.get('A')))
                elif so == 31 and opt_map.get('A') != 'the safety net they used to enjoy has disappeared':
                    round23_anomalies.append(('2007_ky1_q31_opt_A', opt_map.get('A')))
                elif so == 39 and opt_map.get('C') != 'realize the high cost of data restoration':
                    round23_anomalies.append(('2007_ky1_q39_opt_C', opt_map.get('C')))
            if yr == 2009 and cat == 'ky1':
                if so == 7 and (opt_map.get('A') != 'incredible' or opt_map.get('C') != 'inevitable'):
                    round23_anomalies.append(('2009_ky1_q7_opts', opt_map))
                elif so == 9 and (opt_map.get('A') != 'invisible' or opt_map.get('B') != 'limited' or opt_map.get('C') != 'indefinite' or opt_map.get('D') != 'different'):
                    round23_anomalies.append(('2009_ky1_q9_opts', opt_map))
                elif so == 16 and (opt_map.get('B') != 'overcome' or opt_map.get('C') != 'determine'):
                    round23_anomalies.append(('2009_ky1_q16_opts', opt_map))
            if yr == 2022 and cat == 'ky2' and so == 6:
                if opt_map.get('A') != 'well-known':
                    round23_anomalies.append(('2022_ky2_q6_opt_A', opt_map.get('A')))

            # Check Round 24: 2021 ky1 / 2020 ky1 / 2022 ky2 Text 4 & 2007 ky1 Text 3 (Q34-35)
            if yr == 2021 and cat == 'ky1':
                if so == 36 and (expl.startswith('36•') or '［A］控制互联网公司' in expl or len(expl) < 300):
                    round24_anomalies.append(('2021_ky1_q36_expl', expl[:40]))
                elif so == 37 and (expl.startswith('37.') or '［B］' in expl[:100] or len(expl) < 300):
                    round24_anomalies.append(('2021_ky1_q37_expl', expl[:40]))
                elif so == 38 and (opt_map.get('B') != 'It engages in anti-competitive practices.' or expl.startswith('38.')):
                    round24_anomalies.append(('2021_ky1_q38', opt_map.get('B'), expl[:40]))
                elif so == 39 and (opt_map.get('A') != 'focuses on trivialities' or expl.startswith('39.')):
                    round24_anomalies.append(('2021_ky1_q39', opt_map.get('A'), expl[:40]))
                elif so == 40 and (opt_map.get('C') != 'Rules need to be set to diversify online services.' or opt_map.get('D') != "Broadband providers' rights should be protected." or expl.startswith('40.')):
                    round24_anomalies.append(('2021_ky1_q40', opt_map, expl[:40]))
            if yr == 2020 and cat == 'ky1':
                if so == 37 and (expl.startswith('37.') or '根据第二段可知' in expl):
                    round24_anomalies.append(('2020_ky1_q37_expl', expl[:40]))
                elif so == 38 and (stem != 'The countries adopting the unilateral measures share the opinion that' or opt_map.get('C') != "tech multinationals' monopoly should be prevented" or expl.startswith('38.')):
                    round24_anomalies.append(('2020_ky1_q38', stem, opt_map.get('C'), expl[:40]))
                elif so == 39 and (expl.startswith('39.') or '根据第五段可知' in expl):
                    round24_anomalies.append(('2020_ky1_q39_expl', expl[:40]))
                elif so == 40 and (expl.startswith('40.') or '下列哪一项可能是本文的最佳标题' in expl):
                    round24_anomalies.append(('2020_ky1_q40_expl', expl[:40]))
            if yr == 2022 and cat == 'ky2':
                if so == 36 and (expl.startswith('36.') or 'classes are' in expl[:50]):
                    round24_anomalies.append(('2022_ky2_q36_expl', expl[:40]))
                elif so == 37 and (opt_map.get('C') != 'It is important to students.' or expl.startswith('37.')):
                    round24_anomalies.append(('2022_ky2_q37', opt_map.get('C'), expl[:40]))
                elif so == 38 and (stem != "Eric Schwitzgebel's previous findings suggest that ethics professors ________." or expl.startswith('38.')):
                    round24_anomalies.append(('2022_ky2_q38', stem, expl[:40]))
                elif so == 39 and (expl.startswith('39.') or '尼娜•施特罗明格' in expl):
                    round24_anomalies.append(('2022_ky2_q39_expl', expl[:40]))
                elif so == 40 and (expl.startswith('40.') or '埃里克•施维茨格贝尔认为' in expl):
                    round24_anomalies.append(('2022_ky2_q40_expl', expl[:40]))
            if yr == 2007 and cat == 'ky1':
                if so == 34 and (len(expl) < 300 or ('【精准定位】' not in expl and '［精准定位］' not in expl)):
                    round24_anomalies.append(('2007_ky1_q34_expl', len(expl)))
                elif so == 35 and (opt_map.get('B') != 'The Middle Class on the Cliff' or opt_map.get('C') != 'The Middle Class in Conflict' or opt_map.get('D') != 'The Middle Class in Ruins'):
                    round24_anomalies.append(('2007_ky1_q35_opts', opt_map))

            # Round 25 checks
            if yr == 2009 and cat == 'ky1' and so == 38:
                if 'Massachusetts Bay' not in stem or len(expl) < 500 or '［精准定位］' not in expl:
                    round25_anomalies.append(('2009_ky1_q38', stem, len(expl)))
            if yr == 2012 and cat == 'ky1':
                if so == 22 and (opt_map.get('D') != 'recognize the limitations of advertisements' or opt_map.get('B') != "learn from advertisers' experience"):
                    round25_anomalies.append(('2012_ky1_q22', opt_map))
                elif so == 39 and (len(expl) < 500 or ('精准定位' not in expl and '【精准定位】' not in expl)):
                    round25_anomalies.append(('2012_ky1_q39', len(expl)))
            if yr == 2016 and cat == 'ky1' and so == 35:
                if ans != 'B' or opt_map.get('B') != "The necessary amount of companies' spending on it is unknown." or len(expl) < 400 or '［精准定位］' not in expl:
                    round25_anomalies.append(('2016_ky1_q35', ans, opt_map.get('B'), len(expl)))
            if yr == 2010 and cat == 'ky1':
                if so == 23 and opt_map.get('A') != "It is writers' duty to fulfill journalistic goals.":
                    round25_anomalies.append(('2010_ky1_q23', opt_map.get('A')))
                elif so == 24 and (stem != "What can be learned about Cardus according to the last two paragraphs?" or opt_map.get('A') != "His music criticism may not appeal to readers today." or opt_map.get('B') != "His reputation as a music critic has long been in dispute."):
                    round25_anomalies.append(('2010_ky1_q24', stem, opt_map))
                elif so == 31 and (stem not in ["By citing the book The Tipping Point, the author intends to", "By citing the book The Tipping Point, the author intends to ________."] or opt_map.get('B') != "discuss influentials' function in spreading ideas"):
                    round25_anomalies.append(('2010_ky1_q31', stem, opt_map.get('B')))
            if yr == 2001 and cat == 'ky1' and so == 22:
                if opt_map.get('A') != "there is little distinction between specialisation and professionalisation" or opt_map.get('B') != "amateurs can compete with professionals in some areas of science":
                    round25_anomalies.append(('2001_ky1_q22', opt_map))
            if yr == 2002 and cat == 'ky1' and so == 34:
                if opt_map.get('D') != "the price rise of crude leads to the shrinking of heavy industry":
                    round25_anomalies.append(('2002_ky1_q34', opt_map.get('D')))
            if yr == 2013 and cat == 'ky1':
                if so == 37 and opt_map.get('B') != "Federal officers' duty to withhold immigrants' information.":
                    round25_anomalies.append(('2013_ky1_q37', opt_map.get('B')))
                elif so == 39 and opt_map.get('A') != "is dependent on the states' support":
                    round25_anomalies.append(('2013_ky1_q39', opt_map.get('A')))
            if yr == 2014 and cat == 'ky1':
                if so == 21 and opt_map.get('A') != "encourage jobseekers' active engagement in job seeking":
                    round25_anomalies.append(('2014_ky1_q21', opt_map.get('A')))
                elif so == 28 and opt_map.get('B') != "lawyers' and clients' strong resistance":
                    round25_anomalies.append(('2014_ky1_q28', opt_map.get('B')))
                elif so == 37 and opt_map.get('B') != "safeguard individuals' rights to education":
                    round25_anomalies.append(('2014_ky1_q37', opt_map.get('B')))
            if yr == 2015 and cat == 'ky1' and so == 23:
                if opt_map.get('A') != "Aristocrats' excessive reliance on inherited wealth.":
                    round25_anomalies.append(('2015_ky1_q23', opt_map.get('A')))
            if yr == 2017 and cat == 'ky1' and so in range(31, 36):
                if so == 31 and ('［精准定位］' not in expl or expl.startswith('31.')):
                    round25_anomalies.append(('2017_ky1_q31', expl[:40]))
                elif so == 32 and (opt_map.get('B') != 'GDP as the measure of success is widely defied in the UK' or opt_map.get('D') != 'policymakers in the UK are paying less attention to GDP' or 'A recent annual study' in expl):
                    round25_anomalies.append(('2017_ky1_q32', opt_map, expl[-40:]))
                elif so == 33 and ('［精准定位］' not in expl or len(expl) < 350):
                    round25_anomalies.append(('2017_ky1_q33', len(expl)))
                elif so == 34 and ('［精准定位］' not in expl or len(expl) < 400):
                    round25_anomalies.append(('2017_ky1_q34', len(expl)))
                elif so == 35 and stem != "Which of the following is the best title for the text?":
                    round25_anomalies.append(('2017_ky1_q35', stem))
            if yr == 2019 and cat == 'ky1' and so in range(36, 41):
                if so == 36 and (opt_map.get('A') != "better businesses' relations with states" or opt_map.get('D') != "force some states to cut sales tax" or expl.startswith('36.')):
                    round25_anomalies.append(('2019_ky1_q36', opt_map, expl[:40]))
                elif so == 37 and (stem != "It can be learned from paragraphs 2 and 3 that the overruled decisions" or opt_map.get('D') != "were considered unfavorable by states" or '［精准定位］' not in expl):
                    round25_anomalies.append(('2019_ky1_q37', stem, opt_map.get('D')))
                elif so == 38 and (stem != "According to Justice Anthony Kennedy, the physical presence rule has" or opt_map.get('C') != "harmed fair market competition" or '［精准定位］' not in expl):
                    round25_anomalies.append(('2019_ky1_q38', stem, opt_map.get('C')))
                elif so == 39 and (opt_map.get('B') != "Big-chain owners." or '［精准定位］' not in expl or len(expl) < 400):
                    round25_anomalies.append(('2019_ky1_q39', opt_map.get('B'), len(expl)))
                elif so == 40 and (opt_map.get('A') != "gives a factual account of it and discusses its consequences" or opt_map.get('B') != "describes the long and complicated process of its making" or opt_map.get('C') != "presents its main points with conflicting views on them" or opt_map.get('D') != "cites some cases related to it and analyzes their implications" or '［命题解密］' not in expl or len(expl) < 400):
                    round25_anomalies.append(('2019_ky1_q40', opt_map, len(expl)))

            # Check Round 26: 2019 ky1 Text 3 (Q31-Q35), 2016 ky1 Text 2 (Q26-Q30), 2018 ky1 (Text 1-4), 2020 ky1 Text 1-2 (Q21-Q30)
            if yr == 2019 and cat == 'ky1' and so in range(31, 36):
                if so == 31 and ('［精准定位］' not in expl or expl.startswith('31.')):
                    round26_anomalies.append(('2019_ky1_q31', expl[:40]))
                elif so == 32 and ('［精准定位］' not in expl or len(expl) > 2000 or not expl.endswith('唯有［D］项符合这一主基调。')):
                    round26_anomalies.append(('2019_ky1_q32', len(expl), expl[-30:]))
                elif so == 33 and ('［精准定位］' not in expl or not expl.endswith('为正确项。')):
                    round26_anomalies.append(('2019_ky1_q33', expl[-30:]))
                elif so == 34 and (stem != "The author's attitude toward Google's pledges is one of ________." or ans != 'A' or opt_map.get('A') != 'affirmation' or opt_map.get('D') != 'respect' or '［精准定位］' not in expl):
                    round26_anomalies.append(('2019_ky1_q34', stem, ans, opt_map))
                elif so == 35 and (stem != "Which of the following would be the best title for the text?" or opt_map.get('A') != "AI's Future: In the Hands of Tech Giants" or ans != 'C' or not expl.endswith('均予以排除。')):
                    round26_anomalies.append(('2019_ky1_q35', stem, opt_map.get('A'), ans))

            if yr == 2016 and cat == 'ky1' and so in range(26, 31):
                if so == 26 and ('［精准定位］' not in expl or not expl.endswith('故错误。') or len(expl) > 1500):
                    round26_anomalies.append(('2016_ky1_q26', len(expl), expl[-30:]))
                elif so == 27 and (stem != "According to Paragraph 2, the achievements of the National Trust are now being ________." or not expl.endswith('可确定［D］为答案。')):
                    round26_anomalies.append(('2016_ky1_q27', stem, expl[-30:]))
                elif so == 28 and (stem != "Which of the following can be inferred from Paragraph 3?" or not expl.endswith('证实［C］正确。') or '释与摩旬分析' in expl):
                    round26_anomalies.append(('2016_ky1_q28', stem, expl[:40]))
                elif so == 29 and (stem != "The author holds that George Osborne's preference ________." or not expl.endswith('故正确。')):
                    round26_anomalies.append(('2016_ky1_q29', stem, expl[-30:]))
                elif so == 30 and (stem != "In the last paragraph, the author shows his appreciation of ________." or not expl.endswith('故［C］正确。')):
                    round26_anomalies.append(('2016_ky1_q30', stem, expl[-30:]))

            if yr == 2018 and cat == 'ky1':
                if so == 33 and (opt_map.get('C') != "making profits from patients' data is illegal" or '［精准定位］' not in expl or not expl.endswith('锁定正确答案［D］。')):
                    round26_anomalies.append(('2018_ky1_q33', opt_map.get('C'), expl[-30:]))
                elif so in [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 34, 39, 40]:
                    if not expl.startswith('［精准定位］'):
                        round26_anomalies.append((f'2018_ky1_q{so}_header_echo', expl[:40]))

            if yr == 2020 and cat == 'ky1' and so in range(21, 31):
                if not expl.startswith('［精准定位］'):
                    round26_anomalies.append((f'2020_ky1_q{so}_header_echo', expl[:40]))
                if so == 28 and ('2&' in expl or '2&' in stem or not expl.endswith('让权力重获平衡”相符。')):
                    round26_anomalies.append(('2020_ky1_q28_content', expl[:40], expl[-30:]))

            # Check Round 27: 2019 ky1 Text 2 (Q26-Q30), 2016 ky1 Text 3 (Q31-Q35), 2013 ky1 Text 2-3 (Q26-Q35), 2020 ky1 Text 4 (Q36)
            if yr == 2019 and cat == 'ky1' and so in range(26, 31):
                if not expl.startswith('［精准定位］'):
                    round27_anomalies.append(('2019_ky1_q' + str(so) + '_echo', expl[:40]))
                if so == 26 and (len(expl) > 1200 or not expl.endswith('谨防利用②句逻辑或信息设置的干扰。')):
                    round27_anomalies.append(('2019_ky1_q26', len(expl), expl[-30:]))
                elif so == 27 and (len(expl) < 500 or not expl.endswith('（B、D背离初衷，C则扩大作用对象）干扰。')):
                    round27_anomalies.append(('2019_ky1_q27', len(expl), expl[-30:]))
                elif so == 28 and (stem != 'According to Paragraph 5, grade forgiveness enables colleges to ________.' or not expl.endswith('但比对后发现为过度引申。')):
                    round27_anomalies.append(('2019_ky1_q28', stem, expl[-30:]))
                elif so == 29 and (stem != 'What does the phrase "to be aligned" (Line 5, Para. 6) most probably mean?' or not expl.endswith('排除体现矛盾关系的以及互补关系的［B］。')):
                    round27_anomalies.append(('2019_ky1_q29', stem, expl[-30:]))
                elif so == 30 and (stem != 'The author examines the practice of grade forgiveness by ________.' or not expl.endswith('希望借此引发公众对高等教育“商品化”的反思，［B］正确。')):
                    round27_anomalies.append(('2019_ky1_q30', stem, expl[-30:]))

            if yr == 2016 and cat == 'ky1' and so in range(31, 36):
                if not expl.startswith('［精准定位］'):
                    round27_anomalies.append(('2016_ky1_q' + str(so) + '_echo', expl[:40]))
                if so == 31 and (stem != "The author views Milton Friedman's statement about CSR with ________." or len(expl) > 1200 or not expl.endswith('让步假设、虚拟语气等的真实语义和表面含义通常相反。')):
                    round27_anomalies.append(('2016_ky1_q31', stem, len(expl), expl[-30:]))
                elif so == 32 and (stem != "According to Paragraph 2, CSR helps a company by ________." or not expl.endswith('可初步推知［C］正确；而［A］与［B］与该部分信息无直接关联，可排除。')):
                    round27_anomalies.append(('2016_ky1_q32', stem, expl[-30:]))
                elif so == 33 and (stem != 'The expression "more lenient" (Para. 4) is closest in meaning to ________.' or not expl.endswith('而其他三项则无法在其间建立顺滑的逻辑关系，故排除。')):
                    round27_anomalies.append(('2016_ky1_q33', stem, expl[-30:]))
                elif so == 34 and (stem != "When prosecutors evaluate a case, a company's CSR record ________." or not expl.endswith('企业CSR会在其被诉时创造货币价值。')):
                    round27_anomalies.append(('2016_ky1_q34', stem, expl[-30:]))
                elif so == 35 and not expl.endswith('只有［B］是对①句主要内容的同义表达。'):
                    round27_anomalies.append(('2016_ky1_q35', expl[-30:]))

            if yr == 2013 and cat == 'ky1' and so in range(26, 36):
                if not expl.startswith('［精准定位］'):
                    round27_anomalies.append(('2013_ky1_q' + str(so) + '_echo', expl[:40]))
                if so == 26 and (stem != 'It is suggested in Paragraph 1 that "behavioural" ads help advertisers to ________.' or not expl.endswith('不难推断，行为广告能帮广告商省钱。')):
                    round27_anomalies.append(('2013_ky1_q26', stem, expl[-30:]))
                elif so == 27 and (stem != '"the industry" (Line 4, Para. 3) refers to ________.' or len(expl) > 1200 or not expl.endswith('4. 将找到的词、词组或句子与四个选项进行比较，找出最佳答案。')):
                    round27_anomalies.append(('2013_ky1_q27', stem, len(expl), expl[-30:]))
                elif so == 28 and (stem != 'Bob Liodice holds that setting DNT as a default ________.' or not expl.endswith('可锁定［C］。')):
                    round27_anomalies.append(('2013_ky1_q28', stem, expl[-30:]))
                elif so == 29 and not expl.endswith('最终将正确项落在［B］。'):
                    round27_anomalies.append(('2013_ky1_q29', expl[-30:]))
                elif so == 30 and (stem != "The author's attitude towards what Brendon Lynch said in his blog is one of ________." or not expl.endswith('故表否定之意。')):
                    round27_anomalies.append(('2013_ky1_q30', stem, expl[-30:]))
                elif so == 31 and (stem != 'Our vision of the future used to be inspired by ________.' or len(expl) > 1200 or not expl.endswith('故真正的源头在前，即全句主语：科学和技术。')):
                    round27_anomalies.append(('2013_ky1_q31', stem, len(expl), expl[-30:]))
                elif so == 32 and (stem != 'The IUCN\'s "Red List" suggests that human beings are ________.' or len(expl) > 1200 or not expl.endswith('而［B］夸大人在星球中的地位，与“《名录》本身立足于自然保护（the Conservation of Nature）”脱节。')):
                    round27_anomalies.append(('2013_ky1_q32', stem, len(expl), expl[-30:]))
                elif so == 33 and (len(expl) > 1200 or not expl.endswith('阐述性信息“日益流行”、“有助于未来学研究”和“解决了社会问题”均对文意做了扭曲。')):
                    round27_anomalies.append(('2013_ky1_q33', len(expl), expl[-30:]))
                elif so == 34 and (stem != 'To ensure the future of mankind, it is crucial to ________.' or not expl.endswith('干扰项均偏离第六、七段要义。')):
                    round27_anomalies.append(('2013_ky1_q34', stem, expl[-30:]))
                elif so == 35 and (len(expl) > 1200 or not expl.endswith('另外还可结合主题词（本文为“人类未来”）对选项进行过滤，可直接排除两项。')):
                    round27_anomalies.append(('2013_ky1_q35', len(expl), expl[-30:]))

            if yr == 2020 and cat == 'ky1' and so == 36:
                if stem != 'The French Senate has passed a bill to ________.' or len(expl) > 1200 or not expl.endswith('粗犷型学习者甚至只借助“tax一词与［C］中levy一词同义”即可做出选择）。'):
                    round27_anomalies.append(('2020_ky1_q36', stem, len(expl), expl[-30:]))

            # Check Round 28: 2016 Cloze Q20, 2017 Text 4 (Q36-Q40), 2011 Cloze Q20, 2013 Cloze Q20, 2015 Text 3 Q31
            if yr == 2016 and cat == 'ky1' and so == 20:
                if len(expl) > 500 or not expl.endswith('故排除此三项。') or 'Section' in expl or '时尚业' in expl:
                    round28_anomalies.append(('2016_ky1_q20', len(expl), expl[-30:]))

            if yr == 2017 and cat == 'ky1' and so in range(36, 41):
                if not expl.startswith('［精准定位］'):
                    round28_anomalies.append(('2017_ky1_q' + str(so) + '_echo', expl[:40]))
                if so == 36 and (stem != 'The underlined sentence (Para. 1) most probably shows that the court ________.' or len(expl) > 1200 or not expl.endswith('从而确定［C］为正确项。')):
                    round28_anomalies.append(('2017_ky1_q36', stem, len(expl), expl[-30:]))
                elif so == 37 and (stem != 'According to Paragraph 4, an official act is deemed corruptive only if it involves ________.' or len(expl) > 800 or not expl.endswith('由此锁定②句（must为必要条件表达词）并根据该句句意敲定［C］正确。')):
                    round28_anomalies.append(('2017_ky1_q37', stem, len(expl), expl[-30:]))
                elif so == 38 and (stem != 'The court\'s ruling is based on the assumption that public officials are ________.' or len(expl) > 1000 or not expl.endswith('最后不难推断③句所述假设即为①句法院裁决的法律依据，最终得出正确项是［A］。')):
                    round28_anomalies.append(('2017_ky1_q38', stem, len(expl), expl[-30:]))
                elif so == 39 and (stem != 'Well-enforced laws in government transparency are needed to ________.' or len(expl) > 1000 or not expl.endswith('④干扰项最常见的设置方式是偷换对象、反向干扰、改变因果、偷换时态，曲解文意等。')):
                    round28_anomalies.append(('2017_ky1_q39', stem, len(expl), expl[-30:]))
                elif so == 40 and (stem != 'The author\'s attitude toward the court\'s ruling is ________.' or len(expl) > 1200 or not expl.endswith('如本题，作者对裁决的态度透过其所使用的饱含正面色彩的词汇legally sound、reinforces、a step forward可窥一斑。')):
                    round28_anomalies.append(('2017_ky1_q40', stem, len(expl), expl[-30:]))

            if yr == 2011 and cat == 'ky1' and so == 20:
                if len(expl) > 500 or not expl.endswith('用于引出“和之前情况相反的内容”，而文中上下文内容是契合的。') or 'Tommasini' in expl or '古典音乐' in expl:
                    round28_anomalies.append(('2011_ky1_q20', len(expl), expl[-30:]))

            if yr == 2013 and cat == 'ky1' and so == 20:
                if len(expl) > 600 or not expl.endswith('“比正常情况下有用的分数”不合文意。') or '[292 words]' in expl or 'Section' in expl:
                    round28_anomalies.append(('2013_ky1_q20', len(expl), expl[-30:]))

            if yr == 2015 and cat == 'ky1' and so == 31:
                if stem != 'It can be learned from Paragraph 1 that ________.' or len(expl) > 1000 or not expl.startswith('［精准定位］') or not expl.endswith('simplify与“开篇呈现问题”的总基调相反，故为干扰项。'):
                    round28_anomalies.append(('2015_ky1_q31', stem, len(expl), expl[-30:]))

            # Check Round 29: 2004 Cloze (Q5, Q8, Q12), 2005 Text 3 Q35, 2009 Text 3 Q35, 2008 Part B Q42, 2006 Part B Q45
            if yr == 2004 and cat == 'ky1':
                if so == 5 and (len(expl) > 600 or not expl.endswith("例句：Run, or else you'll be late. 快跑，要不然你就会迟到了。") or '语篇分析' in expl):
                    round29_anomalies.append(('2004_ky1_q5', len(expl), expl[-30:]))
                elif so == 8 and (len(expl) > 600 or not expl.endswith("例句：I am sensitive to cold. 我怕冷。") or '语篇分析' in expl):
                    round29_anomalies.append(('2004_ky1_q8', len(expl), expl[-30:]))
                elif so == 12 and (len(expl) > 800 or not expl.endswith("He is in essence an honest person. 他本质上是个诚实的人。") or '语篇分析' in expl):
                    round29_anomalies.append(('2004_ky1_q12', len(expl), expl[-30:]))

            if yr == 2005 and cat == 'ky1' and so == 35:
                if len(expl) > 1000 or not expl.endswith('最后，对号入座，敲定正确答案［A］。') or '越说越俗的英语' in expl:
                    round29_anomalies.append(('2005_ky1_q35', len(expl), expl[-30:]))

            if yr == 2009 and cat == 'ky1' and so == 35:
                if stem != 'According to the last paragraph, development of education ________.' or len(expl) > 1000 or not expl.endswith('故可快速锁定选项［C］。') or '新英格兰的早期文化生活' in expl:
                    round29_anomalies.append(('2009_ky1_q35', stem, len(expl), expl[-30:]))

            if yr == 2008 and cat == 'ky1' and so == 42:
                if not expl.startswith('［精准定位］') and (len(expl) > 1000 or not expl.endswith('因此［G］能承上启下，敲定为答案。')) or 'adds humbly' in expl:
                    round29_anomalies.append(('2008_ky1_q42', len(expl), expl[-30:]))

            if yr == 2006 and cat == 'ky1' and so == 45:
                if len(expl) > 800 or not expl.endswith('故选项应出现在第十一段之后，而不是之前，故排除。') or '对“知识分子”的定义' in expl:
                    round29_anomalies.append(('2006_ky1_q45', len(expl), expl[-30:]))

            # Check Round 30: 2021 ky2 Cloze (Q2, Q11) & Text 4 (Q36), 2022 ky1 Text 4 (Q36, Q39), 2003 ky1 Text 2 Q30, 2007 ky1 Part B Q41
            if yr == 2021 and cat == 'ky2':
                if so == 2 and (len(expl) > 800 or not expl.endswith('one已经是“被分解的、不难理解的一个要素”。') or '语篇分析' in expl or '乘坐伦敦公交车出行' in expl):
                    round30_anomalies.append(('2021_ky2_q2', len(expl), expl[-30:]))
                elif so == 11 and (len(expl) > 600 or not expl.endswith('不能与“将安全作为标准”构成“条件一结果”关联。') or '语篇分析' in expl or '第二段以多个问答形式' in expl):
                    round30_anomalies.append(('2021_ky2_q11', len(expl), expl[-30:]))
                elif so == 36 and (stem != "Nalini Ambady's study deals with ________." or len(expl) > 1500 or not expl.endswith('［A］［C］［D］均运用各项研究对参与者的不同要求捏造干扰，可排除。') or '语篇分析' in expl or '第二段继续介绍安巴迪的研究' in expl):
                    round30_anomalies.append(('2021_ky2_q36', stem, len(expl), expl[-30:]))

            if yr == 2022 and cat == 'ky1':
                if so == 36 and (stem != "The personal grievance provisions of the ERA are intended to ________." or len(expl) > 1400 or not expl.endswith('D项同时包含三个方面的内容，故锁定为正确项。') or '工作能力平平' in expl or 'But these provisions create difficulties' in expl):
                    round30_anomalies.append(('2022_ky1_q36', stem, len(expl), expl[-30:]))
                elif so == 39 and (stem != "What might be an effect of ERA's unjustified dismissal procedures?" or len(expl) > 1300 or not expl.endswith('将选项与原文相比对，详见“锁定答案”与“排除干扰”。') or '语篇分析' in expl or '不正当解雇悖论' in expl):
                    round30_anomalies.append(('2022_ky1_q39', stem, len(expl), expl[-30:]))

            if yr == 2003 and cat == 'ky1' and so == 30:
                if stem != "From the text we learn that Stephen Cooper is ________." or len(expl) > 1000 or not expl.endswith('［B］则利用文中无关信息捏造干扰。') or '铁路公司合并' in expl or 'who support mergers' in expl:
                    round30_anomalies.append(('2003_ky1_q30', stem, len(expl), expl[-30:]))

            if yr == 2007 and cat == 'ky1' and so == 41:
                if len(expl) > 600 or not expl.endswith('这些措施并未涉及“谈论未来”，故排除。') or 'Canadian Constitution' in expl or '形式主语' in expl:
                    round30_anomalies.append(('2007_ky1_q41', len(expl), expl[-30:]))

            # Check Round 31: 2021 ky2 Cloze Q14, 2007 ky1 Cloze Q15, 2004 ky1 Reading Q25,30, 2022 ky1 Reading Q27,32,37,38, 2022 ky2 Reading Q27
            if yr == 2021 and cat == 'ky2' and so == 14:
                if len(expl) > 600 or not expl.endswith('与is meant to take（时间段）无法搭配。') or '语篇分析' in expl or 'The moral of the story' in expl:
                    round31_anomalies.append(('2021_ky2_q14', len(expl), expl[-30:]))

            if yr == 2007 and cat == 'ky1' and so == 15:
                if len(expl) > 800 or not expl.endswith('但wish同样不能由rallying修饰。') or '语篇分析' in expl or 'egalitarian' in expl:
                    round31_anomalies.append(('2007_ky1_q15', len(expl), expl[-30:]))

            if yr == 2004 and cat == 'ky1':
                if so == 25 and (len(expl) > 600 or not expl.endswith('maintains his agent（保留搜索代理）。') or '参考答案at1hCMt2hBMt3hDMt4hA' in expl):
                    round31_anomalies.append(('2004_ky1_q25', len(expl), expl[-30:]))
                elif so == 30 and (len(expl) > 700 or not expl.endswith('而没有提及该现象的消除。') or '【参考答案】t1hBMt2hCMt3hC' in expl):
                    round31_anomalies.append(('2004_ky1_q30', len(expl), expl[-30:]))

            if yr == 2022 and cat == 'ky1':
                if so == 27 and (stem != 'The percentage of UK graduates in non-graduate roles reflects ________.' or len(expl) > 1400 or not expl.endswith('故A、C、D三项皆可排除。') or '从教室到讲堂的转换不是必然之路' in expl):
                    round31_anomalies.append(('2022_ky1_q27', stem, len(expl), expl[-30:]))
                elif so == 32 and (stem != 'The reworked version of The Four Seasons is mentioned to show that ________.' or len(expl) > 900 or not expl.endswith('对此应保持警惕。') or '语篇分析' in expl):
                    round31_anomalies.append(('2022_ky1_q32', stem, len(expl), expl[-30:]))
                elif so == 37 and (stem != 'It can be learned from Paragraph 3 that the provisions may ________.' or len(expl) > 1500 or not expl.endswith('D项窜改第三个因果关系。') or not any(opt.get('key') == 'B' and opt.get('text') == "undermine managers' authority" for opt in opts)):
                    round31_anomalies.append(('2022_ky1_q37', stem, len(expl), expl[-30:]))
                elif so == 38 and (stem != 'Which of the following measures would the Productivity Commission support?' or len(expl) > 1400 or not expl.endswith('故锁定为正确项。') or '语篇分析' in expl):
                    round31_anomalies.append(('2022_ky1_q38', stem, len(expl), expl[-30:]))

            if yr == 2022 and cat == 'ky2' and so == 27:
                if stem != 'It can be inferred from Paragraph 3 that Americans tend to think that ________.' or len(expl) > 800 or not expl.endswith('故正确。') or '语篇分析' in expl or 'United Income' in expl:
                    round31_anomalies.append(('2022_ky2_q27', stem, len(expl), expl[-30:]))

            # Check Round 32: 2006 ky1 T4 Q40 / 2017 ky1 Cloze Q20 / 2019 ky1 Cloze Q20 / 2022 ky2 Cloze Q2 / 2021 ky2 Cloze Q20 / 2002 ky1 Cloze Q8
            if yr == 2006 and cat == 'ky1' and so == 40:
                if len(expl) > 1200 or not expl.startswith('【精准定位】') or not expl.endswith('故均可排除。') or '回｜回回' in expl or '思墨西' in expl:
                    round32_anomalies.append(('2006_ky1_q40', len(expl), expl[:30], expl[-30:]))

            if yr == 2017 and cat == 'ky1' and so == 20:
                if len(expl) > 600 or not expl.endswith('不涉及“为之正名”的问题。') or '巒第三部金' in expl or '催产素的去向' in expl:
                    round32_anomalies.append(('2017_ky1_q20', len(expl), expl[-30:]))

            if yr == 2019 and cat == 'ky1' and so == 20:
                if len(expl) > 800 or not expl.endswith('同样与“从迷途返回”的语境不符。') or '知识补充' in expl or 'Trail blazes' in expl:
                    round32_anomalies.append(('2019_ky1_q20', len(expl), expl[-30:]))

            if yr == 2022 and cat == 'ky2' and so == 2:
                if len(expl) > 700 or not expl.endswith('均偏离文意。') or '语篇分析' in expl or 'Harlan Coben believes' in expl:
                    round32_anomalies.append(('2022_ky2_q2', len(expl), expl[-30:]))

            if yr == 2021 and cat == 'ky2' and so == 20:
                opt_texts = [o.get('text') for o in opts]
                if opt_texts != ['modify', 'review', 'present', 'achieve'] or len(expl) > 600 or not expl.endswith('也无法体现trick的“智慧方法”之意。') or 'against' in expl:
                    round32_anomalies.append(('2021_ky2_q20', opt_texts, len(expl), expl[-30:]))

            if yr == 2002 and cat == 'ky1' and so == 8:
                if not (expl.startswith('8. ［A］ concept') or expl.startswith('［试题考点］')) or len(expl) > 700 or not expl.endswith('而非“究竟看到与否”。') or '计算机也按“代”来划分' in expl:
                    round32_anomalies.append(('2002_ky1_q8', len(expl), expl[:20], expl[-30:]))

            # Check Round 33: 2008 ky1 Cloze (Q4, Q11) / 2007 ky1 Cloze Q7 / 2021 ky1 Text 3 (Q32, Q34) / 2021 ky2 Text 1 Q22 / 2022 ky2 Text 1 Q24
            if yr == 2008 and cat == 'ky1':
                if so == 4 and not expl.startswith('［精准定位］') and (not expl.startswith('4. [A] subsequently') or len(expl) > 600 or not expl.endswith('故排除。') or 'a bacterial cause were actually' in expl):
                    round33_anomalies.append(('2008_ky1_q4', len(expl), expl[:30], expl[-30:]))
                elif so == 11 and not expl.startswith('［精准定位］') and (not expl.startswith('11. [A] unconsciously') or len(expl) > 900 or not expl.endswith('而非“出人意料、不可解释地”。') or '11 . 感染；传染病' in expl):
                    round33_anomalies.append(('2008_ky1_q11', len(expl), expl[:30], expl[-30:]))

            if yr == 2007 and cat == 'ky1' and so == 7:
                if not expl.startswith('7. [A] unique') or len(expl) > 400 or not expl.endswith('这种说法显然不合逻辑。') or 'crown' in expl or 'conserv山' in expl:
                    round33_anomalies.append(('2007_ky1_q7', len(expl), expl[:30], expl[-30:]))

            if yr == 2021 and cat == 'ky1':
                if so == 32 and (not expl.startswith('［精准定位］根据题干关键词Victorian portraits he has collected') or len(expl) > 900 or not expl.endswith('故［B］正确。') or '32.关于他收集的' in expl):
                    round33_anomalies.append(('2021_ky1_q32', len(expl), expl[:30], expl[-30:]))
                elif so == 34 and (stem != 'Mark Twain is quoted to show that the disapproval of smiles in pictures was ________.' or not expl.startswith('［精准定位］题干问及作者引用马克•吐温之言的目的') or len(expl) > 1000 or not expl.endswith('就可以“既见树木，又见森林”了。') or '34.引用马克•吐温的话' in expl):
                    round33_anomalies.append(('2021_ky1_q34', stem, len(expl), expl[:30], expl[-30:]))

            if yr == 2021 and cat == 'ky2' and so == 22:
                if not expl.startswith('［精准定位］第二段②句指出') or len(expl) > 950 or not expl.endswith('故［A］正确。') or '22. 文中引用美国电话电报公司' in expl:
                    round33_anomalies.append(('2021_ky2_q22', len(expl), expl[:30], expl[-30:]))

            if yr == 2022 and cat == 'ky2' and so == 24:
                if not expl.startswith('［精准定位］末段①句指出蛋品行业') or len(expl) > 1000 or not expl.endswith('而且也符合末段主旨。') or '24.从最后一段可以得知' in expl:
                    round33_anomalies.append(('2022_ky2_q24', len(expl), expl[:30], expl[-30:]))

            # Check Round 34: 2021 ky1 T3 (Q33, Q35) / 2022 ky2 T1 (Q21-Q23, Q25) / 2022 ky2 T2 (Q26, Q28-Q30) / 2006 ky1 T2 (Q21, Q23-Q25)
            if yr == 2021 and cat == 'ky1':
                if so == 33 and (not expl.startswith('【精准定位】根据题干关键词kept the Victorians from smiling') or len(expl) > 1100 or not expl.endswith('（【B】【C】项）。') or '33.在19世纪90年代' in expl):
                    round34_anomalies.append(('2021_ky1_q33', len(expl), expl[:30], expl[-30:]))
                elif so == 35 and (not expl.startswith('【精准定位】本文首段介绍作者发现') or len(expl) > 1250 or not expl.endswith('【A】符合文章主题。') or '35.本文回答了以下哪个问题？' in expl):
                    round34_anomalies.append(('2021_ky1_q35', len(expl), expl[:30], expl[-30:]))

            if yr == 2022 and cat == 'ky2':
                if so == 21 and (stem != 'The climate-friendly eggs are produced ________.' or not expl.startswith('［精准定位］气候友好型鸡蛋出现于首段末尾') or len(expl) > 1300 or not expl.endswith('并未指出后者会替代前者。') or '21.气候友好型鸡蛋是' in expl):
                    round34_anomalies.append(('2022_ky2_q21', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 22 and (stem != 'Larry Brown is excited about his progress in ________.' or not expl.startswith('［精准定位］由人名Larry Brown及其态度') or len(expl) > 950 or not expl.endswith('为正确项。') or '22.拉里•布朗对他在' in expl):
                    round34_anomalies.append(('2022_ky2_q22', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 23 and (not expl.startswith('［精准定位］例子位于第四段②句') or len(expl) > 900 or not expl.endswith('［C］符合该论点。') or '23.第四段使用有机鸡蛋的例子' in expl):
                    round34_anomalies.append(('2022_ky2_q23', len(expl), expl[:30], expl[-30:]))
                elif so == 25 and (stem != "John Brunnquell would disagree with Julie Stanton over regenerative products' ________." or not expl.startswith('［精准定位］约翰•布伦克尔和朱莉•斯坦顿分别出自末段和第五段') or len(expl) > 1050 or not expl.endswith('推断出其言论暗含的观点态度。') or '问题速览' in expl):
                    round34_anomalies.append(('2022_ky2_q25', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 26 and (stem != 'The survey conducted by Harris Poll indicates that ________.' or not expl.startswith('［精准定位］根据survey conducted by Harris Poll定位至第二段') or len(expl) > 900 or not expl.endswith('［D］完美契合这两点要求。') or '26.哈里斯民意调查公司' in expl):
                    round34_anomalies.append(('2022_ky2_q26', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 28 and (stem != 'Retirement patterns are changing partly due to ________.' or not expl.startswith('［精准定位］根据Retirement patterns定位至第五段首句') or len(expl) > 650 or not expl.endswith('也就不会掉入命题人利用其中细节设立的陷阱。') or '28.退休模式正在发生变化' in expl):
                    round34_anomalies.append(('2022_ky2_q28', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 29 and (stem != "Many 'unretirees' are increasing their savings by ________." or not expl.startswith('［精准定位］根据increasing their savings定位至第六段②句') or len(expl) > 500 or not expl.endswith('故正确。') or '29.许多“不退休者"通过' in expl):
                    round34_anomalies.append(('2022_ky2_q29', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 30 and (not expl.startswith('［精准定位］根据Brent Weiss定位至第七、八段') or len(expl) > 750 or not expl.endswith('故均排除。') or '问题速览' in expl or 'More Americans are opting to work' in expl):
                    round34_anomalies.append(('2022_ky2_q30', len(expl), expl[:30], expl[-30:]))

            if yr == 2006 and cat == 'ky1':
                if so == 21 and (not expl.startswith('［精准定位］文章首句指出，尽管（人们）无休止地谈论差异') or len(expl) > 650 or not expl.endswith('也有助于锁定［C］。') or '第－段第二行homogenizing' in expl):
                    round34_anomalies.append(('2006_ky1_q21', len(expl), expl[:30], expl[-30:]))
                elif so == 23 and (stem != 'The text suggests that immigrants now in the U.S. ________.' or not expl.startswith('［精准定位］根据题干定位到第二段') or len(expl) > 750 or not expl.endswith('是合乎逻辑的正确推断。') or '23. 本文暗示现在美国的移民' in expl):
                    round34_anomalies.append(('2006_ky1_q23', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 24 and (stem != 'Why are Arnold Schwarzenegger and Garth Brooks mentioned in Paragraph 5?' or not expl.startswith('［精准定位］第五段首先指出') or len(expl) > 650 or not expl.endswith('直指论点核心。') or '24. 第五段为什么提到' in expl):
                    round34_anomalies.append(('2006_ky1_q24', stem, len(expl), expl[:30], expl[-30:]))
                elif so == 25 and (stem != "In the author's opinion, the absorption of immigrants into American society is ________." or not expl.startswith('【精准定位】该题考查作者态度，需纵观全文') or len(expl) > 650 or not expl.endswith('不可将其误当成作者观点。') or '25. 按照作者观点' in expl):
                    round34_anomalies.append(('2006_ky1_q25', stem, len(expl), expl[:30], expl[-30:]))

            # Check Round 35: 2004 ky1 T3 (Q31-Q35) / 2021 ky2 T1 (Q21, Q23, Q24, Q25) / 9 leakage cleanups / zero '参考答案'
            if '参考答案' in expl:
                round35_anomalies.append(('zero_cankaodaan_leakage', yr, cat, so, expl[-50:]))

            if yr == 2004 and cat == 'ky1':
                if so == 31 and (not expl.startswith('【精准定位】\n该句子的下文，即从②句 but 开始论述') or "31.By fEllenSperoisn't" in expl):
                    round35_anomalies.append(('2004_ky1_q31', expl[:50]))
                elif so == 32 and (not expl.startswith('【精准定位】\n第二段前四句先列举了经济减速的表现') or '32.Howdothepublicfeelabout' in expl):
                    round35_anomalies.append(('2004_ky1_q32', expl[:50]))
                elif so == 33 and (not expl.startswith('【精准定位】\n直接定位至第三段②句') or '33.Whenmentioningfthe$4' in expl):
                    round35_anomalies.append(('2004_ky1_q33', expl[:50]))
                elif so == 34 and (not expl.startswith('【精准定位】\n根据题干定位到最后一段首句') or '34.Whycanmanypeopleseefsilverliningsj' in expl):
                    round35_anomalies.append(('2004_ky1_q34', expl[:50]))
                elif so == 35 and (not expl.startswith('【精准定位】\n这篇文章主要涉及美国经济') or 'tThOjh' in expl or 'Dinerscangethotfood' in expl):
                    round35_anomalies.append(('2004_ky1_q35', expl[:50]))

            if yr == 2021 and cat == 'ky2':
                if so == 21 and (stem != 'Research by the World Economic Forum suggests ________.' or not expl.startswith('［精准定位］根据题干关键词Research by the World Economic Forum定位至首段③句') or 'U ❶' in expl or '21.世界经济论坛的研究表明' in expl):
                    round35_anomalies.append(('2021_ky2_q21', stem, expl[:50]))
                elif so == 23 and (stem != 'Efforts to resolve the skills mismatch in Canada ________.' or not expl.startswith('［精准定位］第二段末句指出，加拿大及其他地方所作的努力充其量只能说是迟缓无力的') or '皿❶' in expl or '23.为解决技能不匹配问题' in expl):
                    round35_anomalies.append(('2021_ky2_q23', stem, expl[:50]))
                elif so == 24 and (stem != 'We can learn from Paragraph 3 that there was ________.' or not expl.startswith('［精准定位］第三段①句指出，疫情期间失业率居高不下。') or '24.从第三段我们得知' in expl):
                    round35_anomalies.append(('2021_ky2_q24', stem, expl[:50]))
                elif so == 25 and (stem != 'Scandinavian Airlines decided to ________.' or not expl.startswith('［精准定位］由题干关键词Scandinavian Airlines快速定位至末段③句。') or '25.北欧航空公司决定' in expl):
                    round35_anomalies.append(('2021_ky2_q25', stem, expl[:50]))

            # Leakage tail cleanups
            if yr == 2014 and cat == 'ky1' and so == 28 and 'The ot' in expl:
                round35_anomalies.append(('2014_ky1_q28_leakage', expl[-40:]))
            if yr == 2001 and cat == 'ky1' and so == 34 and 'Examples of benef' in expl:
                round35_anomalies.append(('2001_ky1_q34_leakage', expl[-40:]))
            if yr == 2018 and cat == 'ky1' and so == 29 and 'So when young people' in expl:
                round35_anomalies.append(('2018_ky1_q29_leakage', expl[-40:]))
            if yr == 2017 and cat == 'ky1' and so == 23 and 'It has not gotten anywhere close' in expl:
                round35_anomalies.append(('2017_ky1_q23_leakage', expl[-40:]))
            if yr == 2010 and cat == 'ky1' and so == 28 and 'The Bilski case involves' in expl:
                round35_anomalies.append(('2010_ky1_q28_leakage', expl[-40:]))
            if yr == 2020 and cat == 'ky1' and so == 24 and 'A u town of culture could be' in expl:
                round35_anomalies.append(('2020_ky1_q24_leakage', expl[-40:]))
            if yr == 2013 and cat == 'ky1' and so == 38 and 'The 8-0 objection' in expl:
                round35_anomalies.append(('2013_ky1_q38_leakage', expl[-40:]))
            if yr == 2013 and cat == 'ky1' and so == 39 and 'Some powers do belong' in expl:
                round35_anomalies.append(('2013_ky1_q39_leakage', expl[-40:]))
            if yr == 2022 and cat == 'ky1' and so == 45 and '奢三、语篇分析' in expl:
                round35_anomalies.append(('2022_ky1_q45_leakage', expl[-40:]))

            # Check Round 36:
            # 1. Cloze leakage cleanup: 2014 ky1 Q14 / 2013 ky1 Q7 / 2015 ky1 Q2 / 2012 ky1 Q9, 14, 17
            # 2. 2021 ky2 Text 2 (Q26-Q30) full calibration
            if yr == 2014 and cat == 'ky1' and so == 14:
                if 'The Web-based program' in expl or len(expl) > 600 or not expl.endswith('与文意明显不符。'):
                    round36_anomalies.append(('2014_ky1_cloze_q14', len(expl), expl[-40:]))

            if yr == 2013 and cat == 'ky1' and so == 7:
                if 'Simonsohn suspected the truth was' in expl or len(expl) > 650 or not expl.endswith('语义相反。'):
                    round36_anomalies.append(('2013_ky1_cloze_q7', len(expl), expl[-40:]))

            if yr == 2015 and cat == 'ky1' and so == 2:
                if 'The study is a genome1 -wide analysis' in expl or 'iiMi注释' in expl or len(expl) > 500 or not expl.endswith('而是说明性内容。'):
                    round36_anomalies.append(('2015_ky1_cloze_q2', len(expl), expl[-40:]))

            if yr == 2012 and cat == 'ky1':
                if so == 9 and ('The framers' in expl or len(expl) > 450 or not expl.endswith('之间不涉及“冲突与否”。')):
                    round36_anomalies.append(('2012_ky1_cloze_q9', len(expl), expl[-40:]))
                elif so == 14 and ('Constitutional law is political' in expl or len(expl) > 400 or not expl.endswith('同样与文意无关。')):
                    round36_anomalies.append(('2012_ky1_cloze_q14', len(expl), expl[-40:]))
                elif so == 17 and ('The justices must' in expl or len(expl) > 700 or not expl.endswith('与文意相反。')):
                    round36_anomalies.append(('2012_ky1_cloze_q17', len(expl), expl[-40:]))

            if yr == 2021 and cat == 'ky2':
                if so == 26 and (stem != 'Some people argue that food self-sufficiency in the UK would ________.' or not expl.startswith('［精准定位］根据题干关键词food self-sufficiency in the UK定位至第二段') or '26.有些人提出' in expl or len(expl) > 600):
                    round36_anomalies.append(('2021_ky2_t2_q26', stem, expl[:40]))
                elif so == 27 and (stem != 'The report by the University of Leeds shows that in the UK ________.' or not expl.startswith('［精准定位］根据题干关键词The report by the University of Leeds定位到第三段①句') or '27.利兹大学的报告显示' in expl or len(expl) > 900):
                    round36_anomalies.append(('2021_ky2_t2_q27', stem, expl[:40]))
                elif so == 28 and (stem != 'Crop-growing in the UK is restricted due to ________.' or not expl.startswith('［精准定位］第五段首句指出转向以植物为主的饮食也不会有太大意义') or '28.英国的作物种植因' in expl or 'Just 23 per cent' in expl or not expl.endswith('［B］则颠倒因果。')):
                    round36_anomalies.append(('2021_ky2_t2_q28', stem, expl[:40], expl[-40:]))
                elif so == 29 and (stem != 'It can be learned from the last paragraph that British people ________.' or not expl.startswith('［精准定位］末段①句指出“如今英国人食用的果蔬中仅有23%产自本国”') or '29.从末段可知' in expl or not expl.endswith('故为正确项。')):
                    round36_anomalies.append(('2021_ky2_t2_q29', stem, expl[:40], expl[-40:]))
                elif so == 30 and (stem != "The author's attitude to food self-sufficiency in the UK is ________." or not expl.startswith('［精准定位］本文整体脉络为：引出话题“英国粮食自给自足是否可行”') or '30•作者对英国粮食自给自足的态度' in expl or 'Text 3' in expl or not expl.endswith('更何况这本身实行起来会造成巨大代价”。')):
                    round36_anomalies.append(('2021_ky2_t2_q30', stem, expl[:40], expl[-40:]))

            # Check Round 37:
            # 1. 2013 ky1 Text 1 (Q21-Q25) full golden calibration
            # 2. 2007 ky1 Text 1 (Q21-Q25) full golden calibration
            if yr == 2013 and cat == 'ky1':
                if so == 21 and (stem != 'Priestly criticizes her assistant for her ________.' or not expl.startswith('［精准定位］第一段①句指出Priestly在斥责助手') or not expl.endswith('根据②句解释可知偏离文意。')):
                    round37_anomalies.append(('2013_ky1_t1_q21', stem, expl[:40], expl[-40:]))
                elif so == 22 and (stem != 'According to Cline, mass-market labels urge consumers to ________.' or not expl.startswith('［精准定位］第二段④句指出，大众品牌鼓励消费者') or '22.' in expl[:50] or not expl.endswith('同时排除与之矛盾的［A］、［C］、［D］。')):
                    round37_anomalies.append(('2013_ky1_t1_q22', stem, expl[:40], expl[-40:]))
                elif so == 23 and (stem != 'The word "indictment" (Line 3, Para. 2) is closest in meaning to ________.' or not expl.startswith('［精准定位］由考查词所在句（第二段①句）可知') or '23.' in expl[:50] or not expl.endswith('均体现Cline对快时尚的态度）。')):
                    round37_anomalies.append(('2013_ky1_t1_q23', stem, expl[:40], expl[-40:]))
                elif so == 24 and (stem != 'Which of the following can be inferred from the last paragraph?' or not expl.startswith('［精准定位］末段③句指出，虚荣深植人心') or '24.' in expl[:50] or not expl.endswith('故舍［D］选［C］。')):
                    round37_anomalies.append(('2013_ky1_t1_q24', stem, expl[:40], expl[-40:]))
                elif so == 25 and (stem != 'What is the subject of the text?' or not expl.startswith('［精准定位］文章第一至三段引出并介绍克莱恩该书作对大众品牌驱动快时尚的强烈批判。') or '25.' in expl[:50] or len(expl) < 500 or not expl.endswith('均非全文关注对象。')):
                    round37_anomalies.append(('2013_ky1_t1_q25', stem, expl[:40], expl[-40:]))

            if yr == 2007 and cat == 'ky1':
                if so == 21 and (stem != 'The birthday phenomenon found among soccer players is mentioned to ________.' or opt_map.get('C') != 'introduce the topic of what makes expert performance' or not expl.startswith('［精准定位］文章前两段言及足球运动员生日现象') or '21.' in expl[:50] or not expl.endswith('文首现象仅为引出这一话题服务，敲定［C］正确。')):
                    round37_anomalies.append(('2007_ky1_t1_q21', stem, opt_map.get('C'), expl[:40], expl[-40:]))
                elif so == 22 and (stem != 'The word “mania” (Line 4, Paragraph 2) most probably means ________.' or opt_map.get('D') != 'excitement' or not expl.startswith('［精准定位］被考查词上文指出') or 'Anders Ericsson' in expl or not expl.endswith('最终锁定答案为［B］。')):
                    round37_anomalies.append(('2007_ky1_t1_q22', stem, opt_map.get('D'), expl[:40], expl[-40:]))
                elif so == 23 and (stem != 'According to Ericsson, good memory ________.' or not expl.startswith('［精准定位］第四段②③句明确指出') or '【选项释义与词汇辨析】' in expl or not expl.endswith('相比之下，正确项则通常具有归纳概括性。')):
                    round37_anomalies.append(('2007_ky1_t1_q23', stem, expl[:40], expl[-40:]))
                elif so == 24 and (stem != 'Ericsson and his colleagues believe that ________.' or opt_map.get('A') != 'talent is a dominating factor for professional success' or opt_map.get('D') != 'high achievers owe their success mostly to nurture' or not expl.startswith('［精准定位］第五段④句以另一种方式重述了') or '24.' in expl[:50] or not expl.endswith('由此最终敲定［D］正确。')):
                    round37_anomalies.append(('2007_ky1_t1_q24', stem, opt_map, expl[:40], expl[-40:]))
                elif so == 25 and (stem != 'Which of the following proverbs is closest to the message the text tries to convey?' or not expl.startswith('［精准定位］文章开篇由“优秀球员生日现象”引入') or '25.' in expl[:50] or not expl.endswith('抓住文章脉络进行解答。')):
                    round37_anomalies.append(('2007_ky1_t1_q25', stem, expl[:40], expl[-40:]))

            # Check Round 38: 2011 ky1 Reading Comprehension (Q21-Q40)
            if yr == 2011 and cat == 'ky1' and 21 <= so <= 40:
                if not (expl.startswith('［精准定位］') or expl.startswith('【精准定位】')) or '[A]' in expl[:80] or '21.' in expl[:50] or '28.' in expl[:50] or '31.' in expl[:50]:
                    round38_anomalies.append((f'2011_ky1_q{so}_head_stacked', expl[:60]))
                if so == 24 and stem != 'According to the text, which of the following is true of recordings?':
                    round38_anomalies.append(('2011_ky1_q24_stem', stem))
                elif so == 27 and (opt_map.get('D') != 'their pursuit of new career goals' or opt_map.get('C') != 'their strained relations with the boards'):
                    round38_anomalies.append(('2011_ky1_q27_opts', opt_map))
                elif so == 28 and (stem != 'The word "poached" (Line 3, Paragraph 4) most probably means ________.' or opt_map.get('C') != 'hunted for'):
                    round38_anomalies.append(('2011_ky1_q28', stem, opt_map))
                elif so == 31 and stem != 'Consumers may create "earned" media when they are ________.':
                    round38_anomalies.append(('2011_ky1_q31_stem', stem))
                elif so == 34 and ('Motor9' in stem or 'Toyota Motor9' in expl):
                    round38_anomalies.append(('2011_ky1_q34_motor9', stem, expl[:60]))
                elif so == 36 and stem != 'Jennifer Senior suggests in her article that raising a child can bring ________.':
                    round38_anomalies.append(('2011_ky1_q36_stem', stem))
                elif so == 38 and not expl.startswith('［精准定位］第三段②③句指出：不快乐的无子女者不断被外界信息所烦扰'):
                    round38_anomalies.append(('2011_ky1_q38_expl', expl[:60]))

            # Check Round 39: 2014 ky1 Reading Comprehension (Q21-Q40)
            if yr == 2014 and cat == 'ky1' and 21 <= so <= 40:
                if not (expl.startswith('［精准定位］') or expl.startswith('【精准定位】')) or '[A]' in expl[:80] or '21.' in expl[:50] or '26.' in expl[:50] or '31.' in expl[:50] or '36.' in expl[:50]:
                    round39_anomalies.append((f'2014_ky1_q{so}_head_stacked', expl[:60]))
                if expl.rstrip().endswith(('benefits get into w', 'undergraduate degree in', 'draw people into', 'maintain national')):
                    round39_anomalies.append((f'2014_ky1_q{so}_leakage', expl[-60:]))
                if so == 21 and stem != "George Osborne's scheme was intended to ________.":
                    round39_anomalies.append(('2014_ky1_q21_stem', stem))
                elif so == 24 and stem != "According to Paragraph 3, being unemployed makes one feel ________.":
                    round39_anomalies.append(('2014_ky1_q24_stem', stem))
                elif so == 26 and stem != "A lot of students take up law as their profession due to ________.":
                    round39_anomalies.append(('2014_ky1_q26_stem', stem))
                elif so == 27 and stem != "Which of the following adds to the costs of legal education in most American states?":
                    round39_anomalies.append(('2014_ky1_q27_stem', stem))
                elif so == 28 and stem != "Hindrance to the reform of the legal system originates from ________.":
                    round39_anomalies.append(('2014_ky1_q28_stem', stem))
                elif so == 29 and stem != 'The guild-like ownership structure is considered "restrictive" partly because it ________.':
                    round39_anomalies.append(('2014_ky1_q29_stem', stem))
                elif so == 30 and (stem != "In this text, the author mainly discusses ________." or ans != 'B'):
                    round39_anomalies.append(('2014_ky1_q30', stem, ans))
                elif so == 35 and (stem != "The author believes that the new awards are ________." or ans != 'D'):
                    round39_anomalies.append(('2014_ky1_q35', stem, ans))
                elif so == 37 and (stem != "Influential figures in the Congress required that the AAAS report on how to ________." or '匹语篇分析' in expl or not (expl.startswith('［精准定位］第二段首句明确指出：国会重要人物要求') or expl.startswith('【精准定位】第二段首句明确指出：国会重要人物要求'))):
                    round39_anomalies.append(('2014_ky1_q37', stem, expl[:60]))
                elif so == 38 and stem != "According to Paragraph 3, the report suggests ________.":
                    round39_anomalies.append(('2014_ky1_q38_stem', stem))
                for ok, ov in opt_map.items():
                    if len(str(ov).strip()) <= 1 or str(ov).strip() == ok:
                        round39_anomalies.append((f'2014_ky1_q{so}_opt_placeholder_{ok}', ov))

            # Check Round 40: 2021 ky2 Reading Comprehension Text 3 & 4 (Q31-Q40)
            if yr == 2021 and cat == 'ky2' and 31 <= so <= 40:
                if not expl.startswith('［精准定位］') or '31.' in expl[:50] or '32.' in expl[:50] or '33.' in expl[:50] or '34.' in expl[:50] or '35.' in expl[:50] or '36.' in expl[:50] or '37.' in expl[:50] or '38.' in expl[:50] or '39.' in expl[:50] or '40.' in expl[:50]:
                    round40_anomalies.append((f'2021_ky2_q{so}_head_stacked', expl[:60]))
                if so == 31 and (opt_map.get('A') != 'Their engineers were retained.' or ans != 'A'):
                    round40_anomalies.append(('2021_ky2_q31', ans, opt_map))
                elif so == 32:
                    if ans != 'B' or stem != "Microsoft's critics believe that the big tech companies tend to ________." or opt_map.get('B') != 'eliminate their potential competitors' or not expl.rstrip().endswith('与之相匹配的唯有［B］。'):
                        round40_anomalies.append(('2021_ky2_q32', stem, ans, opt_map, expl[-60:]))
                elif so == 33:
                    if ans != 'C' or stem != "Paul Arnold is concerned that small acquisitions might ________." or opt_map.get('A') != 'weaken big tech companies' or opt_map.get('B') != 'worsen market competition' or opt_map.get('C') != 'harm the national economy' or opt_map.get('D') != 'discourage start-up investors' or not expl.rstrip().endswith('从而锁定正确答案为［C］。'):
                        round40_anomalies.append(('2021_ky2_q33', stem, ans, opt_map, expl[-60:]))
                elif so == 34:
                    if ans != 'C' or stem != "The US Federal Trade Commission intends to ________." or opt_map.get('D') != "supervise start-ups' operation" or not expl.rstrip().endswith('可进一步佐证。'):
                        round40_anomalies.append(('2021_ky2_q34', stem, ans, opt_map, expl[-60:]))
                elif so == 35:
                    if ans != 'A' or stem != "For the five biggest tech companies, their small acquisitions have ________." or opt_map.get('A') != 'brought little financial pressure' or not expl.rstrip().endswith('不难锁定正确项为［A］。'):
                        round40_anomalies.append(('2021_ky2_q35', stem, ans, opt_map, expl[-60:]))
                elif so == 36:
                    if ans != 'B' or stem != "Nalini Ambady's study deals with ________." or opt_map.get('B') != 'the reliability of first impressions' or not expl.rstrip().endswith('［A］［C］［D］均运用各项研究对参与者的不同要求捏造干扰，可排除。'):
                        round40_anomalies.append(('2021_ky2_q36', stem, ans, opt_map, expl[-60:]))
                elif so == 37:
                    if ans != 'A' or stem != "In Ambady's study, rating accuracy dropped when participants ________." or opt_map.get('A') != 'focused on specific details' or not expl.rstrip().endswith('浏览选项后可锁定［A］选项为对评分下降原因的正确描述，其他三个选项均属主观臆断，可排除。'):
                        round40_anomalies.append(('2021_ky2_q37', stem, ans, opt_map, expl[-60:]))
                elif so == 38:
                    if ans != 'A' or stem != "Judith Hall mentions driving to show that ________." or opt_map.get('A') != 'reflection can be distracting' or not expl.rstrip().endswith('因此，朱迪斯•霍尔提及驾驶是为了表明（处理社交信息时）深思熟虑反会让人分心。'):
                        round40_anomalies.append(('2021_ky2_q38', stem, ans, opt_map, expl[-60:]))
                elif so == 39:
                    if ans != 'D' or stem != "When you are making complex decisions, it is advisable to ________." or opt_map.get('D') != 'follow your feelings' or not expl.rstrip().endswith('不在本题考查的信息范围内，因此排除。'):
                        round40_anomalies.append(('2021_ky2_q39', stem, ans, opt_map, expl[-60:]))
                elif so == 40:
                    if ans != 'B' or stem != "What can we learn from the last paragraph?" or opt_map.get('B') != 'Intuition may affect reflective tasks.' or not expl.rstrip().endswith('［B］选项符合这一逻辑推理。'):
                        round40_anomalies.append(('2021_ky2_q40', stem, ans, opt_map, expl[-60:]))

            # Check Round 41: 2017 ky1 Reading Comprehension Text 1 (Q21-Q25)
            if yr == 2017 and cat == 'ky1' and 21 <= so <= 25:
                if not expl.startswith('［精准定位］') or '21.' in expl[:50] or '22.' in expl[:50] or '23.' in expl[:50] or '24.' in expl[:50] or '25.' in expl[:50]:
                    round41_anomalies.append((f'2017_ky1_q{so}_head_stacked', expl[:60]))
                if so == 21:
                    if ans != 'A' or stem != "The crash of EgyptAir Flight 804 is mentioned to ________." or opt_map.get('A') != "explain Americans' tolerance of current security checks" or not expl.rstrip().endswith('其余项均脱离该内容。'):
                        round41_anomalies.append(('2017_ky1_q21', stem, ans, opt_map, expl[-60:]))
                elif so == 22:
                    if ans != 'C' or stem != "Which of the following contributes to long waits at major airports?" or opt_map.get('A') != 'New restrictions on carry-on bags.' or opt_map.get('C') != 'An increase in the number of travelers.' or not expl.rstrip().endswith('不难确定正确项。'):
                        round41_anomalies.append(('2017_ky1_q22', stem, ans, opt_map, expl[-60:]))
                elif so == 23:
                    if ans != 'D' or stem != 'The word "expedited" (Line 4, Para. 5) is closest in meaning to ________.' or opt_map.get('D') != 'faster' or not expl.rstrip().endswith('故faster最接近expedited词义。'):
                        round41_anomalies.append(('2017_ky1_q23', stem, ans, opt_map, expl[-60:]))
                elif so == 24:
                    if ans != 'D' or stem != "One problem with the PreCheck program is ________." or opt_map.get('A') != 'a dramatic reduction of its scale' or opt_map.get('D') != 'an unreasonable price for enrollment' or not expl.rstrip().endswith('过度引申出“国会不愿支持预检计划”。'):
                        round41_anomalies.append(('2017_ky1_q24', stem, ans, opt_map, expl[-60:]))
                elif so == 25:
                    if ans != 'C' or stem != "Which of the following would be the best title for the text?" or opt_map.get('B') != 'PreCheck — a Belated Solution' or opt_map.get('C') != 'Getting Stuck in Security Lines' or not expl.rstrip().endswith('以偏概全。'):
                        round41_anomalies.append(('2017_ky1_q25', stem, ans, opt_map, expl[-60:]))

            # Check Round 42: 2009 ky1 Reading Comprehension Text 1 (Q21-Q25) & Text 2 (Q26-Q28)
            if yr == 2009 and cat == 'ky1' and 21 <= so <= 28:
                if not expl.startswith('［精准定位］') or '21.' in expl[:50] or '22.' in expl[:50] or '23.' in expl[:50] or '24.' in expl[:50] or '25.' in expl[:50] or '26.' in expl[:50] or '27.' in expl[:50] or '28.' in expl[:50]:
                    round42_anomalies.append((f'2009_ky1_q{so}_head_stacked', expl[:60]))
                if so == 21:
                    if ans != 'C' or stem != 'In Wordsworth\'s view, "habit" is characterized by being ________.' or opt_map.get('C') != 'mechanical' or not expl.rstrip().endswith('确定［C］正确。'):
                        round42_anomalies.append(('2009_ky1_q21', stem, ans, opt_map, expl[-60:]))
                elif so == 22:
                    if ans != 'D' or stem != 'Brain researchers have discovered that the formation of new habits can be ________.' or opt_map.get('D') != 'guided' or not expl.rstrip().endswith('故排除。'):
                        round42_anomalies.append(('2009_ky1_q22', stem, ans, opt_map, expl[-60:]))
                elif so == 23:
                    if ans != 'A' or stem != 'The word "ruts" (Line 1, Paragraph 4) is closest in meaning to ________.' or opt_map.get('A') != 'tracks' or not expl.rstrip().endswith('故确定［A］正确。'):
                        round42_anomalies.append(('2009_ky1_q23', stem, ans, opt_map, expl[-60:]))
                elif so == 24:
                    if ans != 'D' or stem != 'Dawna Markova would most probably agree that ________.' or opt_map.get('D') != 'curiosity activates creative minds' or not expl.rstrip().endswith('无关 Dawna 观点。'):
                        round42_anomalies.append(('2009_ky1_q24', stem, ans, opt_map, expl[-60:]))
                elif so == 25:
                    if ans != 'A' or stem != 'Ryan\'s comments suggest that the practice of standardized testing ________.' or opt_map.get('A') != 'prevents new habits from being formed' or len(expl) < 700 or not expl.rstrip().endswith('排除［B］。'):
                        round42_anomalies.append(('2009_ky1_q25', stem, ans, opt_map, expl[-60:]))
                elif so == 26:
                    if ans != 'A' or stem != 'In Paragraphs 1 and 2, the text shows PTK\'s ________.' or opt_map.get('A') != 'easy availability' or not expl.rstrip().endswith('即可推导出答案［A］。'):
                        round42_anomalies.append(('2009_ky1_q26', stem, ans, opt_map, expl[-60:]))
                elif so == 27:
                    if ans != 'C' or stem != 'PTK is used to ________.' or opt_map.get('C') != 'identify parent-child kinship' or not expl.rstrip().endswith('track down kids put up for adoption。'):
                        round42_anomalies.append(('2009_ky1_q27', stem, ans, opt_map, expl[-60:]))
                elif so == 28:
                    if ans != 'D' or stem != 'Skeptical observers believe that ancestry testing fails to ________.' or opt_map.get('D') != 'achieve the claimed accuracy' or not expl.rstrip().endswith('故正确。'):
                        round42_anomalies.append(('2009_ky1_q28', stem, ans, opt_map, expl[-60:]))

            # Check Round 43: 2009 ky1 Reading Comprehension Text 3 & 4 (Q31-Q40)
            if yr == 2009 and cat == 'ky1' and 31 <= so <= 40:
                if not expl.startswith('［精准定位］') or '31.' in expl[:50] or '32.' in expl[:50] or '33.' in expl[:50] or '34.' in expl[:50] or '35.' in expl[:50] or '36.' in expl[:50] or '37.' in expl[:50] or '38.' in expl[:50] or '39.' in expl[:50] or '40.' in expl[:50]:
                    round43_anomalies.append((f'2009_ky1_q{so}_head_stacked', expl[:60]))
                if so == 31:
                    if ans != 'D' or stem != 'The author holds in Paragraph 1 that the importance of education in poor countries ________.' or opt_map.get('D') != 'has been overestimated' or not expl.rstrip().endswith('通常正确答案在两者之中。'):
                        round43_anomalies.append(('2009_ky1_q31', stem, ans, opt_map, expl[-60:]))
                elif so == 32:
                    if ans != 'B' or stem != 'It is stated in Paragraph 1 that the construction of a new educational system ________.' or opt_map.get('B') != 'takes efforts of generations' or not expl.rstrip().endswith('快速锁定答案。'):
                        round43_anomalies.append(('2009_ky1_q32', stem, ans, opt_map, expl[-60:]))
                elif so == 33:
                    if ans != 'B' or stem != 'A major difference between the Japanese and U.S. workforces is that ________.' or opt_map.get('B') != 'the Japanese workforce is more productive' or not expl.rstrip().endswith('故而迅速锁定答案为［B］。'):
                        round43_anomalies.append(('2009_ky1_q33', stem, ans, opt_map, expl[-60:]))
                elif so == 34:
                    if ans != 'C' or stem != 'The author quotes the example of our ancestors to show that education emerged ________.' or opt_map.get('C') != 'when people no longer went hungry' or not expl.rstrip().endswith('故排除。'):
                        round43_anomalies.append(('2009_ky1_q34', stem, ans, opt_map, expl[-60:]))
                elif so == 35:
                    if ans != 'C' or stem != 'According to the last paragraph, development of education ________.' or opt_map.get('A') != 'results directly from competitive environments' or opt_map.get('B') != 'does not depend on economic performance' or opt_map.get('C') != 'follows improved productivity' or not expl.rstrip().endswith('故可快速锁定选项［C］。'):
                        round43_anomalies.append(('2009_ky1_q35', stem, ans, opt_map, expl[-60:]))
                elif so == 36:
                    if ans != 'B' or stem != 'The author holds that in the seventeenth-century New England ________.' or opt_map.get('B') != 'intellectual interests were encouraged' or not expl.rstrip().endswith('因此排除。'):
                        round43_anomalies.append(('2009_ky1_q36', stem, ans, opt_map, expl[-60:]))
                elif so == 37:
                    if ans != 'B' or stem != 'It is suggested in Paragraph 2 that New Englanders ________.' or opt_map.get('A') != 'experienced a comparatively peaceful early history' or opt_map.get('B') != 'brought with them the culture of the Old World' or not expl.rstrip().endswith('得到正确答案［B］。'):
                        round43_anomalies.append(('2009_ky1_q37', stem, ans, opt_map, expl[-60:]))
                elif so == 38:
                    if ans != 'D' or stem != 'The early ministers and political leaders in Massachusetts Bay ________.' or opt_map.get('D') != 'created a new intellectual atmosphere in New England' or not expl.rstrip().endswith('与“新大陆的文化生活”无关。'):
                        round43_anomalies.append(('2009_ky1_q38', stem, ans, opt_map, expl[-60:]))
                elif so == 39:
                    if ans != 'A' or stem != 'The story of John Dane shows that less well-educated New Englanders were often ________.' or opt_map.get('A') != 'influenced by superstitions' or opt_map.get('B') != 'troubled with religious beliefs' or opt_map.get('C') != 'puzzled by church sermons' or opt_map.get('D') != 'frustrated with family earnings' or not expl.rstrip().endswith('从而快速锁定答案［A］。'):
                        round43_anomalies.append(('2009_ky1_q39', stem, ans, opt_map, expl[-60:]))
                elif so == 40:
                    if ans != 'C' or stem != 'The text suggests that early settlers in New England ________.' or opt_map.get('C') != 'came from different intellectual backgrounds' or not expl.rstrip().endswith('如［A］、［B］、［D］。'):
                        round43_anomalies.append(('2009_ky1_q40', stem, ans, opt_map, expl[-60:]))

            # Check Round 45: 2003 ky1 Questions (Q1-Q40 calibration)
            if yr == 2003 and cat == 'ky1':
                if so == 17:
                    if ans != 'B' or opt_map.get('B') != 'down' or 'let down' not in expl:
                        round45_anomalies.append(('2003_ky1_q17', ans, opt_map, expl[:50]))
                elif so == 20:
                    if ans != 'A' or opt_map.get('A') != 'capabilities' or 'within capabilities' not in expl:
                        round45_anomalies.append(('2003_ky1_q20', ans, opt_map, expl[:50]))
                elif 21 <= so <= 40:
                    # Verify no bilingual header leakage in reading explanations
                    if any(f"{so}." in expl[:50] for so in range(21, 41)):
                        round45_anomalies.append((f'2003_ky1_q{so}_header_leak', expl[:60]))
                    
                    if so == 21:
                        if ans != 'B' or stem != 'The emergence of the Net has ________.' or opt_map.get('B') != 'remolded the intelligence services' or not expl.endswith('［A］正确。'):
                            round45_anomalies.append(('2003_ky1_q21', stem, ans, opt_map, expl[-40:]))
                    elif so == 22:
                        if ans != 'A' or stem != "Donovan's story is mentioned in the text to ________." or opt_map.get('A') != 'introduce the topic of online spying' or not expl.endswith('致命错误。'):
                            round45_anomalies.append(('2003_ky1_q22', stem, ans, opt_map, expl[-40:]))
                    elif so == 23:
                        if ans != 'C' or stem != 'The phrase "making the biggest splash" (Line 1, Paragraph 3) most probably means ________.' or opt_map.get('C') != 'achieving the greatest success' or not expl.endswith('错误引申。'):
                            round45_anomalies.append(('2003_ky1_q23', stem, ans, opt_map, expl[-40:]))
                    elif so == 24:
                        if ans != 'D' or stem != 'It can be learned from Paragraph 4 that ________.' or opt_map.get('D') != 'Straitford is able to provide fairly reliable information' or not expl.endswith('故舍［B］选［D］。'):
                            round45_anomalies.append(('2003_ky1_q24', stem, ans, opt_map, expl[-40:]))
                    elif so == 25:
                        if ans != 'B' or stem != 'Straitford is most proud of its ________.' or opt_map.get('B') != 'nonconformist image' or not expl.endswith('选取［B］。'):
                            round45_anomalies.append(('2003_ky1_q25', stem, ans, opt_map, expl[-40:]))
                    elif so == 26:
                        if ans != 'A' or stem != "The author begins his article with Edmund Burke's words to ________." or opt_map.get('A') != 'call on scientists to take some actions' or not expl.endswith('“已有事实”。'):
                            round45_anomalies.append(('2003_ky1_q26', stem, ans, opt_map, expl[-40:]))
                    elif so == 27:
                        if ans != 'B' or stem != 'Misled people tend to think that using an animal in research is ________.' or opt_map.get('A') != 'cruel but natural' or opt_map.get('B') != 'inhuman and unacceptable' or opt_map.get('C') != 'inevitable but vicious' or opt_map.get('D') != 'pointless and wasteful' or not expl.endswith('抵制态度。'):
                            round45_anomalies.append(('2003_ky1_q27', stem, ans, opt_map, expl[-40:]))
                    elif so == 28:
                        if ans != 'B' or stem != "The example of the grandmotherly woman is used to show the public's ________." or opt_map.get('A') != 'discontent with animal research' or opt_map.get('B') != 'ignorance about medical science' or opt_map.get('C') != 'indifference to epidemics' or opt_map.get('D') != 'anxiety about animal rights' or not expl.endswith('故错误。'):
                            round45_anomalies.append(('2003_ky1_q28', stem, ans, opt_map, expl[-40:]))
                    elif so == 29:
                        if ans != 'A' or stem != 'The author believes that, in face of the challenge from animal rights advocates, scientists should ________.' or opt_map.get('A') != 'communicate more with the public' or not expl.endswith('顺滑逻辑。'):
                            round45_anomalies.append(('2003_ky1_q29', stem, ans, opt_map, expl[-40:]))
                    elif so == 30:
                        if ans != 'D' or stem != 'From the text we learn that Stephen Cooper is ________.' or opt_map.get('D') != 'a supporter of animal research' or not expl.endswith('捏造干扰。'):
                            round45_anomalies.append(('2003_ky1_q30', stem, ans, opt_map, expl[-40:]))
                    elif so == 31:
                        if ans != 'C' or stem != 'According to those who support mergers, railway monopoly is unlikely because ________.' or opt_map.get('A') != 'cost reduction is based on competition' or opt_map.get('B') != 'services call for cross-trade coordination' or opt_map.get('C') != 'outside competitors will continue to exist' or opt_map.get('D') != 'shippers will have the railway by the throat' or not expl.endswith('正确答案。'):
                            round45_anomalies.append(('2003_ky1_q31', stem, ans, opt_map, expl[-40:]))
                    elif so == 32:
                        if ans != 'D' or stem != "What is many captive shippers' attitude towards the consolidation in the rail industry?" or opt_map.get('D') != 'Apprehensive' or not expl.endswith('漠不关心”）。'):
                            round45_anomalies.append(('2003_ky1_q32', stem, ans, opt_map, expl[-40:]))
                    elif so == 33:
                        if ans != 'C' or stem != 'It can be inferred from Paragraph 3 that ________.' or opt_map.get('C') != 'overcharged shippers are unlikely to appeal for rate relief' or not expl.endswith('故排除。'):
                            round45_anomalies.append(('2003_ky1_q33', stem, ans, opt_map, expl[-40:]))
                    elif so == 34:
                        if ans != 'B' or stem != 'The word "arbiters" (Line 6, Paragraph 4) most probably refers to those ________.' or opt_map.get('B') != 'who function as judges' or not expl.endswith('正确解释。'):
                            round45_anomalies.append(('2003_ky1_q34', stem, ans, opt_map, expl[-40:]))
                    elif so == 35:
                        if ans != 'A' or stem != 'According to the text, the cost increase in the rail industry is mainly caused by ________.' or opt_map.get('A') != 'the continuing acquisition' or not expl.endswith('［A］为答案。'):
                            round45_anomalies.append(('2003_ky1_q35', stem, ans, opt_map, expl[-40:]))
                    elif so == 36:
                        if ans != 'C' or stem != 'What is implied in the first sentence?' or opt_map.get('A') != 'Americans are better prepared for death than other people.' or opt_map.get('C') != 'Americans are over-confident of their medical technology.' or not expl.endswith('故正确。'):
                            round45_anomalies.append(('2003_ky1_q36', stem, ans, opt_map, expl[-40:]))
                    elif so == 37:
                        if ans != 'A' or stem != 'The author uses the example of cancer patients to show that ________.' or opt_map.get('A') != 'medical resources are often wasted' or opt_map.get('B') != 'doctors are helpless against fatal diseases' or opt_map.get('C') != 'some treatments are too aggressive' or opt_map.get('D') != 'medical costs are becoming unaffordable' or not expl.endswith('曲解原文。'):
                            round45_anomalies.append(('2003_ky1_q37', stem, ans, opt_map, expl[-40:]))
                    elif so == 38:
                        if ans != 'B' or stem != "The author's attitude toward Richard Lamm's remark is one of ________." or opt_map.get('B') != 'reserved consent' or not expl.endswith('［B］。'):
                            round45_anomalies.append(('2003_ky1_q38', stem, ans, opt_map, expl[-40:]))
                    elif so == 39:
                        if ans != 'D' or stem != 'In contrast to the US, Japan and Sweden are funding their medical care ________.' or opt_map.get('D') != 'more reasonably' or not expl.endswith('主题服务。'):
                            round45_anomalies.append(('2003_ky1_q39', stem, ans, opt_map, expl[-40:]))
                    elif so == 40:
                        if ans != 'C' or stem != 'The text intends to express the idea that ________.' or opt_map.get('C') != 'death should be accepted as a fact of life' or not expl.endswith('［C］。'):
                            round45_anomalies.append(('2003_ky1_q40', stem, ans, opt_map, expl[-40:]))

            # Check Round 46: 2002 ky1 Questions (Q1-Q40 calibration & 5 deadly errors fixed)
            if yr == 2002 and cat == 'ky1':
                if so == 5:
                    if ans != 'B' or opt_map.get('B') != 'speeded':
                        round46_anomalies.append(('2002_ky1_q5', ans, opt_map.get('B')))
                elif so == 14:
                    if ans != 'C' or opt_map.get('C') != 'capacity':
                        round46_anomalies.append(('2002_ky1_q14', ans, opt_map.get('C')))
                elif so == 19:
                    if ans != 'B' or opt_map.get('B') != 'controversial':
                        round46_anomalies.append(('2002_ky1_q19', ans, opt_map.get('B')))
                elif so == 21:
                    if ans != 'C' or stem != 'To make your humor work, you should ________.' or opt_map.get('C') != 'address different problems to different people':
                        round46_anomalies.append(('2002_ky1_q21', stem, ans, opt_map))
                elif so == 22:
                    if ans != 'B' or opt_map.get('B') != 'very conscious of their godlike role':
                        round46_anomalies.append(('2002_ky1_q22', ans, opt_map.get('B')))
                elif so == 23:
                    if ans != 'D' or opt_map.get('D') != 'have often been the laughing stock':
                        round46_anomalies.append(('2002_ky1_q23', ans, opt_map.get('D')))
                elif so == 28:
                    if ans != 'D' or opt_map.get('A') != 'fulfill delicate tasks like performing brain surgery':
                        round46_anomalies.append(('2002_ky1_q28', ans, opt_map.get('A')))
                elif so == 29:
                    if ans != 'B' or opt_map.get('D') != 'cultivate human creativity':
                        round46_anomalies.append(('2002_ky1_q29', ans, opt_map.get('D')))
                elif so == 30:
                    if ans != 'C' or stem != 'The author uses the example of a monkey to argue that robots are ________.':
                        round46_anomalies.append(('2002_ky1_q30', stem, ans))
                elif so == 32:
                    if ans != 'D' or stem != 'It can be inferred from the text that the retail price of petrol will go up for even a small change in crude oil prices if ________.':
                        round46_anomalies.append(('2002_ky1_q32', stem, ans))
                elif so == 34:
                    if ans != 'A' or opt_map.get('A') != 'oil price shocks are less shocking now':
                        round46_anomalies.append(('2002_ky1_q34', ans, opt_map.get('A')))
                elif so == 36:
                    if ans != 'B' or "their patients' pain" not in opt_map.get('A', '') or 'physician-assisted suicide' not in opt_map.get('C', ''):
                        round46_anomalies.append(('2002_ky1_q36', ans, opt_map))
                elif so == 39:
                    if ans != 'A' or opt_map.get('A') != 'Bold':
                        round46_anomalies.append(('2002_ky1_q39', ans, opt_map.get('A')))
                elif so == 40:
                    if ans != 'D' or stem != 'George Annas would probably agree that doctors should be punished if they ________.':
                        round46_anomalies.append(('2002_ky1_q40', stem, ans))

                if 21 <= so <= 40:
                    if any(f"{so}." in expl[:50] for so in range(21, 41)):
                        round46_anomalies.append((f'2002_ky1_q{so}_header_leak', expl[:60]))
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round46_anomalies.append((f'2002_ky1_q{so}_missing_underline', stem))

            # Check Round 47: 2001 ky1 Questions (Q1-Q40 calibration & Q12/Q13 deadly errors fixed)
            if yr == 2001 and cat == 'ky1':
                if so == 12:
                    if ans != 'C' or opt_map.get('C') != 'rather than':
                        round47_anomalies.append(('2001_ky1_q12', ans, opt_map.get('C')))
                elif so == 13:
                    if ans != 'B' or opt_map.get('B') != 'makes':
                        round47_anomalies.append(('2001_ky1_q13', ans, opt_map.get('B')))
                elif so == 21:
                    if ans != 'D' or stem != 'The growth of specialisation in the 19th century might be more clearly seen in sciences such as ________.':
                        round47_anomalies.append(('2001_ky1_q21', stem, ans))
                elif so == 27:
                    if ans != 'D' or stem != 'The writer mentioned the case of the United States to justify the policy of ________.':
                        round47_anomalies.append(('2001_ky1_q27', stem, ans))
                elif so == 28:
                    if ans != 'A' or stem != "It seems that now a country's economy depends much on ________.":
                        round47_anomalies.append(('2001_ky1_q28', stem, ans))
                elif so == 39:
                    if ans != 'C' or stem != '"Juggling one\'s life" probably means living a life characterized by ________.':
                        round47_anomalies.append(('2001_ky1_q39', stem, ans))

                if 21 <= so <= 40:
                    if any(f"{so}." in expl[:50] for so in range(21, 41)):
                        round47_anomalies.append((f'2001_ky1_q{so}_header_leak', expl[:60]))
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round47_anomalies.append((f'2001_ky1_q{so}_missing_underline', stem))

            # Check Round 48: 2006 ky1
            if yr == 2006 and cat == 'ky1':
                if so == 14 and opt_map.get('D') != 'whereas':
                    round48_anomalies.append(('2006_ky1_q14_opt_D', opt_map.get('D')))
                elif so == 15 and opt_map.get('C') != 'survival':
                    round48_anomalies.append(('2006_ky1_q15_opt_C', opt_map.get('C')))
                elif so == 16 and opt_map.get('B') not in ['over', '(turn) over']:
                    round48_anomalies.append(('2006_ky1_q16_opt_B', opt_map.get('B')))
                elif so == 30:
                    if opt_map.get('B') != "favors the townsfolk's view" or opt_map.get('C') != "takes a detached attitude":
                        round48_anomalies.append(('2006_ky1_q30_opts', opt_map))
                elif so == 31:
                    if stem != 'The extinction of large prehistoric animals is noted to suggest that ________.' or opt_map.get('A') != 'large animals were vulnerable to the changing environment':
                        round48_anomalies.append(('2006_ky1_q31', stem, opt_map.get('A')))
                elif so == 35:
                    if len(expl) < 600 or '［精准定位］' not in expl:
                        round48_anomalies.append(('2006_ky1_q35_expl_len', len(expl)))
                elif so == 39:
                    if not stem.endswith('________.') or '［精准定位］' not in expl or len(expl) < 700:
                        round48_anomalies.append(('2006_ky1_q39_expl', stem, len(expl)))

                if 21 <= so <= 40:
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round48_anomalies.append((f'2006_ky1_q{so}_missing_underline', stem))
                    if 26 <= so <= 38:
                        if re.search(r'^\s*\d{1,2}\.', expl[:40]):
                            round48_anomalies.append((f'2006_ky1_q{so}_leaked_header', expl[:50]))

            # Check Round 49: 2007 ky1
            if yr == 2007 and cat == 'ky1':
                if so == 1 and opt_map.get('A') != 'natives':
                    round49_anomalies.append(('2007_ky1_q1_opt_A', opt_map.get('A')))
                elif so == 26 and opt_map.get('A') != 'Answering philosophical questions.':
                    round49_anomalies.append(('2007_ky1_q26_opt_A', opt_map.get('A')))
                elif so == 31:
                    if stem != "Today's double-income families are at greater financial risk in that ________." or opt_map.get('B') != 'their chances of being laid off have greatly increased':
                        round49_anomalies.append(('2007_ky1_q31', stem, opt_map.get('B')))
                elif so == 32:
                    if stem != "As a result of President Bush's reform, retired people may have ________." or '［精准定位］' not in expl or len(expl) < 400:
                        round49_anomalies.append(('2007_ky1_q32', stem, len(expl)))
                elif so == 33:
                    if stem != "According to the author, health-savings plans will ________." or opt_map.get('D') != "increase the families' investment risk":
                        round49_anomalies.append(('2007_ky1_q33', stem, opt_map.get('D')))
                elif so == 34 and stem != "It can be inferred from the last paragraph that ________.":
                    round49_anomalies.append(('2007_ky1_q34', stem))
                elif so == 36 and stem != 'The statement "It never rains but it pours" is used to introduce ________.':
                    round49_anomalies.append(('2007_ky1_q36', stem))
                elif so == 37:
                    if stem != "According to Paragraph 2, some organizations check their systems to find out ________." or '［精准定位］' not in expl or len(expl) < 400:
                        round49_anomalies.append(('2007_ky1_q37', stem, len(expl)))
                elif so == 38:
                    if stem != "In bringing up the concept of GASP the author is making the point that ________." or '［精准定位］' not in expl or len(expl) < 400:
                        round49_anomalies.append(('2007_ky1_q38', stem, len(expl)))
                elif so == 39:
                    if stem != "According to Paragraph 4, what puzzles the author is that some bosses fail to ________." or opt_map.get('B') != 'perceive the sensitivity of personal data':
                        round49_anomalies.append(('2007_ky1_q39', stem, opt_map.get('B')))
                elif so == 40 and stem != "It can be inferred from Paragraph 5 that ________.":
                    round49_anomalies.append(('2007_ky1_q40', stem))

                if 21 <= so <= 40:
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round49_anomalies.append((f'2007_ky1_q{so}_missing_underline', stem))
                    if not expl.startswith('［'):
                        round49_anomalies.append((f'2007_ky1_q{so}_non_canonical_start', expl[:40]))
                    if re.search(r'^\s*\d{1,2}\.', expl[:40]):
                        round49_anomalies.append((f'2007_ky1_q{so}_leaked_header', expl[:50]))

                if 41 <= so <= 45:
                    if '［标题匹配］' not in expl or '［干扰项排除］' not in expl:
                        round49_anomalies.append((f'2007_ky1_q{so}_part_b_expl', expl[:50]))

            # Check Round 50: 2008 ky1 Questions (Q1-Q45)
            if yr == 2008 and cat == 'ky1':
                if q.get('question_number') != so:
                    round50_anomalies.append((f'2008_ky1_q{so}_missing_qnum', q.get('question_number')))
                
                # Cloze Q1-Q20
                if 1 <= so <= 20:
                    expected_ans = ['B', 'D', 'A', 'C', 'C', 'A', 'B', 'D', 'B', 'C', 'B', 'D', 'A', 'C', 'D', 'D', 'C', 'A', 'B', 'A'][so - 1]
                    if stem != f"Choose the best option for blank [{so}] in the passage:":
                        round50_anomalies.append((f'2008_ky1_cloze_q{so}_stem', stem))
                    if ans != expected_ans:
                        round50_anomalies.append((f'2008_ky1_cloze_q{so}_ans', ans, expected_ans))
                    if not expl.startswith('［精准定位］'):
                        round50_anomalies.append((f'2008_ky1_cloze_q{so}_expl', expl[:40]))

                # Reading Q21-Q35
                if so == 21 and (ans != 'A' or opt_map.get('A') != 'Women are biologically more vulnerable to stress.'):
                    round50_anomalies.append(('2008_ky1_q21', ans, opt_map.get('A')))
                elif so == 22 and (ans != 'D' or opt_map.get('D') != 'are exposed to more stress'):
                    round50_anomalies.append(('2008_ky1_q22', ans, opt_map.get('D')))
                elif so == 24 and (ans != 'B' or opt_map.get('B') != "Alvarez's salary barely covered her household expenses"):
                    round50_anomalies.append(('2008_ky1_q24', ans, opt_map.get('B')))
                elif so == 25 and (ans != 'D' or opt_map.get('D') != 'Gender Inequality: Women Under Stress'):
                    round50_anomalies.append(('2008_ky1_q25', ans, opt_map.get('D')))
                elif so == 26 and (ans != 'D' or opt_map.get('D') != 'the traditional process of journal publication'):
                    round50_anomalies.append(('2008_ky1_q26', ans, opt_map.get('D')))
                elif so == 27 and (ans != 'C' or opt_map.get('C') != 'It upsets profit-making journal publishers.'):
                    round50_anomalies.append(('2008_ky1_q27', ans, opt_map.get('C')))
                elif so == 28 and (ans != 'A' or opt_map.get('A') != 'it provides an easier access to scientific results'):
                    round50_anomalies.append(('2008_ky1_q28', ans, opt_map.get('A')))
                elif so == 29 and (ans != 'A' or opt_map.get('A') != 'cover the cost of its publication'):
                    round50_anomalies.append(('2008_ky1_q29', ans, opt_map.get('A')))
                elif so == 30 and (ans != 'B' or opt_map.get('B') != 'A new mode of publication is emerging.'):
                    round50_anomalies.append(('2008_ky1_q30', ans, opt_map.get('B')))
                elif so == 31 and (ans != 'A' or opt_map.get('A') != 'illustrate the change of height of NBA players'):
                    round50_anomalies.append(('2008_ky1_q31', ans, opt_map.get('A')))
                elif so == 32 and (ans != 'C' or opt_map.get('C') != 'Living standards.'):
                    round50_anomalies.append(('2008_ky1_q32', ans, opt_map.get('C')))
                elif so == 33 and (ans != 'B' or opt_map.get('B') != 'Human height is conditioned by the upright posture.'):
                    round50_anomalies.append(('2008_ky1_q33', ans, opt_map.get('B')))
                elif so == 34 and (ans != 'D' or opt_map.get('D') != 'the existing data of human height will still be applicable'):
                    round50_anomalies.append(('2008_ky1_q34', ans, opt_map.get('D')))
                elif so == 35 and (ans != 'C' or opt_map.get('C') != 'Americans have reached their genetic growth limit'):
                    round50_anomalies.append(('2008_ky1_q35', ans, opt_map.get('C')))

                # Reading Text 4 (Q36-Q40) - Unknotting misplaced items
                elif so == 36 and (ans != 'D' or 'dental surgery' not in stem or opt_map.get('D') != 'reveal some unknown aspect of his life'):
                    round50_anomalies.append(('2008_ky1_q36', ans, stem, opt_map.get('D')))
                elif so == 37 and (ans != 'B' or opt_map.get('B') != 'in its early days the U.S. was confronted with delicate situations'):
                    round50_anomalies.append(('2008_ky1_q37', ans, opt_map.get('B')))
                elif so == 38 and (ans != 'C' or 'Thomas Jefferson' not in stem or opt_map.get('C') != 'His attitude towards slavery was complex.'):
                    round50_anomalies.append(('2008_ky1_q38', ans, stem, opt_map.get('C')))
                elif so == 39 and (ans != 'A' or opt_map.get('A') != 'Some Founding Fathers benefit politically from slavery.'):
                    round50_anomalies.append(('2008_ky1_q39', ans, opt_map.get('A')))
                elif so == 40 and (ans != 'B' or 'decision to free slaves' not in stem or opt_map.get('B') != 'military experience'):
                    round50_anomalies.append(('2008_ky1_q40', ans, stem, opt_map.get('B')))

                if 21 <= so <= 40:
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round50_anomalies.append((f'2008_ky1_q{so}_missing_underline', stem))
                    if not expl.startswith('［精准定位］'):
                        round50_anomalies.append((f'2008_ky1_q{so}_non_canonical_start', expl[:40]))
                    if re.search(r'^\s*\d{1,2}\.', expl[:40]):
                        round50_anomalies.append((f'2008_ky1_q{so}_leaked_header', expl[:50]))

                # Part B Q41-Q45
                if 41 <= so <= 45:
                    part_b_expected = {41: 'D', 42: 'G', 43: 'A', 44: 'C', 45: 'E'}
                    if ans != part_b_expected[so]:
                        round50_anomalies.append((f'2008_ky1_q{so}_part_b_ans', ans, part_b_expected[so]))
                    if len(q.get('options', [])) != 7:
                        round50_anomalies.append((f'2008_ky1_q{so}_part_b_options_len', len(q.get('options', []))))
                    if not expl.startswith('［精准定位］'):
                        round50_anomalies.append((f'2008_ky1_q{so}_part_b_expl', expl[:40]))

            # Check Round 51: 2009 ky1 Questions (Q1-Q45)
            if yr == 2009 and cat == 'ky1':
                if q.get('question_number') != so:
                    round51_anomalies.append((f'2009_ky1_q{so}_missing_qnum', q.get('question_number')))
                
                # Cloze Q1-Q20
                if 1 <= so <= 20:
                    cloze_answers = ['B', 'A', 'D', 'B', 'C', 'A', 'D', 'C', 'B', 'D', 'D', 'B', 'C', 'D', 'A', 'C', 'B', 'A', 'A', 'C']
                    exp_ans = cloze_answers[so - 1]
                    if stem != f"Choose the best option for blank [{so}] in the passage:":
                        round51_anomalies.append((f'2009_ky1_cloze_q{so}_stem', stem))
                    if ans != exp_ans:
                        round51_anomalies.append((f'2009_ky1_cloze_q{so}_ans', ans, exp_ans))
                    if not expl.startswith('［考点提炼］'):
                        round51_anomalies.append((f'2009_ky1_cloze_q{so}_expl_start', expl[:40]))
                    if so == 2 and 'tended (to do)' not in opt_map.get('A', ''):
                        round51_anomalies.append(('2009_ky1_q2_opt_A', opt_map.get('A')))
                    if so == 14 and opt_map.get('D') != 'for instance':
                        round51_anomalies.append(('2009_ky1_q14_opt_D', opt_map.get('D')))
                    if so == 19 and opt_map.get('B') != 'comprehensive':
                        round51_anomalies.append(('2009_ky1_q19_opt_B', opt_map.get('B')))
                    if so == 20 and opt_map.get('A') != 'By accident':
                        round51_anomalies.append(('2009_ky1_q20_opt_A', opt_map.get('A')))

                # Reading Q21-Q40
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'C', 22: 'D', 23: 'A', 24: 'D', 25: 'A',
                        26: 'A', 27: 'C', 28: 'D', 29: 'A', 30: 'B',
                        31: 'D', 32: 'B', 33: 'B', 34: 'C', 35: 'C',
                        36: 'B', 37: 'B', 38: 'D', 39: 'A', 40: 'C'
                    }
                    if ans != reading_answers[so]:
                        round51_anomalies.append((f'2009_ky1_q{so}_reading_ans', ans, reading_answers[so]))
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round51_anomalies.append((f'2009_ky1_q{so}_reading_stem_end', stem))
                    if not expl.startswith('［精准定位］'):
                        round51_anomalies.append((f'2009_ky1_q{so}_reading_expl_start', expl[:40]))
                    if '［命题解密］' not in expl:
                        round51_anomalies.append((f'2009_ky1_q{so}_reading_expl_decrypt', expl[:40]))
                    if so == 29:
                        if stem != "In the last paragraph, a problem commercial genetic testing faces is ________.":
                            round51_anomalies.append(('2009_ky1_q29_stem', stem))
                        if opt_map.get('A') != 'disorganized data collection':
                            round51_anomalies.append(('2009_ky1_q29_opt_A', opt_map.get('A')))
                    if so == 30:
                        if stem != "An appropriate title for the text is most likely to be ________.":
                            round51_anomalies.append(('2009_ky1_q30_stem', stem))
                        if opt_map.get('B') != 'DNA Testing and Its Problems':
                            round51_anomalies.append(('2009_ky1_q30_opt_B', opt_map.get('B')))

                # Part B Q41-Q45
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'C', 42: 'E', 43: 'A', 44: 'B', 45: 'G'}
                    if stem != f"Choose the best paragraph [A]-[G] that fits into gap ({so}):":
                        round51_anomalies.append((f'2009_ky1_q{so}_part_b_stem', stem))
                    if ans != part_b_answers[so]:
                        round51_anomalies.append((f'2009_ky1_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 7:
                        round51_anomalies.append((f'2009_ky1_q{so}_part_b_opts_len', len(q.get('options', []))))
                    if '民主与教育' in expl or '广义的教育' in expl:
                        round51_anomalies.append((f'2009_ky1_q{so}_part_b_leak', expl[-50:]))

            # Check Round 52: 2010 ky1 Questions (Q1-Q45)
            if yr == 2010 and cat == 'ky1':
                if q.get('question_number') != so:
                    round52_anomalies.append((f'2010_ky1_q{so}_missing_qnum', q.get('question_number')))
                
                # Cloze Q1-Q20
                if 1 <= so <= 20:
                    cloze_answers = ['A', 'B', 'C', 'B', 'C', 'B', 'D', 'A', 'C', 'D', 'C', 'A', 'A', 'D', 'B', 'A', 'D', 'C', 'B', 'D']
                    exp_ans = cloze_answers[so - 1]
                    if stem != f"Choose the best option for blank [{so}] in the passage:":
                        round52_anomalies.append((f'2010_ky1_cloze_q{so}_stem', stem))
                    if ans != exp_ans:
                        round52_anomalies.append((f'2010_ky1_cloze_q{so}_ans', ans, exp_ans))
                    if not expl.startswith('［考点提炼］'):
                        round52_anomalies.append((f'2010_ky1_cloze_q{so}_expl_start', expl[:40]))
                    if '［解题思路］' not in expl or '［错项排除］' not in expl:
                        round52_anomalies.append((f'2010_ky1_cloze_q{so}_expl_structure', expl[:40]))

                # Reading Q21-Q40
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'B', 22: 'A', 23: 'D', 24: 'A', 25: 'B',
                        26: 'C', 27: 'D', 28: 'C', 29: 'B', 30: 'A',
                        31: 'B', 32: 'D', 33: 'A', 34: 'C', 35: 'C',
                        36: 'A', 37: 'D', 38: 'C', 39: 'B', 40: 'D'
                    }
                    if ans != reading_answers[so]:
                        round52_anomalies.append((f'2010_ky1_q{so}_reading_ans', ans, reading_answers[so]))
                    if not (stem.endswith('________.') or stem.endswith('?')):
                        round52_anomalies.append((f'2010_ky1_q{so}_reading_stem_end', stem))
                    if not expl.startswith('［精准定位］'):
                        round52_anomalies.append((f'2010_ky1_q{so}_reading_expl_start', expl[:40]))
                    if '［命题解密］' not in expl:
                        round52_anomalies.append((f'2010_ky1_q{so}_reading_expl_decrypt', expl[:40]))
                    if len(expl) > 1500:
                        round52_anomalies.append((f'2010_ky1_q{so}_reading_expl_len', len(expl)))

                # Part B Q41-Q45
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'B', 42: 'F', 43: 'D', 44: 'G', 45: 'A'}
                    if stem != f"Choose the correct paragraph [A]-[G] for position ({so}):":
                        round52_anomalies.append((f'2010_ky1_q{so}_part_b_stem', stem))
                    if ans != part_b_answers[so]:
                        round52_anomalies.append((f'2010_ky1_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 7:
                        round52_anomalies.append((f'2010_ky1_q{so}_part_b_opts_len', len(q.get('options', []))))

            # Check Round 53: 2010 ky2 Questions (Q1-Q45)
            if yr == 2010 and cat == 'ky2':
                if q.get('question_number') != so:
                    round53_anomalies.append((f'2010_ky2_q{so}_missing_qnum', q.get('question_number')))
                
                # Cloze Q1-Q20
                if 1 <= so <= 20:
                    cloze_answers = ['D', 'C', 'B', 'A', 'A', 'B', 'D', 'C', 'B', 'A', 'C', 'D', 'D', 'A', 'C', 'B', 'D', 'C', 'A', 'B']
                    exp_ans = cloze_answers[so - 1]
                    if ans != exp_ans:
                        round53_anomalies.append((f'2010_ky2_cloze_q{so}_ans', ans, exp_ans))
                    if not expl.startswith('［考点提炼］'):
                        round53_anomalies.append((f'2010_ky2_cloze_q{so}_expl_start', expl[:40]))
                    if '［解题思路］' not in expl or '［错项排除］' not in expl:
                        round53_anomalies.append((f'2010_ky2_cloze_q{so}_expl_structure', expl[:40]))

                # Reading Q21-Q40
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'D', 22: 'A', 23: 'B', 24: 'C', 25: 'C',
                        26: 'A', 27: 'C', 28: 'B', 29: 'D', 30: 'C',
                        31: 'A', 32: 'A', 33: 'D', 34: 'C', 35: 'B',
                        36: 'D', 37: 'A', 38: 'C', 39: 'B', 40: 'D'
                    }
                    if ans != reading_answers[so]:
                        round53_anomalies.append((f'2010_ky2_q{so}_reading_ans', ans, reading_answers[so]))
                    if not expl.startswith('［精准定位］'):
                        round53_anomalies.append((f'2010_ky2_q{so}_reading_expl_start', expl[:40]))
                    if '［命题解密］' not in expl or '［技巧总结］' not in expl:
                        round53_anomalies.append((f'2010_ky2_q{so}_reading_expl_decrypt', expl[:40]))

                # Part B Q41-Q45
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'F', 42: 'T', 43: 'F', 44: 'T', 45: 'F'}
                    if ans != part_b_answers[so]:
                        round53_anomalies.append((f'2010_ky2_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 2:
                        round53_anomalies.append((f'2010_ky2_q{so}_part_b_opts_len', len(q.get('options', []))))
                    if not expl.startswith('［精准定位］') or '［命题解密］' not in expl:
                        round53_anomalies.append((f'2010_ky2_q{so}_part_b_expl', expl[:40]))

            if yr == 2011 and cat == 'ky1':
                if 1 <= so <= 20:
                    cloze_answers = ['C', 'D', 'B', 'B', 'A', 'B', 'A', 'D', 'C', 'A', 'B', 'C', 'D', 'C', 'B', 'D', 'A', 'D', 'A', 'C']
                    exp_ans = cloze_answers[so - 1]
                    if ans != exp_ans:
                        round54_anomalies.append((f'2011_ky1_cloze_q{so}_ans', ans, exp_ans))
                    if '考点提炼' not in expl:
                        round54_anomalies.append((f'2011_ky1_cloze_q{so}_expl_kd', expl[:40]))
                    if '解题思路' not in expl:
                        round54_anomalies.append((f'2011_ky1_cloze_q{so}_expl_sl', expl[:40]))
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'C', 22: 'B', 23: 'D', 24: 'B', 25: 'A',
                        26: 'B', 27: 'D', 28: 'C', 29: 'A', 30: 'C',
                        31: 'D', 32: 'C', 33: 'B', 34: 'A', 35: 'A',
                        36: 'C', 37: 'D', 38: 'A', 39: 'D', 40: 'B'
                    }
                    if ans != reading_answers[so]:
                        round54_anomalies.append((f'2011_ky1_q{so}_reading_ans', ans, reading_answers[so]))
                    if not expl.startswith('［精准定位］'):
                        round54_anomalies.append((f'2011_ky1_q{so}_reading_expl_start', expl[:40]))
                    if '［命题解密］' not in expl:
                        round54_anomalies.append((f'2011_ky1_q{so}_reading_expl_decrypt', expl[:40]))
                    if so == 25:
                        if 'feels' not in q.get('stem', '') or q.get('options', [])[0].get('text') != 'doubtful':
                            round54_anomalies.append(('2011_ky1_q25_stem_opts', q.get('stem')))
                    if so == 40 and ans != 'B':
                        round54_anomalies.append(('2011_ky1_q40_ans_not_b', ans))
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'B', 42: 'D', 43: 'A', 44: 'C', 45: 'F'}
                    if ans != part_b_answers[so]:
                        round54_anomalies.append((f'2011_ky1_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 7:
                        round54_anomalies.append((f'2011_ky1_q{so}_part_b_opts_len', len(q.get('options', []))))

            if yr == 2011 and cat == 'ky2':
                if 1 <= so <= 20:
                    cloze_answers = ['A', 'C', 'B', 'D', 'D', 'B', 'A', 'C', 'C', 'B', 'D', 'B', 'A', 'C', 'A', 'A', 'D', 'A', 'C', 'D']
                    exp_ans = cloze_answers[so - 1]
                    if ans != exp_ans:
                        round55_anomalies.append((f'2011_ky2_cloze_q{so}_ans', ans, exp_ans))
                elif 21 <= so <= 40:
                    reading_answers = {
                        21: 'B', 22: 'D', 23: 'C', 24: 'A', 25: 'B',
                        26: 'D', 27: 'B', 28: 'C', 29: 'A', 30: 'A',
                        31: 'B', 32: 'D', 33: 'C', 34: 'D', 35: 'B',
                        36: 'B', 37: 'C', 38: 'B', 39: 'A', 40: 'D'
                    }
                    if ans != reading_answers[so]:
                        round55_anomalies.append((f'2011_ky2_q{so}_reading_ans', ans, reading_answers[so]))
                elif 41 <= so <= 45:
                    part_b_answers = {41: 'E', 42: 'D', 43: 'C', 44: 'B', 45: 'G'}
                    if ans != part_b_answers[so]:
                        round55_anomalies.append((f'2011_ky2_q{so}_part_b_ans', ans, part_b_answers[so]))
                    if len(q.get('options', [])) != 7:
                        round55_anomalies.append((f'2011_ky2_q{so}_part_b_opts_len', len(q.get('options', []))))

            # Check Round 56: 2012 ky1 Questions & Passages
            if yr == 2012 and cat == 'ky1':
                if so is None or so < 1 or so > 45:
                    round56_anomalies.append(('2012_ky1_invalid_so', so))
                
                exp_pts = 0.5 if so <= 20 else 2.0
                q_pts = q.get('points')
                if q_pts is not None and abs(float(q_pts) - exp_pts) > 1e-4:
                    round56_anomalies.append((f'2012_ky1_q{so}_points', pts, exp_pts))
                
                if so <= 20:
                    cloze_ans_map = {
                        1: 'B', 2: 'A', 3: 'B', 4: 'D', 5: 'C',
                        6: 'B', 7: 'D', 8: 'B', 9: 'A', 10: 'B',
                        11: 'A', 12: 'C', 13: 'C', 14: 'D', 15: 'A',
                        16: 'C', 17: 'A', 18: 'C', 19: 'D', 20: 'D'
                    }
                    if ans != cloze_ans_map.get(so):
                        round56_anomalies.append((f'2012_ky1_q{so}_cloze_ans', ans, cloze_ans_map.get(so)))
                    if len(opts) != 4:
                        round56_anomalies.append((f'2012_ky1_q{so}_cloze_opts_len', len(opts)))
                elif 21 <= so <= 40:
                    reading_ans_map = {
                        21: 'D', 22: 'B', 23: 'A', 24: 'C', 25: 'D',
                        26: 'C', 27: 'D', 28: 'A', 29: 'D', 30: 'A',
                        31: 'A', 32: 'B', 33: 'B', 34: 'D', 35: 'C',
                        36: 'C', 37: 'D', 38: 'B', 39: 'C', 40: 'A'
                    }
                    if ans != reading_ans_map.get(so):
                        round56_anomalies.append((f'2012_ky1_q{so}_reading_ans', ans, reading_ans_map.get(so)))
                    if len(opts) != 4:
                        round56_anomalies.append((f'2012_ky1_q{so}_reading_opts_len', len(opts)))
                    if so == 26:
                        if opt_map.get('C') != 'dishonoring':
                            round56_anomalies.append(('2012_ky1_q26_opt_c', opt_map.get('C')))
                    elif so == 27:
                        if opt_map.get('D') != 'get permission to purchase a power plant':
                            round56_anomalies.append(('2012_ky1_q27_opt_d', opt_map.get('D')))
                    elif so == 28:
                        if opt_map.get('A') != 'managerial practices':
                            round56_anomalies.append(('2012_ky1_q28_opt_a', opt_map.get('A')))
                    elif so == 29:
                        if opt_map.get('D') != "the limits of states' power over nuclear issues":
                            round56_anomalies.append(('2012_ky1_q29_opt_d', opt_map.get('D')))
                    elif so == 30:
                        if opt_map.get('A') != "Entergy's business elsewhere might be affected":
                            round56_anomalies.append(('2012_ky1_q30_opt_a', opt_map.get('A')))
                    elif so == 36:
                        if opt_map.get('B') != 'Jimmy Hoffa used to work as a civil servant':
                            round56_anomalies.append(('2012_ky1_q36_opt_b', opt_map.get('B')))
                elif 41 <= so <= 45:
                    pb_ans_map = {41: 'C', 42: 'D', 43: 'A', 44: 'F', 45: 'G'}
                    if ans != pb_ans_map.get(so):
                        round56_anomalies.append((f'2012_ky1_q{so}_part_b_ans', ans, pb_ans_map.get(so)))
                    if len(opts) != 7:
                        round56_anomalies.append((f'2012_ky1_q{so}_part_b_opts_len', len(opts)))

            if yr == 2012 and cat == 'ky2':
                if so not in range(1, 46):
                    round57_anomalies.append(('2012_ky2_invalid_so', so))
                
                exp_pts = 0.5 if so <= 20 else 2.0
                q_pts = q.get('points')
                if q_pts is not None and abs(float(q_pts) - exp_pts) > 1e-4:
                    round57_anomalies.append((f'2012_ky2_q{so}_points', q_pts, exp_pts))
                
                exp_qtype = 'cloze_item' if so <= 20 else 'reading_item'
                if q.get('q_type') != exp_qtype:
                    round57_anomalies.append((f'2012_ky2_q{so}_qtype', q.get('q_type'), exp_qtype))
                
                if len(expl) < 60:
                    round57_anomalies.append((f'2012_ky2_q{so}_expl_len', len(expl)))
                
                if 1 <= so <= 20:
                    cloze_ans_map_2012 = {
                        1: 'A', 2: 'B', 3: 'D', 4: 'A', 5: 'C',
                        6: 'D', 7: 'B', 8: 'A', 9: 'C', 10: 'B',
                        11: 'D', 12: 'C', 13: 'C', 14: 'A', 15: 'D',
                        16: 'A', 17: 'B', 18: 'C', 19: 'B', 20: 'D'
                    }
                    if ans != cloze_ans_map_2012.get(so):
                        round57_anomalies.append((f'2012_ky2_q{so}_cloze_ans', ans, cloze_ans_map_2012.get(so)))
                    if len(opts) != 4:
                        round57_anomalies.append((f'2012_ky2_q{so}_cloze_opts_len', len(opts)))
                elif 21 <= so <= 40:
                    reading_ans_map_2012 = {
                        21: 'A', 22: 'C', 23: 'D', 24: 'B', 25: 'A',
                        26: 'C', 27: 'B', 28: 'B', 29: 'A', 30: 'C',
                        31: 'A', 32: 'B', 33: 'A', 34: 'C', 35: 'D',
                        36: 'D', 37: 'D', 38: 'B', 39: 'D', 40: 'A'
                    }
                    if ans != reading_ans_map_2012.get(so):
                        round57_anomalies.append((f'2012_ky2_q{so}_reading_ans', ans, reading_ans_map_2012.get(so)))
                    if len(opts) != 4:
                        round57_anomalies.append((f'2012_ky2_q{so}_reading_opts_len', len(opts)))
                elif 41 <= so <= 45:
                    pb_ans_map_2012 = {41: 'A', 42: 'F', 43: 'G', 44: 'C', 45: 'E'}
                    if ans != pb_ans_map_2012.get(so):
                        round57_anomalies.append((f'2012_ky2_q{so}_part_b_ans', ans, pb_ans_map_2012.get(so)))
                    if len(opts) != 7:
                        round57_anomalies.append((f'2012_ky2_q{so}_part_b_opts_len', len(opts)))






        # Passage boundary check
        for p in passages:
            pt = p.get('title', '')
            c = (p.get('content') or '').strip()
            so = p.get('sort_order')

            # Check Round 40: 2021 ky2 Passages (Text 3 & Text 4)
            if yr == 2021 and cat == 'ky2':
                if p.get('id') == 'fbd49496-cbd6-5676-ad1d-29e41cd6aad3':
                    if not c.startswith('When Microsoft bought') or 'Both apps, however, were later' not in c or 'buy and kill' not in c:
                        round40_anomalies.append(('2021_ky2_passage_text3_content', c[:100]))
                elif p.get('id') == 'c45660d2-1cee-5a4f-8852-8203bf51b493':
                    if not c.startswith("We're fairly good at judging") or 'strawberry jams' not in c or 'Thinking too much can also harm our ability to form preferences.' not in c:
                        round40_anomalies.append(('2021_ky2_passage_text4_content', c[:100]))

            # Check Round 41: 2017 ky1 Passage 2 (Text 1)
            if yr == 2017 and cat == 'ky1' and p.get('id') == 'ec90837a-70ab-52e5-8b01-92083581086b':
                if not c.startswith('First two hours, now three hours') or 'EgyptAir Flight 804' not in c or 'Enroll more people in the PreCheck program' not in c or 'underused PreCheck lanes' not in c:
                    round41_anomalies.append(('2017_ky1_passage_text1_content', c[:100]))

            # Check Round 42: 2009 ky1 Passage 2 (Text 1)
            if yr == 2009 and cat == 'ky1' and p.get('id') == '4558fc29-b3c2-5b42-8fe0-886db1970083':
                if not c.startswith('Habits are a funny thing') or 'setting our brains on auto-pilot' not in c or 'unchangeable creatures of habit' not in c or 'Dawna Markova' not in c or 'This is where developing new habits comes in.' not in c:
                    round42_anomalies.append(('2009_ky1_passage_text1_content', c[:100]))

            # Check Round 43: 2009 ky1 Passage 4 (Text 3) & Passage 5 (Text 4)
            if yr == 2009 and cat == 'ky1':
                if p.get('id') == '009572b7-6be8-54fc-bf41-1b95675cf4ec':
                    if not c.startswith('The relationship between formal education and economic growth in poor countries is widely misunderstood') or 'illiterate, non-English-speaking Mexican workers' not in c or "constraints on improving productivity explain why education isn't developing more quickly there than it is." not in c:
                        round43_anomalies.append(('2009_ky1_passage_text3_content', c[:100]))
                elif p.get('id') == '13ea06a2-2815-5010-a422-61e736731501':
                    if not c.startswith('The most thoroughly studied intellectuals in the history of the New World') or 'carriers of European culture, adjusting to New World circumstances' not in c or 'John Winthrop, an educated gentleman, lawyer, and official of the Crown' not in c or 'Our main end was to catch fish.' not in c:
                        round43_anomalies.append(('2009_ky1_passage_text4_content', c[:100]))

            # Check Round 44: 2010 ky1 Passages 0-5
            if yr == 2010 and cat == 'ky1':
                if p.get('id') == '7202d636-987e-50db-b353-d6a943afd957':
                    if not c.startswith("In 1924 America's National Research Council") or c.startswith("T In 1924") or 'alleged "Hawthorne effect" is hard to pin down.' not in c:
                        round44_anomalies.append(('2010_ky1_passage_use_of_english', c[:60]))
                elif p.get('id') == '617af397-6632-5f9b-82d5-b9388d9bbb12':
                    if not c.startswith('Of all the changes that have taken place in English-language newspapers') or 'Neville Cardus' not in c or 'amateur tradition in music criticism has been in headlong retreat.' not in c or 'What can be learned about Cardus' in c or len(c.split()) < 420:
                        round44_anomalies.append(('2010_ky1_passage_text1_content', len(c.split()), c[:80]))
                elif p.get('id') == '6c969315-eaf7-55c2-867f-73543fe33ff5':
                    if not c.startswith('Over the past decade, thousands of patents have been granted') or 'The Bilski case involves a claimed patent on a method for hedging risk in the energy market.' not in c or 'anti-patent trend at the Supreme Court' not in c or len(c.split()) < 420:
                        round44_anomalies.append(('2010_ky1_passage_text2_content', len(c.split()), c[:80]))
                elif p.get('id') == 'd92f03fb-836e-5e00-b5cf-98625e07171f':
                    if not c.startswith('In his book The Tipping Point, Malcolm Gladwell argues') or 'With the exception of a few celebrities like Oprah Winfrey' not in c or 'critical mass of easily influenced people.' not in c or len(c.split()) < 430:
                        round44_anomalies.append(('2010_ky1_passage_text3_content', len(c.split()), c[:80]))
                elif p.get('id') == '9dc10314-cec1-55df-ab57-10c3a373d2df':
                    if not c.startswith('Bankers have been blaming themselves for their troubles in public.') or "Unfortunately, banks' lobbying now seems to be working." not in c or 'It was banks that were on the wrong planet, with accounts that vastly overvalued assets.' not in c or 'Successful markets require independent and even combative standard-setters.' not in c or len(c.split()) < 420:
                        round44_anomalies.append(('2010_ky1_passage_text4_content', len(c.split()), c[:80]))
                elif p.get('id') == '74816315-11f3-5946-91bf-77d6d41c2323':
                    if '[A]' not in c or '[B]' not in c or '[C]' not in c or '[D]' not in c or '[E]' not in c or '[F]' not in c or '[G]' not in c or len(c.split()) < 580:
                        round44_anomalies.append(('2010_ky1_passage_partb_content', len(c.split())))

            # Check Round 45: 2003 ky1 Passages 0-4
            if yr == 2003 and cat == 'ky1':
                if p.get('id') == 'baf9ac68-c463-5062-81e7-086ea2e053c2':
                    if not c.startswith('Teachers need to be aware of the emotional, intellectual, and physical changes') or 'O [4]' in c or 'practice in successful [11] dynamics.' not in c or 'and knowing that their accomplishments are admired by others.' in c or not c.endswith('having clearly stated rules.') or len(c.split()) < 260:
                        round45_anomalies.append(('2003_ky1_passage_use_of_english', len(c.split()), c[:80]))
                elif p.get('id') == '42614f3c-867d-5b54-a985-106027132f60':
                    if not c.startswith('Wild Bill Donovan would have loved the Internet.') or 'Among the firms making the biggest splash in this new world is Straitford, Inc.' not in c or 'takes pride in its independent voice.' not in c or len(c.split()) < 390 or c.count('\n\n') + 1 != 5:
                        round45_anomalies.append(('2003_ky1_passage_text1_content', len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == 'b0b11306-8638-56f7-b906-ba1282efce2c':
                    if not c.startswith('To paraphrase 18th-century statesman Edmund Burke, "all that is needed for the triumph of a misguided cause is that good people do nothing."') or 'extinguish the precious embers of medical progress.' not in c or len(c.split()) < 400 or c.count('\n\n') + 1 != 4:
                        round45_anomalies.append(('2003_ky1_passage_text2_content', len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '9ba61f50-0a1f-5ccf-8eb0-af5b8c9dd841':
                    if not c.startswith('In recent years, railroads have been combining with each other, merging into supersystems') or 'The vast consolidation within the rail industry means that most shippers are served by only one rail company.' not in c or '"Do we really want railroads to be the arbiters of who wins and who loses in the marketplace?"' not in c or 'Many captive shippers fear that they will, as Norfolk Southern and CSX increase their grip on the market.' not in c or len(c.split()) < 445 or c.count('\n\n') + 1 != 5:
                        round45_anomalies.append(('2003_ky1_passage_text3_content', len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == 'ca2c47ce-e376-58c8-8a48-5dd6d192b3b6':
                    if not c.startswith('It is said that in England death is pressing, in Canada inevitable and in California optional.') or 'The author uses the example of cancer patients to show that' in c or '- IB' in c or 'In 1950, the U.S. spent $12.7 billion on health care.' not in c or 'I would not go that far.' not in c or "underfunding research on humbler therapies that could improve people's lives." not in c or len(c.split()) < 435 or c.count('\n\n') + 1 != 5:
                        round45_anomalies.append(('2003_ky1_passage_text4_content', len(c.split()), c.count('\n\n') + 1))

                # Check Round 46: 2002 ky1 Passages (Passage 0-4 Gold Reconstruction)
                if p.get('id') == '8b7dec36-0057-5b3e-8d45-b736f5b913e2':
                    if c.startswith('I ') or c.count('\n\n') + 1 != 3 or len(c.split()) < 265:
                        round46_anomalies.append(('2002_ky1_passage_use_of_english', len(c.split()), c[:80]))
                elif p.get('id') == 'c82eb2c3-d5f7-58fa-981e-0806ff32c124':
                    if c.startswith('lf ') or '. The joke about doctors implies that' in c or c.count('\n\n') + 1 != 5 or len(c.split()) < 430:
                        round46_anomalies.append(('2002_ky1_passage_text1_content', len(c.split()), c[:80]))
                elif p.get('id') == 'e105b25c-a6ec-502d-b204-11a9c304d4fe':
                    if '. The word " gizmos"' in c or "According to the text, what is beyond man's ability" in c or c.count('\n\n') + 1 != 5 or 'What they found' not in c:
                        round46_anomalies.append(('2002_ky1_passage_text2_content', len(c.split()), c[:80]))
                elif p.get('id') == '53474821-9120-5962-acc2-5c36455d7aeb':
                    if len(c.split()) < 400 or c.count('\n\n') + 1 != 5 or 'One more reason not to lose sleep' not in c or 'Iraq suspended oil exports' not in c:
                        round46_anomalies.append(('2002_ky1_passage_text3_content', len(c.split()), c[:80]))
                elif p.get('id') == 'f0cbd337-0bdf-58e8-8723-cf2c30aa0d62':
                    if len(c.split()) < 420 or c.count('\n\n') + 1 != 9 or 'George Annas, chair of the health law department' not in c or 'Approaching Death: Improving Care' not in c:
                        round46_anomalies.append(('2002_ky1_passage_text4_content', len(c.split()), c[:80]))

                # Check Round 47: 2001 ky1 Passages (Passage 0-5 Gold Reconstruction)
                if p.get('id') == '4f5df10d-1837-59f4-98d4-6588100bcaec':
                    if c.startswith('I ') or 'the trial of Rosemary West' not in c or 'Harold Shipman' in c or c.count('\n\n') + 1 != 7 or len(c.split()) < 240:
                        round47_anomalies.append(('2001_ky1_passage_use_of_english', len(c.split()), c[:80]))
                elif p.get('id') == '4e851c3e-3768-52a5-b959-5e5b308906c9':
                    if len(c.split()) < 410 or c.count('\n\n') + 1 != 4 or 'A comparison of British geological publications' not in c:
                        round47_anomalies.append(('2001_ky1_passage_text1_content', len(c.split()), c[:80]))
                elif p.get('id') == 'dea76b45-8738-5e7c-b1ed-77d39cdd1f55':
                    if len(c.split()) < 370 or c.count('\n\n') + 1 != 4 or "America's Second Wave infrastructure" not in c or 'Today, computers are small and cheap' in c:
                        round47_anomalies.append(('2001_ky1_passage_text2_content', len(c.split()), c[:80]))
                elif p.get('id') == 'e1a90001-2001-4000-8000-000000000006':
                    if len(c.split()) < 400 or c.count('\n\n') + 1 != 6 or 'her much-publicized resignation from the editorship' not in c or '12-hour working days, pressured deadlines' not in c:
                        round47_anomalies.append(('2001_ky1_passage_text5_content', len(c.split()), c[:80]))

                # 2006 ky1 Passages Golden Calibration
                elif p.get('id') == 'fd77d6d0-6ded-51ba-9d44-013d77ee979c':
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or c.count('\n\n') + 1 != 4 or len(c.split()) < 270 or 'Ame ri ca' in c:
                        round48_anomalies.append(('2006_ky1_passage_cloze', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '0bac5a94-e87c-55fb-b24c-8c12f9d18ef6':
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or c.count('\n\n') + 1 != 6 or len(c.split()) < 380 or 'Amen can' in c or 'Peop l e' in c:
                        round48_anomalies.append(('2006_ky1_passage_t1', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '28dfa39a-3497-58ab-b17a-4b2e1849a872':
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or c.count('\n\n') + 1 != 6 or len(c.split()) < 440 or not c.startswith('Stratford-on-Avon'):
                        round48_anomalies.append(('2006_ky1_passage_t2', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == 'fe979c03-674c-5223-9d58-f99599d97e78':
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or c.count('\n\n') + 1 != 4 or len(c.split()) < 420 or 'bad way to do business' not in c:
                        round48_anomalies.append(('2006_ky1_passage_t3', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '9e8e8e4e-9255-5653-ab22-be437e84ce83':
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or c.count('\n\n') + 1 != 7 or len(c.split()) < 410 or 'biomass' in c[:50] or 'pornography' in c[-60:]:
                        round48_anomalies.append(('2006_ky1_passage_t4', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '5f091ca1-0269-547e-b380-e82bc98ba95d':
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5:
                        round48_anomalies.append(('2006_ky1_passage_part_b', p.get('type'), p.get('passage_number')))

                # 2007 ky1 Passages Golden Calibration
                elif p.get('id') == 'a6146626-b40e-5ea0-a148-d77c21f68ca1':
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or c.count('\n\n') + 1 != 4 or len(c.split()) < 260 or 'Spani sh' in c:
                        round49_anomalies.append(('2007_ky1_passage_cloze', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '6347524b-92cc-55f6-9c71-961054eb82d0':
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or c.count('\n\n') + 1 != 5 or len(c.split()) < 390 or 'deliberate practiceo' in c or 'the message the text' in c:
                        round49_anomalies.append(('2007_ky1_passage_t1', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == 'cc38bed7-6339-5a13-8ee9-2f840e1befbe':
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or c.count('\n\n') + 1 != 5 or len(c.split()) < 430 or 'Clearly, intelligence encompasses' not in c or "whether it's knowing when to guess" not in c:
                        round49_anomalies.append(('2007_ky1_passage_t2', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '3a4dede3-a1af-5bd5-9cb6-3ba199fd7119':
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or c.count('\n\n') + 1 != 4 or len(c.split()) < 420 or 'During the past generation, the American middle-class family' not in c or 'From the middle-class family perspective' not in c:
                        round49_anomalies.append(('2007_ky1_passage_t3', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == '6d432ded-32e4-5c0a-8da2-59b623ec3075':
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or c.count('\n\n') + 1 != 5 or len(c.split()) < 380 or 'The scramble to organize security checks' not in c or 'puts corporate America on notice' not in c:
                        round49_anomalies.append(('2007_ky1_passage_t4', p.get('type'), len(c.split()), c.count('\n\n') + 1))
                elif p.get('id') == 'f130a52b-7ad6-53c2-96fe-e909afb03e49':
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or c.count('\n\n') + 1 != 7:
                        round49_anomalies.append(('2007_ky1_passage_part_b', p.get('type'), p.get('passage_number')))

            # Check Round 50: 2008 ky1 Passages (Passages 0-5)
            if yr == 2008 and cat == 'ky1':
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or len(c.split()) < 270 or 'prepared to say it anyway' not in c:
                        round50_anomalies.append(('2008_ky1_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or 'Adeline Alvarez married at 18' not in c:
                        round50_anomalies.append(('2008_ky1_passage_t1', p.get('type'), p.get('passage_number')))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or not c.startswith('It used to be so straightforward.'):
                        round50_anomalies.append(('2008_ky1_passage_t2', p.get('type'), p.get('passage_number')))
                elif so == 4:
                    # Text 3 (untruncated, 5 paras, > 440 words, bipedal posture in para 4)
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 440 or 'bipedal posture' not in c:
                        round50_anomalies.append(('2008_ky1_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or 'George Washington, 52, was nearly toothless.' not in c:
                        round50_anomalies.append(('2008_ky1_passage_t4', p.get('type'), p.get('passage_number')))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or '[41]' not in c:
                        round50_anomalies.append(('2008_ky1_passage_part_b', p.get('type'), p.get('passage_number')))

            # Check Round 51: 2009 ky1 Passages (Passages 0-5)
            if yr == 2009 and cat == 'ky1':
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or c.count('\n\n') + 1 != 4 or len(c.split()) < 270 or 'fruit-fly experiments' not in c or not c.endswith('results are inconclusive.'):
                        round51_anomalies.append(('2009_ky1_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or c.count('\n\n') + 1 != 7 or len(c.split()) < 400 or not c.startswith('Habits are a funny thing.') or not c.endswith('developing new habits comes in.'):
                        round51_anomalies.append(('2009_ky1_passage_t1', p.get('type'), p.get('passage_number')))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or c.count('\n\n') + 1 != 6 or len(c.split()) < 390 or not c.startswith('It is a wise father that knows his own child') or not c.endswith('outside evaluation.'):
                        round51_anomalies.append(('2009_ky1_passage_t2', p.get('type'), p.get('passage_number')))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or c.count('\n\n') + 1 != 5 or len(c.split()) < 430 or not c.startswith('The relationship between formal education and economic growth') or not c.endswith("developing more quickly there than it is."):
                        round51_anomalies.append(('2009_ky1_passage_t3', p.get('type'), p.get('passage_number')))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or c.count('\n\n') + 1 != 5 or len(c.split()) < 400 or not c.startswith('The most thoroughly studied intellectuals in the history of the New World') or not c.endswith('"Our main end was to catch fish."'):
                        round51_anomalies.append(('2009_ky1_passage_t4', p.get('type'), p.get('passage_number')))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or c.count('\n\n') + 1 != 7 or not c.startswith('19th and 20th Century Theories of Cultural Anthropology') or '[41]' not in c or '[45]' not in c:
                        round51_anomalies.append(('2009_ky1_passage_part_b', p.get('type'), p.get('passage_number')))

            if yr == 2010 and cat == 'ky1':
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or len(c.split()) < 250 or 'Hawthorne' not in c:
                        round52_anomalies.append(('2010_ky1_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or len(c.split()) < 400 or 'Cardus' not in c:
                        round52_anomalies.append(('2010_ky1_passage_t1', p.get('type'), p.get('passage_number')))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or len(c.split()) < 400 or 'Bilski' not in c:
                        round52_anomalies.append(('2010_ky1_passage_t2', p.get('type'), p.get('passage_number')))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 400 or 'The Tipping Point' not in c:
                        round52_anomalies.append(('2010_ky1_passage_t3', p.get('type'), p.get('passage_number')))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or len(c.split()) < 400 or 'standard-setters' not in c:
                        round52_anomalies.append(('2010_ky1_passage_t4', p.get('type'), p.get('passage_number')))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or '[A]' not in c or '[G]' not in c:
                        round52_anomalies.append(('2010_ky1_passage_part_b', p.get('type'), p.get('passage_number')))

            if yr == 2010 and cat == 'ky2':
                # Check for concatenated words without spaces in any passage
                bad_concats = [w for w in c.split() if len(w) > 17 and '[' not in w and ']' not in w and '-' not in w and '—' not in w and 'antidiscrimination' not in w.lower()]
                if bad_concats:
                    round53_anomalies.append((f'2010_ky2_p{so}_concats', bad_concats))
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or len(c.split()) < 320 or 'swine flu' not in c:
                        round53_anomalies.append(('2010_ky2_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or len(c.split()) < 360 or 'Damien Hirst' not in c:
                        round53_anomalies.append(('2010_ky2_passage_t1', p.get('type'), p.get('passage_number')))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or len(c.split()) < 320 or 'Virginia' not in c:
                        round53_anomalies.append(('2010_ky2_passage_t2', p.get('type'), p.get('passage_number')))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 380 or 'Curtis' not in c or 'Unilever' not in c:
                        round53_anomalies.append(('2010_ky2_passage_t3', p.get('type'), p.get('passage_number')))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or len(c.split()) < 380 or 'Taylor v. Louisiana' not in c:
                        round53_anomalies.append(('2010_ky2_passage_t4', p.get('type'), p.get('passage_number')))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or 'Directions:' in c or 'Copying Birds' not in c:
                        round53_anomalies.append(('2010_ky2_passage_part_b', p.get('type'), p.get('passage_number')))

            if yr == 2011 and cat == 'ky1':
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or 'Aristotle viewed laughter' not in c or 'flow [15] muscular responses' not in c:
                        round54_anomalies.append(('2011_ky1_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or len(c.split()) < 400 or 'Alan Gilbert' not in c or "change the relationship between America's oldest orchestra and the new audience" not in c:
                        round54_anomalies.append(('2011_ky1_passage_t1', p.get('type'), len(c.split())))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or len(c.split()) < 400 or 'Liam McGee' not in c or "The people who've been hurt the worst are those who've stayed too long" not in c:
                        round54_anomalies.append(('2011_ky1_passage_t2', p.get('type'), len(c.split())))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 420 or 'The rough guide to marketing success used to be that you got what you paid for.' not in c or 'Toyota Motor, for example, alleviated some of the damage' not in c:
                        round54_anomalies.append(('2011_ky1_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or len(c.split()) < 430 or 'single mothers like Bullock' not in c or 'delight.99' in c or 'persistentlyd' in c:
                        round54_anomalies.append(('2011_ky1_passage_t4', p.get('type'), len(c.split())))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or '[A] No disciplines have seized' not in c or '[G] The subtle and intelligent' not in c:
                        round54_anomalies.append(('2011_ky1_passage_part_b', p.get('type'), len(c.split())))

            if yr == 2011 and cat == 'ky2':
                # Check for concatenated words without spaces in any passage
                bad_concats = [w for w in c.split() if len(w) > 17 and '[' not in w and ']' not in w and '-' not in w and '—' not in w and 'competitiveness' not in w.lower() and 'antidiscrimination' not in w.lower()]
                if bad_concats:
                    round55_anomalies.append((f'2011_ky2_p{so}_concats', bad_concats))
                if so == 1:
                    # Cloze
                    if p.get('type') != 'cloze' or p.get('passage_number') != 1 or 'The Internet affords anonymity to its users' not in c or 'license [10] by the government' not in c:
                        round55_anomalies.append(('2011_ky2_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    # Text 1
                    if p.get('type') != 'reading' or p.get('passage_number') != 1 or len(c.split()) < 400 or 'Ruth Simmons' not in c or 'outside directors will follow the example of Ms. Simmons' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t1', p.get('type'), len(c.split())))
                elif so == 3:
                    # Text 2
                    if p.get('type') != 'reading' or p.get('passage_number') != 2 or not c.startswith('A year ago the end seemed near.') or 'Trade Commission launched' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t2', p.get('type'), c[:40]))
                elif so == 4:
                    # Text 3
                    if p.get('type') != 'reading' or p.get('passage_number') != 3 or len(c.split()) < 400 or 'immediately following World War II' not in c or 'both desirable and inevitable was widely shared' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    # Text 4
                    if p.get('type') != 'reading' or p.get('passage_number') != 4 or len(c.split()) < 450 or 'Will the European Union make it?' not in c or 'economic co-ordination should involve all 27 members' not in c:
                        round55_anomalies.append(('2011_ky2_passage_t4', p.get('type'), len(c.split())))
                elif so == 6:
                    # Part B
                    if p.get('type') != 'reading_part_b' or p.get('passage_number') != 5 or 'Leading doctors today weigh in on the debate' not in c or c.strip().endswith("producers such as McDonald's."):
                        round55_anomalies.append(('2011_ky2_passage_part_b', p.get('type'), len(c.split())))

            if yr == 2012 and cat == 'ky2':
                bad_concats_2012 = [w for w in ['Thehomeworkrulesshould', 'across-the-boardrule', 'shouldbe', 'e of the or invent them', 'G. [1]. Joe'] if w in c]
                if bad_concats_2012:
                    round57_anomalies.append((f'2012_ky2_p{so}_concats', bad_concats_2012))
                if so == 1:
                    if p.get('type') != 'cloze' or len(c.split()) < 300 or 'G.I. Joe as a mindless war toy' not in c:
                        round57_anomalies.append(('2012_ky2_passage_cloze', p.get('type'), len(c.split())))
                elif so == 2:
                    if p.get('type') != 'reading' or len(c.split()) < 350 or 'District administrators say that homework will still be a part of schooling' not in c or 'assigning more than they are willing to review and correct' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t1', p.get('type'), len(c.split())))
                elif so == 3:
                    if p.get('type') != 'reading' or len(c.split()) < 350 or "and firmly fuses girls' identity to appearance" not in c or 'or invent them where they did not previously exist' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t2', p.get('type'), len(c.split())))
                elif so == 4:
                    if p.get('type') != 'reading' or len(c.split()) < 350 or 'Each meeting was packed' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t3', p.get('type'), len(c.split())))
                elif so == 5:
                    if p.get('type') != 'reading' or len(c.split()) < 250 or 'find silver linings' not in c:
                        round57_anomalies.append(('2012_ky2_passage_t4', p.get('type'), len(c.split())))
                elif so == 6:
                    if p.get('type') != 'reading_part_b' or len(c.split()) < 250 or 'Downstairs became just as fascinating as upstairs' not in c:
                        round57_anomalies.append(('2012_ky2_passage_part_b', p.get('type'), len(c.split())))




            # Check Round 14: 2004 Reading Passages 2-5
            if yr == 2004 and cat == 'ky1':
                if so == 2 and ('Gant Redmon' not in c or 'CareerBuilder' not in c):
                    round14_2004_reading_anomalies.append(('2004_p2', 'missing_gant_redmon'))
                if so == 3 and ('alphabetism' not in c or 'AAAA cars' not in c):
                    round14_2004_reading_anomalies.append(('2004_p3', 'missing_alphabetism'))
                if so == 4 and ('Ellen Spero' not in c or 'Alan Greenspan' not in c):
                    round14_2004_reading_anomalies.append(('2004_p4', 'missing_ellen_spero'))
                if so == 5 and ('Richard Hofstadter' not in c or 'Ralph Waldo Emerson' not in c):
                    round14_2004_reading_anomalies.append(('2004_p5', 'missing_hofstadter'))

            # Check Round 19: Passage integrity
            if yr == 2014 and cat == 'ky1' and so == 4:
                if '[432 words]' in c or not c.endswith('with gratitude and grace.'):
                    round19_anomalies.append(('2014_ky1_text3_end', c[-40:]))
            if yr == 2021 and cat == 'ky2' and so == 1:
                if not c.endswith('better [20] the objective.'):
                    round19_anomalies.append(('2021_ky2_cloze_end', c[-40:]))
            if yr == 2019 and cat == 'ky1':
                if so == 2 and ('Grade inflation' in c or not c.endswith('for the long term.')):
                    round19_anomalies.append(('2019_ky1_text1_end', c[-40:]))
                if so == 3 and not c.startswith('Grade inflation—the gradual increase in average GPAs'):
                    round19_anomalies.append(('2019_ky1_text2_start', c[:50]))
                if so == 5 and ('f,' in c or 'complying with various state sales tax laws' not in c):
                    round19_anomalies.append(('2019_ky1_text4_end', c[-50:]))
            if yr == 2022 and cat == 'ky2' and so == 4:
                if 'According to the last paragraph' in c or not c.endswith('best practices and standards.'):
                    round19_anomalies.append(('2022_ky2_text3_end', c[-50:]))
            if yr == 2008 and cat == 'ky1' and so == 4:
                if 'ba 1;ketball' in c or ' [,' in c or not c.endswith('feel fairly confident."'):
                    round19_anomalies.append(('2008_ky1_text3_end', c[-50:]))
            if yr == 2010 and cat == 'ky2' and so == 6:
                if ',"’' in c:
                    round19_anomalies.append(('2010_ky2_partb_quote', 'contains stray quote'))

            if 'shop249445206' in c or 'taobao.com' in c or '新一文化' in c:
                watermark_hits.append((title, pt, 'watermark_in_passage'))
            if re.search(r'\b(?:[2-4]\d|Q[2-4]\d)\s*[\.・\、\:]\s*[A-Z]', c[-150:]):
                passage_boundary_anomalies.append((title, pt, 'stem_at_end', c[-80:]))
            if re.search(r'\[[A-G]\]\s*[a-zA-Z]{3,}', c[-80:]):
                passage_boundary_anomalies.append((title, pt, 'option_at_end', c[-80:]))
            if c.endswith('boardso') or c.endswith('building block;') or c.endswith('C A B D') or c.endswith('C  A  B  D'):
                passage_boundary_anomalies.append((title, pt, 'garbage_at_end', c[-40:]))

    results["2. 篇章总量 243 篇"] = (total_passages == 243)
    results["3. 试题总量 1,825 题"] = (total_questions == 1825)
    results["4. 试题答案 100% 对齐 (correct_answer == answer)"] = (len(mismatched_answers) == 0)
    results["5. 试题题干 0 处序号冗余前缀"] = (len(stems_with_prefix) == 0)
    results["6. 完型小题 820 题题干 100% 格式统一"] = (len(non_standard_cloze_stems) == 0)
    results["7. Part A 篇章 0 处残存选项代号"] = (len(part_a_leaked_options) == 0)
    results["8. 篇章 0 处生词音标侧栏注解残留"] = (len(gloss_phonetics_found) == 0)
    results["18. 选项字典键顺序 100% 符合 A-B-C-D 规范"] = (len(non_canonical_option_orders) == 0)
    results["21. 篇章与试题拓扑关联 100% 紧密绑定"] = (len(orphan_questions) == 0)
    results["22. 篇章篇首篇尾 0 处伪题干、截断与跨篇串文污染"] = (len(passage_boundary_anomalies) == 0)
    results["23. 试题题干 0 处断裂、截断与多行丢失"] = (len(truncated_stems_found) == 0)
    results["24. 全库试题与选项 0 处解析语义冲突、重复选项与空选项"] = (len(semantic_conflicts) == 0)
    results["25. 全库完型与阅读 0 处选项跨题覆盖与重复"] = (len(duplicate_cloze_reading_options) == 0)
    results["26. 全库试题与篇章 0 处 o£、th&r 异形字符与 44 伪双引号残留"] = (len(ocr_corruptions_found) == 0)
    results["27. 全库新题型 Part B 41-45 题答案与题干 100% 官方黄金吻合"] = (len(part_b_anomalies) == 0)
    results["28. 全库试题与篇章 0 处商业广告与淘宝水印残留"] = (len(watermark_hits) == 0)
    results["29. 选项文本 0 处日文中黑点 (・) 伪符号残留"] = (len(trailing_dot_opts) == 0)
    results["30. 2004 年完型填空 20 题 100% 具备黄皮书真题精解"] = (len(cloze_2004_placeholders) == 0)
    results["31. 2014 年完型第 8 题选项与答案 100% 为 functions (D)"] = (len(cloze_2014_q8_anomalies) == 0)
    results["32. 2010 Q26 / 2012 Q40 / 2016 Q1 / 2017 Q14 / 2013 Q2 官方答案 100% 黄金校准"] = (len(round12_core_anomalies) == 0)
    results["33. 2011 完型第 7/8 题及阅读 40 题选项与答案 100% 官方黄金校准"] = (len([x for x in round12_core_anomalies if '2011' in str(x)]) == 0)
    results["34. 2004 完型篇章正文与 20 题选项 100% 官方黄金还原"] = (len([x for x in round12_core_anomalies if '2004' in str(x)]) == 0)
    results["35. 2002/2009/2010/2016/2017/2020/2021/2022 等25题官方精解与完整选项 100% 黄金还原"] = (len(round13_anomalies) == 0)
    results["36. 2004 年阅读理解 4 篇官方黄金篇章与 20 道试题及黄皮书精解 100% 黄金还原"] = (len(round14_2004_reading_anomalies) == 0)
    results["37. 全库 0 处章节末题译文倒灌、0 处掌柜水印、2005 Q25 题干选项答案 100% 黄金校准"] = (len(round15_anomalies) == 0)
    results["38. 全库 0 处占位符选项，2002/2003/2006/2008/2010/2012/2017/2018/2020/2021/2022 核心题项 100% 黄金校准"] = (len(round16_anomalies) == 0)
    results["39. 2005 完型 20 题官方黄金还原、4 处截断题干与残损选项 100% 官方黄金校准"] = (len(round17_anomalies) == 0)
    results["40. 2011/2014/2001 年阅读理解 13 道被篡改试题官方真实选项、答案与题解 100% 黄金纠偏"] = (len(round18_anomalies) == 0)
    results["41. 全库 243 篇篇章末尾 0 处字数泄露、0 处跨篇截断与倒灌，2019/2021/2022/2014/2008/2010 篇章 100% 黄金校准"] = (len(round19_anomalies) == 0)
    results["42. 2006/2007/2008/2009/2014/2021 年完型与阅读 61 道题选项截断、碎词与题干 100% 官方黄金校准"] = (len(round20_anomalies) == 0)
    results["43. 2001 Q7 / 2015 Q36 官方答案与 2015/2018 跨题解析倒灌 100% 官方黄金纠偏"] = (len(round21_anomalies) == 0)
    results["44. 2008 Text 4 错位错挂、2009 Q29 截断题干与 2010 Q45 倒灌 100% 官方黄金纠偏"] = (len(round22_anomalies) == 0)
    results["45. 2008 Q35 / 2006 Q22,25,31,32,36,38,39 / 2005 阅读16处截断与纠偏 / 2001 Q28 / 完型OCR碎词 100% 官方黄金校准"] = (len(round23_anomalies) == 0)
    results["46. 2021 ky1/2020 ky1/2022 ky2 Text 4 题干选项截断与倒灌、2007 ky1 Q34-35 真实选项与精解 100% 官方黄金校准"] = (len(round24_anomalies) == 0)
    results["47. 2016 Q35 / 2017 Text 2 / 2019 Text 4 / 2001 Q22 / 2002 Q34 / 2010 Q24 Q31 / 2009 Q38 / 2012 Q22 Q39 等 25 题官方黄金校准"] = (len(round25_anomalies) == 0)
    results["48. 2019 Q34 真实题干选项答案、2019 Q35、2016 Text 2 题干与精解纠偏、2018 Q33 选项与 2018/2020 开头回声 100% 官方黄金校准"] = (len(round26_anomalies) == 0)
    results["49. 2019 T2 / 2016 T3 / 2013 T2-T3 / 2020 T4 题干截断补全与超长篇章/跨篇倒灌彻底提纯 100% 官方黄金校准"] = (len(round27_anomalies) == 0)
    results["50. 2016 Cloze Q20 / 2017 Text 4 Q36-40 / 2011 Q20 / 2013 Q20 / 2015 Q31 跨篇倒灌彻底切除与精准精解还原 100% 官方黄金校准"] = (len(round28_anomalies) == 0)
    results["51. 2004 完型 Q5,8,12 语篇倒灌 / 2005 Q35 / 2009 Q35 / 2008 Q42 / 2006 Q45 跨篇倒灌彻底提纯 100% 官方黄金校准"] = (len(round29_anomalies) == 0)
    results["52. 2021 ky2 完型 Q2,11 与 T4 Q36 / 2022 ky1 T4 Q36,39 / 2003 ky1 T2 Q30 / 2007 ky1 Part B Q41 题干截断补全与语篇倒灌彻底提纯 100% 官方黄金校准"] = (len(round30_anomalies) == 0)
    results["53. 2021 ky2 完型 Q14 / 2007 ky1 完型 Q15 / 2004 ky1 阅读 Q25,30 / 2022 ky1 阅读 Q27,32,37,38 / 2022 ky2 阅读 Q27 题干截断补全与语篇倒灌彻底提纯 100% 官方黄金校准"] = (len(round31_anomalies) == 0)
    results["54. 2006 ky1 T4 Q40 二维码乱码切除 / 2017 & 2019 ky1 完型 Q20 章节标题与词汇切除 / 2022 ky2 完型 Q2 语篇切除 / 2021 ky2 完型 Q20 选项错挂修复与杂质切除 / 2002 ky1 完型 Q8 段落倒灌切除 100% 官方黄金校准"] = (len(round32_anomalies) == 0)
    results["55. 2008 ky1 完型 Q4,11 错挂纠偏 / 2007 ky1 完型 Q7 词汇与正文切除 / 2021 ky1 T3 Q32,34 双语重复切除与题干补全 / 2021 ky2 T1 Q22 与 2022 ky2 T1 Q24 双语重复切除 100% 官方黄金校准"] = (len(round33_anomalies) == 0)
    results["56. 2021 ky1 T3 Q33,35 / 2022 ky2 T1 Q21-23,25 / 2022 ky2 T2 Q26,28-30 / 2006 ky1 T2 Q21,23-25 题干截断补全与双语重复/概览错挂切除 100% 官方黄金校准"] = (len(round34_anomalies) == 0)
    results["57. 2004 ky1 T3 模拟题乱码切除与参考答案清零 / 2021 ky2 T1 双语堆叠与倒灌切除 / 9处正文段落残片彻底提纯 100% 官方黄金校准"] = (len(round35_anomalies) == 0)
    results["58. 完型填空6题段落正文及句式倒灌彻底切除 / 2021 ky2 T2 Q26-30 题干下划线补全、双语堆叠切除与技巧总结补齐 100% 官方黄金校准"] = (len(round36_anomalies) == 0)
    results["59. 2013 ky1 T1 严重乱码重构与双语堆叠切除 / 2007 ky1 T1 官方原卷题干选项校准与正文倒灌切除 100% 官方黄金校准"] = (len(round37_anomalies) == 0)
    results["60. 2011 ky1 阅读全篇20题(Q21-40)题干汉译吞噬与恶性OCR修复、双语堆叠切除与精解完整重构 100% 官方黄金校准"] = (len(round38_anomalies) == 0)
    results["61. 2014 ky1 阅读全篇20题(Q21-40)官方答案纠偏(Q30选B/Q35选D)、题干下划线补全、占位符选项彻底填充与双语堆叠倒灌提纯 100% 官方黄金校准"] = (len(round39_anomalies) == 0)
    results["62. 2021 ky2 Text 3-4(Q31-40)官方答案纠偏(Q32选B)、跨篇污染选项修复(Q33)、题干补全、双语堆叠与截断彻底提纯、篇章段落黄金还原 100% 官方黄金校准"] = (len(round40_anomalies) == 0)
    results["63. 2017 ky1 Text 1(Q21-25)跨篇污染选项修复(Q22/24)、题干补全、双语堆叠与截断彻底提纯、篇章段落黄金还原 100% 官方黄金校准"] = (len(round41_anomalies) == 0)
    results["64. 2009 ky1 Text 1(Q21-25)与Text 2(Q26-28)截断题干补全、双语堆叠与截断彻底提纯、篇章7段417词黄金还原 100% 官方黄金校准"] = (len(round42_anomalies) == 0)
    results["65. 2009 ky1 Text 3-4(Q31-40)题干补全、Q35截断选项修复、Q39污染选项还原、双语堆叠彻底提纯、篇章段落黄金还原 100% 官方黄金校准"] = (len(round43_anomalies) == 0)
    results["66. 2010 ky1 阅读 Text 1-4 与 Part B 全篇黄金重构、Q37 真实选项纠偏、Q39 原卷精解还原与双语堆叠切除 100% 官方黄金校准"] = (len(round44_anomalies) == 0)
    results["67. 2003 ky1 完形与阅读全卷 5 篇篇章黄金重构（Text 3 深度补齐 449 词、Text 4 剔除串文）、Q17/Q20 纠偏、Q27/Q28/Q31/Q37 官方真卷选项还原与解析提纯 100% 官方黄金校准"] = (len(round45_anomalies) == 0)
    results["Assertion 68: 2002 年真题 Use of English + Text 1-4 黄金重构，腰斩截断与倒灌彻底消除，Q5/Q14/Q19/Q22/Q39 五大致命错题纠偏，Q1-Q40 题干下划线规范化与解析提纯 100% 官方黄金校准"] = (len(round46_anomalies) == 0)
    results["Assertion 69: 2001 年开山真题 Use of English + Text 1-5 全卷黄金重构，假文本篡改/掉包与严重腰斩彻底消除，Q12/Q13 官方答案致命纠偏，Q1-Q40 题干下划线规范化与解析提纯 100% 官方黄金校准"] = (len(round47_anomalies) == 0)
    results["Assertion 70: 2006 年真题 Use of English + Text 1-4 黄金重构，严重腰斩/碎词/截断/双向跨篇倒灌彻底消除，Q14/15/16 选项提纯，Q21-Q39 题干下划线规范化与解析彻底提纯 100% 官方黄金校准"] = (len(round48_anomalies) == 0)
    results["Assertion 71: 2007 年真题 Use of English + Text 1-4 黄金重构，Text 3 首部截断彻底补齐，碎词倒灌消除，Q31-Q40 题干下划线规范化与解析提纯 100% 官方黄金校准"] = (len(round49_anomalies) == 0)
    results["Assertion 72: 2008 年真题 Use of English + Text 1-4 黄金重构，Text 3 严重腰斩彻底补齐446词，Text 1 补齐遗漏句，Text 4 错位解开与试题选项法医级校准 100% 官方黄金校准"] = (len(round50_anomalies) == 0)
    results["Assertion 73: 2009 年真题 Use of English + Text 1-4 + Part B 全卷黄金重构，Q29 截断题干补全，Q14 真实选项(for instance)纠偏，完型与新题型精解彻底提纯 100% 官方黄金校准"] = (len(round51_anomalies) == 0)
    results["Assertion 74: 2010 年双轨开山 Use of English + Text 1-4 + Part B 全卷黄金重构，Q1-Q45 题号/分值自洽，Q21-Q40 精准定位补全与三段论精解提纯 100% 官方黄金校准"] = (len(round52_anomalies) == 0)
    results["Assertion 75: 2010 年英语二开山第一卷 Use of English + Text 1-4 + Part B 全卷黄金重构，单词黏连彻底消除，指导语切除，Q1-Q45 题号/分值自洽与三段论精解提纯 100% 官方黄金校准"] = (len(round53_anomalies) == 0)
    results["Assertion 76: 2011 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构，Text 3 首部腰斩彻底找回，Text 4 丢失段落补齐与生词残片消除，Q25 官方原版题干选项校准，Q40 官方答案锁定与 Q1-Q45 黄金三段论精解 100% 官方黄金校准"] = (len(round54_anomalies) == 0)
    results["Assertion 77: 2011 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构，Text 2 开头腰斩彻底找回 (A year ago the end seemed near.)，全卷 15 处恶性单词黏连彻底消除，Q1-Q45 题号/分值自洽与官方答案 100% 官方黄金校准"] = (len(round55_anomalies) == 0)
    results["Assertion 78: 2012 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构，Text 4 整篇彻底找回(7段435词)，Text 1 补齐腰斩两段，Text 3 乱码/题干串文切除，Q26-Q30 真实真题选项纠偏与 Q1-Q45 官方答案 100% 官方黄金校准"] = (len(round56_anomalies) == 0)
    results["Assertion 79: 2012 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（Text 1 找回腰斩两句恢复5段、Text 2 补齐截断残损与中句、Q1-Q45 题型/分值/官方标准答案 100% 零差异对齐）"] = (len(round57_anomalies) == 0)
    results["Assertion 80: 2013 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（Text 1 找回丢失段落恢复6段、Text 2 剔除题干倒灌恢复7段、Text 3 补齐VI/VII段、Text 4 切除倒灌残渣恢复7段、Part B 找回缺失选项[A][B]、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round58_anomalies) == 0)
    results["Assertion 81: 2013 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段351词、Text 1 恢复6段366词并补齐G.I. Bill完整句、Text 2 恢复5段402词理顺候鸟脉络、Text 3 恢复6段381词、Text 4 独立设问恢复7段356词、Part B 恢复6段504词含引言及[41]-[45]建议、切除全卷45题假占位符、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round59_anomalies) == 0)
    results["Assertion 82: 2014 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段284词、Text 1 恢复4段341词切除尾部拼接、Text 2 恢复6段415词彻底消除Q26/Q27题干倒灌与腰斩、Text 3 恢复5段380词补齐诺贝尔奖对比、Text 4 恢复6段412词切除Q37题干倒灌、Part B 恢复8段592词完整找回[B][C][D][E]四段、纠偏完型8题与阅读Q27、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round60_anomalies) == 0)
    results["Assertion 83: 2014 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段354词补齐腰斩句、Text 1 恢复4段392词消除黏连、Text 2 恢复5段397词补齐首段Ocean引述与Epley原话、Text 3 恢复4段391词治愈腰斩并理顺结尾设问、Text 4 恢复7段384词补齐政府与拨款计划论述、Part B 恢复8段499词规范艺术家分段切除杂质、Q34纠偏为真题原版选项、彻底治愈全卷45题question_number丢失缺陷、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round61_anomalies) == 0)
    results["Assertion 84: 2015 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段267词、Text 1 恢复7段410词补齐君主立宪选民服务论述、Text 2 恢复7段437词切除倒灌题干与伪造监听句并补齐云计算与汽车类比、Text 3 恢复6段438词还原Parmigiani/Ioannidis/Vaux三大权威引述、Text 4 恢复6段441词还原默多克之女讲话与审判真实表述、Part B 恢复5段324词剥离Directions与选项、Q22/Q32/Q38致命答案纠偏、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round62_anomalies) == 0)
    results["Assertion 85: 2015 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段320词消除占位符残损、Text 1 恢复6段398词纠偏Q21为A及Q25为D、Text 2 恢复5段397词治愈引文格式与Q28真实选项纠偏、Text 3 恢复5段420词还原右脑修辞与团队导向论述消除黏连、Text 4 恢复6段427词消除黏连并还原医保核心失落句、Part B 恢复7段519词剔除OCR杂质并补齐44段社交陪伴完整句、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round63_anomalies) == 0)
    results["Assertion 86: 2016 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型规范3段理顺婚俗脉络、Text 1 恢复7段找回失落第7段并修复首句France注脚与第3段首句截断、Text 2 恢复6段找回第3段6句大篇失落句并剔除showT与倒灌题干、Text 3 恢复6段切除双重重复与OCR乱码并补全罚金论述、Text 4 恢复7段理顺奢侈品转型、Part B 恢复8段剥离指导语与选项、全卷45题question_number彻底自洽赋值1..45、纠偏Q24为真题原版选项、纠偏Q25为D及Q36为A及Q40为B、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round64_anomalies) == 0)
    results["Assertion 87: 2016 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段并补齐年轻企业关联句、Text 1 恢复6段修复101班级与shelf life、Text 2 恢复4段补齐栖息地补偿金论述与Lininger引述、Text 3 恢复4段补全Eberle空瓶子比喻与灵魂时间、Text 4 恢复6段理顺里程碑与Schneider失落求职句、Part B 恢复7段切除乱码-ns与补齐情绪宣泄句、全卷45题question_number自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round65_anomalies) == 0)
    results["Assertion 88: 2017 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（Text 3 与 Text 4 历史颠倒互换彻底归位纠偏、Text 2 补齐失落利留卡拉尼女王首段恢复6段、完型恢复4段并修复yes与碎词、Text 3 剔除词数泄露恢复7段、Text 4 恢复8段独立设问、Part B 剥离指导语与连线图恢复7段[A]-[G]、全卷45题question_number自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round66_anomalies) == 0)
    results["Assertion 89: 2017 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型治愈单一大段黏连恢复4段348词并切除reservedfor、Text 1 恢复4段治愈toprovidethe与Baddeley原句、Text 2 恢复4段治愈therest ofthe并补全静止脸实验与Tronick论述、Text 3 恢复4段并理顺大一新生适应与转专业省钱逻辑、Text 4 恢复10段并纠偏鲍尔奇火灾哲学、Part B 恢复6段理顺五位制造业代表访谈、全卷45题question_number彻底自洽赋值1..45、Q21/22/25/26/28/29/30/32/33/34/36/38/39 严重乱序选项彻底归位、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round67_anomalies) == 0)
    results["Assertion 90: 2018 年英语一 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复4段并切除[1] for答案泄露、Text 1 恢复7段治愈on't dismiss与反斜杠、Text 2 恢复6段切除niversity/nited碎词与beef up/Barna题干倒灌、Text 3 彻底切除Text 2跨篇倒灌段落并完整还原NHS/DeepMind四段论、Text 4 恢复4段理顺USPS赤字与改革、Part B 恢复7段[A]-[G]彻底剔除莎士比亚剧场串题伪选项、全卷45题question_number彻底自洽赋值1..45、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round68_anomalies) == 0)
    results["Assertion 91: 2018 年英语二 Use of English + Text 1-4 + Part B 全卷黄金重构（完型恢复5段350词消除假实验段、Text 1 恢复8段370词对齐Q23第5段与推行本科论述、Text 2 恢复7段416词理顺风能与储能电池进展、Text 3 恢复4段412词补全反垄断法变化慢从句并消除黏连、Text 4 恢复7段439词找回失落第3段深度日程并治愈rethink截断、Part B 恢复584词剥离Directions与分值杂质、彻底治愈全卷45题question_number与score丢失缺陷、Q1-Q45 官方标准答案/题型/分值 100% 零差异对齐）"] = (len(round69_anomalies) == 0)
    
    print("\n=== 断言检查结果 ===")
    all_passed = True
    for metric, status in results.items():
        status_str = "✅ PASS" if status else "❌ FAIL"
        print(f"{status_str} | {metric}")
        if not status:
            all_passed = False

    if not all_passed:
        print("\n=== 失败详情报告 ===")
        if watermark_hits:
            print(f"Watermark hits ({len(watermark_hits)}):", watermark_hits[:5])
        if trailing_dot_opts:
            print(f"Trailing dot options ({len(trailing_dot_opts)}):", trailing_dot_opts[:5])
        if cloze_2004_placeholders:
            print(f"2004 Cloze placeholders ({len(cloze_2004_placeholders)}):", cloze_2004_placeholders[:5])
        if cloze_2014_q8_anomalies:
            print(f"2014 Cloze Q8 anomalies ({len(cloze_2014_q8_anomalies)}):", cloze_2014_q8_anomalies[:5])
        if non_canonical_option_orders:
            print(f"Non-canonical option orders ({len(non_canonical_option_orders)}):", non_canonical_option_orders[:5])
        if duplicate_cloze_reading_options:
            print(f"Duplicate cloze/reading options ({len(duplicate_cloze_reading_options)}):", duplicate_cloze_reading_options[:5])
        if ocr_corruptions_found:
            print(f"OCR corruptions ({len(ocr_corruptions_found)}):", ocr_corruptions_found[:5])
        if part_b_anomalies:
            print(f"Part B anomalies ({len(part_b_anomalies)}):", part_b_anomalies[:5])
        if orphan_questions:
            print(f"Orphan questions ({len(orphan_questions)}):", orphan_questions[:5])
        if passage_boundary_anomalies:
            print(f"Passage boundary anomalies ({len(passage_boundary_anomalies)}):", passage_boundary_anomalies[:5])
        if truncated_stems_found:
            print(f"Truncated stems ({len(truncated_stems_found)}):", truncated_stems_found[:5])
        if semantic_conflicts:
            print(f"Semantic conflicts ({len(semantic_conflicts)}):", semantic_conflicts[:5])
        if mismatched_answers:
            print(f"Mismatched answers ({len(mismatched_answers)}):", mismatched_answers[:5])
        if round13_anomalies:
            print(f"Round 13 anomalies ({len(round13_anomalies)}):", round13_anomalies)
        if round15_anomalies:
            print(f"Round 15 anomalies ({len(round15_anomalies)}):", round15_anomalies)
        if round16_anomalies:
            print(f"Round 16 anomalies ({len(round16_anomalies)}):", round16_anomalies)
        if round17_anomalies:
            print(f"Round 17 anomalies ({len(round17_anomalies)}):", round17_anomalies)
        if round18_anomalies:
            print(f"Round 18 anomalies ({len(round18_anomalies)}):", round18_anomalies)
        if round19_anomalies:
            print(f"Round 19 anomalies ({len(round19_anomalies)}):", round19_anomalies)
        if round20_anomalies:
            print(f"Round 20 anomalies ({len(round20_anomalies)}):", round20_anomalies)
        if round21_anomalies:
            print(f"Round 21 anomalies ({len(round21_anomalies)}):", round21_anomalies)
        if round22_anomalies:
            print(f"Round 22 anomalies ({len(round22_anomalies)}):", round22_anomalies)
        if round23_anomalies:
            print(f"Round 23 anomalies ({len(round23_anomalies)}):", round23_anomalies)
        if round24_anomalies:
            print(f"Round 24 anomalies ({len(round24_anomalies)}):", round24_anomalies)
        if round25_anomalies:
            print(f"Round 25 anomalies ({len(round25_anomalies)}):", round25_anomalies)
        if round26_anomalies:
            print(f"Round 26 anomalies ({len(round26_anomalies)}):", round26_anomalies)
        if round27_anomalies:
            print(f"Round 27 anomalies ({len(round27_anomalies)}):", round27_anomalies)
        if round28_anomalies:
            print(f"Round 28 anomalies ({len(round28_anomalies)}):", round28_anomalies)
        if round29_anomalies:
            print(f"Round 29 anomalies ({len(round29_anomalies)}):", round29_anomalies)
        if round30_anomalies:
            print(f"Round 30 anomalies ({len(round30_anomalies)}):", round30_anomalies)
        if round31_anomalies:
            print(f"Round 31 anomalies ({len(round31_anomalies)}):", round31_anomalies)
        if round32_anomalies:
            print(f"Round 32 anomalies ({len(round32_anomalies)}):", round32_anomalies)
        if round33_anomalies:
            print(f"Round 33 anomalies ({len(round33_anomalies)}):", round33_anomalies)
        if round34_anomalies:
            print(f"Round 34 anomalies ({len(round34_anomalies)}):", round34_anomalies)
        if round35_anomalies:
            print(f"Round 35 anomalies ({len(round35_anomalies)}):", round35_anomalies)
        if round36_anomalies:
            print(f"Round 36 anomalies ({len(round36_anomalies)}):", round36_anomalies)
        if round37_anomalies:
            print(f"Round 37 anomalies ({len(round37_anomalies)}):", round37_anomalies)
        if round38_anomalies:
            print(f"Round 38 anomalies ({len(round38_anomalies)}):", round38_anomalies)
        if round39_anomalies:
            print(f"Round 39 anomalies ({len(round39_anomalies)}):", round39_anomalies)
        if round40_anomalies:
            print(f"Round 40 anomalies ({len(round40_anomalies)}):", round40_anomalies)
        if round41_anomalies:
            print(f"Round 41 anomalies ({len(round41_anomalies)}):", round41_anomalies)
        if round42_anomalies:
            print(f"Round 42 anomalies ({len(round42_anomalies)}):", round42_anomalies)
        if round42_anomalies:
            print(f"Round 42 anomalies ({len(round42_anomalies)}):", round42_anomalies)
        if round43_anomalies:
            print(f"Round 43 anomalies ({len(round43_anomalies)}):", round43_anomalies)
        if round44_anomalies:
            print(f"Round 44 anomalies ({len(round44_anomalies)}):", round44_anomalies)
        if round45_anomalies:
            print(f"Round 45 anomalies ({len(round45_anomalies)}):", round45_anomalies)
        if round46_anomalies:
            print(f"Round 46 anomalies ({len(round46_anomalies)}):", round46_anomalies)
        if round47_anomalies:
            print(f"Round 47 anomalies ({len(round47_anomalies)}):", round47_anomalies)
        if round48_anomalies:
            print(f"Round 48 anomalies ({len(round48_anomalies)}):", round48_anomalies[:10])
        if round49_anomalies:
            print(f"Round 49 anomalies ({len(round49_anomalies)}):", round49_anomalies[:10])
        if round50_anomalies:
            print(f"Round 50 anomalies ({len(round50_anomalies)}):", round50_anomalies[:10])
        if round51_anomalies:
            print(f"Round 51 anomalies ({len(round51_anomalies)}):", round51_anomalies[:10])
        if round52_anomalies:
            print(f"Round 52 anomalies ({len(round52_anomalies)}):", round52_anomalies[:10])
        if round53_anomalies:
            print(f"Round 53 anomalies ({len(round53_anomalies)}):", round53_anomalies[:10])
        if round54_anomalies:
            print(f"Round 54 anomalies ({len(round54_anomalies)}):", round54_anomalies[:10])
        if round55_anomalies:
            print(f"Round 55 anomalies ({len(round55_anomalies)}):", round55_anomalies[:10])
        if round56_anomalies:
            print(f"Round 56 anomalies ({len(round56_anomalies)}):", round56_anomalies[:10])
        if round57_anomalies:
            print(f"Round 57 anomalies ({len(round57_anomalies)}):", round57_anomalies[:10])
        if round58_anomalies:
            print(f"Round 58 anomalies ({len(round58_anomalies)}):", round58_anomalies[:10])
        if round59_anomalies:
            print(f"Round 59 anomalies ({len(round59_anomalies)}):", round59_anomalies[:10])
        if round60_anomalies:
            print(f"Round 60 anomalies ({len(round60_anomalies)}):", round60_anomalies[:10])
        if round61_anomalies:
            print(f"Round 61 anomalies ({len(round61_anomalies)}):", round61_anomalies[:10])
        if round62_anomalies:
            print(f"Round 62 anomalies ({len(round62_anomalies)}):", round62_anomalies[:10])
        if round63_anomalies:
            print(f"Round 63 anomalies ({len(round63_anomalies)}):", round63_anomalies[:10])
        if round64_anomalies:
            print(f"Round 64 anomalies ({len(round64_anomalies)}):", round64_anomalies[:10])
        if round65_anomalies:
            print(f"Round 65 anomalies ({len(round65_anomalies)}):", round65_anomalies[:10])
        if round66_anomalies:
            print(f"Round 66 anomalies ({len(round66_anomalies)}):", round66_anomalies[:10])
        if round67_anomalies:
            print(f"Round 67 anomalies ({len(round67_anomalies)}):", round67_anomalies[:10])
        if round68_anomalies:
            print(f"Round 68 anomalies ({len(round68_anomalies)}):", round68_anomalies[:10])
        if round58_anomalies:
            print(f"Round 58 anomalies ({len(round58_anomalies)}):", round58_anomalies[:10])
        if round59_anomalies:
            print(f"Round 59 anomalies ({len(round59_anomalies)}):", round59_anomalies[:10])
        if round60_anomalies:
            print(f"Round 60 anomalies ({len(round60_anomalies)}):", round60_anomalies[:10])
        sys.exit(1)
    else:
        print(f"\n🎉 恭喜！全库 {len(results)} 项法医级断言指标 100% 全部通过！无任何缺陷残留！")

if __name__ == '__main__':
    main()
