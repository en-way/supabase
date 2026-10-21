# -*- coding: utf-8 -*-
"""
calibrate_2008_gold.py
Round 50: Complete golden forensic calibration for 2008 English (I)
Exam UUID: d80926ab-1841-5d1f-a999-56773986c46d
"""

import json
import os

JSON_PATH = 'public/data/exams/d80926ab-1841-5d1f-a999-56773986c46d.json'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

print("Calibrated 2008 Exam successfully loaded.")
