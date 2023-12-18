import math
import re
from typing import List, Tuple, Set

import networkx as nx
import matplotlib.pyplot as plt
from shapely import Polygon, Point
import shapely.plotting
from tqdm import tqdm

from src.day10.assignment1 import construct_maze, find_cylce


def process_file(file_name: str, plots: bool = False) -> int:
    maze = construct_maze(file_name)
    cycle, g = find_cylce(maze)
    cycle_nodes = set().union([(corner[0], corner[1]) for edge in cycle for corner in edge])

    polygon = Polygon([[corner[0], corner[1]] for edge in cycle for corner in edge])

    if plots:
        shapely.plotting.plot_polygon(polygon, color="b")

    tiles_covered = polygon.buffer(0.5, cap_style="square", join_style="mitre").area - len(cycle_nodes)

    if plots:
        plt.show()

    return tiles_covered


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
