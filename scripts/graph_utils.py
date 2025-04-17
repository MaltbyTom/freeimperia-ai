import networkx as nx
import matplotlib.pyplot as plt

def load_gml_graph(filepath):
    try:
        G = nx.read_gml(filepath)
        print(f"Loaded graph with {len(G.nodes())} nodes and {len(G.edges())} edges.")
        return G
    except Exception as e:
        print(f"Failed to load graph: {e}")
        return None

def draw_graph(G, layout="spring", with_labels=True, node_size=500, font_size=8):
    if layout == "spring":
        pos = nx.spring_layout(G)
    elif layout == "kamada_kawai":
        pos = nx.kamada_kawai_layout(G)
    elif layout == "circular":
        pos = nx.circular_layout(G)
    else:
        pos = nx.spring_layout(G)

    edge_labels = nx.get_edge_attributes(G, 'type')
    nx.draw(G, pos, with_labels=with_labels, node_size=node_size, font_size=font_size, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
    plt.show()