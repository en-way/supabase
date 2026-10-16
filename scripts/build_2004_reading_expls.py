import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

content = open('scratch_2004_clean_decoded.txt', encoding='utf-8').read()

def clean_chinese_text(text):
    # Fix cipher remnants
    text = re.sub(r'Me([A-D])o', r'[\1] ', text)
    text = re.sub(r'e([A-D])o', r'[\1]', text)
    text = re.sub(r'e([A-D])\b', r'[\1]', text)
    
    # Specific proper names
    text = text.replace('Zedmon', 'Redmon')
    text = text.replace('Zavitch', 'Ravitch')
    text = text.replace('‘odiac', 'Zodiac')
    text = text.replace('‘o.‘ysman', 'Zoe Zysman')
    text = text.replace('‘ysman', 'Zysman')
    text = text.replace('CareerSitevs', "CareerSite's")
    text = text.replace('Careerbuildervs', "CareerBuilder's")
    text = text.replace('sitevs', "site's")
    text = text.replace('therevs', "there's")
    text = text.replace('Itvs', "It's")
    text = text.replace('arenvt', "aren't")
    text = text.replace('isnvt', "isn't")
    text = text.replace('donvt', "don't")
    text = text.replace('wouldnvt', "wouldn't")
    text = text.replace('couldnvt', "couldn't")
    text = text.replace('worldvs', "world's")
    text = text.replace('Bushvs', "Bush's")
    text = text.replace('Ravitchvs', "Ravitch's")
    text = text.replace('Hofstadtervs', "Hofstadter's")
    text = text.replace('Emersonvs', "Emerson's")
    text = text.replace('countryvs', "country's")
    text = text.replace('childrenvs', "children's")
    text = text.replace('Greenspanvs', "Greenspan's")
    text = text.replace('Manhattanvs', "Manhattan's")
    text = text.replace('Americavs', "America's")
    text = text.replace('Y30', '$30')
    text = text.replace('Y4million', '$4 million').replace('Y10million', '$10 million')
    text = text.replace('Y4 million', '$4 million').replace('Y10 million', '$10 million')
    
    # Section titles
    text = text.replace('MMn精准定位y', '【精准定位】\n')
    text = text.replace('n精准定位y', '【精准定位】\n')
    text = text.replace('MMn命题解密y', '\n【命题解密】\n')
    text = text.replace('n命题解密y', '\n【命题解密】\n')
    text = text.replace('MMn干扰设置y', '\n【干扰项分析】\n')
    text = text.replace('n干扰设置y', '\n【干扰项分析】\n')
    text = text.replace('MM参考答案a', '【参考答案】')
    text = text.replace('M全局真题精解M', '')
    text = text.replace('M真题精解M', '')

    lines = []
    for line in text.split('\n'):
        # Skip page markers
        if line.strip().startswith('<<<PAGE_') or (line.strip().isdigit() and len(line.strip()) <= 3):
            continue
        if any('\u4e00' <= c <= '\u9fff' for c in line):
            line = re.sub(r'([’\u4e00-\u9fff\)])y([’\u4e00-\u9fff\(])', r'\1，\2', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])y\s+', r'\1，', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])M\s*', r'\1。', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])n\s*', r'\1；', line)
            line = re.sub(r'([’\u4e00-\u9fff\)])c\s*', r'\1：', line)
            line = re.sub(r't([\u4e00-\u9fff])', r'（\1', line)
            line = re.sub(r'([\u4e00-\u9fff])h', r'\1）', line)
            line = re.sub(r'f([\u4e00-\u9fff\w\s\-\'\’]+)j', r'“\1”', line)
            if line.endswith('M'): line = line[:-1] + '。'
            if line.endswith('y'): line = line[:-1] + '，'
            if line.endswith('n'): line = line[:-1] + '；'
            if line.endswith('c'): line = line[:-1] + '：'
            if line.endswith('-'): line = line[:-1] + '？'
        lines.append(line)
    
    return '\n'.join(lines).strip()

q_ranges = {
    # Text 1:
    21: ('21.HowdidZedmonfindhisjob-', 'MMj aWiththousandsofcareer-relatedsiteson'),
    22: ('22.Whichofthefollowingcanbeadisadvantageof', '23.Theexpressionftipservicejt^ine3y[aragraph'),
    23: ('23.Theexpressionftipservicejt^ine3y[aragraph', 'iTheremaybemorematchesinthedatabasenjob'),
    24: ('24.Why does CareerSitevsagentoffereachjob', 'MMp aEventhosewhoarenvthuntingforjobsmay'),
    25: ('25.Whichofthefollowingistrueaccordingtothetext-', '2aYy4 姓氏字母排序歧视现象'),
    
    # Text 2:
    26: ('26.Whatdoestheauthorintendtoillustratewith', 'M M - a Thusthe Americanpresidentandvice-'),
    27: ('27.Whatcanweinferfromthefirstthree[aragraphs-', '30.Whichofthefollowingistrueaccordingtot'),
    28: ('28.The4thparagraphsuggeststhat', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
    29: ('29.Whatdoestheauthormeanby fmostpeopleare', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
    30: ('30.Whichofthefollowingistrueaccordingtothe', '2aYyH 美国经济的疲软没有引起消费者的恐慌'),
    
    # Text 3:
    31: ('31.By fEllenSperoisnvtbitinghernailsjustyetj', 'M M j aEvenbefore Alan Greenspanvsadmission'),
    32: ('32.Howdothepublicfeelaboutthecurrenteco-', '33.WhenmentioningftheY4millionto Y10mil-'),
    33: ('33.WhenmentioningftheY4millionto Y10mil-', 'MMv aManyfolksseertuwajutetecr'),
    34: ('34.Whycanmanypeopleseefsilverliningsjtothe', '35.Towhichofthefollowingistheauthorlikelytoagree-'),
    35: ('35.Towhichofthefollowingistheauthorlikelytoagree-', '2aYy7 美国学校轻视才智'),
    
    # Text 4:
    36: ('36.WhatdoAmericanparentsexpecttheirchildren', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
    37: ('37.WecanlearnfromthetextthatAmericanshave', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
    38: ('38.TheviewsofZavitchandEmersononschooling', '40.Whatdoestheauthorthinkofintellect-'),
    39: ('39.Emersonyaccordingtothetextyisprobably', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
    40: ('40.Whatdoestheauthorthinkofintellect-', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
}

expl_dict = {}
for q, (start_str, end_str) in q_ranges.items():
    pos_start = content.find(start_str)
    if pos_start == -1:
        print(f"ERROR: cannot find start of Q{q}: {start_str}")
        continue
    pos_end = content.find(end_str, pos_start + 10)
    if pos_end == -1:
        print(f"ERROR: cannot find end of Q{q}: {end_str}")
        continue
    raw_chunk = content[pos_start:pos_end].strip()
    cleaned = clean_chinese_text(raw_chunk)
    # Ensure it starts with "q. "
    if not cleaned.startswith(f"{q}."):
        cleaned = f"{q}. " + cleaned
    expl_dict[q] = cleaned
    print(f"Extracted Q{q}: len={len(cleaned)}")

with open("scratch_2004_reading_expls_clean.json", "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in expl_dict.items()}, f, ensure_ascii=False, indent=2)

print("Saved all 20 questions to scratch_2004_reading_expls_clean.json!")
