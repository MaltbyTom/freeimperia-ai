🛠️ tool_audit_suggestions.md

    Suggestions collected during the tool-by-tool audit in April 2025
    For Free Imperia AI, branch: dev
    Repository: MaltbyTom/freeimperia-ai

🧩 apply_relationship_patterns.py

    Add live progress stats (currently uses tqdm, which is good — maybe include skipped vs matched?).

    Consider surfacing more of the matcher engine behavior (e.g., similarity scores, debug flag for matched patterns).

    Allow filtering for output (e.g., only save relationships of a given name or source).

    Add CLI flag to export unmatched phrases separately by pattern type.

🎯 score_and_cluster_phrases.py

    Consider integrating cosine similarity + regex-based clustering into a tunable hybrid scoring function.

    Provide example output or a seed cluster structure for new users.

    Add CLI flag to exclude low-score phrases from clusters entirely.

    Allow YAML schema validation against a known tag taxonomy.

👥 clustered_matcher_ui_v3.py

    Add support for filtering or previewing cluster scores.

    Provide batch editing capabilities (tag multiple phrases at once).

    Add optional graph preview of affected relationships based on tags applied.

    Support saving both .yaml and .jsonl versions at once.

🧪 test2.py

    Warn the user if they are targeting the wrong file (e.g., fallback to output/relationships.jsonl if tagged/relationships_tagged.jsonl not found).

    Highlight invalid or partial entries (e.g., missing source_page, text, or relationship).

    Consider adding a filter to show only matches of a specific relationship type or source page prefix.

🧹 cleanup_freeimperia.py

    Prevent nesting the backup folder inside itself (✅ fixed).

    Optional dry-run mode to preview which files would be moved.

    Record a log (cleanup_report.yaml) of what was moved, for reversibility.

    Support manual file tagging in config/files_registry.yaml to mark safe/unsafe files.

📊 jsonl_to_graph.py

    Add validation for broken or missing relationships before graphing.

    Export intermediate .graphml or .dot formats for testing in tools like Gephi.

    Consider relationship-style visualization mode: aspect-of, member-of, vassal-of, etc.

🔎 tag_index_builder.py / tag_index_viewer_v3.py

    Optionally generate tag usage statistics: frequency, co-occurrence, and confidence.

    Let the viewer offer YAML patch suggestions if tags are poorly distributed or ambiguous.

🧠 wiki_relationship_extractor_utf8.py

    Add support for extracting embedded links with nested parentheses or brackets.

    Optionally preserve surrounding context beyond the sentence for smarter similarity matches.

    Suggest phrases for user-tagging when scores are ambiguous or multiple matches are tied.

❓ matcher_ui_v2.py / matcher_ui_v3.py

    Add side-by-side comparison view for conflicting cluster matches.

    Allow inline editing of the raw phrase and immediate re-score.

    Consider optional AI-generated tag suggestions with confidence scoring (e.g., "This seems like a vassal-of").

📌 Overall Recommendations

    Centralize file paths, outputs, and dependencies in config/project_structure.yaml.

    Add mode flags to every CLI tool (e.g., --dry-run, --verbose, --debug, --audit-log).

    Validate that every tool respects rules.yaml, especially file count and output behavior.