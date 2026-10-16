import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

cipher_map = {
    '!': 'M', '"': 'a', '#': 'n', '$': 'y', '%': 't', '&': 'h', '’': 'e',
    '(': 'o', ')': 'r', '*': 'i', '+': 's', ',': 'c', '-': 'u', '.': 'f',
    '/': 'j', '0': '-', '1': 'v', '2': 'l', '3': 'm', '4': 'd', '5': 'b',
    '6': 'g', '7': 'p', '8': '.', '9': 'T', ':': '1', ';': '2', '<': 'w',
    '=': '3', '>': '4', '?': '5', '@': '+', 'A': 'E', 'B': 'z', 'C': 'O',
    'D': 'Y', 'E': 'k', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': '9',
    'K': '%', 'L': 'H', 'M': 'S', 'N': '7', 'O': '6', 'P': 'x', 'Q': 'I',
    'R': 'q', 'S': 'W', 'T': '8', 'U': '0', 'V': 'G', 'W': 'F'
}

def decode_text(text):
    res = []
    for c in text:
        if c in cipher_map:
            res.append(cipher_map[c])
        else:
            res.append(c)
    return ''.join(res)

doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

print("=== Decoded 2004 Passage Page 1 ===")
p1_text = doc[0].get_text()
decoded_p1 = decode_text(p1_text)
print(decoded_p1[:1500])
