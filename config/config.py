from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 📂 Data input files
WIKI_PAGES_JSON = BASE_DIR / "data" / "wiki_pages.json"
RELATIONSHIP_PATTERNS_YAML = BASE_DIR / "patterns" / "relationships.yaml"
RELATIONSHIP_PATTERNS_EXPANDED = BASE_DIR / "patterns" / "relationships_expanded.yaml"

# 📂 Output files
MATCHED_RELATIONSHIPS_JSONL = BASE_DIR / "output" / "relationships.jsonl"
UNMATCHED_PHRASES_TXT = BASE_DIR / "output" / "unmatched_phrases.txt"
GRAPH_DATA_JSON = BASE_DIR / "output" / "graph_data.json"

# 📂 Tagged output
RELATIONSHIPS_TAGGED_JSONL = BASE_DIR / "tagged" / "relationships_tagged.jsonl"
SKIPPED_CLUSTERS_TXT = BASE_DIR / "tagged" / "skipped_clusters.txt"

# 🧪 Testing or backup
WIKI_PAGES_BACKUP = BASE_DIR / "output" / "wiki_pages_backup.json"
TEST_GRAPH_JSON = BASE_DIR / "output" / "test" / "graph_data.json"
TEST_RELATIONSHIPS_JSONL = BASE_DIR / "output" / "test" / "relationships.jsonl"