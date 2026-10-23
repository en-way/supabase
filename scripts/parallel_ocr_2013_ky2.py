# -*- coding: utf-8 -*-
import fitz
import sys
import os
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed

PDF_PATH = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf'

_worker_ocr = None
_worker_doc = None

def init_worker():
    global _worker_ocr, _worker_doc
    from rapidocr_onnxruntime import RapidOCR
    _worker_ocr = RapidOCR()
    _worker_doc = fitz.open(PDF_PATH)

def ocr_single_page(page_num, dpi=110):
    global _worker_ocr, _worker_doc
    try:
        page = _worker_doc[page_num - 1]
        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes('png')
        res, _ = _worker_ocr(img_bytes)
        text = '\n'.join([r[1] for r in res]) if res else ''
        return page_num, text, None
    except Exception as e:
        return page_num, '', str(e)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=1)
    parser.add_argument('--end', type=int, default=72)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--out', type=str, default=r'd:\A16pro\Aing\antigravity\supabase\scripts\2013_ky2_full_raw.txt')
    args = parser.parse_args()

    pages = list(range(args.start, args.end + 1))
    print(f"Starting parallel OCR for pages {args.start} to {args.end} with {args.workers} workers...", flush=True)

    results = {}
    with ProcessPoolExecutor(max_workers=args.workers, initializer=init_worker) as executor:
        futures = {executor.submit(ocr_single_page, p): p for p in pages}
        completed_count = 0
        for future in as_completed(futures):
            p, text, err = future.result()
            completed_count += 1
            if err:
                print(f"[{completed_count}/{len(pages)}] Page {p} FAILED: {err}", flush=True)
            else:
                results[p] = text
                if completed_count % 5 == 0 or completed_count == len(pages):
                    print(f"[{completed_count}/{len(pages)}] Page {p} completed ({len(text)} chars)", flush=True)

    with open(args.out, 'w', encoding='utf-8') as f:
        for p in sorted(results.keys()):
            f.write(f"\n\n=== PAGE {p} ===\n\n" + results[p])

    print(f"All {len(results)} pages saved to {args.out}", flush=True)

if __name__ == '__main__':
    main()
