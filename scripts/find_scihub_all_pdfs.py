# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")

for p in base_dir.rglob("*.pdf"):
    try:
        doc = fitz.open(str(p))
        for i in range(len(doc)):
            t = doc[i].get_text()
            if "Sci-Hub" in t or "sci-hub" in t or "Sci-hub" in t:
                print(f"Match in {p.name} Page {i+1}")
                break
    except Exception as e:
        pass
