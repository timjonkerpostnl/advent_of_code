import math
import re
from typing import List, Tuple, Set

import networkx as nx
import matplotlib.pyplot as plt
from shapely import Polygon, Point
import shapely.plotting
from tqdm import tqdm

from src.day10.assignment1 import construct_maze, find_cylce


def node_on_boundary(node: Tuple[int, int], maze_size: Tuple[int, int]) -> bool:
    return node[0] == 0 or node[0] == maze_size[0] - 1 or node[1] == 0 or node[1] == maze_size[1] - 1


def process_file(file_name: str, plots: bool = False) -> int:
    tiles_covered = 0
    maze = construct_maze(file_name)
    cycle, g = find_cylce(maze)
    cycle_nodes = set().union([(corner[0], corner[1]) for edge in cycle for corner in edge])

    subgraph = nx.Graph()
    for row_idx, row in enumerate(maze):
        for column_idx, connection in enumerate(row):
            if (column_idx, row_idx) in cycle_nodes:
                continue
            subgraph.add_node((column_idx, row_idx))
            if row_idx < len(maze) - 1 and (column_idx, row_idx + 1) not in cycle_nodes:
                subgraph.add_edge((column_idx, row_idx), (column_idx, row_idx + 1))
            if column_idx < len(row) - 1 and (column_idx + 1, row_idx) not in cycle_nodes:
                subgraph.add_edge((column_idx, row_idx), (column_idx + 1, row_idx))

    components = list(nx.connected_components(subgraph))
    polygon = Polygon([[corner[0], corner[1]] for edge in cycle for corner in edge])

    if plots:
        shapely.plotting.plot_polygon(polygon, color="b")

    for component in tqdm(components):
        if all(not node_on_boundary(node, (len(maze[0]), len(maze))) for node in component) and Point(next(iter(component))).within(polygon):
            tiles_covered += len(component)
            if plots:
                for point in component:
                    shapely.plotting.plot_points(Point(point), color="g")
        elif plots:
            for point in component:
                shapely.plotting.plot_points(Point(point), color="r")

    if plots:
        plt.show()

    return tiles_covered


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
