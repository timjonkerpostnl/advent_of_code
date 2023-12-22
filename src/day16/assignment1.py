import re
from typing import List, Tuple

import numpy as np
from tqdm import tqdm


def process_node(maze_size: Tuple[int, int], node: Tuple[int, int, str], visits: List[Tuple[int, int, str]]) -> List[List[Tuple[int, int, str]]]:
    last_visit = visits[-1]
    if node[0] >= maze_size[0] or node[1] >= maze_size[1]:
        # Node is outside of grid
        return []
    if node[2] == ".":
        if last_visit[2] == ">":
            new_node = (last_visit[0], last_visit[1] + 1, last_visit[2]),
        elif last_visit[2] == "<":
            new_node = (last_visit[0], last_visit[1] - 1, last_visit[2]),
        elif last_visit[2] == "v":
            new_node = (last_visit[0] + 1, last_visit[1], last_visit[2]),
        else:
            new_node = (last_visit[0] - 1, last_visit[1], last_visit[2]),
    elif node[2] == "/":
        if last_visit[2] == ">":
            new_node = (last_visit[0] - 1, last_visit[1], "^"),
        elif last_visit[2] == "<":
            new_node = (last_visit[0] + 1, last_visit[1], "v"),
        elif last_visit[2] == "v":
            new_node = (last_visit[0], last_visit[1] - 1, "<"),
        else:
            new_node = (last_visit[0], last_visit[1] + 1, ">"),
    elif node[2] == "\\":
        if last_visit[2] == ">":
            new_node = (last_visit[0] + 1, last_visit[1], "v"),
        elif last_visit[2] == "<":
            new_node = (last_visit[0] - 1, last_visit[1], "^"),
        elif last_visit[2] == "v":
            new_node = (last_visit[0], last_visit[1] + 1, ">"),
        else:
            new_node = (last_visit[0], last_visit[1] - 1, "<"),
    elif node[2] == "|":
        if last_visit[2] == ">" or last_visit[2] == "<":
            new_node = (last_visit[0] + 1, last_visit[1], "v"), (last_visit[0] - 1, last_visit[1], "^")
        elif last_visit[2] == "v":
            new_node = (last_visit[0] + 1, last_visit[1], "v"),
        else:
            new_node = (last_visit[0] - 1, last_visit[1], "^"),
    elif node[2] == "-":
        if last_visit[2] == "v" or last_visit[2] == "^":
            new_node = (last_visit[0], last_visit[1] - 1, "<"), (last_visit[0], last_visit[1] + 1, ">")
        elif last_visit[2] == ">":
            new_node = (last_visit[0], last_visit[1] + 1, ">"),
        else:
            new_node = (last_visit[0], last_visit[1] - 1, "<"),
    else:
        raise ValueError("Unknown")

    result = []
    for n in new_node:
        new_visits = visits.copy()
        new_visits.append(n)
        result.append(new_visits)
    return result

def process_start_node(start_node, maze, maze_size):
    beams = [[start_node]]
    complete_beams = []
    all_nodes_and_directions = set()
    while beams:
        next_beams = []
        for beam in beams:
            last_beam = beam[-1]
            beam_row = last_beam[0]
            beam_col = last_beam[1]
            if last_beam in all_nodes_and_directions or beam_row >= maze_size[0] or beam_row < 0 or beam_col >= \
                    maze_size[1] or beam_col < 0:
                complete_beams.append(beam)
            else:
                all_nodes_and_directions.add(last_beam)
                node_object = maze[beam_row][beam_col][2]
                node = (beam_row, beam_col, node_object)
                new_beams = process_node(maze_size, node, beam)
                next_beams += new_beams
        beams = next_beams
    energized_tiles = {(node[0], node[1]) for beam in complete_beams for node in beam if
                       0 <= node[0] < maze_size[0] and 0 <= node[1] < maze_size[1]}
    num_energized_tiles = len(energized_tiles)
    return num_energized_tiles


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        maze = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            node_list = [(idx, col_idx, character) for col_idx, character in enumerate(stripped_line)]
            maze.append(node_list)

        maze_size = (len(maze), len(maze[0]))
        summed = process_start_node((0, 0, ">"), maze, maze_size)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
