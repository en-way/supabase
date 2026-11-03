import json
import glob
import re
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Real valid long English words to exclude from "glued" flag
REAL_WORDS = {
    'interdisciplinary', 'hospitalizations', 'antidiscrimination', 
    'unrepresentative', 'unsubstantiated', 'characteristics',
    'correspondingly', 'differentiation', 'telecommunications',
    'institutionalized', 'misunderstandings', 'environmentalist',
    'straightforward', 'unprecedentedly', 'confrontational',
    'counterproductive', 'distinguishable', 'instrumentation',
    'disproportionate', 'electrochemical', 'industrialization',
    'enthusiastically', 'congratulations', 'inappropriately'
}

exams = sorted(glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json'))

for p in exams:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    title = d.get('title', '')
    if '英语（二）' not in title and '英语二' not in title:
        continue
    year = d.get('exam', {}).get('year', 'Unknown')
    exam_id = d.get('exam', {}).get('id')
    
    found_glued = []
    found_trailing_nums = []
    found_dividers = []
    found_shi = []

    for q in d.get('questions', []):
        q_num = q.get('question_number')
        expl = q.get('explanation', '')
        
        if '====' in expl:
            found_dividers.append((q_num, '===='))
            
        # Glued tokens
        words = re.findall(r'[A-Za-z]{14,}', expl)
        suspicious = [w for w in words if w.lower() not in REAL_WORDS]
        if suspicious:
            found_glued.append((q_num, suspicious))
            
        # Standalone trailing page numbers
        lines = [l.strip() for l in expl.strip().split('\n') if l.strip()]
        if lines and re.fullmatch(r'\d{1,3}', lines[-1]):
            found_trailing_nums.append((q_num, lines[-1]))
            
        if '十' in expl:
            for m in re.finditer(r'[\u4e00-\u9fa5]十[\u4e00-\u9fa5]', expl):
                s = m.group(0)
                if not any(num in s for num in '一二三四五六七八九十百千万'):
                    found_shi.append((q_num, s))

    if found_glued or found_trailing_nums or found_dividers or found_shi:
        print(f"================ {year} (Exam ID: {exam_id}) ================")
        if found_dividers:
            print(f"  Dividers: {found_dividers}")
        if found_trailing_nums:
            print(f"  Trailing page numbers: {found_trailing_nums}")
        if found_shi:
            print(f"  '十' as '+': {found_shi}")
        if found_glued:
            print(f"  Glued phrases ({len(found_glued)} questions):")
            for qn, ws in found_glued:
                print(f"    Q{qn}: {ws}")
