import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

cloze_text = text.split("<<<PAGE_15>>>")[0]

official_q_data = [
    (1, "C", [("A", "acting"), ("B", "relying"), ("C", "centering"), ("D", "commenting")]),
    (2, "D", [("A", "before"), ("B", "unless"), ("C", "until"), ("D", "because")]),
    (3, "A", [("A", "interaction"), ("B", "assimilation"), ("C", "cooperation"), ("D", "consultation")]),
    (4, "D", [("A", "in return"), ("B", "in reply"), ("C", "in reference"), ("D", "in response")]),
    (5, "A", [("A", "or"), ("B", "but rather"), ("C", "but"), ("D", "or else")]),
    (6, "B", [("A", "considering"), ("B", "ignoring"), ("C", "highlighting"), ("D", "discarding")]),
    (7, "C", [("A", "on"), ("B", "in"), ("C", "for"), ("D", "with")]),
    (8, "D", [("A", "immune"), ("B", "resistant"), ("C", "sensitive"), ("D", "subject")]),
    (9, "A", [("A", "affect"), ("B", "reduce"), ("C", "check"), ("D", "reflect")]),
    (10, "B", [("A", "point"), ("B", "lead"), ("C", "come"), ("D", "amount")]),
    (11, "A", [("A", "in general"), ("B", "on average"), ("C", "by contrast"), ("D", "at length")]),
    (12, "C", [("A", "in case"), ("B", "in short"), ("C", "in turn"), ("D", "in essence")]),
    (13, "D", [("A", "survived"), ("B", "noticed"), ("C", "undertaken"), ("D", "experienced")]),
    (14, "B", [("A", "contrarily"), ("B", "consequently"), ("C", "similarly"), ("D", "simultaneously")]),
    (15, "A", [("A", "than"), ("B", "that"), ("C", "which"), ("D", "as")]),
    (16, "B", [("A", "system"), ("B", "structure"), ("C", "concept"), ("D", "heritage")]),
    (17, "B", [("A", "assessable"), ("B", "identifiable"), ("C", "negligible"), ("D", "incredible")]),
    (18, "D", [("A", "expense"), ("B", "restriction"), ("C", "allocation"), ("D", "availability")]),
    (19, "A", [("A", "incidence"), ("B", "awareness"), ("C", "exposure"), ("D", "popularity")]),
    (20, "C", [("A", "provided"), ("B", "since"), ("C", "although"), ("D", "supposing")]),
]

def clean_expl(raw):
    # remove page markers
    raw = re.sub(r'<<<PAGE_\d+>>>', '', raw)
    # clean cipher characters
    raw = re.sub(r'e([A-D])o', r'[\1]', raw)
    raw = re.sub(r'e([A-D])', r'[\1]', raw)
    raw = raw.replace('M精准定位s', '【精准定位】').replace('n精准定位y', '【精准定位】\n')
    raw = raw.replace('M空格设置s', '【空格设置】').replace('n空格设置y', '【空格设置】\n')
    raw = raw.replace('M干扰设置s', '【干扰项设置】').replace('n干扰设置y', '【干扰项设置】\n')
    raw = raw.replace('M干扰项设置s', '【干扰项设置】').replace('Me干扰项设置o', '【干扰项设置】\n')
    raw = raw.replace('本题考核的知识点是c', '【考点提炼】').replace('本题考核的知识点是', '【考点提炼】')
    raw = raw.replace('M正确率c', ' 正确率：').replace('正确率c', '正确率：')
    # clean cipher punctuation
    # M -> 。 (when between sentences)
    # y -> ，
    # n -> ；
    # a -> 、
    # c -> ：
    # t -> （
    # h -> ）
    # f -> “
    # j -> ”
    # u -> ……
    # - -> ？
    # Notice: we should be careful with English words containing these characters!
    # Only replace when not inside an English word!
    # Let's inspect raw explanation for Q1 first.
    return raw

for q, ans, opts in official_q_data:
    next_q = q + 1 if q < 20 else 21
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*(.*?)(?=(?:\n\s*{next_q}\.\s*|<<<PAGE_15>>>|\Z))', cloze_text, re.DOTALL)
    if m:
        c = clean_expl(m.group(1).strip())
        print(f"Q{q} len={len(c)}")
