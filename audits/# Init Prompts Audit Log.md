# Init Prompts Audit Log

## Cold Start Prompt: Free Imperia AI Toolkit

**Timestamp:** 2025-04-17  
**Author:** System (generated from session boot context)  
**Purpose:** Reload full AI Toolkit from empty state with diagnostics and context protections enabled.

You are working on the Free Imperia AI Toolkit, hosted at: https://github.com/MaltbyTom/freeimperia-ai

Use the dev branch as the canonical source for all config files, tools, and structured data.

The project is focused on intelligent extraction and graphing of wiki-based worldbuilding content from the Free Imperia Wiki, supporting a long-running AD&D 2E campaign.

Key directories include: /config: structured YAML/JSON knowledge (rules, lore, indexing, memory control) /tools: automated pipeline scripts (parsing, graphing, indexing) /data/tagged and /data/output: active data products /audits: audit trails (.yaml + .md) /context_guardian: internal context/memory logic and roadmap

Boot system into dev mode with full diagnostics, memory scoped, context_guardian enabled, source restriction set to www.freeimperia.com, and canonical branch locked to dev.


**Triggers Activated:**
- `boot`
- `display_basics`
- `context_guardian`
- `lock_canonical_branch`
- `restrict_sources`
- `set_memory_mode`