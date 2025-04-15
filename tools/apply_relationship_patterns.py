# apply_relationship_patterns.py

import yaml
import json
from tqdm import tqdm
from pathlib import Path

def load_patterns():
    with open("relationships.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_pages():
    with open("output/wiki_pages.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("🔁 Loading patterns and pages...")
    patterns = load_patterns()
    pages = load_pages()

    matched = []
    unmatched = []

    for title, text in tqdm(pages.items()):
        for relationship in patterns:
            name = relationship["name"]
            for pattern in relationship["patterns"]:
                if "{target}" not in pattern:
                    continue
                before, after = pattern.split("{target}")
                if before in text and after in text:
                    start = text.index(before) + len(before)
                    end = text.index(after, start)
                    target = text[start:end].strip()
                    matched.append({
                        "source": title,
                        "target": target,
                        "relationship": name,
                        "pattern": pattern
                    })
                else:
                    unmatched.append(text.strip())

    # Output matches
    Path("output").mkdir(exist_ok=True)
    with open("output/relationships.jsonl", "w", encoding="utf-8") as f:
        for rel in matched:
            f.write(json.dumps(rel) + "\n")

    with open("output/unmatched_phrases.txt", "w", encoding="utf-8") as f:
        for u in unmatched:
            f.write(u + "\n")

    print(f"✅ Wrote {len(matched)} matched relationships.")
    print(f"🧠 Logged {len(unmatched)} unmatched phrases.")

if __name__ == "__main__":
    main()