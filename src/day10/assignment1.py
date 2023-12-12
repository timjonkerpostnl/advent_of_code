import math
import re
from typing import List, Tuple, Set

import networkx as nx
import matplotlib.pyplot as plt


def transform_connection(x: str) -> Set[str]:
    if x == ".":
        return set()
    elif x == "|":
        return {"N", "S"}
    elif x == "-":
        return {"E", "W"}
    elif x == "L":
        return {"N", "E"}
    elif x == "J":
        return {"N", "W"}
    elif x == "7":
        return {"W", "S"}
    elif x == "F":
        return {"E", "S"}
    elif x == "S":
        return {"N", "W", "S", "E"}


def find_cylce(maze):
    g = nx.Graph()
    starting_pos = (-1, -1)
    for row_idx, row in enumerate(maze):
        for column_idx, connection in enumerate(row):
            if connection == ".":
                continue
            g.add_node((column_idx, row_idx))
            if {"N", "W", "S", "E"} == connection:
                starting_pos = (column_idx, row_idx)
            if row_idx < len(maze) - 1 and "S" in connection and "N" in maze[row_idx + 1][column_idx]:
                g.add_edge((column_idx, row_idx), (column_idx, row_idx + 1))
            if column_idx < len(row) - 1 and "E" in connection and "W" in maze[row_idx][column_idx + 1]:
                g.add_edge((column_idx, row_idx), (column_idx + 1, row_idx))
    cycle = nx.find_cycle(g, starting_pos)
    return cycle, g


def process_file(file_name: str) -> int:
    path_length = 0
    maze = construct_maze(file_name)

    cycle, _ = find_cylce(maze)

    # nx.draw(g, pos={n: (n[0], len(maze[0]) - n[1]) for n in g.nodes}, with_labels=True)
    # plt.show()

    return int(len(cycle) / 2)


def construct_maze(file_name):
    maze = []
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            maze.append([transform_connection(x) for x in stripped_line])
    return maze


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
