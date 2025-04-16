# 🗺️ Free Imperia AI: Project Roadmap

Welcome to the Free Imperia AI project — an evolving toolkit built to help language models understand, index, and reason over complex tabletop roleplaying lore, with an initial focus on a richly interconnected AD&D 2E setting hosted on [freeimperia.com](http://www.freeimperia.com).

Our goal is to transform raw campaign wiki content into structured, queryable knowledge — enabling AI-assisted storytelling, search, visualization, and eventually in-universe reasoning and generation.

> **Tagline**: *From tangled legend to living logic.*

---

## ✅ Current Phase: Stabilized Core + Memory-Conscious Expansion

We’ve just completed:
- Full audit of tooling and data
- Memory management rules
- Config indexing + boot behavior
- Branch hygiene and main/dev realignment

We are now expanding carefully to ensure reliability and longevity.

---

## 📌 Roadmap Phases

### 🔹 Phase 0: Wiki Extraction & NLP Bootstrapping *(✅ Complete)*

- ✅ Extract raw page data from the wiki (`wiki_relationship_extractor_utf8.py`)
- ✅ Apply relationship patterns (`apply_relationship_patterns.py`)
- ✅ Save matched and unmatched data
- ✅ Define initial class/kit divine relationships
- ✅ Create first knowledge graph via `jsonl_to_graph.py`

---

### 🔹 Phase 1: Memory-Aware Refactor *(✅ Complete)*

- ✅ Split large files into referenceable configs
- ✅ Implement core `rules.yaml` and boot confirmation
- ✅ Build memory tracking & overflow defense tools
- ✅ Shrink large YAML configs into semantically indexed files
- ✅ Validate with structured `tools_registry.yaml`, `file_stability.yaml`, and `config_index.yaml`

---

### 🔹 Phase 2: Audit + Cleanup *(✅ Complete)*

- ✅ Full tools audit (`tools_audit.yaml`, `tools_audit.md`)
- ✅ Full data audit (`data_audit.yaml`, `data_audit.md`)
- ✅ Implement `cleanup_freeimperia.py` and `cleanup_data_files.py`
- ✅ Create and enforce `rules.yaml` update policy
- ✅ Eliminate unused / conflicting outputs
- ✅ Refactor all tools for `config/config.py` consistency

---

### 🔹 Phase 3: Graph Accuracy & Tagging Pipelines *(🔄 In Progress)*

- 🔁 Continue tagging unmatched phrases
- 🔁 Improve tag interfaces with `clustered_matcher_ui_v3.py`
- 🔁 Expand relationships via `relationships_expanded.yaml`
- 🔁 Refine divine & political graphs (especially cross-sphere)
- 🔁 Track ambiguous structures (e.g. Thor/Tulkas)
- 🔁 Flag false positives like “is noble house”

---

### 🔹 Phase 4: World Data Modeling *(🧭 Upcoming)*

- 🌍 Geo-index locations via map overlays and grid references (e.g. "Nexus Prime: N20")
- 📍 Cross-reference with `places_on_arda` page
- 🧠 Enable AI to interpret maps as referential entities
- 📈 Build out location graphs linked to events, politics, divine sites

---

### 🔹 Phase 5: Narrative Reasoning & AI Collaboration *(🎯 Goal)*

- 🧬 Let models navigate the campaign like a living semantic space
- 📖 Answer complex questions like:
  - *“Who are the children of Loki?”*
  - *“Which factions oppose the Cult of Sauron?”*
  - *“Where is Radwen likely to be headed based on prophecy?”*
- 🎙️ Enable co-GM support, intelligent NPCs, timeline extrapolation

---

## 🧰 Tooling Dashboard

| Tool | Description | Inputs | Outputs |
|------|-------------|--------|---------|
| `wiki_relationship_extractor_utf8.py` | Extracts text + detected names from wiki JSON | Raw wiki | `wiki_pages.json` |
| `apply_relationship_patterns.py` | Pattern-matches relationships | `wiki_pages.json`, `relationships.yaml` | `relationships.jsonl`, `unmatched_phrases.txt` |
| `score_and_cluster_phrases.py` | Clusters unmatched phrases | `unmatched_phrases.txt` | clusters (internal) |
| `clustered_matcher_ui_v3.py` | UI to tag clusters & generate `relationships_tagged.jsonl` | clusters | `relationships_tagged.jsonl` |
| `jsonl_to_graph.py` | Builds graph from `relationships.jsonl` | `relationships.jsonl` | `graph_data.json` |
| `tag_index_builder.py` | Indexes tags by source/target pairs | `relationships_tagged.jsonl` | `tags_index.json` |
| `tag_index_viewer_v3.py` | Views tagged relationships by entity | `tags_index.json` | CLI Output |
| `cleanup_freeimperia.py` | Moves unused tools and files | Project root | `backup_unused/` |
| `cleanup_data_files.py` | Deletes stale outputs and backups | `data/output/`, `data/tagged/` | Reduced disk state |
| `generate_config_indexes.py` | Summarizes config usage + validation | All config files | `config_index.yaml` |
| `memory_status.py` | Outputs current document memory state | Internal | CLI Output |
| `test2.py` | Test validator for matched relationships | `relationships.jsonl` | CLI output |

---

## 💬 Suggestions from Audit

- Use `.jsonl` for all large semistructured text
- Add source page and sentence for every tagged relationship
- Incorporate phrase similarity in cluster UI scoring
- Introduce `!memory-status` checks in every major loop
- Rebuild `rules.yaml` with guaranteed merges + boot rules
- Separate UI logic and logic-processing in matchers

---

## 📜 License & Contribution

MIT Licensed. Contributions welcome!

- Please branch off `dev` and submit pull requests
- Include updated audit logs when changing tools
- This project welcomes collab from semantic engineers, D&D lore nerds, and software archaeologists

---

## 🔗 Repo Info

- GitHub: [github.com/MaltbyTom/freeimperia-ai](https://github.com/MaltbyTom/freeimperia-ai)
- Branch: `dev`
- Map: [Map of Endoré](http://www.freeimperia.com/endore2p1.jpg)

---

> 🧙 “Let the wiki speak its hidden truths — and let the LLMs learn to listen.”

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