import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

raw = json.load(open('scratch_2004_reading_expls_raw.json', encoding='utf-8'))

def clean_expl(q_num, text):
    # Cut off subsequent paragraph texts or vocabulary sections
    # In HuangPiShu, a new paragraph analysis usually starts with lines like "MM...", "aaa...", or next question
    # Let's inspect where the explanation stops: after option explanations
    lines = text.split('\n')
    expl_lines = []
    
    stop_words = ['aaaaaa', 'M词汇注释', 'M语篇分析', '结构分析', '背景知识']
    for l in lines:
        if any(sw in l for sw in stop_words):
            break
        # also skip page headers/footers like '<<<PAGE_...' or lone numbers
        if l.strip().startswith('<<<PAGE_') or l.strip().isdigit():
            continue
        expl_lines.append(l)
    
    cleaned_text = '\n'.join(expl_lines)
    
    # Cipher fixes
    cleaned_text = re.sub(r'Me([A-D])o', r'[\1] ', cleaned_text)
    cleaned_text = re.sub(r'e([A-D])o', r'[\1]', cleaned_text)
    cleaned_text = re.sub(r'e([A-D])\b', r'[\1]', cleaned_text)
    
    # Specific proper names
    cleaned_text = cleaned_text.replace('Zedmon', 'Redmon')
    cleaned_text = cleaned_text.replace('Zavitch', 'Ravitch')
    cleaned_text = cleaned_text.replace('‘odiac', 'Zodiac')
    cleaned_text = cleaned_text.replace('‘o.‘ysman', 'Zoe Zysman')
    cleaned_text = cleaned_text.replace('‘ysman', 'Zysman')
    cleaned_text = cleaned_text.replace('CareerSitevs', "CareerSite's")
    cleaned_text = cleaned_text.replace('Careerbuildervs', "CareerBuilder's")
    cleaned_text = cleaned_text.replace('sitevs', "site's")
    cleaned_text = cleaned_text.replace('therevs', "there's")
    cleaned_text = cleaned_text.replace('Itvs', "It's")
    cleaned_text = cleaned_text.replace('arenvt', "aren't")
    cleaned_text = cleaned_text.replace('isnvt', "isn't")
    cleaned_text = cleaned_text.replace('donvt', "don't")
    cleaned_text = cleaned_text.replace('wouldnvt', "wouldn't")
    cleaned_text = cleaned_text.replace('couldnvt', "couldn't")
    cleaned_text = cleaned_text.replace('worldvs', "world's")
    cleaned_text = cleaned_text.replace('Bushvs', "Bush's")
    cleaned_text = cleaned_text.replace('Ravitchvs', "Ravitch's")
    cleaned_text = cleaned_text.replace('Hofstadtervs', "Hofstadter's")
    cleaned_text = cleaned_text.replace('Emersonvs', "Emerson's")
    cleaned_text = cleaned_text.replace('countryvs', "country's")
    cleaned_text = cleaned_text.replace('childrenvs', "children's")
    cleaned_text = cleaned_text.replace('Greenspanvs', "Greenspan's")
    cleaned_text = cleaned_text.replace('Manhattanvs', "Manhattan's")
    cleaned_text = cleaned_text.replace('Americavs', "America's")
    
    # Punctuation markers in Chinese sentences:
    # In the cipher, Chinese clauses often ended with 'y' (comma), 'M' (period), 'n' (semicolon), 't'/'h' (parentheses), 'c' (colon), 'f'/'j' (quotes), '-' (dash)
    # Be careful not to replace English letters inside English words!
    def fix_mixed_line(line):
        # If line contains Chinese, replace Chinese-context punctuation
        if any('\u4e00' <= c <= '\u9fff' for c in line):
            # Replace Chinese headers
            line = line.replace('MMn精准定位y', '【精准定位】\n')
            line = line.replace('n精准定位y', '【精准定位】\n')
            line = line.replace('MMn命题解密y', '\n【命题解密】\n')
            line = line.replace('n命题解密y', '\n【命题解密】\n')
            line = line.replace('MMn干扰设置y', '\n【干扰项分析】\n')
            line = line.replace('n干扰设置y', '\n【干扰项分析】\n')
            line = line.replace('MM参考答案a', '【参考答案】')
            line = line.replace('M全局真题精解M', '【全局真题精解】')
            line = line.replace('M真题精解M', '')
            
            # Punctuation replacements when adjacent to Chinese or at line ends
            line = re.sub(r'([’\u4e00-\u9fff\)])y([’\u4e00-\u9fff\(])', r'\1，\2', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])y\s+', r'\1，', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])M\s*', r'\1。', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])n\s*', r'\1；', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])c\s*', r'\1：', line)
            line = re.sub(r't([\u4e00-\u9fff])', r'（\1', line)
            line = re.sub(r'([\u4e00-\u9fff])h', r'\1）', line)
            line = re.sub(r'f([\u4e00-\u9fff\w\s\-\'\’]+)j', r'“\1”', line)
            # Trailing M, y, n, -
            if line.endswith('M'): line = line[:-1] + '。'
            if line.endswith('y'): line = line[:-1] + '，'
            if line.endswith('n'): line = line[:-1] + '；'
            if line.endswith('c'): line = line[:-1] + '：'
            if line.endswith('-'): line = line[:-1] + '？'
        return line

    fixed_lines = [fix_mixed_line(l) for l in cleaned_text.split('\n')]
    final_text = '\n'.join(fixed_lines).strip()
    return final_text

for q in range(21, 41):
    cleaned = clean_expl(q, raw[str(q)])
    print(f"=== Q{q} (len={len(cleaned)}) ===")
    lines = cleaned.split('\n')
    for l in lines[:8]:
        print("  ", l)
    if len(lines) > 8:
        print("   ...")
        for l in lines[-3:]:
            print("  ", l)
