# 🧠 freeimperia-ai — AI-Augmented Knowledge Graph Tooling for Worldbuilding Wikis

This project is an open-source AI pipeline for extracting and organizing structured relationship data from fantasy wiki content. The tools were developed to enhance the *Free Imperia* campaign setting, an expansive high-fantasy world built in the AD&D 2E system and hosted in a [DokuWiki instance](https://www.dokuwiki.org/).

The system is designed to help Dungeon Masters and contributors **automatically parse, tag, cluster, and graph** complex in-universe lore such as divine hierarchies, character affiliations, and ongoing plot threads.

### 📚 Intended Workflow

This project builds a bridge between a text-heavy game wiki and AI-assisted knowledge tools. The idea is to:

1. **Tokenize** raw wiki content
2. **Extract candidate relationship phrases**
3. **Cluster similar patterns and tag semantic relationships**
4. **Generate graph-ready structured data**
5. **Enable search, visualization, or LLM comprehension of world lore**

The result is a cleanly modeled dataset of characters, divine forces, political groups, and narrative arcs that can power world exploration, game prep, or even NPC dialog systems.

> ⚔️ Although born from a D&D setting, this pipeline can apply to *any fictional wiki* or dense relationship-based corpus.

---

## 📦 File Structure

All tool, config, and data files are organized into modular subdirectories for clarity:

freeimperia-ai/ ├── config/ # Core configuration and rules │ ├── project_structure.yaml │ ├── rules.yaml │ ├── tools_registry.yaml │ ├── world_lore_reference.yaml │ └── file_stability.yaml │ ├── data/ # Input/output data for the processing pipeline │ ├── output/ # Final extracted or matched outputs │ └── tagged/ # Human-reviewed or partially tagged data │ ├── tools/ # Python tools for each stage of the process ├── audits/ # Audit reports for tools and data └── README.md # You are here!


---

## 🛠 Tools Overview

All tools are listed in [`tools_registry.yaml`](config/tools_registry.yaml) and audited in [`audits/tool_audit.md`](audits/tool_audit.md).

| Tool | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| `wiki_relationship_extractor_utf8.py` | Extracts raw relationship phrases from wiki pages | `wiki_pages.json` | `relationships.jsonl`, `unmatched_phrases.txt` |
| `score_and_cluster_phrases.py` | Clusters and scores unmatched phrases | `unmatched_phrases.txt` | `scored_phrases.jsonl` |
| `clustered_matcher_ui_v3.py` | UI to tag phrase clusters with relationships | `scored_phrases.jsonl` | `relationships_tagged.jsonl`, `skipped_clusters.txt` |
| `tag_index_builder.py` | Builds an index of tagged clusters | `relationships_tagged.jsonl` | `tag_index.yaml` |
| `tag_index_viewer_v3.py` | Views and filters the tag index | `tag_index.yaml` | — |
| `apply_relationship_patterns.py` | Applies pattern-matched relationships across pages | `relationships.yaml`, `wiki_pages.json` | `relationships.jsonl` |
| `jsonl_to_graph.py` | Converts relationships into graph-ready format | `relationships.jsonl` | `graph_data.json` |
| `matcher_ui_v2.py` / `matcher_ui_v3.py` | Manual tagging interfaces | `unmatched_phrases.txt` | `relationships_tagged.jsonl` |
| `cleanup_freeimperia.py` | Moves unused or deprecated files to backup | project root | `backup_unused/` |
| `cleanup_data_files.py` | Deletes known temp data, renames backups | `data/output/`, `data/tagged/` | Cleaned directories |
| `test2.py` | Displays high-confidence pattern-matched examples for QA | `relationships.jsonl` | console |
| `config.py` | Shared constants and file paths | n/a | used internally |

---

## 📘 Rules & Memory Management

- The system enforces tool usage and memory policies via [`rules.yaml`](config/rules.yaml)
- Context overflow is mitigated by offloading or summarizing files
- Never claims to save or push unless verified
- Reference files like `world_lore_reference.yaml` are used in place of in-memory lore
- Audit trails for tools and data are maintained in `audits/`

---

## 💡 Future Expansion

Planned features:
- Graph visualization with interactive filtering
- Export to Neo4j or RDF formats
- Real-time tagging UI for multiplayer worldbuilding
- Spelljammer and planar relationship modeling
- Import support for Markdown and Obsidian vaults

---

## ⚔️ About the Setting

The Free Imperia is a Spelljammer-inspired high-fantasy setting that merges Tolkienian cosmology with multiverse politics and divine intrigue. Characters such as Lancelot, Aslan, and Tiamat appear alongside original factions, kirins made real by prayer, and skyfaring elf nobility seeking lost Valinor.

All examples and outputs are drawn from this deep, evolving campaign wiki hosted at [www.freeimperia.com](http://www.freeimperia.com/).

---

## 📜 License & Contribution

MIT Licensed. Contributions welcome! Use the `dev` branch and submit pull requests with clear descriptions and updated audit logs.


## ⚙️ Config Files

### `config/config.py`
Contains shared paths and constants. All tools refer to this file for consistency.

### `config/project_structure.yaml`
Defines the expected directory structure and helps validate setup.

### `tagged/relationships_expanded.yaml`
Expanded list of relationship patterns with names and example structures.
Used in pattern-based matching.

---

## 📊 Data Files

- `output/wiki_pages.json`: All parsed page text from wiki
- `output/relationships.jsonl`: Main extracted relationships
- `tagged/relationships_tagged.jsonl`: Human-tagged relationships for training
- `output/graph_data.json`: Final graph-formatted output
- `output/unmatched_phrases.txt`: Phrases that were not pattern matched

---

## ✅ Getting Started

```bash
python tools/wiki_relationship_extractor_utf8.py
python tools/apply_relationship_patterns.py
python tools/score_and_cluster_phrases.py
python tools/clustered_matcher_ui_v3.py
python tools/jsonl_to_graph.py
```

Use `cleanup_freeimperia.py` occasionally to archive unused or deprecated files.

---

## 🔗 Repo Info
- **GitHub**: [github.com/MaltbyTom/freeimperia-ai](https://github.com/MaltbyTom/freeimperia-ai)
- **Branch**: `dev`

---

Let me know if you'd like to auto-generate the index of relationship types, prepare documentation for hosting on ReadTheDocs or GitHub Pages, or integrate a Makefile for tool orchestration.

