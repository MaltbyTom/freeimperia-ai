import os
import re
import yaml
import json
import spacy
import argparse
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

nlp = spacy.load("en_core_web_md")

# Load relationship patterns from YAML
def load_relationships(yaml_path="relationships.yaml"):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)["relationships"]

# Scrape from entities index instead of sitemap
def get_links_from_index_page(index_url):
    res = requests.get(index_url)
    soup = BeautifulSoup(res.text, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/fiwiki/doku.php?id="):
            full_url = "https://www.freeimperia.com" + href
            urls.append(full_url)
    return list(set(urls))

# Get clean text from wiki page
def extract_text_from_url(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        content = soup.find("div", {"class": "page"})
        return content.get_text(separator="\n") if content else ""
    except Exception as e:
        print(f"[!] Error reading {url}: {e}")
        return ""

# Create spaCy docs for patterns
def prepare_pattern_docs(patterns):
    docs = []
    for entry in patterns:
        for pattern in entry.get("patterns", []):
            docs.append({
                "name": entry["name"],
                "pattern": pattern,
                "doc": nlp(pattern)
            })
    return docs

# Generate title from URL
def get_title_from_url(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    page = qs.get("id", [""])[0]
    return page.replace("_", " ").title()

# Split names into alias fragments
def generate_aliases(name):
    parts = name.split(" ")
    aliases = set([name])
    if len(parts) > 1:
        aliases.update(parts)
    return list(aliases)

# Match relationships semantically
def match_relationships(text, title, pattern_docs, threshold=0.85):
    doc = nlp(text)
    matches = []
    unmatched = []

    for sent in doc.sents:
        sent_text = sent.text.strip()
        sent_doc = nlp(sent_text)
        best = None
        best_score = 0
        for pattern in pattern_docs:
            score = sent_doc.similarity(pattern["doc"])
            if score > threshold and score > best_score:
                best = pattern
                best_score = score

        if best:
            matches.append({
                "source": title,
                "sentence": sent_text,
                "relationship": best["name"],
                "pattern": best["pattern"],
                "similarity": round(best_score, 3)
            })
        else:
            if any(word in sent_text.lower() for word in ["worship", "serve", "son", "champion", "grudge", "student"]):
                unmatched.append(sent_text)
    return matches, unmatched

# Main function
def run_extraction(test=False, output_dir="output", yaml_path="relationships.yaml"):
    os.makedirs(output_dir, exist_ok=True)
    patterns = load_relationships(yaml_path)
    pattern_docs = prepare_pattern_docs(patterns)

    index_page = "https://www.freeimperia.com/fiwiki/doku.php?id=start&do=index"
    urls = get_links_from_index_page(index_page)

    if test:
        urls = [u for u in urls if any(x in u.lower() for x in ["mica", "eltan", "kane"])]
        output_dir = os.path.join(output_dir, "test")
        os.makedirs(output_dir, exist_ok=True)

    relationships = []
    unmatched = []
    entity_map = {}

    for url in tqdm(urls, desc="Processing pages"):
        title = get_title_from_url(url)
        text = extract_text_from_url(url)
        rels, unmatch = match_relationships(text, title, pattern_docs)
        relationships.extend(rels)
        unmatched.extend(unmatch)
        entity_map[title] = {
            "id": title,
            "url": url,
            "aliases": generate_aliases(title)
        }

    # Output relationships
    with open(os.path.join(output_dir, "relationships.jsonl"), "w", encoding="utf-8") as f:
        for r in relationships:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # Output unmatched phrases
    with open(os.path.join(output_dir, "unmatched_phrases.txt"), "w", encoding="utf-8") as f:
        for phrase in unmatched:
            f.write(phrase + "\n")

    # Output node-link graph
    graph = {
        "nodes": [],
        "links": []
    }
    added_nodes = set()

    for rel in relationships:
        src = rel["source"]
        target_guess = rel["sentence"].split()[-1]
        src_url = entity_map[src]["url"]
        tgt_url = entity_map.get(target_guess, {}).get("url", "")

        if src not in added_nodes:
            graph["nodes"].append({"id": src, "url": src_url})
            added_nodes.add(src)
        if target_guess not in added_nodes:
            graph["nodes"].append({"id": target_guess, "url": tgt_url})
            added_nodes.add(target_guess)

        graph["links"].append({
            "source": src,
            "target": target_guess,
            "label": rel["relationship"]
        })

    with open(os.path.join(output_dir, "graph_data.json"), "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    print(f"✅ Extracted {len(relationships)} relationships.")
    print(f"🧠 Logged {len(unmatched)} unmatched candidate phrases.")
    print(f"🌐 Graph file written to graph_data.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Run in test mode on selected pages")
    parser.add_argument("--output", default="output", help="Output directory")
    parser.add_argument("--yaml", default="relationships.yaml", help="YAML file path")
    args = parser.parse_args()

    run_extraction(test=args.test, output_dir=args.output, yaml_path=args.yaml)