# tools/overrun_guard.py

from tools.memory_status import get_memory_status
from tools.sectional_loader import load_rules_section

class MemoryWarningException(Exception):
    pass

def check_memory_before_critical(name_of_action="operation"):
    status = get_memory_status()
    rules = load_rules_section("memory-monitor")

    warn_limits = rules.get("warn_if_exceeds", {})
    mitigation_steps = rules.get("mitigation", [])

    docs = status["docs_in_memory"]
    if docs >= warn_limits.get("documents", 100):
        msg = f"🚨 Memory limit exceeded: {docs} active documents during {name_of_action}."
        print(msg)
        for action in mitigation_steps:
            print(f"🛠️ Suggestion: {action}")
        raise MemoryWarningException(msg)

    # (Optional extension: add check for file count, size, etc.)
    return True