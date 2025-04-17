import yaml
import os

RULE_PATHS = [
    "config/core_rules.yaml",
    "config/rules.yaml"
]

def load_rules():
    rules = {}
    for path in RULE_PATHS:
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = yaml.safe_load(f)
                rules[path] = content
    return rules
