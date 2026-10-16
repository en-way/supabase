import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

def restore_chinese_punctuation(s):
    # s has Chinese characters mixed with cipher punctuation
    # First protect known tags and English option markers
    # e.g., 【考点提炼】, 【精准定位】, 【空格设置】, 【干扰项设置】, [A], [B], [C], [D]
    
    # Cipher punctuation map in Chinese context:
    # M -> 。 (or multiple M -> empty/space)
    # y -> ，
    # n -> ；
    # a -> 、
    # c -> ：
    # f -> “
    # j -> ”
    # u -> …
    
    # Let's replace multiple M first
    s = re.sub(r'M{2,}', '', s)
    s = re.sub(r'a{5,}', '', s)
    
    # Between Chinese chars:
    # char + M -> char + 。
    s = re.sub(r'([\u4e00-\u9fff])M', r'\1。', s)
    s = re.sub(r'M([\u4e00-\u9fff])', r'。\1', s)
    s = re.sub(r'([\u4e00-\u9fff])y', r'\1，', s)
    s = re.sub(r'y([\u4e00-\u9fff])', r'，\1', s)
    s = re.sub(r'([\u4e00-\u9fff])n', r'\1；', s)
    s = re.sub(r'n([\u4e00-\u9fff])', r'；\1', s)
    s = re.sub(r'([\u4e00-\u9fff])a([\u4e00-\u9fff])', r'\1、\2', s)
    s = re.sub(r'([\u4e00-\u9fff])c', r'\1：', s)
    s = re.sub(r'c([\u4e00-\u9fff])', r'：\1', s)
    
    # Quotes: f + Chinese/English + j -> “...”
    s = re.sub(r'f([\u4e00-\u9fff\w\s\-\.]+?)j', r'“\1”', s)
    
    # Parens: t + Chinese/English + h -> （...）
    s = re.sub(r't([\u4e00-\u9fff\w\s\-\.]+?)h', r'（\1）', s)
    
    # Ellipsis: u+ -> ……
    s = re.sub(r'u{2,}', '……', s)
    
    # Any remaining M after Chinese or period
    s = re.sub(r'([\u4e00-\u9fff])M', r'\1。', s)
    s = s.replace('M\n', '。\n').replace('M', '。')
    s = s.replace('。+', '。').replace('。。', '。')
    
    return s

# Test on Q1 and Q3
cloze_text = text.split("<<<PAGE_15>>>")[0]
for q in [1, 3, 6, 7]:
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*(.*?)(?=(?:\n\s*{q+1}\.\s*|<<<PAGE_15>>>|\Z))', cloze_text, re.DOTALL)
    if m:
        c = m.group(1)
        c = re.sub(r'<<<PAGE_\d+>>>', '', c)
        c = re.sub(r'e([A-D])o', r'[\1]', c)
        c = re.sub(r'e([A-D])', r'[\1]', c)
        c = c.replace('M精准定位s', '【精准定位】').replace('n精准定位y', '【精准定位】\n')
        c = c.replace('M空格设置s', '【空格设置】').replace('n空格设置y', '【空格设置】\n')
        c = c.replace('M干扰设置s', '【干扰项设置】').replace('n干扰设置y', '【干扰项设置】\n')
        c = c.replace('M干扰项设置s', '【干扰项设置】').replace('Me干扰项设置o', '【干扰项设置】\n')
        c = c.replace('本题考核的知识点是c', '【考点提炼】').replace('本题考核的知识点是', '【考点提炼】')
        c = c.replace('M正确率c', ' 正确率：').replace('正确率c', '正确率：')
        res = restore_chinese_punctuation(c)
        print(f"=== Q{q} RESTORED ===")
        print(res[:400])
        print("...")
