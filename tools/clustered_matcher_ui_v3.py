import os
import json
import streamlit as st
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

st.set_page_config(page_title="Clustered Matcher UI v3", layout="wide")
st.title("🧠 Clustered Matcher UI v3")

# Load phrases
with open("output/unmatched_phrases.txt", "r", encoding="utf-8") as f:
    phrases = [line.strip() for line in f if line.strip()]

# Load tagged phrases for auto-skip
tagged_jsonl = "tagged/relationships_tagged.jsonl"
already_tagged = set()
if os.path.exists(tagged_jsonl):
    with open(tagged_jsonl, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                already_tagged.add(obj["text"])
            except:
                pass

# Filter out already-tagged phrases
phrases_to_cluster = [p for p in phrases if p not in already_tagged]
st.write(f"📄 Loaded {len(phrases)} unmatched phrases ({len(phrases_to_cluster)} remaining after tag filter).")

# Vectorize and cluster
vectorizer = TfidfVectorizer(stop_words="english").fit(phrases_to_cluster)
X = vectorizer.transform(phrases_to_cluster)
clustering = DBSCAN(eps=0.5, min_samples=2, metric="cosine").fit(X)
labels = clustering.labels_

clusters = defaultdict(list)
for idx, label in enumerate(labels):
    if label != -1:
        clusters[label].append(phrases_to_cluster[idx])

cluster_ids = sorted(clusters.keys())

# Track skipped clusters
SKIPPED_FILE = "tagged/skipped_clusters.txt"
skipped_clusters = set()
if os.path.exists(SKIPPED_FILE):
    with open(SKIPPED_FILE, "r", encoding="utf-8") as f:
        skipped_clusters = set(map(int, f.read().splitlines()))

# Cluster selection UI
st.sidebar.header("🔍 Cluster Navigation")
cluster_ids_to_show = [cid for cid in cluster_ids if cid not in skipped_clusters]
if not cluster_ids_to_show:
    st.sidebar.warning("🎉 All clusters have been processed or skipped!")
    st.stop()

selected_cluster = st.sidebar.selectbox("Select Cluster", cluster_ids_to_show)

current_cluster = clusters[selected_cluster]
st.subheader(f"🧩 Cluster {selected_cluster} ({len(current_cluster)} phrases)")

checked_phrases = []
with st.form(f"form_{selected_cluster}"):
    st.markdown("### ✍️ Select Phrases to Tag")
    for idx, phrase in enumerate(current_cluster):
        if st.checkbox(phrase, key=f"chk_{idx}_{phrase}"):
            checked_phrases.append(phrase)

    st.markdown("### 🏷️ Tag Selected Phrases")
    rel_name = st.text_input("Relationship Name (e.g., 'commands', 'wields')")
    pattern_hint = st.text_area("Pattern(s) - one per line", placeholder="{source} is a bodyguard to {target}")
    submit_tag = st.form_submit_button("✅ Tag Selected")

# Skip option
if st.button("⏭️ Skip This Cluster"):
    with open(SKIPPED_FILE, "a", encoding="utf-8") as sf:
        sf.write(str(selected_cluster) + "\n")
    st.rerun()

# ✅ NEW: Copyable phrase preview
with st.expander("📋 Copyable Phrase Preview"):
    st.code("\n".join(current_cluster), language="text")

# Handle tagging
if submit_tag and rel_name and checked_phrases:
    patterns = [line.strip() for line in pattern_hint.split("\n") if line.strip()]
    rel_entry = {"name": rel_name, "patterns": patterns}
    os.makedirs("tagged", exist_ok=True)
    yaml_file = "tagged/relationships_expanded.yaml"
    jsonl_file = "tagged/relationships_tagged.jsonl"

    try:
        import yaml
        if os.path.exists(yaml_file):
            with open(yaml_file, "r", encoding="utf-8") as f:
                existing = yaml.safe_load(f) or {}
        else:
            existing = {}
        existing.setdefault("relationships", []).append(rel_entry)
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(existing, f, allow_unicode=True)
        st.success("✅ Appended to relationships_expanded.yaml")
    except Exception as e:
        st.error(f"❌ YAML Error: {e}")

    try:
        with open(jsonl_file, "a", encoding="utf-8") as jf:
            for phrase in checked_phrases:
                jf.write(json.dumps({
                    "text": phrase,
                    "relationship": rel_name,
                    "score": 1.0,
                    "linked_entities": [],
                    "source_page": "manual",
                    "category": "manual"
                }, ensure_ascii=False) + "\n")
        st.success("✅ Appended to relationships_tagged.jsonl")
        st.rerun()
    except Exception as e:
        st.error(f"❌ JSONL Error: {e}")
