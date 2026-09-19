import os
import sys
import glob
import json
import urllib.request
import urllib.error

def load_env():
    env_vars = {}
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env_vars[k.strip()] = v.strip()
    return env_vars

ENV = load_env()
PROJECT_REF = ENV.get('SUPABASE_PROJECT_REF', 'pghybspsjtzihpzpahcf')
ACCESS_TOKEN = ENV.get('SUPABASE_ACCESS_TOKEN', '')

def run_sql(query: str):
    """Execute raw SQL against Supabase project using the Management API."""
    url = f"https://api.supabase.com/v1/projects/{PROJECT_REF}/database/query"
    req = urllib.request.Request(
        url,
        data=json.dumps({"query": query}).encode('utf-8'),
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            return json.loads(data) if data else []
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        raise RuntimeError(f"HTTP {e.code}: {error_body}")

def get_tables():
    """List all user tables in the public schema with their row count and columns."""
    sql = """
    SELECT 
        t.table_name,
        COALESCE(
            json_agg(
                json_build_object(
                    'column_name', c.column_name,
                    'data_type', c.data_type,
                    'is_nullable', c.is_nullable,
                    'column_default', c.column_default
                ) ORDER BY c.ordinal_position
            ) FILTER (WHERE c.column_name IS NOT NULL), '[]'
        ) as columns
    FROM information_schema.tables t
    LEFT JOIN information_schema.columns c 
        ON t.table_schema = c.table_schema AND t.table_name = c.table_name
    WHERE t.table_schema = 'public' AND t.table_type = 'BASE TABLE'
    GROUP BY t.table_name
    ORDER BY t.table_name;
    """
    return run_sql(sql)

def get_policies():
    """List all Row Level Security (RLS) policies in public schema."""
    sql = """
    SELECT 
        schemaname,
        tablename,
        policyname,
        permissive,
        roles,
        cmd,
        qual,
        with_check
    FROM pg_policies
    WHERE schemaname = 'public'
    ORDER BY tablename, policyname;
    """
    return run_sql(sql)

def apply_migrations():
    """Apply any pending SQL migration files from supabase/migrations/."""
    # Ensure migration table exists
    init_meta_sql = """
    CREATE SCHEMA IF NOT EXISTS supabase_migrations;
    CREATE TABLE IF NOT EXISTS supabase_migrations.schema_migrations (
        version character varying(255) PRIMARY KEY,
        statements text[],
        name text
    );
    """
    run_sql(init_meta_sql)

    # Get applied versions
    applied = set()
    res = run_sql("SELECT version FROM supabase_migrations.schema_migrations;")
    for r in res:
        applied.add(str(r.get('version')))

    # Find local migration files
    mig_dir = os.path.join(os.path.dirname(__file__), '..', 'supabase', 'migrations')
    if not os.path.exists(mig_dir):
        os.makedirs(mig_dir, exist_ok=True)
        print("Created supabase/migrations directory.")
        return

    files = sorted(glob.glob(os.path.join(mig_dir, "*.sql")))
    if not files:
        print("No migration files found in supabase/migrations/.")
        return

    for fpath in files:
        fname = os.path.basename(fpath)
        version = fname.split('_')[0]
        if version in applied:
            print(f"Skipping already applied: {fname}")
            continue

        print(f"Applying migration: {fname} ...")
        with open(fpath, 'r', encoding='utf-8') as f:
            sql_content = f.read()

        # Run migration SQL
        run_sql(sql_content)

        # Record migration
        record_sql = f"""
        INSERT INTO supabase_migrations.schema_migrations (version, name)
        VALUES ('{version}', '{fname}')
        ON CONFLICT (version) DO NOTHING;
        """
        run_sql(record_sql)
        print(f"Migration applied successfully: {fname}")

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'status':
        print(f"Connected to project: {PROJECT_REF}")
        tables = get_tables()
        print(f"Found {len(tables)} tables in 'public' schema.")
        for t in tables:
            print(f" - {t['table_name']} ({len(t.get('columns', []))} columns)")
    elif cmd == 'migrate':
        apply_migrations()
    elif cmd == 'policies':
        policies = get_policies()
        print(f"Found {len(policies)} RLS policies.")
        for p in policies:
            print(f" - [{p['tablename']}] {p['policyname']} ({p['cmd']})")
    else:
        print(f"Unknown command: {cmd}")
