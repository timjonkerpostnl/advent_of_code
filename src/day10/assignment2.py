import math
import re
from typing import List, Tuple, Set

import networkx as nx
import matplotlib.pyplot as plt
from shapely import Polygon, Point
import shapely.plotting
from tqdm import tqdm

from src.day10.assignment1 import construct_maze, find_cylce


def process_file(file_name: str) -> int:
    tiles_covered = 0
    maze = construct_maze(file_name)

    cycle, g = find_cylce(maze)
    cycle_nodes = set().union([(corner[0], len(maze[0]) - corner[1]) for edge in cycle for corner in edge])
    polygon = Polygon([[corner[0], len(maze[0]) - corner[1]] for edge in cycle for corner in edge])
    points = [Point(col_idx, len(maze[0]) - row_idx) for row_idx, row in enumerate(maze) for col_idx in range(len(row))]

    # shapely.plotting.plot_polygon(polygon, color="b")
    for point in tqdm(points):
        if (point.x, point.y) not in cycle_nodes and point.within(polygon):
            # shapely.plotting.plot_points(point, color="g")
            tiles_covered += 1
        # else:
        # shapely.plotting.plot_points(point, color="r")

    # plt.show()

    return tiles_covered


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
