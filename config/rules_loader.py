# rules_loader.py

import os
import yaml

RULE_FILES = ["rules.yaml", "core_rules.yaml"]
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "")

def load_rules(branch="dev"):
    """
    Loads and merges rules.yaml and core_rules.yaml from /config
    """
    merged_rules = {}

    for rule_file in RULE_FILES:
        rule_path = os.path.join(CONFIG_PATH, rule_file)
        if not os.path.exists(rule_path):
            raise FileNotFoundError(f"Missing rule file: {rule_file}")

        with open(rule_path, "r") as f:
            rule_data = yaml.safe_load(f)
            merged_rules.update(rule_data or {})

    # Inject dynamic info
    merged_rules["canonical_branch"] = branch
    return merged_rules
