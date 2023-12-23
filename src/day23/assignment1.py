import sys
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

        graph = nx.DiGraph()
        source = (0, maze[0].find("."))
        target = (len(maze) - 1, maze[-1].find("."))
        for row_idx, row in enumerate(maze):
            for col_idx, value in enumerate(row):
                if value == ".":
                    if row_idx < len(maze) - 1 and maze[row_idx + 1][col_idx] not in "^#":
                        graph.add_edge((row_idx, col_idx), (row_idx + 1, col_idx))
                    if col_idx < len(maze[0]) - 1 and maze[row_idx][col_idx + 1] not in "<#":
                        graph.add_edge((row_idx, col_idx), (row_idx, col_idx + 1))
                    if row_idx > 0 and maze[row_idx - 1][col_idx] not in "v#":
                        graph.add_edge((row_idx, col_idx), (row_idx - 1, col_idx))
                    if col_idx > 0 and maze[row_idx][col_idx - 1] not in ">#":
                        graph.add_edge((row_idx, col_idx), (row_idx, col_idx - 1))
                elif value == ">":
                    if col_idx < len(maze[0]) - 1 and maze[row_idx][col_idx + 1] not in "<#":
                        graph.add_edge((row_idx, col_idx), (row_idx, col_idx + 1))
                elif value == "v":
                    if row_idx < len(maze) - 1 and maze[row_idx + 1][col_idx] not in "^#":
                        graph.add_edge((row_idx, col_idx), (row_idx + 1, col_idx))

        # nx.draw(graph, pos={n: (n[1], len(maze) - n[0]) for n in graph.nodes}, with_labels=True)
        # plt.show()
    return graph, source, target


def longest_hamiltonian_path(graph: nx.DiGraph, source: Tuple[int, int], target: Tuple[int, int]):
    def dfs(current_path: List[Tuple[int, int]], longest_path):
        if current_path[-1] == target:
            if len(current_path) > len(longest_path):
                longest_path[:] = current_path[:]
            return

        # Continue DFS for each neighbor not in the current path
        current_node = current_path[-1]
        for neighbor in graph.out_edges(current_node):
            if neighbor[1] not in current_path:
                dfs(current_path + [neighbor[1]], longest_path)

    # Initialize with an empty path
    longest_path = []

    dfs([source], longest_path)

    return longest_path


def process_file(file_name: str) -> int:
    graph, source, target = get_graph(file_name)

    longest_path = longest_hamiltonian_path(graph, source, target)

    return len(longest_path) - 1


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    result = process_file("input.txt")
    print(result)
