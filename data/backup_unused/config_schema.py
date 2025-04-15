from config import *

SCHEMA = {
    "output/relationships.jsonl": {
        "type": "jsonl",
        "structure": {
            "source": "str",
            "text": "str",
            "relationship": "str",
            "target": "str",
            "score": "float",
            "category": "str"
        }
    },
    "output/wiki_pages.json": {
        "type": "json",
        "structure": {
            "<page_name>": "str (raw page text)"
        }
    },
    "relationships.yaml": {
        "type": "yaml",
        "structure": {
            "relationships": [
                {
                    "name": "str",
                    "patterns": ["str", "str", "..."]
                }
            ]
        }
    },
    "output/unmatched_phrases.txt": {
        "type": "txt",
        "structure": "One unmatched phrase per line"
    },
    "tagged/relationships_tagged.jsonl": {
        "type": "jsonl",
        "structure": {
            "source": "str",
            "text": "str",
            "relationship": "str",
            "target": "str",
            "tags": ["str"]
        }
    }
}

def describe_schema():
    print("🧾 FILE FORMAT SCHEMA:")
    for path, spec in SCHEMA.items():
        print(f"\n📄 {path}")
        print(f"  ├─ Type: {spec['type']}")
        print(f"  └─ Structure:")
        for k, v in spec["structure"].items():
            print(f"      • {k}: {v}")

if __name__ == "__main__":
    describe_schema()