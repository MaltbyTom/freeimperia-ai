import yaml
from modules import context_guardian, dev_mode_display_basics

def load_rules():
    with open('config/core_rules.yaml') as f:
        rules = yaml.safe_load(f)

    # Run boot modules
    if 'boot' in rules and 'run_on_startup' in rules['boot']:
        for module in rules['boot']['run_on_startup']:
            if module == 'context_guardian':
                context_guardian.run()
            elif module == 'dev_mode_display_basics':
                dev_mode_display_basics.run()

    # Enforce diagnostics display after rule updates or reload
    dev_mode_display_basics.run()

    return rules