import re
import json

def extract_concepts_from_edges(input_path, output_path):
    concepts = set()

    with open(input_path, "r", encoding="utf-8") as infile:
        for line in infile:
            edge = json.loads(line.strip())
            for key in ("source", "target"):
                match = re.match(r"\[\[(.*?)\]\]", edge[key])
                if match:
                    concepts.add(match.group(1))

    with open(output_path, "w", encoding="utf-8") as outfile:
        for concept in sorted(concepts):
            outfile.write(concept + "\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python graph_concepts_extractor.py <input_jsonl> <output_txt>")
        sys.exit(1)

    extract_concepts_from_edges(sys.argv[1], sys.argv[2])
