# tools/sectional_loader.py

import yaml
import json
import os
import datetime

from typing import Optional, Union

RULES_PATH = os.path.join("config", "rules.yaml")

def load_rules_limits():
    try:
        with open(RULES_PATH, "r", encoding="utf-8") as f:
            rules = yaml.safe_load(f)
            return rules.get("global", {}).get("memory-budget", {})
    except Exception:
        return {}

def log_load(file_path: str, keys_loaded: list):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"📥 Loaded from {file_path} at {timestamp}")
    print(f"🔑 Keys: {keys_loaded}")

def sectional_load(file_path: str, section: Optional[str] = None) -> Union[dict, list]:
    _, ext = os.path.splitext(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        if ext.lower() == ".yaml":
            data = yaml.safe_load(f)
        elif ext.lower() == ".json":
            data = json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {ext}")

    if section and isinstance(data, dict):
        if section in data:
            log_load(file_path, [section])
            return data[section]
        else:
            raise KeyError(f"Section '{section}' not found in {file_path}")
    else:
        keys = list(data.keys()) if isinstance(data, dict) else ["[non-dict root]"]
        log_load(file_path, keys)
        return data