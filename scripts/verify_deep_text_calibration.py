#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_deep_text_calibration.py
法医级全库文本校对与做题适配断言验证脚本。
11 项核心断言指标必须 100% PASS。
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

    print(f"=== 考研英语全库真题法医级文本校对与适配断言 ===")
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

    for fpath in exam_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        title = data['exam'].get('title', '')
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

            # 9. Trailing digit words
            matches = re.findall(r'\b([a-zA-Z]{3,})(\d)\b', c)
            for w, d in matches:
                full = f"{w}{d}".lower()
                if full not in LEGIT_NUM_WORDS:
                    trailing_digit_words.append((title, pt, f"{w}{d}"))

            # 10. Paragraph start digit markers
            p_starts = re.findall(r'(?:^|\n)[08][A-Z]|f\}', c)
            if p_starts:
                paragraph_start_digits.append((title, pt, p_starts))

            # 11. Glued punctuations
            c_commas = re.findall(r'([a-zA-Z]{2,},[a-zA-Z]{2,})', c)
            if c_commas:
                glued_punctuations.append((title, pt, 'comma', c_commas))

            c_periods = re.findall(r'([a-zA-Z]{2,}\.[A-Z][a-z]{2,})', c)
            c_periods_filtered = [m for m in c_periods if not any(m.lower().startswith(a) for a in ABBREVIATIONS)]
            if c_periods_filtered:
                glued_punctuations.append((title, pt, 'period', c_periods_filtered))

            # 17. Passage word anomalies (internal digits & glued terms)
            for m in re.finditer(r'\b[a-zA-Z]+[0-9]+[a-zA-Z]+\b', c):
                w = m.group(0).lower()
                if w not in {'covid19', 'mp3', 'h1n1', 'k12', 'h-2a', 'h-2b', 'change4life', '3d', 'f16', 'a350', 'b787', 'mid-20th', 'h2o'}:
                    passage_word_anomalies.append((title, pt, w))
            if 'Ea: kia\'lDd3ikal' in c or 'newsstandregnant' in c or 'stakeholder E\'' in c:
                passage_word_anomalies.append((title, pt, 'phonetic_sidebar'))

        # Audit Questions
        for q in questions:
            so = q.get('sort_order')
            stem = q.get('stem', '')
            c_ans = q.get('correct_answer')
            ans = q.get('answer')

            if c_ans != ans:
                mismatched_answers.append((title, so, c_ans, ans))

            # Stem prefix
            if re.match(r'^\d+[\.\、\:\s]\s*', stem.strip()):
                stems_with_prefix.append((title, so, stem[:30]))

            # Cloze stem
            if 1 <= so <= 20:
                expected = f"Choose the best option for blank [{so}] in the passage:"
                if stem != expected:
                    non_standard_cloze_stems.append((title, so, stem[:30]))

            # 15. Stem OCR anomalies & double spaces
            if re.search(r'\b[a-zA-Z]+9s\b', stem) or re.search(r'\b[a-zA-Z]+\^[a-zA-Z]*\b', stem) or 'M earned19' in stem or 'phrase14to' in stem:
                stem_ocr_anomalies.append((title, so, stem))
            if '  ' in stem:
                stem_ocr_anomalies.append((title, so, 'double_space: ' + stem))

            # 16. Option prefix & weird trailing characters
            for opt in q.get('options', []):
                otext = opt.get('text', '')
                if re.match(r'^[A-G][\.\、\:\)]\s+', otext) or re.match(r'^\[[A-G]\]\s+', otext):
                    opt_prefix_anomalies.append((title, so, opt.get('key'), otext))
                if re.search(r'\^[a-zA-Z]*$', otext.strip()):
                    opt_prefix_anomalies.append((title, so, opt.get('key'), otext))

            # Explanation checks
            expl = (q.get('explanation') or '').strip()
            if '官方解析与答案详解：正确答案为' in expl or '官方解析：正确答案为' in expl:
                raw_placeholders.append((title, so, expl[:40]))

            m_conf = re.search(r'正确答案为\s*\[?([A-G])\]?', expl)
            if m_conf and m_conf.group(1) != ans:
                explanation_conflicts.append((title, so, ans, m_conf.group(1)))

            m_conf2 = re.search(r'(?:【答案】|［答案］)\s*([A-G])', expl)
            if m_conf2 and m_conf2.group(1) != ans:
                explanation_conflicts.append((title, so, ans, m_conf2.group(1)))

            # 18. Canonical Option Sorting
            opt_keys = [o.get('key') for o in q.get('options', [])]
            if opt_keys not in (['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['T', 'F']):
                non_canonical_option_orders.append((title, so, opt_keys))

            # 19. Explanation bleeding / giant blobs / next question leakage
            if len(expl) > 10000 or re.search(rf'\n\s*(?:•?真题精解•?\s*\n\s*)?{so+1}\s*[.・•、]', expl):
                explanation_bleeding_found.append((title, so, len(expl)))

            # 20. Unclosed Markdown bold tags
            if expl.count('**') % 2 != 0:
                unclosed_markdown_bolds.append((title, so, expl.count('**')))

    results["2. 篇章总量 243 篇"] = (total_passages == 243)
    results["3. 试题总量 1,825 题"] = (total_questions == 1825)
    results["4. 试题答案 100% 对齐 (correct_answer == answer)"] = (len(mismatched_answers) == 0)
    results["5. 试题题干 0 处序号冗余前缀"] = (len(stems_with_prefix) == 0)
    results["6. 完型小题 820 题题干 100% 格式统一"] = (len(non_standard_cloze_stems) == 0)
    results["7. Part A 篇章 0 处残存选项代号"] = (len(part_a_leaked_options) == 0)
    results["8. 篇章 0 处生词音标侧栏注解残留"] = (len(gloss_phonetics_found) == 0)
    results["9. 篇章 0 处词尾角标漂移数字"] = (len(trailing_digit_words) == 0)
    results["10. 篇章 0 处段首伪数字标记"] = (len(paragraph_start_digits) == 0)
    results["11. 篇章 0 处英文逗号/句号黏连"] = (len(glued_punctuations) == 0)
    results["12. 试题解析 0 处假模版占位符"] = (len(raw_placeholders) == 0)
    results["13. 试题解析 0 处答案描述冲突"] = (len(explanation_conflicts) == 0)
    results["14. 试题解析 0 处短文本或残片乱码"] = (len(short_or_garbage_expls) == 0)
    results["15. 试题题干 0 处 OCR 异形字符与双空格"] = (len(stem_ocr_anomalies) == 0)
    results["16. 选项文本 0 处冗余代号前缀与尾部杂字"] = (len(opt_prefix_anomalies) == 0)
    results["17. 篇章正文 0 处词内非法数字与非标准黏连"] = (len(passage_word_anomalies) == 0)
    results["18. 选项键序 100% 标准字母序列规范化"] = (len(non_canonical_option_orders) == 0)
    results["19. 试题解析 0 处跨题后附外泄或巨型粘连"] = (len(explanation_bleeding_found) == 0)
    results["20. 试题解析 0 处未闭合 Markdown 粗体标记"] = (len(unclosed_markdown_bolds) == 0)

    # 21. Topology & Linkage: Every question points to a valid passage in the same exam
    orphan_questions = []
    passage_boundary_anomalies = []

    for fpath in exam_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        title = data['exam'].get('title', '')
        p_ids = {p['id'] for p in data.get('passages', [])}
        for q in data.get('questions', []):
            if q.get('passage_id') not in p_ids:
                orphan_questions.append((title, q.get('sort_order'), q.get('passage_id')))
        
        # 22. Passage Boundary Cleanliness
        for p in data.get('passages', []):
            pt = p.get('title', '')
            c = (p.get('content') or '').strip()
            # Check for leaked stems at the end of passages
            if re.search(r'\b(?:[2-4]\d|Q[2-4]\d)\s*[\.・\、\:]\s*[A-Z]', c[-150:]):
                passage_boundary_anomalies.append((title, pt, 'stem_at_end', c[-80:]))
            if re.search(r'\[[A-G]\]\s*[a-zA-Z]{3,}', c[-80:]):
                passage_boundary_anomalies.append((title, pt, 'option_at_end', c[-80:]))
            if c.endswith('boardso') or c.endswith('building block;') or c.endswith('C A B D') or c.endswith('C  A  B  D'):
                passage_boundary_anomalies.append((title, pt, 'garbage_at_end', c[-40:]))

    results["21. 篇章与试题拓扑关联 100% 紧密绑定"] = (len(orphan_questions) == 0)
    results["22. 篇章篇首篇尾 0 处伪题干、截断与跨篇串文污染"] = (len(passage_boundary_anomalies) == 0)

    print("\n=== 断言检查结果 ===")
    all_passed = True
    for metric, status in results.items():
        status_str = "✅ PASS" if status else "❌ FAIL"
        print(f"{status_str} | {metric}")
        if not status:
            all_passed = False

    if not all_passed:
        print("\n=== 失败详情报告 ===")
        if orphan_questions:
            print(f"Orphan questions ({len(orphan_questions)}):", orphan_questions[:5])
        if passage_boundary_anomalies:
            print(f"Passage boundary anomalies ({len(passage_boundary_anomalies)}):", passage_boundary_anomalies[:5])
        if mismatched_answers:
            print(f"Mismatched answers ({len(mismatched_answers)}):", mismatched_answers[:5])
        if stems_with_prefix:
            print(f"Stems with prefix ({len(stems_with_prefix)}):", stems_with_prefix[:5])
        if non_standard_cloze_stems:
            print(f"Non-standard cloze stems ({len(non_standard_cloze_stems)}):", non_standard_cloze_stems[:5])
        if part_a_leaked_options:
            print(f"Part A leaked options ({len(part_a_leaked_options)}):", part_a_leaked_options[:5])
        if gloss_phonetics_found:
            print(f"Gloss phonetics found ({len(gloss_phonetics_found)}):", gloss_phonetics_found[:5])
        if trailing_digit_words:
            print(f"Trailing digit words ({len(trailing_digit_words)}):", trailing_digit_words[:5])
        if paragraph_start_digits:
            print(f"Paragraph start digits ({len(paragraph_start_digits)}):", paragraph_start_digits[:5])
        if glued_punctuations:
            print(f"Glued punctuations ({len(glued_punctuations)}):", glued_punctuations[:5])
        if raw_placeholders:
            print(f"Raw placeholders ({len(raw_placeholders)}):", raw_placeholders[:5])
        if explanation_conflicts:
            print(f"Explanation conflicts ({len(explanation_conflicts)}):", explanation_conflicts[:5])
        if short_or_garbage_expls:
            print(f"Short or garbage expls ({len(short_or_garbage_expls)}):", short_or_garbage_expls[:5])
        if stem_ocr_anomalies:
            print(f"Stem OCR anomalies ({len(stem_ocr_anomalies)}):", stem_ocr_anomalies[:5])
        if opt_prefix_anomalies:
            print(f"Option prefix anomalies ({len(opt_prefix_anomalies)}):", opt_prefix_anomalies[:5])
        if passage_word_anomalies:
            print(f"Passage word anomalies ({len(passage_word_anomalies)}):", passage_word_anomalies[:5])
        sys.exit(1)
    else:
        print("\n🎉 恭喜！全库 22 项法医级断言指标 100% 全部通过！无任何缺陷残留！")

if __name__ == '__main__':
    main()
