import math
import re
from itertools import combinations
from typing import List, Tuple, Set


def process_file(file_name: str) -> int:
    summed = 0
    universe = build_universe(file_name)

    galaxy_positions = []
    for row_idx, row in enumerate(universe):
        for col_idx, char in enumerate(row):
            if char == "#":
                galaxy_positions.append((col_idx, row_idx))

    for position1, position2 in combinations(galaxy_positions, 2):
        summed += abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

    return summed


def build_universe(file_name):
    universe = []
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if "#" not in stripped_line:
                # Contains no galaxy
                universe.append(stripped_line)
            universe.append(stripped_line)
    transposed_universe = list(map(list, zip(*universe)))
    new_universe = transposed_universe.copy()
    num_doubles_found = 0
    for row_idx, row in enumerate(transposed_universe):
        if all(x == "." for x in row):
            new_universe.insert(row_idx + num_doubles_found, row)
            num_doubles_found += 1
    universe = list(map(list, zip(*new_universe)))
    return universe


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
