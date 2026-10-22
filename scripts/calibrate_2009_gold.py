# -*- coding: utf-8 -*-
"""
calibrate_2009_gold.py
Round 51: Golden Forensic Calibration for 2009 English (I)
Exam UUID: 9369aa41-c91e-548c-bf99-1ad46a07ac25
"""

import sys
import json
import os
import re

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops
from prepare_2009_cloze_gold import CLOZE_DATA

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = 'public/data/exams/9369aa41-c91e-548c-bf99-1ad46a07ac25.json'

print("=== Starting 2009 ky1 Golden Calibration ===")

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

# 1. Update Exam Meta
if 'exam' not in local_data:
    local_data['exam'] = {}
local_data['exam']['title'] = "2009年全国硕士研究生入学统一考试英语（一）真题"
local_data['exam']['id'] = "9369aa41-c91e-548c-bf99-1ad46a07ac25"
local_data['exam']['category_id'] = "ky1"
local_data['exam']['year'] = 2009
local_data['exam']['exam_type'] = "real"
local_data['exam']['total_score'] = 60
local_data['exam']['pass_score'] = 36
local_data['title'] = local_data['exam']['title']
local_data['id'] = local_data['exam']['id']
local_data['year'] = 2009

print(f"Exam Meta Calibrated: {local_data['exam']['title']}")

# 2. Fetch DB questions & passages to get canonical data
db_questions = db_ops.run_sql("""
    select q.id, q.sort_order, q.passage_id, q.stem, q.options, q.correct_answer, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
    where e.year = 2009 and e.category_id = 'ky1'
    order by q.sort_order;
""")
db_q_map = {q['sort_order']: q for q in db_questions}
print(f"Fetched {len(db_questions)} DB questions.")

db_passages = db_ops.run_sql("""
    select p.id, p.title, p.section_type, p.content
    from passages p
    join exams e on p.exam_id = e.id
    where e.year = 2009 and e.category_id = 'ky1'
    order by p.id;
""")
db_p_map = {p['id']: p for p in db_passages}
print(f"Fetched {len(db_passages)} DB passages.")

# 3. Calibrate Passages
passage_meta = [
    {"type": "cloze", "passage_number": 1, "title": "Section I: Use of English"},
    {"type": "reading", "passage_number": 1, "title": "Section II: Reading Comprehension Part A - Text 1"},
    {"type": "reading", "passage_number": 2, "title": "Section II: Reading Comprehension Part A - Text 2"},
    {"type": "reading", "passage_number": 3, "title": "Section II: Reading Comprehension Part A - Text 3"},
    {"type": "reading", "passage_number": 4, "title": "Section II: Reading Comprehension Part A - Text 4"},
    {"type": "reading_part_b", "passage_number": 5, "title": "Section II: Reading Comprehension Part B"}
]

for i, p in enumerate(local_data.get('passages', [])):
    meta = passage_meta[i]
    p['type'] = meta['type']
    p['passage_number'] = meta['passage_number']
    p['title'] = meta['title']
    print(f"Passage {i} calibrated: id={p['id']} type={p['type']} num={p['passage_number']}")

# 4. Read Subagent Q29 and Q30 Gold data
with open('scripts/round51_subagent_q29_30.txt', 'r', encoding='utf-8') as f:
    subagent_text = f.read()

# 5. Calibrate Questions Q1-Q45
local_questions = local_data.get('questions', [])
if len(local_questions) != 45:
    raise ValueError(f"Expected 45 questions, found {len(local_questions)}")

calibrated_questions = []

for idx, lq in enumerate(local_questions):
    q_num = idx + 1
    db_q = db_q_map.get(q_num)
    
    qid = lq.get('id') or db_q['id']
    pid = lq.get('passage_id') or db_q['passage_id']
    
    cq = {
        "id": qid,
        "question_number": q_num,
        "sort_order": q_num,
        "passage_id": pid,
        "category_id": "ky1",
        "year": 2009
    }
    
    if 1 <= q_num <= 20:
        gold = CLOZE_DATA[q_num]
        cq["prompt"] = f"Choose the best option for blank [{q_num}] in the passage:"
        cq["stem"] = cq["prompt"]
        cq["options"] = gold["options"]
        cq["answer"] = gold["answer"]
        cq["correct_answer"] = gold["answer"]
        cq["explanation"] = gold["explanation"].strip()
        
    elif 21 <= q_num <= 40:
        db_stem = db_q['stem'].strip()
        # Ensure trailing underline and period
        if q_num == 29:
            db_stem = "In the last paragraph, a problem commercial genetic testing faces is ________."
        elif q_num == 30:
            db_stem = "An appropriate title for the text is most likely to be ________."
        elif not db_stem.endswith('.') and not db_stem.endswith('?'):
            if db_stem.endswith('________'):
                db_stem = db_stem + '.'
            else:
                db_stem = db_stem + ' ________.'
                
        cq["prompt"] = db_stem
        cq["stem"] = db_stem
        
        # Options
        db_opts = db_q['options']
        if isinstance(db_opts, str):
            db_opts = json.loads(db_opts)
        
        if q_num == 29:
            db_opts = [
                {"key": "A", "text": "disorganized data collection", "value": "A"},
                {"key": "B", "text": "overlapping database building", "value": "B"},
                {"key": "C", "text": "excessive sample comparison", "value": "C"},
                {"key": "D", "text": "lack of patent evaluation", "value": "D"}
            ]
        elif q_num == 30:
            db_opts = [
                {"key": "A", "text": "Fors and Againsts of DNA Testing", "value": "A"},
                {"key": "B", "text": "DNA Testing and Its Problems", "value": "B"},
                {"key": "C", "text": "DNA Testing Outside the Lab", "value": "C"},
                {"key": "D", "text": "Lies Behind DNA Testing", "value": "D"}
            ]
        cq["options"] = db_opts
        
        # Answer
        cq["answer"] = db_q['correct_answer']
        cq["correct_answer"] = db_q['correct_answer']
        
        # Explanation
        if q_num == 29:
            cq["explanation"] = """［精准定位］末段②句指出，商业基因检测公司使用的数据库并未系统地收集数据，而是将多个研究项目的信息混杂在一起。[A]为正确选项。

［命题解密］正确项[A] disorganized data collection 是第六段②句 don’t rely on data collected systematically but rather lump together information 的同义替换。
[B]将③句 have a lot of data from some regions and not others“数据地区来源不均衡”曲解为“数据重复(overlapping)”。[C]取段中 sample, compared, a lot of data 碎片化信息捏造出“样本比对过多(excessive sample comparison)”。[D]将④句“基因检测计算机程序申请专利且不接受外界评估(the computer programs... may be patented and not subject to... outside evaluation)”偷换为“缺乏专利评估(lack of patent evaluation)”。

［技巧总结］本题形似考查综合性事实细节，实对段中既体现段落主旨又集词汇、语法难点于一身的长难句②句设题。解题时重在借助逻辑连接词、近义/同义复现、特殊句式结构等找到全段语义重心，并根据特殊句式或逻辑连接词推断难点词汇之意。具体思路：借助关联词 In addition 可将段落分为前后两部分；再借近义/同义复现 reference collections、Databases、DNA database 推知前部分落脚点在“数据库”，由此可基本确定数据库为主要批判点(重心即考点)，从而锁定均关乎数据库的[A] disorganized(源自②句 don’t rely on data collected systematically but rather lump together information from different research projects)、[B] overlapping(源于③句 have a lot of data from some regions and not others)；最后借助取舍结构 not A but rather B(不是 A 而是 B)、from A and not B(来自 A 而不是 B)可知两句语义重心在“信息收集不系统(也即 lump together 之意)、地域分布不均”问题上，只有[A]符合要求。""".strip()
        elif q_num == 30:
            cq["explanation"] = """［精准定位］文首两段引出 DNA 检测；中间两段介绍 DNA 检测的用途及条件；末两段分析指出 DNA 检测的问题。[B]最切合文意。

［命题解密］正确项[B]是对全篇全部内容的覆盖，又明确了文章论述的对象。
[A]中 Fors 源自第三段 Among the most popular、the latest rage among passionate genealogists(最流行的有……、最近在狂热系谱学家中……)等内容而来，令学生可能产生作者在讲述“DNA 检测的优点”的错觉，而那只是对 DNA 检测的客观介绍，并非意指其“好的方面”。[C]将第二段“available without prescriptions、over-the-counter(无需处方即可获得)”视为“DNA Testing Outside the Lab(实验室外的 DNA 检测)”，而商业基因检测并非就是实验室外的基因检测。[D]根据第五段 skeptical、false precision(怀疑的、伪精确性)等内容而来，但文意旨在“揭示 DNA 检测只能揭示一两位祖先信息，精确性有待提高”，而选项中 Lies(谎言)贬义色彩过重，而且该选项没有涵盖前四段对 DNA testing 的介绍。

［技巧总结］命题点通常依全篇布局均匀分布，因此纵观其他四道题题干以窥视全篇主旨内容不失为解答文章主旨题(标题题)的捷径。具体思路为：纵观其他四题，前两题针对首四段，考查 PTK(DNA检测一种)的特点、用途(availability、pricing, used to)；第三、四题针对末两段，考查 DNA 检测的弊端(fails, problem)；就此可见，文章对 DNA 检测的特点、用途及问题都做了诠释，[B]能涵盖这些信息。""".strip()
        else:
            cq["explanation"] = db_q['explanation'].strip()
            
    elif 41 <= q_num <= 45:
        cq["prompt"] = f"Choose the best paragraph [A]-[G] that fits into gap ({q_num}):"
        cq["stem"] = cq["prompt"]
        
        db_opts = db_q['options']
        if isinstance(db_opts, str):
            db_opts = json.loads(db_opts)
        cq["options"] = db_opts
        
        cq["answer"] = db_q['correct_answer']
        cq["correct_answer"] = db_q['correct_answer']
        
        raw_exp = db_q['explanation'] or ''
        # Cut leak in Q45 if present
        if q_num == 45:
            for cutoff in ['；守：', '广义的教育', '本文节选自']:
                if cutoff in raw_exp:
                    raw_exp = raw_exp.split(cutoff)[0]
        # Clean excessive blank lines
        clean_exp = re.sub(r'\n{3,}', '\n\n', raw_exp.strip())
        cq["explanation"] = clean_exp
        
    calibrated_questions.append(cq)

local_data['questions'] = calibrated_questions

# 6. Save calibrated JSON
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)

print(f"Successfully calibrated 2009 local JSON: {JSON_PATH}")
print(f"Total Passages: {len(local_data['passages'])}, Total Questions: {len(local_data['questions'])}")
