import hashlib
import json
import sys
import io

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def canonical_json_stringify(obj):
    if obj is None:
        return "null"
    if isinstance(obj, (int, float, str, bool)):
        return json.dumps(obj, ensure_ascii=False)
    if isinstance(obj, list):
        return "[" + ",".join(canonical_json_stringify(x) for x in obj) + "]"
    if isinstance(obj, dict):
        sorted_keys = sorted(obj.keys())
        pairs = [json.dumps(k, ensure_ascii=False) + ":" + canonical_json_stringify(obj[k]) for k in sorted_keys]
        return "{" + ",".join(pairs) + "}"
    return json.dumps(str(obj), ensure_ascii=False)

def compute_data_hash(data):
    canonical_str = canonical_json_stringify(data)
    return hashlib.sha256(canonical_str.encode('utf-8')).hexdigest()

print("=== Running Data Hash Determinism & Anti-Abuse Test Suite ===")

# Test 1: Key ordering invariance
obj_a = {
    "mistakes": [
        {"questionId": "q1", "wrongAnswer": "A", "wrongCount": 1},
        {"questionId": "q2", "wrongAnswer": "B", "wrongCount": 2}
    ],
    "vocabulary": [{"word": "stimuli", "translation": "刺激"}],
    "examResults": {
        "exam_2024": {"score": 85, "isPassed": True}
    }
}

obj_b = {
    "examResults": {
        "exam_2024": {"isPassed": True, "score": 85}
    },
    "vocabulary": [{"translation": "刺激", "word": "stimuli"}],
    "mistakes": [
        {"wrongCount": 1, "questionId": "q1", "wrongAnswer": "A"},
        {"wrongAnswer": "B", "wrongCount": 2, "questionId": "q2"}
    ]
}

hash_a = compute_data_hash(obj_a)
hash_b = compute_data_hash(obj_b)

print(f"Hash A: {hash_a}")
print(f"Hash B: {hash_b}")
assert hash_a == hash_b, "Test 1 Failed: Hashes must match despite key re-ordering!"
print("✔ Test 1 Passed: Perfect key ordering invariance!")

# Test 2: Mutation detection
obj_mutated = json.loads(json.dumps(obj_a))
obj_mutated["mistakes"][0]["wrongCount"] = 2
hash_mutated = compute_data_hash(obj_mutated)

assert hash_mutated != hash_a, "Test 2 Failed: Mutated data must produce different hash!"
print("✔ Test 2 Passed: Strict mutation sensitivity!")

# Test 3: Anti-abuse identical data behavior simulation
class MockCloudStorage:
    def __init__(self):
        self.upload_calls = 0
        self.download_calls = 0
        self.db_summary = None

    def upload_backup(self, local_data, local_hash):
        if self.db_summary and self.db_summary.get("dataHash") == local_hash:
            return {"success": True, "isIdentical": True, "message": "Identical, 0 network call"}
        self.upload_calls += 1
        self.db_summary = {"dataHash": local_hash, "backedUpAt": "2026-10-29T12:00:00Z"}
        return {"success": True, "isIdentical": False}

    def download_backup(self, current_local_hash):
        if self.db_summary and self.db_summary.get("dataHash") == current_local_hash:
            return {"success": True, "isIdentical": True, "message": "Identical, 0 network call"}
        self.download_calls += 1
        return {"success": True, "isIdentical": False, "data": obj_a}

mock = MockCloudStorage()

# First upload: should execute
res1 = mock.upload_backup(obj_a, hash_a)
assert res1["success"] and not res1["isIdentical"], "First upload must proceed"
assert mock.upload_calls == 1, "Upload count must be 1"
print("✔ Test 3.1 Passed: Initial cloud backup succeeds.")

# Second upload with same data: must be blocked!
res2 = mock.upload_backup(obj_a, hash_a)
assert res2["success"] and res2["isIdentical"], "Second identical upload must be hard blocked"
assert mock.upload_calls == 1, "Upload count must stay 1 (0 network/storage waste)"
print("✔ Test 3.2 Passed: Identical upload hard blocked with 0 storage writes!")

# Download with same data: must be blocked!
res3 = mock.download_backup(hash_a)
assert res3["success"] and res3["isIdentical"], "Download with matching hash must be hard blocked"
assert mock.download_calls == 0, "Download count must stay 0 (0 egress waste)"
print("✔ Test 3.3 Passed: Identical download hard blocked with 0 egress transfer!")

# Download with changed data: should proceed
res4 = mock.download_backup(hash_mutated)
assert res4["success"] and not res4["isIdentical"], "Download with different hash must proceed"
assert mock.download_calls == 1, "Download count must be 1"
print("✔ Test 3.4 Passed: Out-of-sync download executes cleanly.")

print("\n🎉 ALL DATA HASH & ANTI-ABUSE INVARIANT TESTS PASSED (100%)!")
