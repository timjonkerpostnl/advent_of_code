import networkx as nx
from matplotlib import pyplot as plt
from shapely import Polygon
from tqdm import tqdm

def create_graph(file_name):
    with open(file_name) as f:
        maze = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            maze.append(stripped_line)

        graph = nx.Graph()
        start = (0, 0)
        for row_idx, row in enumerate(maze):
            for col_idx, value in enumerate(row):
                if value != "#":
                    if row_idx < len(maze) - 1 and maze[row_idx + 1][col_idx] != "#":
                        graph.add_edge((row_idx, col_idx), (row_idx + 1, col_idx))
                    if col_idx < len(maze[0]) - 1 and maze[row_idx][col_idx + 1] != "#":
                        graph.add_edge((row_idx, col_idx), (row_idx, col_idx + 1))
                    if value == "S":
                        start = (row_idx, col_idx)

        # nx.draw(graph, pos={n: (n[1], len(maze) - n[0]) for n in graph.nodes}, with_labels=True)
        # plt.show()
    return graph, start


def process_file(file_name: str, max_length) -> int:
    graph, start = create_graph(file_name)

    paths = nx.single_source_shortest_path_length(graph, start, max_length)
    reachable_nodes = [node for node in graph.nodes if node in paths and paths[node] % 2 == 0]
    # node_colors = ["g" if node in reachable_nodes else "r" for node in graph.nodes]
    # nx.draw(graph, pos={n: (n[1], 11 - n[0]) for n in graph.nodes}, node_color=node_colors, with_labels=True)
    # plt.show()
    return len(reachable_nodes)


if __name__ == "__main__":
    result = process_file("input.txt", 64)
    print(result)
