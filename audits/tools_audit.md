# 🧪 Tools Audit Report — `tools/`

This audit documents all working tools in the `tools/` directory of the `freeimperia-ai` project as of the latest development cycle. All tools have been tested and aligned with the project structure.

---

## 📁 Directory: `tools/`

Each script is listed with:
- ✅ Status
- 🧠 Description
- 📥 Inputs
- 📤 Outputs
- 🔁 Related Tools
- 🗒️ Notes

---

### `apply_relationship_patterns.py` ✅  
**🧠 Purpose**: Applies pattern-based matching to extract structured relationships from wiki page text.  
**📥 Input**:
- `data/wiki_pages.json`
- `config/relationships.yaml`
**📤 Output**:
- `output/relationships.jsonl`
- `output/unmatched_phrases.txt`
**🔁 Related**: `score_and_cluster_phrases.py`, `jsonl_to_graph.py`  
**🗒️ Notes**: Core engine for turning raw page text into structured graph-ready relationships.

---

### `cleanup_freeimperia.py` ✅  
**🧠 Purpose**: Archives unused or orphaned files to `backup_unused/` for safety.  
**📥 Input**: Root project directory scan  
**📤 Output**: Moved files to `backup_unused/`  
**🗒️ Notes**: Can be reused after future bursts of data/file generation.

---

### `clustered_matcher_ui_v3.py` ✅  
**🧠 Purpose**: Interactive tagging of semantically clustered relationship phrases.  
**📥 Input**:
- `output/unmatched_phrases.txt`
**📤 Output**:
- `tagged/relationships_tagged.jsonl`
- `tagged/relationships_expanded.yaml`
**🔁 Related**: `score_and_cluster_phrases.py`, `tag_index_builder.py`  
**🗒️ Notes**: Includes YAML export, similarity scoring, batch tagging.

---

### `jsonl_to_graph.py` ✅  
**🧠 Purpose**: Converts tagged relationships into interactive graph data.  
**📥 Input**:
- `output/relationships.jsonl`
**📤 Output**:
- `output/graph_data.json`
**🗒️ Notes**: Key output for visual and web-based graph rendering.

---

### `matcher_ui_v2.py` / `matcher_ui_v3.py` ✅  
**🧠 Purpose**: Manual tagging UI for unmatched phrases.  
**📥 Input**:
- `output/unmatched_phrases.txt`
**📤 Output**:
- `tagged/relationships_tagged.jsonl`
**🗒️ Notes**: Useful for direct phrase-to-tag matching without clustering.

---

### `score_and_cluster_phrases.py` ✅  
**🧠 Purpose**: Embeds and clusters unmatched relationship phrases for human-aided tagging.  
**📥 Input**:
- `output/unmatched_phrases.txt`
**📤 Output**:
- `output/clustered_phrases.jsonl`
**🔁 Related**: `clustered_matcher_ui_v3.py`  
**🗒️ Notes**: Pre-step to help reduce noise in phrase tagging.

---

### `tag_index_builder.py` ✅  
**🧠 Purpose**: Indexes all relationship tags used for graph previews and analytics.  
**📥 Input**:
- `tagged/relationships_tagged.jsonl`
**📤 Output**:
- `tagged/relationship_tag_index.json`
**🗒️ Notes**: Helps analyze which tags are common or rare.

---

### `tag_index_viewer_v3.py` ✅  
**🧠 Purpose**: Interactive browser for the tag index file.  
**📥 Input**:
- `tagged/relationship_tag_index.json`
**📤 Output**: UI-based exploration  
**🗒️ Notes**: Especially helpful to guide pattern refinement or prune unused tags.

---

### `test2.py` ✅  
**🧠 Purpose**: Quick filter and print for specific tags (e.g. `is noble house`) for QA.  
**📥 Input**:
- `output/relationships.jsonl`
**📤 Output**: Console print  
**🗒️ Notes**: Excellent for spot-checking extraction fidelity.

---

### `wiki_relationship_extractor_utf8.py` ✅  
**🧠 Purpose**: Parses raw wiki pages and extracts candidate relationship phrases.  
**📥 Input**: Your DocuWiki-formatted HTML or converted `data/wiki_pages.json`  
**📤 Output**:
- `output/unmatched_phrases.txt`
- `output/wiki_pages.json`
**🗒️ Notes**: The front line of ingestion for new world-building content.

---

## ✅ Summary

| Tool | Status |
|------|--------|
| `apply_relationship_patterns.py` | ✅ |
| `cleanup_freeimperia.py` | ✅ |
| `clustered_matcher_ui_v3.py` | ✅ |
| `jsonl_to_graph.py` | ✅ |
| `matcher_ui_v2.py` | ✅ |
| `matcher_ui_v3.py` | ✅ |
| `score_and_cluster_phrases.py` | ✅ |
| `tag_index_builder.py` | ✅ |
| `tag_index_viewer_v3.py` | ✅ |
| `test2.py` | ✅ |
| `wiki_relationship_extractor_utf8.py` | ✅ |

All tools have passed validation and match the `project_structure.yaml` file layout. Each is suitable for inclusion in the README and tool registry.

---