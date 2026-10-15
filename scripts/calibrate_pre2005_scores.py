#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/calibrate_pre2005_scores.py

校准 2001-2004 年考研英语一真题总分与及格线：
- 2001-2004 年客观题仅含完型填空（20题×0.5分=10分）与传统阅读Part A（20题×2分=40分），客观题总满分为 50 分，及格基准分（60%）为 30 分。
- 2005-2025 年客观题增加新题型Part B（5题×2分=10分），客观题总满分为 60 分，及格基准分为 36 分。
"""

import os
import sys
import io
import glob
import json

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def calibrate():
    exams_dir = os.path.join(REPO_ROOT, "public", "data", "exams")
    all_files = sorted(glob.glob(os.path.join(exams_dir, "*.json")))
    
    calibrated_files = 0
    for f in all_files:
        with open(f, "r", encoding="utf-8") as fp:
            data = json.load(fp)
        exam = data.get("exam", {})
        year = exam.get("year")
        if year in [2001, 2002, 2003, 2004]:
            exam["total_score"] = 50
            exam["pass_score"] = 30
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)
            print(f"✅ Calibrated {os.path.basename(f)}: {year} total_score=50, pass_score=30")
            calibrated_files += 1

    exams_json_path = os.path.join(REPO_ROOT, "public", "data", "exams.json")
    with open(exams_json_path, "r", encoding="utf-8") as fp:
        index_data = json.load(fp)

    calibrated_index = 0
    for e in index_data:
        if e.get("year") in [2001, 2002, 2003, 2004]:
            e["total_score"] = 50
            e["pass_score"] = 30
            calibrated_index += 1

    with open(exams_json_path, "w", encoding="utf-8") as fp:
        json.dump(index_data, fp, ensure_ascii=False, indent=2)

    print(f"🎉 Successfully calibrated {calibrated_files} exam files and {calibrated_index} index entries!")

if __name__ == "__main__":
    calibrate()
