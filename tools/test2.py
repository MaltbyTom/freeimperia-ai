import json

from config.config import MATCHED_RELATIONSHIPS_JSONL

def load_relationships():
    with open(MATCHED_RELATIONSHIPS_JSONL, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def main():
    relationships = load_relationships()
    print(f"✅ Loaded {len(relationships)} relationships.\n")

    for entry in relationships:
        if entry["relationship"] == "is noble house":
            print(f"📄 Source Page: {entry['source']}")
            print(f"💬 Sentence: {entry.get('text', '(no text)')}")
            print(f"🔁 Relationship: {entry['relationship']}")
            print(f"📎 Category: pattern-match")
            print("-" * 120)

if __name__ == "__main__":
    main()