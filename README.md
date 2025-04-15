# 🧠 Free Imperia Relationship Graph Toolset

This toolkit automatically extracts, clusters, tags, and visualizes lore relationships from a DokuWiki-powered worldbuilding site — originally developed for a long-running AD&D 2E campaign.

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Repo

```bash
git clone https://github.com/your-username/free-imperia-graph-tools.git
cd free-imperia-graph-tools
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

---

## 📦 Included Tools

### `wiki_relationship_extractor_utf8.py`
Extracts candidate relationship phrases from wiki text.
- Preserves internal `[[links]]` for accurate source/target IDs
- Uses semantic scoring to match against known YAML patterns
- Outputs:
  - `relationships.jsonl`
  - `unmatched_phrases.txt`

### `clustered_matcher_ui_v3.py`
Interactive Streamlit app for tagging clustered phrase patterns.
- Batch-tag entire clusters of similar phrases
- Suggests likely tag types
- Outputs:
  - `relationships_expanded.yaml`
  - `relationships_tagged.jsonl`

### `jsonl_to_graph.py`
Builds a node-edge graph from tagged phrases.
- Resolves `{source}` and `{target}` from `linked_entities`
- Adds sentence context to each edge
- Outputs:
  - `graph_data.json` (for viewer)

### `tag_index_builder.py`
Consolidates a tag index showing how patterns are used.
- Combines YAML, tagged data, and graph edges
- Outputs:
  - `tag_index.json`

### `tag_index_viewer_v3.py`
Explore tag usage and add review notes.
- View all occurrences of each tag/pattern
- Comment or flag sentences for review
- Export annotations or YAML snippets

---

## 🔄 Workflow Summary

1. `python wiki_relationship_extractor_utf8.py`
2. `streamlit run clustered_matcher_ui_v3.py`
3. `python jsonl_to_graph.py`
4. `python tag_index_builder.py`
5. `streamlit run tag_index_viewer_v3.py`

---

## 🗃️ File Outputs

| File | Description |
|------|-------------|
| `wiki_pages.json` | Cached wiki content |
| `relationships.jsonl` | Raw matched relationships |
| `relationships_expanded.yaml` | Defined pattern sets |
| `relationships_tagged.jsonl` | Final tagged phrases |
| `graph_data.json` | Input for interactive viewer |
| `tag_index.json` | Summary of tag usage |
| `review_notes.json` | Optional review output from viewer |

---

## 🧪 Coming Soon / Optional Tools

- `entity_merge_suggester.py`
- `pattern_suggester.py`
- `multi-graph explorer`
- `full text tokenizer` for language model indexing

---

