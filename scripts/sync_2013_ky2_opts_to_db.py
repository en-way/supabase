import json
import os
from supabase import create_client

def get_supabase_client():
    env_file = '.env.local'
    env_vars = {}
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env_vars[k.strip()] = v.strip().strip("'").strip('"')

    url = env_vars.get('NEXT_PUBLIC_SUPABASE_URL') or os.environ.get('NEXT_PUBLIC_SUPABASE_URL')
    key = env_vars.get('SUPABASE_SERVICE_ROLE_KEY') or os.environ.get('SUPABASE_SERVICE_ROLE_KEY') or env_vars.get('NEXT_PUBLIC_SUPABASE_ANON_KEY')
    return create_client(url, key)

def sync_opts():
    supabase = get_supabase_client()
    with open('public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    exam_id = data['exam']['id']
    questions = data.get('questions', [])
    print(f"Syncing options for {len(questions)} questions of exam {exam_id}...")

    # Fetch DB questions
    res = supabase.table('questions').select('id, question_number, sort_order').eq('exam_id', exam_id).execute()
    db_qs = {q['question_number'] or q['sort_order']: q['id'] for q in res.data}

    updated = 0
    for q in questions:
        q_no = q['question_number']
        db_id = db_qs.get(q_no)
        if not db_id:
            print(f"Warning: db question not found for Q{q_no}")
            continue

        payload = {
            'options': q['options'],
            'points': q.get('points', 0.5 if q_no <= 20 else 2.0),
            'answer': q.get('answer'),
            'correct_answer': q.get('correct_answer'),
            'explanation': q.get('explanation')
        }
        res_up = supabase.table('questions').update(payload).eq('id', db_id).execute()
        updated += len(res_up.data)

    print(f"Successfully synced options for {updated} questions to Supabase production database.")

if __name__ == '__main__':
    sync_opts()
