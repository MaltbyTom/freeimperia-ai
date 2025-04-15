import os
import re
import json
import spacy
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load spaCy model for semantic features
nlp = spacy.load("en_core_web_md")

# Config
INPUT_FILE = "output/unmatched_phrases.txt"
OUTPUT_JSONL = "output/scored_phrases.jsonl"
NUM_CLUSTERS = 100

def clean(phrase):
    return re.sub(r"[^\w\s]", "", phrase).strip().lower()

def get_confidence(phrase):
    # Simple heuristics
    score = 0
    if any(word in phrase.lower() for word in ["worship", "serve", "grudge", "knight", "champion", "devoted"]):
        score += 2
    if len(phrase) < 120:
        score += 1
    if re.search(r"[A-Z][a-z]+", phrase):
        score += 1
    if "{" in phrase or "}" in phrase:
        score -= 1
    return min(score, 5)

def score_phrases(phrases):
    docs = [nlp(p) for p in phrases]
    scored = []
    for i, doc in enumerate(docs):
        score = get_confidence(phrases[i])
        scored.append({
            "text": phrases[i],
            "score": score,
            "vector": doc.vector.tolist()
        })
    return scored

def cluster_phrases(scored):
    vectors = [entry["vector"] for entry in scored]
    tfidf = TfidfVectorizer().fit_transform([s["text"] for s in scored])
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42).fit(tfidf)
    for i, label in enumerate(kmeans.labels_):
        scored[i]["cluster"] = int(label)
    return scored

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = [line.strip() for line in f if line.strip()]
    raw = sorted(set(raw))
    print(f"Loaded {len(raw)} phrases.")

    scored = score_phrases(raw)
    clustered = cluster_phrases(scored)

    with open(OUTPUT_JSONL, "w", encoding="utf-8") as f:
        for entry in clustered:
            out = {
                "text": entry["text"],
                "score": entry["score"],
                "cluster": entry["cluster"]
            }
            f.write(json.dumps(out, ensure_ascii=False) + "\n")

    print(f"✅ Wrote scored + clustered output to {OUTPUT_JSONL}")

if __name__ == "__main__":
    main()
