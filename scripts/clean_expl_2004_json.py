import json
import re

with open("scripts/expl_2004.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for k, text in d.items():
    # Remove standalone page numbers or stray lines
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    # Fix option collocations
    text = text.replace('pointttoh', 'point (to)').replace('leadttoh', 'lead (to)')
    text = text.replace('comettoh', 'come (to)').replace('amountttoh', 'amount (to)')
    text = text.replace('actingtonh', 'acting (on)').replace('relyingtonh', 'relying (on)')
    text = text.replace('centeringtonh', 'centering (on)').replace('commentingtonh', 'commenting (on)')
    text = text.replace('interactiontwithh', 'interaction (with)').replace('assimilationtintoh', 'assimilation (into)')
    text = text.replace('cooperationtwithh', 'cooperation (with)').replace('consultationtwithh', 'consultation (with)')
    text = text.replace('tinhreturntforh', 'in return (for)').replace('tinhreplyttoh', 'in reply (to)')
    text = text.replace('tinhreferencettoh', 'in reference (to)').replace('tinhresponsettoh', 'in response (to)')
    text = text.replace('immunettoh', 'immune (to)').replace('resistantttoh', 'resistant (to)')
    text = text.replace('sensitivettoh', 'sensitive (to)').replace('subjectttoh', 'subject (to)')
    text = text.replace('tinhcase', 'in case').replace('tinhshort', 'in short')
    text = text.replace('tinhturn', 'in turn').replace('tinhessence', 'in essence')
    text = text.replace('incidencetofh', 'incidence (of)').replace('awarenesstofh', 'awareness (of)')
    text = text.replace('exposurettoh', 'exposure (to)')
    
    # Fix typos in English words caused by cipher:
    # '。anytheories' -> 'Many theories'
    # 'sugges(' -> 'suggest'
    # 'tha(' -> 'that'
    # 'fac(' -> 'fact'
    # '：hanges' -> 'changes'
    # 'o；' -> 'on'
    # 'focusingo；' -> 'focusing on'
    text = text.replace('。anytheories', 'Many theories')
    text = text.replace('sugges(', 'suggest').replace('tha(', 'that').replace('fac(', 'fact')
    text = text.replace('：hanges', 'changes').replace('o；', 'on').replace('focusingo；', 'focusing on')
    text = text.replace('centeron', 'center on')
    text = re.sub(r't([a-zA-Z\s\-\.\']+)h', r'(\1)', text)
    text = text.replace('f', '“').replace('j', '”')
    text = text.replace('“orlackof', 'for lack of')
    text = text.replace('“act', 'fact')
    text = text.replace('“or', 'for')
    text = text.replace('o句', '末句').replace('e句', '本句').replace('t句', '本句').replace('y句', '该句').replace('n句', '该句')
    d[k] = text.strip()

with open("scripts/expl_2004.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Finished post-cleaning expl_2004.json!")
