import os

def list_directory_structure(root_dir, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {"venv", "__pycache__", ".git"}

    print(f"📁 Directory structure for: {root_dir}\n")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        rel_path = os.path.relpath(dirpath, root_dir)
        if any(part in exclude_dirs for part in rel_path.split(os.sep)):
            continue

        indent = "  " * rel_path.count(os.sep)
        print(f"{indent}📂 {os.path.basename(dirpath)}/")
        for filename in sorted(filenames):
            full_path = os.path.join(dirpath, filename)
            size_kb = os.path.getsize(full_path) // 1024
            print(f"{indent}  📄 {filename} ({size_kb} KB)")

if __name__ == "__main__":
    current_dir = os.path.abspath(".")
    list_directory_structure(current_dir)