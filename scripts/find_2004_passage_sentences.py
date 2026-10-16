import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for the English sentences of the passage
# P1: Many theories concerning the causes of juvenile delinquency...
# P2: Most theories of juvenile delinquency have focused on children from disadvantaged families...
# P3: Changes in the social structure may also...
# P4: Families have also experienced changes...
# P5: Other identifiable causes of offensive acts...

lines = text.split('\n')
passage_lines = []
capturing = False

for l in lines:
    if 'Manythe M orahisecutrf' in l or 'Manytheories' in l or 'causesofju' in l:
        capturing = True
    if capturing:
        passage_lines.append(l)
    if '4444444444' in l or '<<<PAGE_15>>>' in l:
        if len(passage_lines) > 200:
            break

print("Collected lines:", len(passage_lines))
for pl in passage_lines[:60]:
    if any(k in pl for k in ['Many', 'theories', 'Theories', 'children', 'social', 'family', 'Families', 'structure', 'delinquency']):
        print(" ", pl)
