import json
import os
import spacy
from difflib import get_close_matches
from pathlib import Path
from collections import defaultdict

nlp = spacy.load("en_core_web_md")

# Paths
JSONL_FILE = "relationships_tagged.jsonl"
GRAPH_FILE = "graph_data.json"
WIKI_CACHE_FILE = "output/wiki_pages.json"

def load_existing_graph():
    if not os.path.exists(GRAPH_FILE):
        return {"nodes": [], "edges": []}
    with open(GRAPH_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_tagged_jsonl():
    with open(JSONL_FILE, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def load_wiki_pages():
    if not os.path.exists(WIKI_CACHE_FILE):
        raise FileNotFoundError("Missing wiki cache: " + WIKI_CACHE_FILE)
    with open(WIKI_CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def fuzzy_match(name, known_entities, cutoff=0.8):
    matches = get_close_matches(name, known_entities, n=1, cutoff=cutoff)
    return matches[0] if matches else None

def extract_named_entities(text):
    doc = nlp(text)
    return list(set(ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE", "NORP"]))

def add_node(graph, node_id, label=None, node_type="entity"):
    if not any(n["id"] == node_id for n in graph["nodes"]):
        graph["nodes"].append({
            "id": node_id,
            "label": label or node_id,
            "type": node_type
        })

def add_edge(graph, source, target, label, context=None):
    if not any(e["source"] == source and e["target"] == target and e["label"] == label for e in graph["edges"]):
        edge = {"source": source, "target": target, "label": label}
        if context:
            edge["context"] = context
        graph["edges"].append(edge)

def run_conversion():
    print("🔄 Loading files...")
    tagged = load_tagged_jsonl()
    wiki = load_wiki_pages()
    graph = load_existing_graph()
    known_entities = set(wiki.keys())

    print(f"📑 Found {len(tagged)} tagged patterns.")

    for entry in tagged:
        pattern = entry.get("pattern")
        rel_type = entry.get("relationship")
        context = entry.get("text")
        linked = entry.get("linked_entities", [])

        # If we have links, prefer them directly
        if len(linked) >= 2:
            source = linked[0]
            target = linked[1]
            add_node(graph, source)
            add_node(graph, target)
            add_edge(graph, source, target, rel_type, context)
        else:
            # Fallback to NER + fuzzy match
            ents = extract_named_entities(context)
            if len(ents) >= 2:
                src = fuzzy_match(ents[0], known_entities)
                tgt = fuzzy_match(ents[1], known_entities)
                if src and tgt:
                    add_node(graph, src)
                    add_node(graph, tgt)
                    add_edge(graph, src, tgt, rel_type, context)

    with open(GRAPH_FILE, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)

    print(f"✅ Graph saved to {GRAPH_FILE}")
    print(f"🧠 Nodes: {len(graph['nodes'])}, Edges: {len(graph['edges'])}")

if __name__ == "__main__":
    run_conversion()
