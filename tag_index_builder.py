import json
import yaml
from collections import defaultdict

YAML_FILE = "relationships_expanded.yaml"
JSONL_FILE = "relationships_tagged.jsonl"
GRAPH_FILE = "graph_data.json"
OUTPUT_INDEX = "tag_index.json"

def load_yaml_patterns():
    with open(YAML_FILE, "r", encoding="utf-8") as f:
        y = yaml.safe_load(f)
        return {entry["name"]: entry["patterns"] for entry in y.get("relationships", [])}

def load_tagged_jsonl():
    with open(JSONL_FILE, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def load_graph_data():
    try:
        with open(GRAPH_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"nodes": [], "edges": []}

def build_tag_index():
    print("🔄 Building tag index...")
    patterns = load_yaml_patterns()
    tagged = load_tagged_jsonl()
    graph = load_graph_data()

    index = {}

    for rel_type, pats in patterns.items():
        index[rel_type] = {
            "patterns": list(set(pats)),
            "occurrences": []
        }

    for line in tagged:
        rel = line.get("relationship")
        pattern = line.get("pattern")
        context = line.get("text")
        source = line.get("linked_entities", [None, None])[0]
        target = line.get("linked_entities", [None, None])[1]
        index.setdefault(rel, {"patterns": [], "occurrences": []})
        index[rel]["occurrences"].append({
            "pattern": pattern,
            "context": context,
            "source": source,
            "target": target
        })

    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"✅ Tag index written to {OUTPUT_INDEX}")
    print(f"📚 Indexed {len(index)} relationship types")

if __name__ == "__main__":
    build_tag_index()
