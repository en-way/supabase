# -*- coding: utf-8 -*-
"""
sync_comprehensive_audit_batch.py
Synchronizes all audited passages and questions across all 41 exams to Supabase in chunked atomic SQL transactions.
"""

import sys
import os
import glob
import json
import time

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Chunked Supabase Batch Sync ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Fetch all DB questions
print("Fetching all questions from Supabase...")
db_q = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation, q.points, q.q_type, q.passage_id
    from questions q
    join exams e on q.exam_id = e.id
""")
db_q_map = {r['id']: r for r in db_q}
print(f"Total DB questions fetched: {len(db_q)}")

# 2. Fetch all DB passages
print("Fetching all passages from Supabase...")
db_p = db_ops.run_sql("""
    select p.id, p.exam_id, e.year, e.category_id, p.sort_order, p.title, p.content, p.section_type
    from passages p
    join exams e on p.exam_id = e.id
""")
db_p_map = {r['id']: r for r in db_p}
print(f"Total DB passages fetched: {len(db_p)}")

all_sql_statements = []
p_update_count = 0
q_update_count = 0

all_json_files = sorted(glob.glob(r'public/data/exams/*.json'))

for fpath in all_json_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    exam_id = data['exam']['id']
    
    # Check passages
    passages = data.get('passages', [])
    for idx, p in enumerate(passages):
        p_id = p.get('id')
        if p.get('sort_order') is None:
            p['sort_order'] = idx + 1
        p_so = p.get('sort_order')
        p_title = p.get('title', '')
        p_content = p.get('content', '')
        p_section = p.get('section_type') or p.get('type', 'reading')
        
        db_p_item = db_p_map.get(p_id)
        if db_p_item:
            diff = False
            if (db_p_item.get('title') or '').strip() != p_title.strip():
                diff = True
            if (db_p_item.get('content') or '').strip() != p_content.strip():
                diff = True
            if db_p_item.get('sort_order') != p_so:
                diff = True
            
            if diff:
                sql = (
                    f"UPDATE passages SET "
                    f"title = {sql_escape(p_title)}, "
                    f"content = {sql_escape(p_content)}, "
                    f"section_type = {sql_escape(p_section)}, "
                    f"sort_order = {p_so} "
                    f"WHERE id = '{p_id}';"
                )
                all_sql_statements.append(sql)
                p_update_count += 1
        else:
            print(f"Passage ID not in DB: {p_id} ({yr} {cat} #{idx+1})")

    # Check questions
    for q in data.get('questions', []):
        q_id = q.get('id')
        db_q_item = db_q_map.get(q_id)
        if not db_q_item:
            print(f"Question ID not in DB: {q_id}")
            continue
        
        diff = False
        if (q.get('stem') or '').strip() != (db_q_item.get('stem') or '').strip():
            diff = True
        if (q.get('explanation') or '').strip() != (db_q_item.get('explanation') or '').strip():
            diff = True
        if q.get('correct_answer') != db_q_item.get('correct_answer'):
            diff = True
        
        # Options diff check
        j_opts = json.dumps(q.get('options', []), sort_keys=True)
        d_opts = db_q_item.get('options')
        if isinstance(d_opts, str):
            try:
                d_opts = json.loads(d_opts)
            except:
                pass
        d_opts_str = json.dumps(d_opts if isinstance(d_opts, (list, dict)) else [], sort_keys=True)
        if j_opts != d_opts_str:
            diff = True
        
        if diff:
            opts_json = json.dumps(q.get('options', []), ensure_ascii=False)
            ca = q.get('correct_answer') or q.get('answer')
            stem = q.get('stem', '')
            expl = q.get('explanation', '')
            
            sql = (
                f"UPDATE questions SET "
                f"stem = {sql_escape(stem)}, "
                f"options = {sql_escape(opts_json)}::jsonb, "
                f"correct_answer = {sql_escape(ca)}, "
                f"explanation = {sql_escape(expl)} "
                f"WHERE id = '{q_id}';"
            )
            all_sql_statements.append(sql)
            q_update_count += 1

print(f"\nPrepared updates: {p_update_count} passages, {q_update_count} questions.")
print(f"Total SQL statements to execute: {len(all_sql_statements)}")

# Execute in chunks of 80 statements per transaction to stay well under HTTP payload limits
CHUNK_SIZE = 80
chunks = [all_sql_statements[i:i + CHUNK_SIZE] for i in range(0, len(all_sql_statements), CHUNK_SIZE)]

print(f"Splitting into {len(chunks)} chunks of <= {CHUNK_SIZE} statements each...")

for idx, chunk in enumerate(chunks):
    batch_sql = "BEGIN;\n" + "\n".join(chunk) + "\nCOMMIT;"
    print(f"Executing chunk {idx+1}/{len(chunks)} ({len(chunk)} statements)...", end=" ", flush=True)
    t0 = time.time()
    db_ops.run_sql(batch_sql)
    t1 = time.time()
    print(f"DONE ({t1 - t0:.2f}s)")

print("\n=== Supabase Sync Completed Successfully! ===")
