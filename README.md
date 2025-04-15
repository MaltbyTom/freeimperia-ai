# 📚 FreeImperia-AI: Relationship Extraction and Visualization Toolkit

This toolkit supports automated relationship extraction, clustering, tagging, and graph generation for the **Free Imperia** AD&D 2E campaign setting, sourced from a DocuWiki-based site.

---

## 📁 Directory Structure

```
freeimperia-ai/
├── tools/                  # Core extraction, tagging, and transformation tools
├── config/                 # Project configuration files
├── data/                   # Input/output data files (JSON, JSONL, YAML)
├── tagged/                 # Tagged relationships and semantic clusters
├── output/                 # Extracted relationships, graph files, unmatched phrases
├── backup_unused/          # Files/scripts moved during cleanup
└── README.md               # This file
```

---

## 🧰 Core Tools (in `/tools`)

### 🧠 `wiki_relationship_extractor_utf8.py`
- **Purpose**: Extracts semantic relationships from DocuWiki pages using regex and pattern matchers.
- **Output**: `output/wiki_pages.json`, `output/unmatched_phrases.txt`

### 🔄 `apply_relationship_patterns.py`
- **Purpose**: Applies structured pattern rules to generate matched relationships.
- **Output**: `output/relationships.jsonl`
- **Uses**: `config/relationships.yaml` or `tagged/relationships_expanded.yaml`

### 🧩 `score_and_cluster_phrases.py`
- **Purpose**: Scores and clusters unmatched sentences using semantic similarity.
- **Output**: Clustered phrases to assist human tagging

### 🧙 `clustered_matcher_ui_v3.py`
- **Purpose**: Interactive UI for tagging relationship clusters and exporting labeled data.
- **Output**: `tagged/relationships_tagged.jsonl`

### 📈 `jsonl_to_graph.py`
- **Purpose**: Converts JSONL-tagged relationships into graph format (GraphJSON or other).
- **Output**: `output/graph_data.json`

### 🧪 `test2.py`
- **Purpose**: Small utility to preview or debug relationship entries from a `.jsonl` file.

### 🧼 `cleanup_freeimperia.py`
- **Purpose**: Moves unused or legacy files into `backup_unused/` safely.
- **Behavior**: Skips whitelisted files and directories.

### 🏷️ `tag_index_builder.py`
- **Purpose**: Builds a lookup index of all tagged relationship types and sources.
- **Output**: Internal utility for UI support.

### 🕵️ `tag_index_viewer_v3.py`
- **Purpose**: Explore and filter tagged relationship index for QA/debugging.

### 🧪 `matcher_ui_v3.py`
- **Purpose**: Older UI for tagging individual lines, useful for smaller batches.

---

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

