import yaml
from pathlib import Path
from pprint import pprint

CONFIG_DIR = Path("config")
INDEX_OUTPUT = CONFIG_DIR / "config_index.yaml"

def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    print("📂 Indexing configuration files...")

    index = {
        "tools_by_input_file": {},
        "tools_by_output_file": {},
        "rules_by_category": {},
        "file_classification": {
            "transient": [],
            "long_term": [],
            "audit_only": [],
        },
    }

    # --- Tools Registry Parsing ---
    tools_registry = load_yaml(CONFIG_DIR / "tools_registry.yaml")
    for tool in tools_registry.get("tools", []):
        name = tool["name"]
        for input_file in tool.get("inputs", []):
            index["tools_by_input_file"].setdefault(input_file, []).append(name)
        for output_file in tool.get("outputs", []):
            index["tools_by_output_file"].setdefault(output_file, []).append(name)

    # --- Project Structure (file classification) ---
    structure = load_yaml(CONFIG_DIR / "project_structure.yaml")
    for path, metadata in structure.get("files", {}).items():
        category = metadata.get("classification", "long_term")
        index["file_classification"].setdefault(category, []).append(path)

    # --- Core Rules Indexing (robust) ---
    ruleset = load_yaml(CONFIG_DIR / "core_ruleset.yaml")
    for category, rules in ruleset.items():
        if isinstance(rules, dict):
            index["rules_by_category"][category] = list(rules.keys())
        elif isinstance(rules, list):
            index["rules_by_category"][category] = [str(r) for r in rules]
        else:
            index["rules_by_category"][category] = [f"<unsupported: {type(rules).__name__}>"]

    # Save index
    with open(INDEX_OUTPUT, "w", encoding="utf-8") as f:
        yaml.dump(index, f, sort_keys=False)

    print(f"✅ Saved config index to: {INDEX_OUTPUT}")
    pprint(index)

if __name__ == "__main__":
    main()