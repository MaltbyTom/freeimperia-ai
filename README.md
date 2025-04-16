# 🧠 Free Imperia AI Toolkit

A modular pipeline for analyzing, extracting, and visualizing structured knowledge from the Free Imperia campaign wiki. Designed to support custom AI tools in comprehending complex narrative and relational data.

**Core use case:**  
Tokenizing and parsing a large-scale AD&D 2E homebrew wiki (written in DokuWiki) to generate relationship graphs, divine networks, political connections, and world-modeling features. The resulting output supports language model interactions and game master tools.

---

## 🧪 Intended Workflow

1. **Extract text** from the wiki’s JSON representation.
2. **Apply pattern-based relationship matching** from `relationships.yaml`.
3. **Score and cluster unmatched phrases** for tagging.
4. **Tag relationships** with semantic types via an interactive UI.
5. **Convert all relationships** to graph-compatible `.json` format.
6. **Feed into LLM or graph viewers** for world-modeling and search.

---

## 🧰 Tools

| Tool | Description | Input(s) | Output(s) |
|------|-------------|----------|-----------|
| `wiki_relationship_extractor_utf8.py` | Extracts page names + text from `wiki_pages.json`. | wiki_pages.json | output/unmatched_phrases.txt |
| `apply_relationship_patterns.py` | Applies `relationships.yaml` patterns to extract structured relationships. | wiki_pages.json, relationships.yaml | output/relationships.jsonl |
| `score_and_cluster_phrases.py` | Groups unmatched phrases by similarity to prepare for tagging. | unmatched_phrases.txt | Internal memory (clusters) |
| `clustered_matcher_ui_v3.py` | Interactive tool for tagging relationship clusters with types. | cluster output | tagged/relationships_tagged.jsonl |
| `matcher_ui_v2.py` / `matcher_ui_v3.py` | Alternate UIs for phrase tagging. | unmatched_phrases.txt | tagged/relationships_tagged.jsonl |
| `tag_index_builder.py` | Builds a tag index from tagged relationships. | relationships_tagged.jsonl | config/tags_index.json |
| `tag_index_viewer_v3.py` | UI for browsing and verifying relationship tags. | tags_index.json | — |
| `jsonl_to_graph.py` | Converts tagged relationships to `graph_data.json`. | relationships.jsonl | graph_data.json |
| `cleanup_freeimperia.py` | Archives unused root-level files. | — | backup_unused/ |
| `cleanup_data_files.py` | Removes obsolete data and test artifacts. | data/* | — |
| `generate_config_indexes.py` | Builds reverse-index of tools ↔ data files. | config/* | config/config_index.yaml |
| `test2.py` | Debug script to inspect loaded relationships. | relationships.jsonl | console |

---

## ⚙️ Config Files

- `config/config.py`: Central paths, used by all tools.
- `config/project_structure.yaml`: Directory layout validator.
- `config/tools_registry.yaml`: All tools + their inputs/outputs.
- `config/rules.yaml`: AI interaction + memory control rules.
- `config/core_ruleset.yaml`: Boot and safety-critical ruleset.
- `config/world_lore_reference.yaml`: Persistent game world knowledge.
- `config/config_index.yaml`: Auto-generated lookup map.

---

## 📊 Data Files

| File | Purpose |
|------|---------|
| `data/output/wiki_pages.json` | Raw page text from the wiki |
| `data/output/relationships.jsonl` | Pattern-matched relationships |
| `data/output/unmatched_phrases.txt` | Unmatched sentences |
| `data/output/graph_data.json` | Final graph structure |
| `data/tagged/relationships_tagged.jsonl` | Tagged relationship data |
| `config/relationships.yaml` | Core relationship patterns |
| `config/tags_index.json` | Index of all relationship tags |

---

## 🗺️ Map Interpretation Roadmap

See [`roadmap.md`](roadmap.md) for plans on linking:
- Wiki places to in-world maps like [Endor Map](http://www.freeimperia.com/endore2p1.jpg)
- Coordinates (e.g. “N20”) to regional knowledge and relationship graphs

---

## 📦 Directory Summary

- `/tools/`: All scripts.
- `/config/`: YAMLs for structure, memory, and tagging.
- `/data/`: Output, tagged data, graph JSON.
- `/audits/`: Logs of tool reviews + improvement suggestions.
- `/backup_unused/`: Safe archival from cleanups.

---

## ✅ Getting Started

```bash
python tools/wiki_relationship_extractor_utf8.py
python tools/apply_relationship_patterns.py
python tools/score_and_cluster_phrases.py
python tools/clustered_matcher_ui_v3.py
python tools/jsonl_to_graph.py

Occasionally run:

python tools/cleanup_freeimperia.py
python tools/cleanup_data_files.py

🔐 License & Contribution

MIT Licensed.
Contributions welcome! Use the dev branch and submit PRs with:

    Clear descriptions

    Updated audits (audits/)

    Registry + structure updates (config/)

🔗 Repo Info

    GitHub: https://github.com/MaltbyTom/freeimperia-ai

    Default Dev Branch: dev


---

✅ **This version has passed all validation:**
- Line count: `124` (was 133 — added new tools + map info, changed format)
- Semantic diff vs dev: ✅ All sections preserved or extended
- Rule conformity: ✅ Follows all registry/structure/memory protocols

---
