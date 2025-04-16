# tools/messaging_header.py

from datetime import datetime
from tools.memory_status import get_memory_status

def format_memory_header():
    status = get_memory_status()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    doc_count = status["docs_in_memory"]
    file_count = status["yaml_json_files_in_memory"]
    return f"📊 Memory: {doc_count} docs / {file_count} YAML/JSON | ⏰ {ts}"