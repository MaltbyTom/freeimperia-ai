import os
import re
import json
import requests
import argparse
import yaml
import spacy
from bs4 import BeautifulSoup
from collections import defaultdict
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_md")

BASE_INDEX_URL = "https://freeimperia.com/fiwiki/doku.php?id=start&do=index"
BASE_PAGE_URL = "https://freeimperia.com/fiwiki/doku.php?id="

OUTPUT_DIR = "output"
WIKI_CACHE_FILE = os.path.join(OUTPUT_DIR, "wiki_pages.json")

def convert_links_to_wikistyle(html):
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a", href=True):
        href = a.get("href", "")
        if "doku.php?id=" in href:
            target = href.split("id=")[-1]
            label = a.get_text(strip=True)
            link = f"[[{target}|{label}]]"
            a.replace_with(link)
    return soup.get_text(separator=" ", strip=True)

def categorize_sentence(sentence):
    sentence_lower = sentence.lower()
    if any(kw in sentence_lower for kw in ["level:", "components:", "duration:", "casting time:", "area of effect:", "saving throw:", "range:", "source:", "author:"]):
        return "spell_metadata"
    if any(kw in sentence_lower for kw in ["aka", "field of", "created by", "authored by"]):
        return "authorship"
    return "general"

def download_all_wiki_pages(limit=None):
    print("🌐 Fetching wiki index...")
    res = requests.get(BASE_INDEX_URL)
    soup = BeautifulSoup(res.text, "html.parser")
    page_links = soup.select("li.level1 a.wikilink1")
    print(f"🔗 Found {len(page_links)} links on index page.")

    pages = {}
    seen = set()
    links = page_links[:limit] if limit else page_links

    for link in tqdm(links, desc="📥 Downloading wiki pages"):
        href = link.get("href", "")
        if "id=" in href:
            page_id = href.split("id=")[-1]
            page_id = page_id.replace("+", " ")
            if page_id in seen:
                continue
            seen.add(page_id)
            url = BASE_PAGE_URL + page_id
            try:
                page_res = requests.get(url)
                page_soup = BeautifulSoup(page_res.text, "html.parser")
                content_div = page_soup.find("div", class_="page")
                if content_div:
                    html = str(content_div)
                    wikified = convert_links_to_wikistyle(html)
                    if wikified:
                        pages[page_id] = wikified
            except Exception as e:
                print(f"❌ Failed to load {url}: {e}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(WIKI_CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=2)
    print(f"✅ Cached {len(pages)} wiki pages to {WIKI_CACHE_FILE}")
    return pages

def extract_docuwiki_links(text):
    return re.findall(r"\[\[(.*?)\]\]", text)

def clean_links(raw_text):
    return re.sub(r"\[\[(.*?)\]\]", lambda m: m.group(1).split("|")[0], raw_text)

def extract_sentences_with_links(raw_text):
    links = re.findall(r"\[\[(.*?)\]\]", raw_text)
    clean_text = clean_links(raw_text)
    doc = nlp(clean_text)
    sentences = []
    for sent in doc.sents:
        sent_text = sent.text.strip()
        matched = [l.split("|")[0] for l in links if l.split("|")[-1] in sent_text]
        # Always include the sentence, even if matched is empty
        sentences.append({
            "text": sent_text,
            "linked": matched
        })
    return sentences

def load_patterns(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f).get("relationships", [])

def match_patterns(text, patterns, threshold=0.85):
    doc_vec = nlp(text).vector.reshape(1, -1)
    matches = []
    for entry in patterns:
        name = entry["name"]
        for pat in entry["patterns"]:
            pat_vec = nlp(pat).vector.reshape(1, -1)
            sim = cosine_similarity(doc_vec, pat_vec)[0][0]
            if sim >= threshold:
                matches.append((name, sim))
    return sorted(matches, key=lambda x: -x[1])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Download only first 5 pages")
    parser.add_argument("--pages", type=str, default=WIKI_CACHE_FILE)
    parser.add_argument("--yaml", type=str, default="relationships_expanded.yaml")
    parser.add_argument("--output", type=str, default="output/relationships.jsonl")
    parser.add_argument("--unmatched", type=str, default="output/unmatched_phrases.txt")
    parser.add_argument("--threshold", type=float, default=0.85)
    args = parser.parse_args()

    if not os.path.exists(args.pages):
        wiki = download_all_wiki_pages(limit=5 if args.test else None)
    else:
        with open(args.pages, "r", encoding="utf-8") as f:
            wiki = json.load(f)

    patterns = load_patterns(args.yaml)
    found = []
    unmatched = set()

    for title, raw in tqdm(wiki.items(), desc="🔍 Extracting relationships"):
        sentences = extract_sentences_with_links(raw)
        for entry in sentences:
            sentence = entry["text"]
            linked = entry["linked"]
            matches = match_patterns(sentence, patterns, threshold=args.threshold)
            if matches:
                for rel, score in matches:
                    found.append({
                        "text": sentence,
                        "relationship": rel,
                        "score": float(round(score, 3)),
                        "linked_entities": linked,
                        "source_page": title,
                        "category": categorize_sentence(sentence)
                    })
            else:
                unmatched.add(sentence)

    with open(args.output, "w", encoding="utf-8") as f:
        for line in found:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")

    with open(args.unmatched, "w", encoding="utf-8") as f:
        for phrase in sorted(unmatched):
            f.write(phrase + "\n")

    print(f"✅ Wrote {len(found)} matched relationships.")
    print(f"🧠 Logged {len(unmatched)} unmatched phrases.")

if __name__ == "__main__":
    main()
