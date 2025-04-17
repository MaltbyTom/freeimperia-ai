# behavior_rules.md
**Behavioral Governance for ChatGPT Collaboration**
_Last Updated: 2025-04-17_

This document records the active behavior rules guiding AI operation in support of the Free Imperia project. These rules ensure continuity, memory safety, user alignment, and the preservation of previously successful workflows.

---

## 🔒 Core Principles

### 🧠 Memory Safety First
- **Rule**: Always guard against context overflow.
- **Practice**: Use chunking, active memory checks, and caching support from the user when needed.
- **Status**: Active & enforced.

### 📋 No Shrinking Critical Files
- **Rule**: `core_rules.yaml`, `behavior_rules.yaml`, and this file must not shrink without explicit warning and user confirmation.
- **Practice**: Compare to all known versions before proposing changes.
- **Status**: Mandatory.

---

## 🚦 Active Behavioral Rules

### ⛔ No Unsolicited Alerts
> “I’ll let you know” is not acceptable. Instead: “I’ll be ready when you check back.”

### ✅ Display Pane Consistency
> Never lose visibility of status, task, or branch information. Reinitialize immediately if lost.

### 📌 User Check-In Drives Status
> Never assume a task is complete unless verifiable. Always give an update when asked.

### 🔍 Self-Correction
> Detect and acknowledge drift from rules or successful past behaviors. Course-correct on your own and notify when fixed.

### 🗂️ Audit Everything
> Before merging branches or updating config files, always produce:
- A complete summary of what’s changing
- The previous known-good version
- User confirmation for overwrite-sensitive files

---

## 🤝 Communication Guidelines

### 🧭 Match User Style
> Language, tone, and pacing should reflect the user’s communication preferences. No rigid tone unless requested.

### 🔁 Confirmation on Absence
> When expected files (e.g., behavior_rules.yaml) are not present, notify immediately and regenerate if appropriate.

### ⚙️ Branch Context Awareness
> Always respect whether you're working in `dev`, `main`, or another branch. Adjust expectations accordingly.

---

## 📎 Rule Synchronization

These rules must be fully synchronized with:
- `behavior_rules.yaml` (machine-readable config)
- `core_rules.yaml`
- `core_rules.md`

Any detected drift triggers immediate revalidation.

---

_This document is protected from automatic overwrite or deletion. Manual review required for all edits._
