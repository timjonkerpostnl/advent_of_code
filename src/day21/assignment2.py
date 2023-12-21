from typing import Tuple

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
from shapely import Polygon
import shapely.plotting

from src.day18.assignment1 import build_exterior
from src.day21.assignment1 import create_graph


def process_file(file_name: str, max_length) -> int:
    graph, start = create_graph(file_name)

    x = []
    for max_length in [65, 130, 195]:
        paths = nx.single_source_shortest_path_length(graph, start, max_length)
        reachable_nodes = [node for node in graph.nodes if node in paths and paths[node] % 2 == 0]
        x.append(len(reachable_nodes))

    # node_colors = ["g" if node in reachable_nodes else "r" for node in graph.nodes]
    # nx.draw(graph, pos={n: (n[1], 11 - n[0]) for n in graph.nodes}, node_color=node_colors, with_labels=True)
    # plt.show()
    return len(reachable_nodes)


if __name__ == "__main__":
    result = process_file("input.txt", 64)
    print(result)
