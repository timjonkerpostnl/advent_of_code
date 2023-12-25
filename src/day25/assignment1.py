import networkx as nx
from matplotlib import pyplot as plt
from shapely import Polygon
from tqdm import tqdm


def build_graph(file_name: str) -> nx.Graph:
    with open(file_name) as f:
        graph = nx.Graph()
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            node1, connected_to = stripped_line.split(": ")
            for node2 in connected_to.split(" "):
                graph.add_edge(node1, node2)
    return graph


def process_file(file_name: str) -> int:
    graph = build_graph(file_name)

    min_edge_cut = nx.minimum_edge_cut(graph)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edges(graph, pos, edgelist=min_edge_cut, edge_color='r', width=2)
    plt.show()

    graph.remove_edges_from(min_edge_cut)
    components = nx.connected_components(graph)
    product = 1
    for component in components:
        product *= len(component)

    return product


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
