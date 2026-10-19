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
    for fpath in exam_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        title = data['exam'].get('title', '')
        yr = data['exam'].get('year')
        cat = data['exam'].get('category_id')
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
                if len(opts) != 4 or ans != 'C' or len(expl) < 400 or 'far from reaching human mental standards' not in [o.get('text') for o in opts]:
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
                if not expl_norm.endswith('确定答案E后，我们马上可以排除F。'):
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
                if so == 39 and (ans != 'C' or opt_map.get('C') != 'biased against classical liberal ideas' or not expl.startswith('39.')):
                    round18_anomalies.append(('2014_q39', ans, opt_map, expl[:30]))
                if so == 40 and (ans != 'B' or opt_map.get('B') != 'Illiberal Education and "The Heart of the Matter"' or not expl.startswith('40.')):
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
                if so == 16 and opt_map.get('B') != '(turn) over':
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
                if so == 35 and opt_map.get('A') != 'results directly from competitive':
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
                    if not stem.endswith('to') or ans != 'D' or opt_map.get('C') != 'stress the role of slaves in the U.S. history' or '乔治”大为不同' in expl or len(expl) < 400:
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
                    if stem != 'In the last paragraph, a problem commercial genetic testing faces is' or ans != 'A' or expl.startswith('29.'):
                        round22_anomalies.append(('2009_ky1_q29', stem, ans, expl[:30]))
                elif so == 30:
                    if stem != 'An appropriate title for the text is most likely to be' or ans != 'B' or expl.startswith('30 . . .'):
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
                    if stem != 'According to the author, the department stores of the 19th century' or ans != 'A' or opt_map.get('A') != 'played a role in the spread of popular culture' or opt_map.get('D') != 'owed its emergence to the culture of consumption':
                        round23_anomalies.append(('2006_ky1_q22', stem, ans, opt_map))
                elif so == 25 and opt_map.get('B') != 'successful':
                    round23_anomalies.append(('2006_ky1_q25_opt_B', opt_map.get('B')))
                elif so == 31 and (opt_map.get('A') != 'large animals were vulnerable to the changing' or opt_map.get('D') != 'slow-growing fish outlive fast-growing ones'):
                    round23_anomalies.append(('2006_ky1_q31_opts', opt_map))
                elif so == 32:
                    if stem != "We can infer from Dr. Myers and Dr. Worm’s paper that" or ans != 'A' or opt_map.get('A') != 'the stock of large predators in some old fisheries has reduced by 90%' or opt_map.get('C') != 'the catch sizes in new fisheries are only 20% of the original amount':
                        round23_anomalies.append(('2006_ky1_q32', stem, ans, opt_map))
                elif so == 36:
                    if stem != 'By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that' or ans != 'D' or opt_map.get('D') != 'artists have changed their focus of interest' or expl.startswith('情况并非总是如此'):
                        round23_anomalies.append(('2006_ky1_q36', stem, ans, opt_map.get('D'), expl[:50]))
                elif so == 38 and opt_map.get('A') != 'emerges in the wake of the anti-happy art':
                    round23_anomalies.append(('2006_ky1_q38_opt_A', opt_map.get('A')))
                elif so == 39:
                    if stem != 'We can learn from the last paragraph that the author believes' or opt_map.get('D') != 'the anti-happy art flourishes when economy booms' or opt_map.get('B') != 'the anti-happy art is distasteful but refreshing':
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
                if stem != "It seems that now a country's economy depends much on" or opt_map.get('D') != 'how much control it has over foreign corporations' or '2&现在看来' in expl:
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
                if not stem.endswith('Massachusetts Bay') or len(expl) < 500 or '［精准定位］' not in expl:
                    round25_anomalies.append(('2009_ky1_q38', stem, len(expl)))
            if yr == 2012 and cat == 'ky1':
                if so == 22 and (opt_map.get('D') != 'recognize the limitations of advertisements' or opt_map.get('B') != "learn from advertisers' experience"):
                    round25_anomalies.append(('2012_ky1_q22', opt_map))
                elif so == 39 and (len(expl) < 500 or '［精准定位］' not in expl):
                    round25_anomalies.append(('2012_ky1_q39', len(expl)))
            if yr == 2016 and cat == 'ky1' and so == 35:
                if ans != 'B' or opt_map.get('B') != "The necessary amount of companies' spending on it is unknown." or len(expl) < 400 or '［精准定位］' not in expl:
                    round25_anomalies.append(('2016_ky1_q35', ans, opt_map.get('B'), len(expl)))
            if yr == 2010 and cat == 'ky1':
                if so == 23 and opt_map.get('A') != "It is writers' duty to fulfill journalistic goals.":
                    round25_anomalies.append(('2010_ky1_q23', opt_map.get('A')))
                elif so == 24 and (stem != "What can be learned about Cardus according to the last two paragraphs?" or opt_map.get('A') != "His music criticism may not appeal to readers today." or opt_map.get('B') != "His reputation as a music critic has long been in dispute."):
                    round25_anomalies.append(('2010_ky1_q24', stem, opt_map))
                elif so == 31 and (stem != "By citing the book The Tipping Point, the author intends to" or opt_map.get('B') != "discuss influentials' function in spreading ideas"):
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
                if len(expl) > 1000 or not expl.endswith('因此［G］能承上启下，敲定为答案。') or 'adds humbly' in expl:
                    round29_anomalies.append(('2008_ky1_q42', len(expl), expl[-30:]))

            if yr == 2006 and cat == 'ky1' and so == 45:
                if len(expl) > 800 or not expl.endswith('故选项应出现在第十一段之后，而不是之前，故排除。') or '对“知识分子”的定义' in expl:
                    round29_anomalies.append(('2006_ky1_q45', len(expl), expl[-30:]))




        # Passage boundary check
        for p in passages:
            pt = p.get('title', '')
            c = (p.get('content') or '').strip()
            so = p.get('sort_order')

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
        sys.exit(1)
    else:
        print(f"\n🎉 恭喜！全库 {len(results)} 项法医级断言指标 100% 全部通过！无任何缺陷残留！")

if __name__ == '__main__':
    main()
