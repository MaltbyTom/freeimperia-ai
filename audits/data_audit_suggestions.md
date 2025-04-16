# ✍️ Suggestions & Improvements from Data Audit

## ⚠️ Relationship Matching Issues
- `"is noble house"` pattern matches numerous false positives — needs higher-confidence rules or disambiguation filters.
- Alignment-level patterns (`"LG Human"`) can accidentally trigger relationship matching. These should be restricted to class/race tagging only.

## 💡 Tagging & Semantic Suggestions
- Develop a verification pass to flag "unusual" relationships like:
  - `worships Durin Edgesharp`
  - `is a church of Josh Orcman`
- Consider expanding pattern format to allow scoring thresholds (e.g., only log if `score > 0.8`)

## 🧹 Suggested Cleanups
- Remove `output/test/`, all contents are zero KB.
- Keep only `relationships_expanded.yaml` and one backup.
- Archive `wiki_pages_backup.json` unless used as a known rollback.

## 🧠 Memory Use Suggestions
- Large files like `unmatched_phrases.txt` can be indexed and searched instead of loaded entirely.
- Consider hashing sentences to map which ones trigger misfires.

## 🛠 Future Tool Idea
- `relationship_cleaner.py`: Filters known-bad matches, flags odd pairings, checks against known lore in `lore.yaml`.

---

If you'd like, I can generate that last tool for you next.