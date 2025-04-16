# 📦 Data File Audit — Free Imperia AI Project

This audit covers all data files present in the `output/`, `tagged/`, and `config/` directories, mapping their purpose, usage, and cleanup status.

---

## ✅ Files in Active Use

| File                               | Purpose                                         | Used By                              |
|------------------------------------|--------------------------------------------------|--------------------------------------|
| `output/wiki_pages.json`          | Source content from all wiki pages              | `apply_relationship_patterns.py`, `wiki_relationship_extractor_utf8.py` |
| `output/relationships.jsonl`      | Canonical matched relationships (auto + tagged) | `jsonl_to_graph.py`, `test2.py`, `matcher_ui_v3.py` |
| `output/unmatched_phrases.txt`    | For review and refinement of patterns           | — (reference only)                   |
| `output/graph_data.json`          | Final graph of nodes and relationships          | Used for visualization/export        |
| `tagged/relationships_tagged.jsonl`| Human-reviewed tagged relationships            | `matcher_ui_v3.py`                   |
| `tagged/relationships_expanded.yaml`| Relationship pattern expansions               | `apply_relationship_patterns.py`     |
| `config/config.py`                | Shared config across tools                      | All tool runners                     |
| `config/rules.yaml`               | AI memory and behavior management               | Referenced when handling large sets  |
| `config/lore.yaml`                | Worldbuilding reference material                | As needed                            |
| `config/project_structure.yaml`   | Maps tool inputs/outputs                        | Internal use                         |

---

## 🗃️ Optional / Backups

| File                                        | Notes                  |
|---------------------------------------------|------------------------|
| `tagged/relationships_expanded_backup.yaml` | Manual backup          |
| `tagged/relationships_expanded backup2.yaml`| Manual backup          |

---

## ❌ Unused or Deprecated

| File                            | Notes                     |
|---------------------------------|---------------------------|
| `output/wiki_pages_backup.json`| Legacy copy               |
| `output/test/`                 | Empty directory           |
| `tagged/skipped_clusters.txt` | From older matcher version|

---

## 🛠 Recommendations

- Add a cleanup script to archive or delete deprecated files.
- Keep only the most recent backup YAML for `relationships_expanded.yaml`.
- If `unmatched_phrases.txt` exceeds 2MB, consider segmenting or compressing.
- Consider logging pattern coverage and hit rates for smarter iteration.

---

## Memory Status During Audit

- ✅ Audit ran cleanly.
- ✅ No overflow or lost context.
- ✅ `rules.yaml` functioned as intended to keep scratch work external.