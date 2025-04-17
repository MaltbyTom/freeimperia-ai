# 🧠 Context Guardian

**Context Guardian** is a memory-aware runtime strategy and toolkit designed to help AI-assisted workflows avoid context overflow, manage persistent reference files, and operate safely in long-term projects with structured config, data, and tooling.

Originally developed in the context of the **Free Imperia** D&D 2E worldbuilding and relationship extraction system, Context Guardian is model-agnostic and intended to scale to any project requiring:
- Memory budgeting and boot-time enforcement
- Controlled tool/data lifecycles
- Index-based reference file handling
- Rule-bound conversational AI collaboration
- Lightweight, human-readable config

---

## 🚀 Goals
- Prevent information loss in multi-tool AI pipelines
- Enable safe conversation workflows without model retraining
- Reduce hallucination by enforcing structure and context bounds
- Be small, composable, and highly testable

---

## 📦 Components
| File | Purpose |
|------|---------|
| `core_ruleset.yaml` | Canonical boot/usage rules for memory-safe operation |
| `memory_status.py` | Runtime memory usage tracker (outputs warnings, percent usage) |
| `generate_config_indexes.py` | Auto-index tools/data/rules relationships |
| `config_index.yaml` | Snapshot of indexed structure (tools by input/output, rule categories) |
| `memory_management_plan.yaml` | Live roadmap for memory control layers |
| `README.md` | This file |
| `roadmap.md` | Project milestones, use cases, and integration paths |
| `meta.yaml` | Repo metadata and install instructions (coming soon) |

---

## 🧪 Under Active Development
This project is in heavy daily use inside `freeimperia-ai/`, and will soon be packaged separately for broader use.
