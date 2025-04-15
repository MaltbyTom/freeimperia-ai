import json
import yaml
from tqdm import tqdm
from config.config import WIKI_PAGES_JSON, RELATIONSHIP_PATTERNS_YAML, MATCHED_RELATIONSHIPS_JSONL, UNMATCHED_PHRASES_TXT

def load_patterns():
    with open(RELATIONSHIP_PATTERNS_YAML, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_pages():
    with open(WIKI_PAGES_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def match_patterns(text, patterns):
    matches = []
    for relationship in patterns:
        name = relationship["name"]
        for pattern in relationship["patterns"]:
            if "{target}" in pattern:
                split_pat = pattern.split("{target}")
                if len(split_pat) == 2:
                    prefix, suffix = split_pat
                    for word in text.split():
                        if prefix in text and suffix in text:
                            idx_start = text.find(prefix) + len(prefix)
                            idx_end = text.find(suffix, idx_start)
                            if idx_end != -1:
                                target = text[idx_start:idx_end].strip()
                                matches.append((name, target))
                elif len(split_pat) == 1:
                    prefix = split_pat[0]
                    if prefix in text:
                        rest = text.split(prefix, 1)[1].strip().split()
                        if rest:
                            target = rest[0]
                            matches.append((name, target))
            else:
                if pattern in text:
                    matches.append((name, pattern))
    return matches

def main():
    print("🔁 Loading patterns and pages...")
    patterns = load_patterns()
    pages = load_pages()

    matched = []
    unmatched = []

    for title, page_text in tqdm(pages.items()):
        matches = match_patterns(page_text, patterns)
        if matches:
            for rel, target in matches:
                matched.append({
                    "source": f"[[{title}]]",
                    "target": target,
                    "relationship": rel,
                    "text": page_text
                })
        else:
            unmatched.append(page_text)

    with open(MATCHED_RELATIONSHIPS_JSONL, "w", encoding="utf-8") as f:
        for entry in matched:
            f.write(json.dumps(entry) + "\n")

    with open(UNMATCHED_PHRASES_TXT, "w", encoding="utf-8") as f:
        for line in unmatched:
            f.write(line + "\n")

    print(f"✅ Wrote {len(matched)} matched relationships.")
    print(f"🧠 Logged {len(unmatched)} unmatched phrases.")

if __name__ == "__main__":
    main()