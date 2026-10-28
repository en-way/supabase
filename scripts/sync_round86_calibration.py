# -*- coding: utf-8 -*-
"""
sync_round86_calibration.py
Syncs Round 86 calibrations (2011 ky1 and 2011 ky2 standardized titles) to Supabase DB.
"""

import sys
import os
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 86 Calibration Sync to Supabase ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

db_p = db_ops.run_sql("""
    select p.id, e.year, e.category_id, p.sort_order, p.title
    from passages p
    join exams e on p.exam_id = e.id
    where e.year = 2011
""")

p_map = {(p['year'], p['category_id'], p['sort_order']): p for p in db_p}

title_map = {
    2: 'Section II: Reading Comprehension Part A - Text 1',
    3: 'Section II: Reading Comprehension Part A - Text 2',
    4: 'Section II: Reading Comprehension Part A - Text 3',
    5: 'Section II: Reading Comprehension Part A - Text 4',
}

sql_statements = []
for cat in ['ky1', 'ky2']:
    for so, t in title_map.items():
        db_item = p_map.get((2011, cat, so))
        if db_item and db_item.get('title') != t:
            pid = db_item['id']
            sql_statements.append(f"UPDATE passages SET title = {sql_escape(t)} WHERE id = '{pid}';")
            print(f"Queued title update: 2011 {cat} P{so} -> {t}")

print(f"Total SQL statements: {len(sql_statements)}")

if sql_statements:
    tx = "BEGIN;\n" + "\n".join(sql_statements) + "\nCOMMIT;"
    db_ops.run_sql(tx)
    print("Database sync committed successfully!")
else:
    print("No DB updates needed.")
