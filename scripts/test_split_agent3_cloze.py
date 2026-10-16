import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'C:/Users/57867/.gemini/antigravity/brain/bff42094-214a-421b-9c4b-ebcabd69b641/scratch'

for y in [2011, 2012, 2013, 2014, 2015]:
    fp = os.path.join(p, f'{y}_cloze_raw_pdf.txt')
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find where explanation begins (after "总体分析" and passage reading)
    # Usually around "试题精解" or "•真题精解•"
    pos = text.find('试题精解')
    if pos != -1:
        text = text[pos:]

    # Let's see how question numbers are represented
    # Pattern: a number 1..20 at the beginning of a line or after newline
    # Often like: "1.\n［考点提炼］" or "1. [A] ... \n［考点提炼］"
    lines = text.split('\n')
    questions = {}
    current_q = None
    buf = []

    for line in lines:
        m = re.match(r'^\s*(\d{1,2})\s*[\.、]\s*(?:\[[A-D]\]|[A-D]|\s*)*', line)
        # Check if this line is a question header and followed by 考点 or has options
        # Note: question numbers must be 1 to 20
        if m:
            num = int(m.group(1))
            if 1 <= num <= 20:
                # If we already have this question and the new one has 考点, or if it's the next question
                if current_q is not None:
                    questions[current_q] = '\n'.join(buf).strip()
                current_q = num
                buf = [line]
                continue
        if current_q is not None:
            # Stop if we hit Reading section
            if any(k in line for k in ['Section II', 'Reading Comprehension', '语篇分析及试题精解']):
                break
            buf.append(line)

    if current_q is not None:
        questions[current_q] = '\n'.join(buf).strip()

    print(f'Year {y}: found {len(questions)}/20 questions')
    missing = [i for i in range(1, 21) if i not in questions]
    if missing:
        print(f'  Missing: {missing}')
    else:
        # Check lengths
        min_len = min(len(q) for q in questions.values())
        print(f'  All 20 present! Min length: {min_len}')
