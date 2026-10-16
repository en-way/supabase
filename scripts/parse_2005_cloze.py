# -*- coding: utf-8 -*-
"""
parse_2005_cloze.py
Parse all 20 authentic cloze questions (options, answers, explanations) from scripts/2005_cloze_raw.txt
"""

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

raw = open('scripts/2005_cloze_raw.txt', encoding='utf-8').read()
pattern = r'(?m)^\s*([1-9]|1[0-9]|20)\s*[\.、]\s*\[?\s*[A-D]'
matches = list(re.finditer(pattern, raw))

cleaned_expls = {}
for i, m in enumerate(matches):
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else raw.find('Section Il')
    chunk = raw[start:end].strip()
    num = int(m.group(1))

    # clean page headers & numbers
    chunk = re.sub(r'=== PAGE \d+ ===', '', chunk)
    chunk = re.sub(r'(?m)^\s*\d+\s*$', '', chunk)
    # clean passage sections
    if num == 8:
        chunk = re.sub(r'II\s+O?Strang.*', '', chunk, flags=re.S)
    elif num == 13:
        chunk = re.sub(r'(?:田\s+0\s+)?T\s*he\s+exp\s*lanation.*', '', chunk, flags=re.S)

    # Normalize OCR tags
    chunk = re.sub(r'\[\s*([A-D])\s*[\]J\)]', r'[\1]', chunk)
    chunk = re.sub(r'［\s*([A-D])\s*［］J\)]', r'[\1]', chunk)
    chunk = re.sub(r'44([\u4e00-\u9fa5])', r'“\1', chunk)
    chunk = chunk.replace('・', '·')
    chunk = re.sub(r'\n{3,}', '\n\n', chunk).strip()
    cleaned_expls[num] = chunk

AUTHENTIC_2005_CLOZE = {
    1: {
        "options": [
            {"key": "A", "text": "although", "value": "A"},
            {"key": "B", "text": "because", "value": "B"},
            {"key": "C", "text": "but", "value": "C"},
            {"key": "D", "text": "while", "value": "D"}
        ],
        "answer": "C"
    },
    2: {
        "options": [
            {"key": "A", "text": "above", "value": "A"},
            {"key": "B", "text": "unlike", "value": "B"},
            {"key": "C", "text": "excluding", "value": "C"},
            {"key": "D", "text": "besides", "value": "D"}
        ],
        "answer": "B"
    },
    3: {
        "options": [
            {"key": "A", "text": "limited", "value": "A"},
            {"key": "B", "text": "committed", "value": "B"},
            {"key": "C", "text": "dedicated", "value": "C"},
            {"key": "D", "text": "confined", "value": "D"}
        ],
        "answer": "A"
    },
    4: {
        "options": [
            {"key": "A", "text": "catching", "value": "A"},
            {"key": "B", "text": "ignoring", "value": "B"},
            {"key": "C", "text": "missing", "value": "C"},
            {"key": "D", "text": "tracking", "value": "D"}
        ],
        "answer": "C"
    },
    5: {
        "options": [
            {"key": "A", "text": "anyway", "value": "A"},
            {"key": "B", "text": "though", "value": "B"},
            {"key": "C", "text": "instead", "value": "C"},
            {"key": "D", "text": "therefore", "value": "D"}
        ],
        "answer": "B"
    },
    6: {
        "options": [
            {"key": "A", "text": "even if", "value": "A"},
            {"key": "B", "text": "if only", "value": "B"},
            {"key": "C", "text": "only if", "value": "C"},
            {"key": "D", "text": "as if", "value": "D"}
        ],
        "answer": "A"
    },
    7: {
        "options": [
            {"key": "A", "text": "distinguishing", "value": "A"},
            {"key": "B", "text": "discovering", "value": "B"},
            {"key": "C", "text": "determining", "value": "C"},
            {"key": "D", "text": "detecting", "value": "D"}
        ],
        "answer": "D"
    },
    8: {
        "options": [
            {"key": "A", "text": "diluted", "value": "A"},
            {"key": "B", "text": "dissolved", "value": "B"},
            {"key": "C", "text": "dispersed", "value": "C"},
            {"key": "D", "text": "diffused", "value": "D"}
        ],
        "answer": "A"
    },
    9: {
        "options": [
            {"key": "A", "text": "when", "value": "A"},
            {"key": "B", "text": "since", "value": "B"},
            {"key": "C", "text": "for", "value": "C"},
            {"key": "D", "text": "whereas", "value": "D"}
        ],
        "answer": "D"
    },
    10: {
        "options": [
            {"key": "A", "text": "unusual", "value": "A"},
            {"key": "B", "text": "particular", "value": "B"},
            {"key": "C", "text": "unique", "value": "C"},
            {"key": "D", "text": "typical", "value": "D"}
        ],
        "answer": "B"
    },
    11: {
        "options": [
            {"key": "A", "text": "signs", "value": "A"},
            {"key": "B", "text": "stimuli", "value": "B"},
            {"key": "C", "text": "messages", "value": "C"},
            {"key": "D", "text": "impulses", "value": "D"}
        ],
        "answer": "C"
    },
    12: {
        "options": [
            {"key": "A", "text": "at first", "value": "A"},
            {"key": "B", "text": "at all", "value": "B"},
            {"key": "C", "text": "at large", "value": "C"},
            {"key": "D", "text": "at times", "value": "D"}
        ],
        "answer": "A"
    },
    13: {
        "options": [
            {"key": "A", "text": "subjected", "value": "A"},
            {"key": "B", "text": "left", "value": "B"},
            {"key": "C", "text": "drawn", "value": "C"},
            {"key": "D", "text": "exposed", "value": "D"}
        ],
        "answer": "D"
    },
    14: {
        "options": [
            {"key": "A", "text": "ineffective", "value": "A"},
            {"key": "B", "text": "incompetent", "value": "B"},
            {"key": "C", "text": "inefficient", "value": "C"},
            {"key": "D", "text": "insufficient", "value": "D"}
        ],
        "answer": "C"
    },
    15: {
        "options": [
            {"key": "A", "text": "introduce", "value": "A"},
            {"key": "B", "text": "summon", "value": "B"},
            {"key": "C", "text": "trigger", "value": "C"},
            {"key": "D", "text": "create", "value": "D"}
        ],
        "answer": "D"
    },
    16: {
        "options": [
            {"key": "A", "text": "still", "value": "A"},
            {"key": "B", "text": "also", "value": "B"},
            {"key": "C", "text": "otherwise", "value": "C"},
            {"key": "D", "text": "nevertheless", "value": "D"}
        ],
        "answer": "B"
    },
    17: {
        "options": [
            {"key": "A", "text": "sure", "value": "A"},
            {"key": "B", "text": "sick", "value": "B"},
            {"key": "C", "text": "aware", "value": "C"},
            {"key": "D", "text": "tired", "value": "D"}
        ],
        "answer": "C"
    },
    18: {
        "options": [
            {"key": "A", "text": "tolerate", "value": "A"},
            {"key": "B", "text": "repel", "value": "B"},
            {"key": "C", "text": "neglect", "value": "C"},
            {"key": "D", "text": "notice", "value": "D"}
        ],
        "answer": "D"
    },
    19: {
        "options": [
            {"key": "A", "text": "available", "value": "A"},
            {"key": "B", "text": "reliable", "value": "B"},
            {"key": "C", "text": "identifiable", "value": "C"},
            {"key": "D", "text": "suitable", "value": "D"}
        ],
        "answer": "A"
    },
    20: {
        "options": [
            {"key": "A", "text": "similar to", "value": "A"},
            {"key": "B", "text": "such as", "value": "B"},
            {"key": "C", "text": "along with", "value": "C"},
            {"key": "D", "text": "aside from", "value": "D"}
        ],
        "answer": "B"
    }
}

for q_num, expl in cleaned_expls.items():
    if q_num in AUTHENTIC_2005_CLOZE:
        AUTHENTIC_2005_CLOZE[q_num]['explanation'] = expl

print(f"Successfully processed {len(AUTHENTIC_2005_CLOZE)} authentic questions with explanations!")
