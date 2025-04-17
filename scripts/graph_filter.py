import json

def filter_edges(input_path, output_path, filter_fn):
    with open(input_path, "r", encoding="utf-8") as infile:
        edges = [json.loads(line.strip()) for line in infile]

    filtered_edges = [edge for edge in edges if filter_fn(edge)]

    with open(output_path, "w", encoding="utf-8") as outfile:
        for edge in filtered_edges:
            outfile.write(json.dumps(edge, ensure_ascii=False) + "\n")

def example_filter(edge):
    # Example: Only keep edges where relation is not "mentions"
    return edge["relation"] != "mentions"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python graph_filter.py <input_jsonl> <output_jsonl>")
        sys.exit(1)

    filter_edges(sys.argv[1], sys.argv[2], example_filter)
