"""
messaging_header.py

Generates standardized chat headers for all system messages.
Includes memory stats, timestamp, and boot status — compliant with Free Imperia AI rules.yaml.
"""

import datetime

def format_memory_header(memory_status, boot_status):
    """
    Returns a formatted header block for Free Imperia AI tools and replies.
    
    Args:
        memory_status (dict): { 'active_documents': int, 'max_documents': int }
        boot_status (bool): True if boot confirmed

    Returns:
        str: Header string with memory, timestamp, and boot confirmation
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    boot_str = "✅ Boot confirmed" if boot_status else "⚠️ Boot not confirmed"
    
    doc_usage = f"{memory_status['active_documents']}/{memory_status['max_documents']}"

    return (
        f"📊 **Memory:** {doc_usage} docs used  \n"
        f"🧠 **Boot Status:** {boot_str}  \n"
        f"⏰ *{timestamp}*"
    )

# Example usage (can be removed or toggled in production)
if __name__ == "__main__":
    example_memory = { 'active_documents': 6, 'max_documents': 100 }
    print(format_memory_header(example_memory, boot_status=True))