import streamlit as st
import json
import pandas as pd
from collections import Counter
import yaml
from io import StringIO

st.set_page_config(layout="wide", page_title="📚 Tag Index Viewer v3")

TAG_FILE = "tag_index.json"

@st.cache_data
def load_index():
    with open(TAG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_yaml_export(data, selected_tag):
    return yaml.dump({
        "relationships": [{
            "name": selected_tag,
            "patterns": data[selected_tag]["patterns"]
        }]
    }, allow_unicode=True)

def generate_jsonl_export(occurrences):
    return "\n".join([json.dumps({
        "pattern": occ.get("pattern"),
        "relationship": selected_tag,
        "source": occ.get("source"),
        "target": occ.get("target")
    }, ensure_ascii=False) for occ in occurrences])

data = load_index()
st.title("📚 Relationship Tag Index Explorer v3")

rel_types = sorted(data.keys())
selected_tag = st.selectbox("🧠 Select a relationship type", rel_types)

if selected_tag:
    rel_data = data[selected_tag]
    patterns = rel_data.get("patterns", [])
    occurrences = rel_data.get("occurrences", [])

    st.subheader(f"🏷 Patterns for `{selected_tag}`")
    st.code("\n".join(patterns), language="yaml")

    st.subheader("📊 Pattern Usage Frequency")
    pat_counts = Counter([o["pattern"] for o in occurrences])
    df_counts = pd.DataFrame(pat_counts.items(), columns=["Pattern", "Count"])
    st.bar_chart(df_counts.set_index("Pattern"))

    st.subheader("🔍 Pattern Drilldown")
    selected_pat = st.selectbox("Select a pattern to explore", sorted(set(p["pattern"] for p in occurrences)))
    filtered = [o for o in occurrences if o["pattern"] == selected_pat]

    annotations = []

    for i, occ in enumerate(filtered):
        with st.expander(f"[{i+1}] {occ.get('context')[:60]}..."):
            st.markdown(f"**Pattern:** `{occ.get('pattern')}`")
            st.markdown(f"**Source:** `{occ.get('source')}`")
            st.markdown(f"**Target:** `{occ.get('target')}`")
            st.code(occ.get("context"))
            comment = st.text_input(f"💬 Comment on [{i+1}]", key=f"comment_{i}")
            flag = st.checkbox(f"⚠️ Mark as needs review", key=f"flag_{i}")
            if comment or flag:
                annotations.append({
                    "index": i + 1,
                    "pattern": occ.get("pattern"),
                    "source": occ.get("source"),
                    "target": occ.get("target"),
                    "context": occ.get("context"),
                    "comment": comment,
                    "flagged": flag
                })

    st.subheader("📝 Export Annotated Comments")
    if annotations:
        if st.download_button("⬇️ Download Review Notes", data=json.dumps(annotations, indent=2, ensure_ascii=False),
                              file_name="review_notes.json"):
            st.success("Comments exported")

    st.subheader("📤 Export Options")
    col1, col2 = st.columns(2)
    with col1:
        if st.download_button("⬇️ Export to YAML", generate_yaml_export(data, selected_tag),
                              file_name=f"{selected_tag}.yaml"):
            st.success("Exported YAML")
    with col2:
        if st.download_button("⬇️ Export to JSONL", generate_jsonl_export(occurrences),
                              file_name=f"{selected_tag}.jsonl"):
            st.success("Exported JSONL")
