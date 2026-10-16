import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

char_map = {
    '’': 'e', '(': 'o', ')': 'r', '*': 'i', '+': 's',
    '0': '-', '1': 'v', '2': 'l', '3': 'm', '4': 'd', '5': 'b',
    '6': 'g', '7': 'p', '8': '.', '9': 'T', ':': '1', ';': '2', '<': 'w',
    '=': '3', '>': '4', '?': '5', '@': '+', 'A': 'E', 'B': 'z', 'C': 'O',
    'D': 'Y', 'E': 'k', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': '9',
    'K': '%', 'L': 'H', 'M': 'S', 'N': '7', 'O': '6', 'P': 'x', 'Q': 'I',
    'R': 'q', 'S': 'W', 'T': '8', 'U': '0', 'V': 'G', 'W': 'F'
}

def decode_line(line):
    # Regex replace options first to safe tokens
    line = re.sub(r'’F\(?', '§OPT_A§', line)
    line = re.sub(r'’G\(?', '§OPT_B§', line)
    line = re.sub(r'’H\(?', '§OPT_C§', line)
    line = re.sub(r'’I\(?', '§OPT_D§', line)
    
    line = line.replace("!语篇分析!", "【语篇分析】").replace("!真题精解!", "【真题精解】")
    line = line.replace("#精准定位$", "【精准定位】\n").replace("#空格设置$", "【空格设置】\n").replace("#干扰设置$", "【干扰项设置】\n")
    line = line.replace("本题考核的知识点是,", "【考点提炼】").replace("正确率,", "正确率：")
    
    # decode characters
    res = []
    i = 0
    while i < len(line):
        if line[i:i+7] == '§OPT_A§':
            res.append('[A] ')
            i += 7
            continue
        if line[i:i+7] == '§OPT_B§':
            res.append('[B] ')
            i += 7
            continue
        if line[i:i+7] == '§OPT_C§':
            res.append('[C] ')
            i += 7
            continue
        if line[i:i+7] == '§OPT_D§':
            res.append('[D] ')
            i += 7
            continue
            
        c = line[i]
        if '\u4e00' <= c <= '\u9fff' or c in '，。！？；：“”（）《》【】\n ':
            res.append(c)
        elif c == '!':
            # check if it is padding like !!!!!!!
            if i+1 < len(line) and line[i+1] == '!':
                # skip multiple !
                while i+1 < len(line) and line[i+1] == '!':
                    i += 1
                res.append(' ')
            else:
                res.append('。')
        elif c == '$':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= prev_c <= '\u9fff') or ('\u4e00' <= next_c <= '\u9fff') or prev_c in '。，：；）”':
                res.append('，')
            else:
                res.append('y')
        elif c == '#':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= prev_c <= '\u9fff') or ('\u4e00' <= next_c <= '\u9fff'):
                res.append('；')
            else:
                res.append('n')
        elif c == '"':
            if i+4 < len(line) and line[i:i+5] == '"""""':
                while i+1 < len(line) and line[i+1] == '"':
                    i += 1
            else:
                prev_c = line[i-1] if i > 0 else ''
                next_c = line[i+1] if i+1 < len(line) else ''
                if ('\u4e00' <= prev_c <= '\u9fff') and ('\u4e00' <= next_c <= '\u9fff'):
                    res.append('、')
                else:
                    res.append('a')
        elif c == ',':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= prev_c <= '\u9fff') or ('\u4e00' <= next_c <= '\u9fff'):
                res.append('：')
            else:
                res.append('c')
        elif c == '%':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= next_c <= '\u9fff') or prev_c in '，。； ' or (next_c == '(' and line[i:i+4] == '%(#&'):
                res.append('(')
            else:
                res.append('t')
        elif c == '&':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= prev_c <= '\u9fff') or next_c in '，。； \n' or prev_c == '#':
                res.append(')')
            else:
                res.append('h')
        elif c == '.':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= next_c <= '\u9fff') or prev_c in '，。； ：':
                res.append('“')
            else:
                res.append('f')
        elif c == '/':
            prev_c = line[i-1] if i > 0 else ''
            next_c = line[i+1] if i+1 < len(line) else ''
            if ('\u4e00' <= prev_c <= '\u9fff') or next_c in '，。； ：':
                res.append('”')
            else:
                res.append('j')
        elif c == '-':
            if i+1 < len(line) and line[i+1] == '-':
                res.append('……')
                i += 1
            else:
                res.append('u')
        elif c in char_map:
            res.append(char_map[c])
        else:
            res.append(c)
        i += 1
    return ''.join(res)

print("Decoded Page 3:")
lines = doc[2].get_text().split('\n')
for l in lines[15:40]:
    dl = decode_line(l).strip()
    if dl:
        print(dl)
