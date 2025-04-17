import os
import re
import json
from bs4 import BeautifulSoup

def extract_relationships_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    wikilinks = re.findall(r"\[\[(.*?)\]\]", text)
    relationships = []

    for source in set(wikilinks):
        source_clean = source.split("|")[0].strip()
        for target in wikilinks:
            target_clean = target.split("|")[0].strip()
            if source_clean != target_clean:
                relationships.append({
                    "source": f"[[{source_clean}]]",
                    "target": f"[[{target_clean}]]",
                    "type": "mentions"
                })

    return relationships

def crawl_directory_for_relationships(root_dir):
    all_relationships = []
    for subdir, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith(".txt"):
                filepath = os.path.join(subdir, filename)
                relationships = extract_relationships_from_file(filepath)
                all_relationships.extend(relationships)
    return all_relationships

def main():
    input_dir = "data/wiki_pages"
    output_file = "data/extracted_relationships.jsonl"

    relationships = crawl_directory_for_relationships(input_dir)
    with open(output_file, "w", encoding="utf-8") as f:
        for relation in relationships:
            json.dump(relation, f)
            f.write("\n")

    print(f"Extracted {len(relationships)} relationships to {output_file}")

if __name__ == "__main__":
    main()
