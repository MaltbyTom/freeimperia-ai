def run():
    import datetime
    from system_state import get_memory_status, get_active_modules, get_branch

    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')
    memory_status = get_memory_status()
    active_modules = get_active_modules()
    branch = get_branch()

    print(f"\n🕒 Timestamp (UTC): {timestamp}")
    print(f"📂 Canonical Branch: {branch}")
    print(f"🧠 Memory Mode: {memory_status['mode']}")
    print(f"🚦 Boot Mode: {memory_status['boot']}")
    print(f"🛡️ Context Guardian: {memory_status['context_guardian']}")
    print(f"📊 Memory Load: {memory_status['load_description']}")
    print(f"📋 Active Boot Modules: {', '.join(active_modules)}")
    print(f"📁 Tracked Indexes: {', '.join(memory_status['tracked_indexes'])}\n")