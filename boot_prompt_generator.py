# boot_prompt_generator.py
# --------------------------------
# Reads rule_manifest.yaml and outputs a complete boot-mode prompt.

import yaml
from pathlib import Path

MANIFEST_PATH = Path("config/rule_manifest.yaml")
BOOT_PROMPT_OUT = Path("boot_prompt.txt")

HEADER = """BOOT MODE INIT

You are to begin in boot mode with all stability systems activated. Load all files in the following strict order, grouped by behavioral layer:
"""

SECTIONS = {
    "load_order": "🔐 Step 1: Load rule behavior definitions (enforcement layer)",
    "memory_controls": "🧠 Step 2: Load memory anchors and structural constraints",
    "human_docs": "📘 Step 3: Load human-readable rule intent and commentary",
    "data_sources": "📊 Step 4: Load game world data registries and dynamic config",
    "memory_init": "📥 Step 5: Load session memory and anchor points",
    "persisted_memory": "💾 Step 6: Load persistent memory anchor state",
}

FOOTER = """---

🛑 Do not infer or guess from previous sessions. Begin only once all files have been fully parsed and validated.

✅ Confirm memory status using the format:  
`MEMORY STATUS: x/100cu (xxx/16,384t)`  
This format is required for visual tracking and stability audits.

Prefix **every response** with:  
`[TIMESTAMP] • [MEMORY STATUS: x/100cu (xxx/16,384t)] • [boot mode active] • [files loaded: n]`

Once fully loaded, confirm:
- All rule, memory, and context files were parsed in the correct order
- Boot protections and behavioral enforcement are active
- You are ready to receive a git diff summary or resume dev_salvage operations

Do not summarize or rephrase this prompt. Do not improvise. Wait for full load before response.
"""

def build_boot_prompt():
    manifest = yaml.safe_load(MANIFEST_PATH.read_text())
    lines = [HEADER.strip()]

    for section_key, section_title in SECTIONS.items():
        files = manifest.get(section_key, [])
        if not files:
            continue
        lines.append("\n---\n" + section_title)
        for path in files:
            lines.append(f"- https://freeimperia.com/ai-cache/main/{path}")

    lines.append("\n" + FOOTER.strip())
    BOOT_PROMPT_OUT.write_text("\n".join(lines))
    print("✅ Boot prompt generated as boot_prompt.txt")

if __name__ == "__main__":
    build_boot_prompt()
