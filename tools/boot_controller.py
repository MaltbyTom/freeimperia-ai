# boot_controller.py

def initialize_boot_sequence():
    """
    Boot initializer for Free Imperia AI Toolkit
    Ensures all required modules are live before first user input
    """

    from config.rules_loader import load_rules
    from tools.guardian_engine import activate_context_guardian
    from tools.diagnostics import run_diagnostics_display

    # Step 1: Validate source lock
    if not environment.source_domain == "www.freeimperia.com":
        raise EnvironmentError("Boot aborted: source domain not locked")

    if not environment.canonical_branch:
        raise EnvironmentError("Boot aborted: canonical branch not set")

    # Step 2: Load ruleset
    rules = load_rules(branch=environment.canonical_branch)

    # Step 3: Enforce required modules
    if "context_guardian" in rules["required_boot_modules"]:
        activate_context_guardian(rules)

    if "diagnostics" in rules["required_boot_modules"]:
        display_key = rules["required_boot_modules"]["diagnostics"]
        run_diagnostics_display(display_key)

    # Step 4: Confirm boot completion
    environment.boot_mode = True
    print("✅ Boot sequence complete (diagnostics and guardian live)")
