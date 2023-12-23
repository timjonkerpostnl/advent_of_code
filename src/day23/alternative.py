import datetime
from collections import defaultdict
from typing import List, Tuple

import networkx as nx
from matplotlib import pyplot as plt
from tqdm import tqdm


def get_graph(file_name):
    with open(file_name) as f:
        maze = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            maze.append(stripped_line)

        graph = nx.Graph()
        source = (0, maze[0].find("."))
        target = (len(maze) - 1, maze[-1].find("."))
        for row_idx, row in enumerate(maze):
            for col_idx, value in enumerate(row):
                if value in ".><v^":
                    if row_idx < len(maze) - 1 and maze[row_idx + 1][col_idx] not in "#":
                        graph.add_edge((row_idx, col_idx), (row_idx + 1, col_idx))
                    if col_idx < len(maze[0]) - 1 and maze[row_idx][col_idx + 1] not in "#":
                        graph.add_edge((row_idx, col_idx), (row_idx, col_idx + 1))

        # nx.draw(graph, pos={n: (n[1], len(maze) - n[0]) for n in graph.nodes})
        # plt.show()
    return graph, source, target


def build_junction_graph(graph, source, target):
    junction_graph = nx.Graph()
    junctions = [source] + [n for n in graph.nodes if len(list(graph.neighbors(n))) >= 3] + [target]
    for junction in junctions[:-1]:
        paths = []
        for neighbor in list(graph.neighbors(junction)):
            paths.append([junction, neighbor])
        for path in paths:
            while path[-1] == junction or path[-1] not in junctions:
                neighbors = [n for n in graph.neighbors(path[-1]) if n not in path]

                path.append(neighbors[0])
            junction_graph.add_edge(path[0], path[-1], weight=len(path) - 1)
    return junction_graph


def calculate_upper_bound(subgraph: nx.Graph, target: Tuple[int, int]) -> int:
    connected_component = nx.node_connected_component(subgraph, target)
    max_weight = 0
    for node in connected_component:
        max_weight += max(data['weight'] for u, v, data in subgraph.edges(data=True) if u == node or v == node)
    return max_weight


def longest_hamiltonian_path(graph: nx.Graph, source: Tuple[int, int], target: Tuple[int, int]):
    longest_path_length = 0
    shortest_paths = {
        node: nx.shortest_path_length(graph, node, target, weight="weight")
        for node in graph.nodes
    }

    def dfs(current_path: List[Tuple[int, int]]):
        nonlocal longest_path_length
        current_path_length = nx.path_weight(graph, current_path, weight='weight')
        if current_path[-1] == target:
            if current_path_length > longest_path_length:
                longest_path_length = current_path_length
                print(longest_path_length)
            return

        # Continue DFS for each neighbor not in the current path
        current_node = current_path[-1]
        subgraph = nx.subgraph(graph, set(graph.nodes).difference(current_path))
        for neighbor in sorted(graph.neighbors(current_node), key=lambda neighbor: -shortest_paths[neighbor]):
            if (
                    neighbor == target or
                    (
                        neighbor not in current_path and
                        nx.has_path(subgraph, neighbor, target) and
                        current_path_length + calculate_upper_bound(subgraph, target) > longest_path_length
                    )
            ):
                dfs(current_path + [neighbor])

    dfs([source])

    return longest_path_length


def process_file(file_name: str) -> int:
    graph, source, target = get_graph(file_name)

    junction_graph = build_junction_graph(graph, source, target)

    # nx.draw(junction_graph, pos={n: (n[1], 23 - n[0]) for n in graph.nodes})
    # plt.show()
    start = datetime.datetime.now()
    longest_path_length = longest_hamiltonian_path(junction_graph, source, target)
    print(f"Duration: {(datetime.datetime.now() - start).total_seconds()}")

    # paths = nx.all_simple_paths(junction_graph, source, target)
    # longest_path_length = max(nx.path_weight(junction_graph, path, weight='weight') for path in paths)

    return longest_path_length


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)