import json
import re

with open("scripts/expl_2004.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for k, text in d.items():
    # Fix English words corrupted by “/” replacement
    text = text.replace('“ocus', 'focus').replace('“ewer', 'fewer').replace('“or', 'for').replace('“act', 'fact')
    text = text.replace('“ailure', 'failure').replace('“amily', 'family').replace('“rom', 'from')
    text = text.replace('“orm', 'form').replace('“irst', 'first').replace('“ound', 'found')
    text = text.replace('“ield', 'field').replace('“ull', 'full').replace('“actor', 'factor')
    text = text.replace('“eel', 'feel').replace('“unction', 'function')
    text = text.replace('“ree', 'free').replace('“requent', 'frequent')
    text = text.replace('“ast', 'fast').replace('“uture', 'future')
    text = text.replace('“ood', 'food').replace('“ace', 'face')
    text = text.replace('“ive', 'five').replace('“our', 'four')
    text = text.replace('“ine', 'fine').replace('“ew', 'few')
    text = text.replace('“ellow', 'fellow').replace('“low', 'flow')
    text = text.replace('“riend', 'friend').replace('“ront', 'front')
    text = text.replace('“orce', 'force').replace('“ear', 'fear')
    text = text.replace('“avor', 'favor').replace('“all', 'fall')
    text = text.replace('“ollow', 'follow').replace('“ormer', 'former')
    text = text.replace('“orth', 'forth').replace('“ormat', 'format')
    text = text.replace('al(houg)', 'although').replace('al(houg', 'although')
    text = text.replace('”ob', 'job').replace('”ust', 'just').replace('”oin', 'join')
    text = text.replace('”uvenile', 'juvenile').replace('”udge', 'judge')
    text = text.replace('identi“iable', 'identifiable').replace('insu““iciently', 'insufficiently')
    text = text.replace('di““icult', 'difficult').replace('a““ect', 'affect')
    text = text.replace('e““ect', 'effect').replace('su““icient', 'sufficient')
    text = text.replace('o““', 'off').replace('o“', 'of')
    text = text.replace('su““er', 'suffer').replace('di““er', 'differ')
    text = text.replace('de“ine', 'define').replace('con“irm', 'confirm')
    text = text.replace('in“luence', 'influence')
    d[k] = text

with open("scripts/expl_2004.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Finished fixing words in expl_2004.json!")
