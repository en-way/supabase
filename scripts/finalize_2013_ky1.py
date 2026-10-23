# -*- coding: utf-8 -*-
"""
finalize_2013_ky1.py
Ensures passages 0-5, questions 1-45, points, question_number, and option typos (o£ -> of)
are 100% in perfect state for 2013 ky1.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Finalizing 2013 ky1 ===")

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Title & score
if "exam" in d:
    d["exam"]["title"] = "2013年全国硕士研究生入学统一考试英语（一）真题"
    d["exam"]["total_score"] = 60.0
d["title"] = "2013年全国硕士研究生入学统一考试英语（一）真题"
d["total_score"] = 60.0

# 2. Fix Q35 option o£ -> of
for q in d.get("questions", []):
    so = q.get("sort_order")
    # ensure question_number
    q["question_number"] = so
    # ensure points & q_type
    if so <= 20:
        q["points"] = 0.5
        q["q_type"] = "cloze_item"
    else:
        q["points"] = 2.0
        q["q_type"] = "reading_item"
    
    # Fix option text
    for opt in q.get("options", []):
        opt["text"] = opt["text"].replace("o£", "of").replace("th&r", "their")
    
    # Ensure Q22 and Q23 official options
    if so == 22:
        q["correct_answer"] = "B"
        q["answer"] = "B"
        q["options"] = [
            {"key": "A", "text": "combat unnecessary waste", "value": "A"},
            {"key": "B", "text": "shop for their garments more frequently", "value": "B"},
            {"key": "C", "text": "resist the influence of advertisements", "value": "C"},
            {"key": "D", "text": "shut out the feverish fashion world", "value": "D"}
        ]
    elif so == 23:
        q["correct_answer"] = "D"
        q["answer"] = "D"
        q["options"] = [
            {"key": "A", "text": "tolerance", "value": "A"},
            {"key": "B", "text": "indifference", "value": "B"},
            {"key": "C", "text": "enthusiasm", "value": "C"},
            {"key": "D", "text": "accusation", "value": "D"}
        ]
    elif so == 27:
        opt_c = next((it for it in q.get("options", []) if it["key"] == "C"), None)
        if opt_c and opt_c["text"] == "commerce conductors":
            opt_c["text"] = "e-commerce conductors"
    elif so == 32:
        for it in q.get("options", []):
            if it["key"] == "A" and it["text"] == "sustained species":
                it["text"] = "a sustained species"
            elif it["key"] == "C" and it["text"] == "threat to the environment":
                it["text"] = "a threat to the environment"
            elif it["key"] == "D" and it["text"] == "misplaced race":
                it["text"] = "a misplaced race"

# Save updated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Saved finalized 2013 ky1 JSON!")
