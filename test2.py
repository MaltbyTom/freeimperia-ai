import json
from config import RELATIONSHIPS_JSONL

print(f"✅ Loading relationships from {RELATIONSHIPS_JSONL}")
with open(RELATIONSHIPS_JSONL, "r", encoding="utf-8") as f:
    entries = [json.loads(line) for line in f]

print(f"✅ Loaded {len(entries)} relationships.\n")

for entry in entries[:20]:  # show a sample of 20
    print(f"📄 Source Page: {entry.get('source', 'unknown')}")
    print(f"💬 Sentence: {entry.get('text', '[no text found]')}")
    print(f"🔁 Relationship: {entry['relationship']} (score: {entry.get('score', '?')})")
    print(f"📎 Category: {entry.get('category', '?')}")
    print("—" * 80)