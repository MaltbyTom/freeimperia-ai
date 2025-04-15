import streamlit as st
import yaml
import os
import re
from pathlib import Path

DEFAULT_FILE = "output/unmatched_phrases.txt"
STORAGE_YAML = "relationships_expanded.yaml"
SKIPPED_FILE = "skipped_phrases.txt"

st.set_page_config(layout="wide")
st.title("🧠 Relationship Pattern Tagger v2")

# Load unmatched phrases
@st.cache_data
def load_phrases(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return sorted(set(lines))

# Load YAML
def load_yaml(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return yaml.safe_load(f).get("relationships", [])
    return []

# Save YAML
def save_yaml(relationship_dict, filename=STORAGE_YAML):
    with open(filename, "w", encoding="utf-8") as f:
        yaml.dump({"relationships": relationship_dict}, f, allow_unicode=True)
    st.success(f"Saved updated YAML to {filename}")

# Save skipped phrases
def save_skipped(skipped_set):
    with open(SKIPPED_FILE, "w", encoding="utf-8") as f:
        for phrase in sorted(skipped_set):
            f.write(phrase + "\n")
    st.success(f"Saved skipped phrases to {SKIPPED_FILE}")

# Add pattern to YAML safely
def add_to_yaml(existing, new_type, new_pattern):
    for entry in existing:
        if entry["name"] == new_type:
            if new_pattern not in entry["patterns"]:
                entry["patterns"].append(new_pattern)
            return
    existing.append({"name": new_type, "patterns": [new_pattern]})

# Basic target suggestion
def suggest_target_phrase(phrase):
    words = phrase.split()
    stopwords = ["the", "a", "an", "to", "of", "with", "in", "on", "by"]
    candidates = [w for w in words if w[0].isupper() and w.lower() not in stopwords]
    if candidates:
        phrase_escaped = re.escape(candidates[-1])
        return re.sub(rf"\b{phrase_escaped}\b", "{target}", phrase, count=1)
    return phrase

# Load files
phrase_file = st.text_input("📄 Path to unmatched_phrases.txt", value=DEFAULT_FILE)
phrases = load_phrases(phrase_file)
existing_yaml = load_yaml(STORAGE_YAML)
skipped_phrases = set(load_phrases(SKIPPED_FILE))

# Remove previously skipped
filtered_phrases = [p for p in phrases if p not in skipped_phrases]
st.write(f"Loaded {len(filtered_phrases)} phrases to review.")

# Phrase browsing
idx = st.number_input("📍 Phrase index", min_value=0, max_value=len(filtered_phrases)-1, value=0, step=1)
current = filtered_phrases[idx]
suggested = suggest_target_phrase(current)

st.subheader("📌 Current Phrase")
st.code(current)

existing_types = sorted(set(e["name"] for e in existing_yaml))
rel_type = st.selectbox("🏷️ Relationship type", options=existing_types + ["<new>"])
if rel_type == "<new>":
    rel_type = st.text_input("🔤 Enter new relationship type")

pattern = st.text_input("✏️ Pattern (use {target})", value=suggested)

# Tagging buttons
col1, col2, col3 = st.columns(3)
if col1.button("✅ Add to YAML"):
    add_to_yaml(existing_yaml, rel_type.strip(), pattern.strip())
    save_yaml(existing_yaml)

if col2.button("⏭️ Skip Phrase"):
    pass  # Do nothing

if col3.button("🚫 Not a Relationship"):
    skipped_phrases.add(current)
    save_skipped(skipped_phrases)

# YAML and skipped views
if st.checkbox("📖 Show current YAML"):
    st.code(yaml.dump({"relationships": existing_yaml}, allow_unicode=True), language="yaml")

if st.checkbox("📤 Show skipped phrases"):
    st.code("\n".join(sorted(skipped_phrases)))