import json
import networkx as nx

def load_relationships_from_jsonl(filepath):
    relationships = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            relationships.append(json.loads(line))
    return relationships

def build_graph(relationships):
    G = nx.DiGraph()
    for rel in relationships:
        src = rel["source"]
        tgt = rel["target"]
        rel_type = rel.get("type", "unspecified")
        G.add_node(src)
        G.add_node(tgt)
        G.add_edge(src, tgt, type=rel_type)
    return G

def export_graph(G, output_path):
    nx.write_gml(G, output_path)
    print(f"Graph exported to {output_path}")

def main():
    input_file = "data/extracted_relationships.jsonl"
    output_file = "data/wiki_graph.gml"

    relationships = load_relationships_from_jsonl(input_file)
    G = build_graph(relationships)
    export_graph(G, output_file)

if __name__ == "__main__":
    main()
