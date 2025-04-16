# tools/prompt_wrapper.py

import datetime
from tools.memory_status import get_memory_status

def header():
    status = get_memory_status()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"📊 Memory: {status['docs_in_memory']}/100 docs | ⏰ {now}"

def wrap_response(text: str, force_header=True) -> str:
    lines = text.splitlines()
    if force_header or len(lines) > 10:
        return f"{header()}\n\n{text}"
    return text