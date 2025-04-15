import shutil
from pathlib import Path
from config import BASE_DIR, BACKUP_DIR

# Define what folders/files are safe to ignore or relocate
SAFE_FILES = {
    "config.py", "requirements.txt", "README.md", 
    "apply_relationship_patterns.py", "score_and_cluster_phrases.py",
    "wiki_relationship_extractor_utf8.py", "jsonl_to_graph.py",
    "matcher_ui_v2.py", "matcher_ui_v3.py", "clustered_matcher_ui_v3.py",
    "test2.py", "cleanup_freeimperia.py", "tag_index_viewer_v3.py",
    "tag_index_builder.py", "wiki_re_plus.py"
}

SAFE_DIRS = {"output", "tagged", "venv", "__pycache__", "backup_unused"}

def move_to_backup(path):
    target = BACKUP_DIR / path.name
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"📦 Moving {path} → {target}")
    shutil.move(str(path), str(target))

def main():
    print(f"📁 Scanning {BASE_DIR} for unused files and folders...")
    BACKUP_DIR.mkdir(exist_ok=True)

    for item in BASE_DIR.iterdir():
        if item.name in SAFE_FILES or item.name in SAFE_DIRS or item.name.startswith("."):
            continue
        move_to_backup(item)

    print("✅ Cleanup complete. Unused files/folders moved to:", BACKUP_DIR)

if __name__ == "__main__":
    main()