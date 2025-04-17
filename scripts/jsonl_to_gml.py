import networkx as nx
import json

def jsonl_to_gml(jsonl_path, gml_path):
    G = nx.DiGraph()

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            record = json.loads(line.strip())

            source = record.get("source")
            target = record.get("target")
            relation = record.get("relation")

            # Ensure nodes exist
            if source not in G:
                G.add_node(source, label=source)
            if target not in G:
                G.add_node(target, label=target)

            # Add the edge with relation as an attribute
            G.add_edge(source, target, type=relation)

    nx.write_gml(G, gml_path)
    print(f"GML file saved to: {gml_path}")