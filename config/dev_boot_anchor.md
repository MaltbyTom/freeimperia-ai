## Dev Boot Anchor — State Capture (April 17, 2025)

### Purpose
This document captures the exact design, boot order, memory model, and architectural assumptions behind the "working" boot profile for `dev_salvage`, confirmed as stable.

### Includes
- Source-of-truth: `rule_manifest.yaml`
- Generated prompt: `boot_prompt.txt`
- Enforcement layer order and diagnostics format
- Rule zoning: core, memory, documentation, data, session
- Confirmation that the distributed rules problem was identified and resolved

### Architecture Highlights
- Memory usage tracked in `x/100cu (tokens/t)` format
- Only YAML and Markdown used for reliable booting
- Memory manager split into hard-enforced and pointered optional zones
- Boot system now portable to Ollama, Claude, local GPTs

### Next Steps
- Start test boots using generated prompt
- Track stability and memory growth
- Begin design of frontend UI to edit and validate `rule_manifest.yaml`
- Stage migration path from `dev_salvage` to `dev` once confirmed stable
