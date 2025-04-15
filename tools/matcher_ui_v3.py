import streamlit as st
import yaml
import os
import re
from pathlib import Path

DEFAULT_FILE = "output/unmatched_phrases.txt"
STORAGE_YAML = "relationships_expanded.yaml"
SKIPPED_FILE = "skipped_phrases.txt"

st.set_page_config(layout="wide")
st.title("🧠 Relationship Pattern Tagger v3")

@st.cache_data
def load_phrases(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return sorted(set(lines))

def load_yaml(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return yaml.safe_load(f).get("relationships", [])
    return []

def save_yaml(relationship_dict, filename=STORAGE_YAML):
    with open(filename, "w", encoding="utf-8") as f:
        yaml.dump({"relationships": relationship_dict}, f, allow_unicode=True)
    st.success(f"Saved updated YAML to {filename}")

def save_skipped(skipped_set):
    with open(SKIPPED_FILE, "w", encoding="utf-8") as f:
        for phrase in sorted(skipped_set):
            f.write(phrase + "\n")
    st.success(f"Saved skipped phrases to {SKIPPED_FILE}")

def add_to_yaml(existing, rel_type, patterns):
    for entry in existing:
        if entry["name"] == rel_type:
            for pat in patterns:
                if pat not in entry["patterns"]:
                    entry["patterns"].append(pat)
            return
    existing.append({"name": rel_type, "patterns": patterns})

phrase_file = st.text_input("📄 Path to unmatched_phrases.txt", value=DEFAULT_FILE)
phrases = load_phrases(phrase_file)
existing_yaml = load_yaml(STORAGE_YAML)
skipped_phrases = set(load_phrases(SKIPPED_FILE))
filtered_phrases = [p for p in phrases if p not in skipped_phrases]

batch_size = st.slider("🔢 Batch size", 1, 10, 3)
batch_start = st.number_input("📍 Batch start index", 0, len(filtered_phrases)-1, 0, step=batch_size)
batch_end = min(batch_start + batch_size, len(filtered_phrases))
current_batch = filtered_phrases[batch_start:batch_end]

st.subheader("📌 Current Phrases")
for i, phrase in enumerate(current_batch):
    st.code(f"[{batch_start+i}] {phrase}")

existing_types = sorted(set(e["name"] for e in existing_yaml))
rel_type = st.selectbox("🏷️ Relationship type", options=existing_types + ["<new>"])
if rel_type == "<new>":
    rel_type = st.text_input("🔤 Enter new relationship type")

targets_input = st.text_input("🎯 Targets (comma-separated)", value="")
multi_patterns = [t.strip() for t in targets_input.split(",") if t.strip()]

col1, col2, col3 = st.columns(3)
if col1.button("✅ Add to YAML"):
    add_to_yaml(existing_yaml, rel_type.strip(), multi_patterns)
    save_yaml(existing_yaml)

if col2.button("🚫 Mark All as Not Relationships"):
    skipped_phrases.update(current_batch)
    save_skipped(skipped_phrases)

if col3.button("💾 Save Only"):
    save_yaml(existing_yaml)
    save_skipped(skipped_phrases)

if st.checkbox("📖 Show current YAML"):
    st.code(yaml.dump({"relationships": existing_yaml}, allow_unicode=True), language="yaml")

if st.checkbox("📤 Show skipped phrases"):
    st.code("\n".join(sorted(skipped_phrases)))
