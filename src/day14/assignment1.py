import re
from typing import List

import numpy as np
from tqdm import tqdm


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        puzzle = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            puzzle.append(list(stripped_line))
    transposed_puzzle = list(map(list, zip(*puzzle)))
    for row in transposed_puzzle:
        summed += weight_in_column(row)

    return summed


def weight_in_column(row: List[str]) -> int:
    row.append("#")
    row.insert(0, "#")
    obstacles = [index for index, char in enumerate(row) if char == "#"]
    summed = 0
    for obstacle1, obstacle2 in zip(obstacles[:-1], obstacles[1:]):
        num_rocks_in_between = sum(1 for x in row[obstacle1:obstacle2] if x == "O")
        last_rock_position = obstacle1 + num_rocks_in_between
        summed += sum(len(row) - 2 - (x - 1) for x in range(obstacle1 + 1, last_rock_position + 1))
    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
