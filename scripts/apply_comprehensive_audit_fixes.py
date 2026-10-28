# -*- coding: utf-8 -*-
"""
apply_comprehensive_audit_fixes.py
Comprehensive multi-agent remediation script applying all gold calibrations across all 41 exams.
"""

import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

EXAMS_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def load_exam(exam_id):
    path = os.path.join(EXAMS_DIR, f"{exam_id}.json")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f), path

def save_exam(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def clean_option_schema(options):
    """Normalize options to have standard {key, value, text, content}"""
    normalized = []
    for opt in options:
        k = opt.get('key') or opt.get('value')
        t = opt.get('text') or opt.get('content') or ''
        normalized.append({
            'key': k,
            'value': k,
            'text': t,
            'content': t
        })
    return normalized

def strip_option_bracket_prefix(text):
    """Strip leading [A] or (A) prefix from option text"""
    return re.sub(r'^\s*(\[[A-G]\]|\([A-G]\))\s*', '', text).strip()

def run_all_fixes():
    print("=== Starting Comprehensive Multi-Agent Audit Fixes ===")
    modified_count = 0

    # 1. 2010 ky1 (e5abf09b-e94d-5994-b944-7c5711cd4e4d)
    print("\n--- 1. Fixing 2010 ky1 (Cloze Text Restoration) ---")
    d, path = load_exam("e5abf09b-e94d-5994-b944-7c5711cd4e4d")
    authentic_2010_cloze = (
        "In 1924 America's National Research Council sent two engineers to supervise a series of experiments "
        "at a telephone-parts factory called the Hawthorne Plant near Chicago. It hoped they would learn how shop-floor lighting [1] workers' productivity. "
        "Instead, the studies ended [2] giving their name to the \"Hawthorne effect\", the extremely influential idea that the very [3] of being experimented upon changed subjects' behavior.\n\n"
        "The idea arose because of the [4] behavior of the women in the plant. According to [5] of the experiments, their hourly output rose when lighting was increased, "
        "but also when it was dimmed. It did not [6] what was done in the experiment; [7] something was changed, productivity rose. "
        "A(n) [8] that they were being experimented upon seemed to be [9] to alter workers' behavior [10] itself.\n\n"
        "After several decades, the same data were [11] to econometric analysis. The Hawthorne experiments had another surprise in store. "
        "[12] the descriptions on record, no systematic [13] was found that levels of productivity were related to changes in lighting.\n\n"
        "It turns out that the peculiar way of conducting the experiments may have led to [14] interpretations of what happened. "
        "[15], lighting was always changed on a Sunday. When work started again on Monday, output [16] rose compared with the previous Saturday and [17] to rise for the next couple of days. "
        "[18], a comparison with data for weeks when there was no experimentation showed that output always went up on Mondays. "
        "Workers [19] to be diligent for the first few days of the week in any case, before [20] a plateau and then slackening off. "
        "This suggests that the alleged \"Hawthorne effect\" is hard to pin down."
    )
    d['passages'][0]['content'] = authentic_2010_cloze
    save_exam(path, d)
    print("  -> 2010 ky1 Cloze restored to 4 paragraphs, 20 blanks [1]-[20].")
    modified_count += 1

    # 2. 2019 ky1 (5bcba462-0a1e-59b2-9fcb-c171d242db3b)
    print("\n--- 2. Fixing 2019 ky1 (Cloze Blanks, Mojibake & Part B Option Prefixes) ---")
    d, path = load_exam("5bcba462-0a1e-59b2-9fcb-c171d242db3b")
    # Clean Cloze
    cloze_text = d['passages'][0]['content']
    # Replace bare numbers with [N]
    replacements_2019 = [
        ("smartphones. 1 of us just walk", "smartphones. [1] of us just walk"),
        ("phones 2 on batteries", "phones [2] on batteries"),
        ("realize. 3 you get lost", "realize. [3] you get lost"),
        ("you 4 can't find north", "you [4] can't find north"),
        ("navigate 5 to civilization", "navigate [5] to civilization"),
        ("well 6 a trail", "well [6] a trail"),
        ("completely 7 area", "completely [7] area"),
        ("Which 8 is downhill", "Which [8] is downhill"),
        ("fresh water. 9 , if you head downhill", "fresh water. [9], if you head downhill"),
        ("should 10 see signs", "should [10] see signs"),
        ("sights — you may be 11 how", "sights — you may be [11] how"),
        ("sights \ufffd you may be 11 how", "sights — you may be [11] how"),
        ("sights \ufffd you may be [11] how", "sights — you may be [11] how"),
        ("Another 12 : Climb high", "Another [12]: Climb high"),
        ("habitation. 13 , even in dense forest", "habitation. [13], even in dense forest"),
        ("able to 14 gaps in", "able to [14] gaps in"),
        ("carve 15 the woods", "carve [15] the woods"),
        ("toward these 16 to find", "toward these [16] to find"),
        ("horizon for 17 light sources", "horizon for [17] light sources"),
        ("pollution.\n\n18 , assuming you're lost", "pollution.\n\n[18], assuming you're lost"),
        ("for the 19 we leave", "for the [19] we leave"),
        ("features can 20 you to civilization", "features can [20] you to civilization")
    ]
    for old_s, new_s in replacements_2019:
        cloze_text = cloze_text.replace(old_s, new_s)
    # Also clean any remaining mojibake in passage
    cloze_text = cloze_text.replace('\ufffd', '—')
    d['passages'][0]['content'] = cloze_text

    # Strip prefixes in Q41-Q45
    for q in d['questions']:
        if q.get('sort_order', 0) >= 41:
            for opt in q.get('options', []):
                opt['text'] = strip_option_bracket_prefix(opt['text'])
    save_exam(path, d)
    print("  -> 2019 ky1 Cloze blanks bracketed, spacing/mojibake cleaned, Q41-Q45 option prefixes stripped.")
    modified_count += 1

    # 3. 2018 ky1 (e95fe05a-07f4-53d1-a11f-9b636acc6469)
    print("\n--- 3. Fixing 2018 ky1 (Part B Option Prefixes) ---")
    d, path = load_exam("e95fe05a-07f4-53d1-a11f-9b636acc6469")
    for q in d['questions']:
        if q.get('sort_order', 0) >= 41:
            for opt in q.get('options', []):
                opt['text'] = strip_option_bracket_prefix(opt['text'])
    save_exam(path, d)
    print("  -> 2018 ky1 Q41-Q45 option prefixes stripped.")
    modified_count += 1

    # 4. 2022 ky1 (6d676d85-a38a-5fe4-9506-31de03b648b6)
    print("\n--- 4. Fixing 2022 ky1 (Part B Directions Stripping) ---")
    d, path = load_exam("6d676d85-a38a-5fe4-9506-31de03b648b6")
    pb_content = d['passages'][5]['content']
    directions_lead = "In the following text, five people express their views about zoos. For questions 41-45, choose from the arguments (A-G) the one which each person would most likely support."
    if pb_content.startswith(directions_lead):
        pb_content = pb_content[len(directions_lead):].strip()
        d['passages'][5]['content'] = pb_content
        print("  -> 2022 ky1 Part B Directions stripped.")
    save_exam(path, d)
    modified_count += 1

    # 5. 2025 ky1 (c75ee9ef-ec21-5396-b3bf-4e30260d2918)
    print("\n--- 5. Fixing 2025 ky1 (Part B Paragraph [E] Truncation) ---")
    d, path = load_exam("c75ee9ef-ec21-5396-b3bf-4e30260d2918")
    pb_content = d['passages'][5]['content']
    target_truncated = "massive field is tiny"
    target_fixed = "massive challenge. The depth of field is tiny"
    if target_truncated in pb_content:
        d['passages'][5]['content'] = pb_content.replace(target_truncated, target_fixed)
        print("  -> 2025 ky1 Part B [E] restored missing phrase.")
    save_exam(path, d)
    modified_count += 1

    # 6. 2006 ky1 (c6e9dbac-6148-532e-90d2-2a8d3682a6ac)
    print("\n--- 6. Fixing 2006 ky1 (Part B Directions, Appended Text, Q41-Q45 Gold Paragraphs) ---")
    d, path = load_exam("c6e9dbac-6148-532e-90d2-2a8d3682a6ac")
    pb_content = d['passages'][5]['content']
    # Strip directions at top
    pb_lines = pb_content.splitlines()
    clean_lines = []
    in_directions = True
    for line in pb_lines:
        if in_directions:
            if "Directions:" in line or "In the following article" in line or "Mark your answers" in line:
                continue
            if line.strip() == "":
                continue
            in_directions = False
        clean_lines.append(line)
    clean_text = "\n".join(clean_lines)

    # Authentic 7 paragraphs [A]-[G]
    gold_paragraphs_2006 = {
        'A': "Although no such evidence was presented, the casino's marketing department continued to pepper him with mailings. And he entered the casino and used his Fun Card without being detected.",
        'B': "It is unclear what luring was required, given his compulsive behavior. And in what sense was his will operative?",
        'C': "By the time he had lost $5,000 he said to himself that if he could get back to even, he would quit. One night he won $5,500, but he did not quit.",
        'D': "Gambling has been a common feature of American life forever, but for a long time it was broadly considered a sin, or a social disease. Now it is a social policy: the most important and aggressive promoter of gambling in America is the government.",
        'E': "David Williams's suit should trouble this gambling nation. But don't bet on it.",
        'F': "It is worrisome that society is medicalizing more and more behavioral problems, often defining as addictions what earlier, sterner generations explained as weakness of will.",
        'G': "The anonymous, lonely, undistracted nature of online gambling is especially conducive to compulsive behavior. But even if the government knew how to move against Internet gambling, what would be its grounds for doing so?"
    }

    # Cut off appended [A] through [G] from passage if present
    # Look for [A] Although no such evidence
    if "\n\n[A]" in clean_text or "\n[A]" in clean_text:
        split_idx = clean_text.find("[A] Although no such evidence")
        if split_idx != -1:
            clean_text = clean_text[:split_idx].strip()
    d['passages'][5]['content'] = clean_text

    # Update Q41-Q45 options
    for q in d['questions']:
        if q.get('sort_order', 0) >= 41:
            q['options'] = [
                {'key': k, 'value': k, 'text': gold_paragraphs_2006[k], 'content': gold_paragraphs_2006[k]}
                for k in sorted(gold_paragraphs_2006.keys())
            ]
    save_exam(path, d)
    print("  -> 2006 ky1 Part B Directions stripped, appended text removed, Q41-Q45 restored to authentic exam paragraphs.")
    modified_count += 1

    # 7. 2011 ky1 (111d6c78-81a1-53dc-a039-dad4c94ebd35)
    print("\n--- 7. Fixing 2011 ky1 (Part B Directions, Title, question_number, Option Prefixes) ---")
    d, path = load_exam("111d6c78-81a1-53dc-a039-dad4c94ebd35")
    d['passages'][5]['title'] = "Section II: Reading Comprehension Part B"
    pb_content = d['passages'][5]['content']
    # Strip directions and flowchart
    idx_start = pb_content.find("[A] No disciplines have seized")
    if idx_start != -1:
        d['passages'][5]['content'] = pb_content[idx_start:].strip()
    # Populate question_number and strip prefixes in Q41-Q45
    for q in d['questions']:
        q['question_number'] = q['sort_order']
        if q.get('sort_order', 0) >= 41:
            for opt in q.get('options', []):
                opt['text'] = strip_option_bracket_prefix(opt['text'])
    save_exam(path, d)
    print("  -> 2011 ky1 Part B Directions stripped, title standardized, question_number assigned, option prefixes cleaned.")
    modified_count += 1

    # 8. 2014 ky1 (240cc48a-439b-5d27-8464-f7dc53e060dc)
    print("\n--- 8. Fixing 2014 ky1 (Part B Directions & Corrupt Flowchart Stripping) ---")
    d, path = load_exam("240cc48a-439b-5d27-8464-f7dc53e060dc")
    pb_content = d['passages'][5]['content']
    idx_start = pb_content.find("[A] Some archaeological sites")
    if idx_start != -1:
        d['passages'][5]['content'] = pb_content[idx_start:].strip()
        print("  -> 2014 ky1 Part B Directions and corrupt diagram stripped cleanly.")
    save_exam(path, d)
    modified_count += 1

    # 9. 2011 ky2 (53a52573-0afc-51a4-86b6-b2f321cbe6a8)
    print("\n--- 9. Fixing 2011 ky2 (Part B Directions, Title, question_number) ---")
    d, path = load_exam("53a52573-0afc-51a4-86b6-b2f321cbe6a8")
    d['passages'][5]['title'] = "Section II: Reading Comprehension Part B"
    pb_content = d['passages'][5]['content']
    target_start = "Leading doctors today weigh in on the debate"
    idx_start = pb_content.find(target_start)
    if idx_start != -1:
        d['passages'][5]['content'] = pb_content[idx_start:].strip()
    for q in d['questions']:
        q['question_number'] = q['sort_order']
    save_exam(path, d)
    print("  -> 2011 ky2 Part B Directions stripped, title standardized, question_number assigned to all 45.")
    modified_count += 1

    # 10. 2012 ky2 (2d124f8f-f9af-5b94-9cc9-0087a76ee289)
    print("\n--- 10. Fixing 2012 ky2 (Q16 Authentic Exam Options Restoration) ---")
    d, path = load_exam("2d124f8f-f9af-5b94-9cc9-0087a76ee289")
    for q in d['questions']:
        if q.get('sort_order') == 16:
            q['options'] = [
                {'key': 'A', 'value': 'A', 'text': 'paralleled', 'content': 'paralleled'},
                {'key': 'B', 'value': 'B', 'text': 'counteracted', 'content': 'counteracted'},
                {'key': 'C', 'value': 'C', 'text': 'duplicated', 'content': 'duplicated'},
                {'key': 'D', 'value': 'D', 'text': 'contradicted', 'content': 'contradicted'}
            ]
            q['answer'] = 'A'
            q['correct_answer'] = 'A'
            break
    save_exam(path, d)
    print("  -> 2012 ky2 Q16 restored to official exam options: paralleled, counteracted, duplicated, contradicted.")
    modified_count += 1

    # 11. 2014 ky2 (307952b3-040c-5ab4-a893-687e97d737ec)
    print("\n--- 11. Fixing 2014 ky2 (Q34 Options Schema Completion) ---")
    d, path = load_exam("307952b3-040c-5ab4-a893-687e97d737ec")
    for q in d['questions']:
        if q.get('sort_order') == 34:
            q['options'] = clean_option_schema(q['options'])
            break
    save_exam(path, d)
    print("  -> 2014 ky2 Q34 options schema normalized with value key.")
    modified_count += 1

    # 12. 2020 ky2 (ee996af1-3aaa-5380-9465-08125c4db713)
    print("\n--- 12. Fixing 2020 ky2 (Q38 Explanation Duplication Stripping) ---")
    d, path = load_exam("ee996af1-3aaa-5380-9465-08125c4db713")
    for q in d['questions']:
        if q.get('sort_order') == 38:
            expl = q.get('explanation', '')
            # Look for 38. The word
            idx = expl.find("38. The word")
            if idx != -1:
                q['explanation'] = expl[idx:].strip()
            elif "·真题精解·\n38." in expl:
                idx = expl.find("·真题精解·\n38.")
                q['explanation'] = expl[idx:].strip()
            break
    save_exam(path, d)
    print("  -> 2020 ky2 Q38 explanation duplication removed.")
    modified_count += 1

    # 13. 2021 ky2 (4ebd819e-c832-5890-9048-ba16040a5607)
    print("\n--- 13. Fixing 2021 ky2 (Q12, Q13, Q24, Q27, Q29 Official Calibration) ---")
    d, path = load_exam("4ebd819e-c832-5890-9048-ba16040a5607")
    for q in d['questions']:
        so = q.get('sort_order')
        if so == 12:
            # Fix option D typo
            for opt in q['options']:
                if opt['key'] == 'D':
                    opt['text'] = 'policy'
                    opt['content'] = 'policy'
        elif so == 13:
            # Restore authentic Q13
            q['stem'] = "Choose the best option for blank [13] in the passage:"
            q['options'] = [
                {'key': 'A', 'value': 'A', 'text': 'reported', 'content': 'reported'},
                {'key': 'B', 'value': 'B', 'text': 'revealed', 'content': 'revealed'},
                {'key': 'C', 'value': 'C', 'text': 'admitted', 'content': 'admitted'},
                {'key': 'D', 'value': 'D', 'text': 'noticed', 'content': 'noticed'}
            ]
            q['answer'] = 'D'
            q['correct_answer'] = 'D'
            q['explanation'] = (
                "【命题解密】动词辨析。根据句意：“你有没有注意到，你的航班可能晚点一个小时起飞，但仍然准点到达？”"
                "notice意为“注意，察觉”，符合语境；reported“报告”；revealed“透露”；admitted“承认”，均不符合生活观察场景，故选[D] noticed。"
            )
        elif so == 24:
            q['answer'] = 'C'
            q['correct_answer'] = 'C'
        elif so == 27:
            q['answer'] = 'C'
            q['correct_answer'] = 'C'
        elif so == 29:
            q['answer'] = 'A'
            q['correct_answer'] = 'A'
    save_exam(path, d)
    print("  -> 2021 ky2 Q12/13/24/27/29 successfully calibrated to official ground truth.")
    modified_count += 1

    # 14. Cloze Options Notes Pollution Cleaning (2002, 2003, 2007, 2008, 2009 ky1)
    print("\n--- 14. Cleaning Cloze Study Notes / Collocations across Early ky1 ---")
    # 2002 ky1: e1b9d134-9546-55ab-9a60-c7e5b04046a3
    d, path = load_exam("e1b9d134-9546-55ab-9a60-c7e5b04046a3")
    for q in d['questions']:
        so = q.get('sort_order')
        if so == 4:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'process', 'content': 'process'},
                            {'key': 'B', 'value': 'B', 'text': 'company', 'content': 'company'},
                            {'key': 'C', 'value': 'C', 'text': 'light', 'content': 'light'},
                            {'key': 'D', 'value': 'D', 'text': 'form', 'content': 'form'}]
        elif so == 6:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'on', 'content': 'on'},
                            {'key': 'B', 'value': 'B', 'text': 'out', 'content': 'out'},
                            {'key': 'C', 'value': 'C', 'text': 'over', 'content': 'over'},
                            {'key': 'D', 'value': 'D', 'text': 'off', 'content': 'off'}]
        elif so == 8:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'concept', 'content': 'concept'},
                            {'key': 'B', 'value': 'B', 'text': 'dimension', 'content': 'dimension'},
                            {'key': 'C', 'value': 'C', 'text': 'effect', 'content': 'effect'},
                            {'key': 'D', 'value': 'D', 'text': 'perspective', 'content': 'perspective'}]
    save_exam(path, d)
    print("  -> 2002 ky1 Cloze options cleaned.")

    # 2003 ky1: 91ff038a-e3f9-5b6d-82c5-1328735be1d1
    d, path = load_exam("91ff038a-e3f9-5b6d-82c5-1328735be1d1")
    for q in d['questions']:
        if q.get('sort_order') == 1:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'thought', 'content': 'thought'},
                            {'key': 'B', 'value': 'B', 'text': 'idea', 'content': 'idea'},
                            {'key': 'C', 'value': 'C', 'text': 'opinion', 'content': 'opinion'},
                            {'key': 'D', 'value': 'D', 'text': 'advice', 'content': 'advice'}]
            break
    save_exam(path, d)
    print("  -> 2003 ky1 Cloze options cleaned.")

    # 2007 ky1: e560bab8-4d9a-5149-a93f-1ee1d7bf4225
    d, path = load_exam("e560bab8-4d9a-5149-a93f-1ee1d7bf4225")
    for q in d['questions']:
        so = q.get('sort_order')
        if so == 4:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'related', 'content': 'related'},
                            {'key': 'B', 'value': 'B', 'text': 'close', 'content': 'close'},
                            {'key': 'C', 'value': 'C', 'text': 'open', 'content': 'open'},
                            {'key': 'D', 'value': 'D', 'text': 'devoted', 'content': 'devoted'}]
        elif so == 5:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'access', 'content': 'access'},
                            {'key': 'B', 'value': 'B', 'text': 'succession', 'content': 'succession'},
                            {'key': 'C', 'value': 'C', 'text': 'right', 'content': 'right'},
                            {'key': 'D', 'value': 'D', 'text': 'return', 'content': 'return'}]
    save_exam(path, d)
    print("  -> 2007 ky1 Cloze options cleaned.")

    # 2008 ky1: d80926ab-1841-5d1f-a999-56773986c46d
    d, path = load_exam("d80926ab-1841-5d1f-a999-56773986c46d")
    for q in d['questions']:
        so = q.get('sort_order')
        if so == 1:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'selected', 'content': 'selected'},
                            {'key': 'B', 'value': 'B', 'text': 'prepared', 'content': 'prepared'},
                            {'key': 'C', 'value': 'C', 'text': 'obliged', 'content': 'obliged'},
                            {'key': 'D', 'value': 'D', 'text': 'pleased', 'content': 'pleased'}]
        elif so == 6:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'thought', 'content': 'thought'},
                            {'key': 'B', 'value': 'B', 'text': 'sight', 'content': 'sight'},
                            {'key': 'C', 'value': 'C', 'text': 'cost', 'content': 'cost'},
                            {'key': 'D', 'value': 'D', 'text': 'risk', 'content': 'risk'}]
        elif so == 8:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'progress', 'content': 'progress'},
                            {'key': 'B', 'value': 'B', 'text': 'fact', 'content': 'fact'},
                            {'key': 'C', 'value': 'C', 'text': 'need', 'content': 'need'},
                            {'key': 'D', 'value': 'D', 'text': 'question', 'content': 'question'}]
        elif so == 15:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'given up', 'content': 'given up'},
                            {'key': 'B', 'value': 'B', 'text': 'got over', 'content': 'got over'},
                            {'key': 'C', 'value': 'C', 'text': 'carried on', 'content': 'carried on'},
                            {'key': 'D', 'value': 'D', 'text': 'put down', 'content': 'put down'}]
        elif so == 19:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'limited', 'content': 'limited'},
                            {'key': 'B', 'value': 'B', 'text': 'subjected', 'content': 'subjected'},
                            {'key': 'C', 'value': 'C', 'text': 'converted', 'content': 'converted'},
                            {'key': 'D', 'value': 'D', 'text': 'directed', 'content': 'directed'}]
    save_exam(path, d)
    print("  -> 2008 ky1 Cloze options cleaned.")

    # 2009 ky1: 9369aa41-c91e-548c-bf99-1ad46a07ac25
    d, path = load_exam("9369aa41-c91e-548c-bf99-1ad46a07ac25")
    for q in d['questions']:
        so = q.get('sort_order')
        if so == 2:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'tended', 'content': 'tended'},
                            {'key': 'B', 'value': 'B', 'text': 'feared', 'content': 'feared'},
                            {'key': 'C', 'value': 'C', 'text': 'happened', 'content': 'happened'},
                            {'key': 'D', 'value': 'D', 'text': 'threatened', 'content': 'threatened'}]
        elif so == 13:
            q['options'] = [{'key': 'A', 'value': 'A', 'text': 'agree', 'content': 'agree'},
                            {'key': 'B', 'value': 'B', 'text': 'belong', 'content': 'belong'},
                            {'key': 'C', 'value': 'C', 'text': 'refer', 'content': 'refer'},
                            {'key': 'D', 'value': 'D', 'text': 'apply', 'content': 'apply'}]
    save_exam(path, d)
    print("  -> 2009 ky1 Cloze options cleaned.")

    # 15. Universal Schema Normalization Across All 41 Exams
    print("\n--- 15. Universal Standardization across ALL 41 Exams ---")
    all_files = [f for f in os.listdir(EXAMS_DIR) if f.endswith('.json')]
    for fname in all_files:
        fpath = os.path.join(EXAMS_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Standardize passage metadata if missing
        passages = data.get('passages', [])
        for idx, p in enumerate(passages):
            if p.get('type') is None:
                p['type'] = 'cloze' if idx == 0 else ('reading' if idx < 5 else 'reading_part_b')
            if p.get('passage_number') is None:
                p['passage_number'] = 1 if idx == 0 else (idx if idx < 5 else 5)
        
        # Standardize questions
        for q in data.get('questions', []):
            if q.get('question_number') is None:
                q['question_number'] = q.get('sort_order')
            if 'options' in q and isinstance(q['options'], list):
                q['options'] = clean_option_schema(q['options'])
        
        save_exam(fpath, data)

    print("\n=== All 41 Exams Successfully Calibrated and Standardized! ===")

if __name__ == '__main__':
    run_all_fixes()
