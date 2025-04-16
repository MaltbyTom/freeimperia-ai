# tools/memory_enforced_runner.py

from tools.prompt_wrapper import confirm_boot_state
from tools.overrun_guard import enforce_memory_safety
from tools.sectional_loader import load_section
from tools.messaging_header import format_memory_header

import subprocess
import sys

def run_safely(tool_path):
    print(format_memory_header())
    
    if not confirm_boot_state():
        print("🚫 Aborting: Boot requirements not met.")
        return

    if not enforce_memory_safety():
        print("⚠️ Memory safeguards triggered — operation halted.")
        return

    try:
        print(f"🚀 Launching tool: {tool_path}")
        subprocess.run([sys.executable, tool_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Tool failed: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run a Free Imperia tool with memory safety.")
    parser.add_argument("tool", help="Path to tool script (e.g. tools/apply_relationship_patterns.py)")
    args = parser.parse_args()
    run_safely(args.tool)