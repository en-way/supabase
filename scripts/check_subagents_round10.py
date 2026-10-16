import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

subagents = [
    ('b23ba8e7-ebe1-4a89-a43f-b8cfcb8bcb50', 'Agent 1 (ky2 2010-2015)'),
    ('13a05a49-1b90-43dd-b11a-4519b940e00a', 'Agent 2 (ky2 2016-2020)'),
    ('8990501b-09d3-40c6-aedf-c44fb3df702e', 'Agent 3 (ky2 2021-2025)')
]

for aid, name in subagents:
    p = f'C:/Users/57867/.gemini/antigravity/brain/{aid}/.system_generated/logs/transcript.jsonl'
    lines = open(p, 'r', encoding='utf-8').readlines()
    print(f'=== {name}: {len(lines)} steps ===')
    for l in reversed(lines):
        d = json.loads(l)
        if d.get('content'):
            print(f"Step {d.get('step_index')}: {d.get('content')[:250].replace('\n', ' ')}")
            break
