# -*- coding: utf-8 -*-
"""
sync_round85_calibration.py
Syncs Round 85 calibrations (2005 ky1 passages & Q41-Q45, 2012 ky1 passage sort_orders) to Supabase DB.
"""

import sys
import os
import json
import time

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 85 Calibration Sync to Supabase ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Fetch DB passages for 2005 ky1 and 2012 ky1
db_p = db_ops.run_sql("""
    select p.id, p.exam_id, e.year, e.category_id, p.sort_order, p.title, p.content
    from passages p
    join exams e on p.exam_id = e.id
    where (e.year = 2005 and e.category_id = 'ky1')
       or (e.year = 2012 and e.category_id = 'ky1')
""")
print(f"Fetched {len(db_p)} passages from DB for 2005/2012 ky1")

# Map DB passages by (year, category_id, sort_order) and by id
p_map = {}
for p in db_p:
    p_map[(p['year'], p['category_id'], p['sort_order'])] = p
    p_map[p['id']] = p

# 2. Fetch DB questions for 2005 ky1 Q41-Q45
db_q = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, q.stem, q.options
    from questions q
    join exams e on q.exam_id = e.id
    where e.year = 2005 and e.category_id = 'ky1' and q.sort_order between 41 and 45
""")
print(f"Fetched {len(db_q)} questions from DB for 2005 ky1 Q41-Q45")
q_map = {q['sort_order']: q for q in db_q}

sql_statements = []

# Process 2005 ky1 JSON
with open('public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json', 'r', encoding='utf-8') as f:
    d2005 = json.load(f)

for p in d2005['passages']:
    so = p.get('sort_order')
    db_item = p_map.get((2005, 'ky1', so))
    if not db_item:
        # try by id
        db_item = p_map.get(p.get('id'))
    if db_item:
        pid = db_item['id']
        c = p.get('content', '')
        if (db_item.get('content') or '').strip() != c.strip():
            sql_statements.append(f"UPDATE passages SET content = {sql_escape(c)} WHERE id = '{pid}';")
            print(f"Passage update queued: 2005 ky1 sort_order={so}")

for q in d2005['questions']:
    so = q.get('sort_order')
    if so in [41, 42, 43, 44, 45]:
        db_item = q_map.get(so)
        if db_item:
            qid = db_item['id']
            stem = q.get('stem', '')
            opts_json = json.dumps(q.get('options', []), ensure_ascii=False)
            sql_statements.append(f"UPDATE questions SET stem = {sql_escape(stem)}, options = {sql_escape(opts_json)}::jsonb WHERE id = '{qid}';")
            print(f"Question update queued: 2005 ky1 Q{so}")

# Process 2012 ky1 JSON (sort_order check)
with open('public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json', 'r', encoding='utf-8') as f:
    d2012 = json.load(f)

for p in d2012['passages']:
    so = p.get('sort_order')
    pid = p.get('id')
    db_item = p_map.get(pid)
    if db_item and db_item.get('sort_order') != so:
        sql_statements.append(f"UPDATE passages SET sort_order = {so} WHERE id = '{pid}';")
        print(f"Passage sort_order update queued: 2012 ky1 P {pid} -> {so}")

print(f"Total SQL statements to execute: {len(sql_statements)}")

if sql_statements:
    tx = "BEGIN;\n" + "\n".join(sql_statements) + "\nCOMMIT;"
    db_ops.run_sql(tx)
    print("Database sync committed successfully!")
else:
    print("No DB updates needed.")
