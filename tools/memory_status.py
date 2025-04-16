# tools/memory_status.py

import datetime
import os
import sys
import psutil
import yaml

# Optional: Path to rules.yaml for budget values
RULES_PATH = os.path.join("config", "rules.yaml")

def load_rules():
    try:
        with open(RULES_PATH, "r", encoding="utf-8") as f:
            rules = yaml.safe_load(f)
            return rules.get("global", {}).get("memory-budget", {})
    except Exception as e:
        print(f"⚠️ Could not load rules.yaml: {e}")
        return {}

def get_memory_stats():
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / (1024 * 1024)  # in MB
    return round(memory_mb, 2)

def report_memory_status():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memory_mb = get_memory_stats()
    rules = load_rules()

    max_files = rules.get("max_files_in_memory", 3)
    max_docs = rules.get("max_documents_total", 100)
    warning_threshold = rules.get("warning_threshold", 90)

    # Simulated values until integrated with actual doc tracking
    active_files = len([f for f in sys.modules if 'freeimperia' in f])
    active_docs = 7  # Stubbed; replace with actual count

    print(f"📊 Memory Status — {timestamp}")
    print(f"🧠 Memory Usage: {memory_mb} MB RAM")
    print(f"📂 Active Files: {active_files} / {max_files}")
    print(f"📄 Active Docs: {active_docs} / {max_docs}")

    if active_docs > warning_threshold:
        print("⚠️ Context Warning: Approaching document overflow limit!")

    if active_files > max_files:
        print("⚠️ File Load Limit Exceeded (max_files_in_memory)")

if __name__ == "__main__":
    report_memory_status()