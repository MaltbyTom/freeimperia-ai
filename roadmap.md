# 🗺️ Free Imperia AI Toolchain – Project Roadmap

## 🎯 Overview

**Free Imperia AI** is a tooling ecosystem built to transform a rich, DokuWiki-hosted 2E AD&D campaign setting into a structured, LLM-readable, relationship-aware knowledge graph. This system supports deep campaign analysis, character interconnection, divine/cosmic relationships, and plot forecasting — and it's designed for reuse by other GMs and worldbuilders.

By parsing raw wiki content into structured data and tagging semantic relationships, we make it possible for language models to intelligently "understand" and assist in the storytelling, documentation, and player immersion of complex homebrew worlds.

---

## 📦 Project State: `v0.9.0-alpha-infra`

✅ Core infrastructure is in place.  
✅ Codebase cleaned, validated, and audited.  
🚧 NLP and tagging tools are operational but require refinement.  
🕳️ Graph visualization and UI interfaces still to come.  
🧠 Memory management, audit policy, and context tools under active improvement.

---

## 🧠 Contributor Philosophy

- Be **explicit**, not clever.  
- Assume **AI-assisted development** — tools must clarify their inputs and outputs.
- Prefer **auditability over elegance**.
- Every file, tool, or rule must either be:
  - Registered in `tools_registry.yaml` or `project_structure.yaml`
  - Or intentionally excluded with comment rationale.

---

## 🔁 Pipeline Dashboard

### 🧪 Phase 1: Data Extraction and Cleaning
| Tool                             | Status      | Notes |
|----------------------------------|-------------|-------|
| `wiki_relationship_extractor_utf8.py` | ✅ | Extract raw entity relationships |
| `apply_relationship_patterns.py`       | ✅ | Pattern-match against known semantic links |
| `score_and_cluster_phrases.py`        | ✅ | Group semantically similar unstructured phrases |
| `cleanup_freeimperia.py`              | ✅ | Archive unused scripts and reduce noise |
| `cleanup_data_files.py`               | ✅ | Prune temp and backup data files |
| `tag_index_builder.py`                | ✅ | Build searchable index for interactive UI |
| `tag_index_viewer_v3.py`              | ✅ | Visualize tagged data for QA |

---

### 🧩 Phase 2: Manual Tagging, Graph Output & Validation
| Tool                           | Status | Notes |
|--------------------------------|--------|-------|
| `clustered_matcher_ui_v3.py`   | ✅     | Manually apply tags to clustered semantic phrases |
| `jsonl_to_graph.py`            | ✅     | Transform JSONL-tagged data to graph structures |
| `matcher_ui_v2.py` & `matcher_ui_v3.py` | ✅ | Alternative UIs for relationship confirmation |
| `test2.py`                     | ⚠️     | Needs adaptation to new data directory structure |

**Graph Output Path:**  
- Output to: `data/output/graph_data.json`  
- Final JSONL relationships: `data/output/relationships.jsonl`

---

### 🌐 Phase 3: Usability, UI, and Web Embeds
| Feature                       | Status | Notes |
|------------------------------|--------|-------|
| Interactive Graph Viewer     | ⏳     | Will allow exploration of divine, political, and personal networks |
| NLP Suggestion Engine        | ⏳     | Context-aware tag proposals |
| Integration into `www.freeimperia.com` | ⏳ | Static + LLM query support |
| GitHub push → Netlify/docs   | Planned | Autogenerate docs from README, `rules.yaml`, and `tools_registry.yaml` |

---

## 🛠️ Suggestions from Tool & Data Audits

- Add a dedicated tool for pruning **false-positive relationships** (`e.g. "is noble house"` misfires).
- Develop `tag_suggestion_tool.py` to make tagging UI faster and safer.
- Add YAML-based presets for "divine", "political", "personal" tag categories.
- Use `memory-status` triggers during large audit/toolchain flows to prevent context collapse.

---

## 📚 Key Configs & Reference

- `config/rules.yaml` – Memory, file usage, and behavior policies  
- `config/tools_registry.yaml` – Declares inputs/outputs and logic of each tool  
- `config/world_lore_reference.yaml` – For divine structures, plot arcs, and alignment nuances  
- `audits/` – Contains `tool_audit.yaml`, `data_audit.yaml`, and markdown summaries

---

## ✅ Next Steps

- [ ] 🌍 Generate divine & character graphs for web embedding  
- [ ] 🧪 Write unit tests for `apply_relationship_patterns.py` and `jsonl_to_graph.py`  
- [ ] 🧠 Improve memory reuse by prioritizing reference file summaries  
- [ ] 🗃️ Add interactive filtering to `tag_index_viewer_v3.py`  
- [ ] 🧭 Expand `README.md` to include examples and screenshots

---

## 💬 Contact & Community

We believe the future of GM tooling is collaborative, structured, and AI-enhanced.  
**Want to build your own system like Free Imperia AI?**  
Clone, fork, or file an issue on GitHub:  
**https://github.com/MaltbyTom/freeimperia-ai**

---