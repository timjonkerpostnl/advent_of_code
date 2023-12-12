import math
import re
from itertools import combinations
from typing import List, Tuple, Set


def build_universe(file_name):
    universe = []
    rows_that_expand = []
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if "#" not in stripped_line:
                rows_that_expand.append(idx)
            universe.append(stripped_line)
    transposed_universe = list(map(list, zip(*universe)))
    cols_that_expand = []
    for row_idx, row in enumerate(transposed_universe):
        if all(x == "." for x in row):
            cols_that_expand.append(row_idx)
    return universe, rows_that_expand, cols_that_expand


def process_file(file_name: str, distance_between_galaxies: int = 1000000) -> int:
    summed = 0
    universe, rows_that_expand, cols_that_expand = build_universe(file_name)

    galaxy_positions = []
    for row_idx, row in enumerate(universe):
        for col_idx, char in enumerate(row):
            if char == "#":
                galaxy_positions.append((col_idx, row_idx))

    for position1, position2 in combinations(galaxy_positions, 2):
        distance = 0
        if position1[0] > position2[0]:
            p_big, p_small = position1[0], position2[0]
        else:
            p_big, p_small = position2[0], position1[0]

        distance += p_big - p_small
        for col_traversed in range(p_small, p_big):
            if col_traversed in cols_that_expand:
                distance += distance_between_galaxies - 1

        if position1[1] > position2[1]:
            p_big, p_small = position1[1], position2[1]
        else:
            p_big, p_small = position2[1], position1[1]

        distance += p_big - p_small
        for row_traversed in range(p_small, p_big):
            if row_traversed in rows_that_expand:
                distance += distance_between_galaxies - 1

        summed += distance

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
