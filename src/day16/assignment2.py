import re
from collections import defaultdict
from typing import List

import numpy as np
from tqdm import tqdm

from src.day15.assignment1 import calculate_hash
from src.day16.assignment1 import process_node, process_start_node


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        maze = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            node_list = [(idx, col_idx, character) for col_idx, character in enumerate(stripped_line)]
            maze.append(node_list)

        maze_size = (len(maze), len(maze[0]))
        start_nodes = [(0, col_idx, "v") for col_idx in range(maze_size[1])] + \
                      [(maze_size[0] - 1, col_idx, "^") for col_idx in range(maze_size[1])] + \
                      [(row_idx, 0, ">") for row_idx in range(maze_size[0])] + \
                      [(row_idx, maze_size[1] - 1, "<") for row_idx in range(maze_size[0])]

        num_energized_tiles = []
        for start_node in tqdm(start_nodes):
            num_energized_tiles.append(process_start_node(start_node, maze, maze_size))

        summed = max(num_energized_tiles)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
