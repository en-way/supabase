import fitz, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== Checking 2023 ky2 Text 3 & Text 4 in Yellow Book ===")
for p in pathlib.Path(r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）').rglob('*2023*'):
    if '英语（二）' in p.name or '英语二' in p.name:
        doc = fitz.open(str(p))
        print(f"Checking {p.name} ({len(doc)} pages)...")
        for pno in range(len(doc)):
            t = doc[pno].get_text()
            if 'Text 3' in t or 'Text 4' in t:
                # check word count lines or snippet
                lines = [l for l in t.splitlines() if 'words]' in l.lower()]
                if lines:
                    print(f"  p{pno}: {lines}")
