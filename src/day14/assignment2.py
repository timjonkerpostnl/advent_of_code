import re
from typing import List

import numpy as np
from tqdm import tqdm


def shift_rocks_row(row):
    row.append("#")
    row.insert(0, "#")
    obstacles = [index for index, char in enumerate(row) if char == "#"]
    for obstacle1, obstacle2 in zip(obstacles[:-1], obstacles[1:]):
        num_rocks_in_between = sum(1 for x in row[obstacle1:obstacle2] if x == "O")
        last_rock_position = obstacle1 + num_rocks_in_between
        row[obstacle1 + 1 : last_rock_position + 1] = ["O"] * num_rocks_in_between
        row[last_rock_position + 1 : obstacle2] = ["."] * (obstacle2 - 1 - last_rock_position)
    return row[1:-1]


def shift_rocks(puzzle: List[List[str]]) -> List[List[str]]:
    new_puzzle = []
    for row in puzzle:
        new_row = shift_rocks_row(row)
        new_puzzle.append(new_row)
    return new_puzzle


def tilt_north(puzzle: List[List[str]]):
    transposed_puzzle = list(map(list, zip(*puzzle)))
    shifted = shift_rocks(transposed_puzzle)
    new_puzzle = list(map(list, zip(*shifted)))
    return new_puzzle


def tilt_south(puzzle: List[List[str]]):
    transposed_puzzle = list(map(list, zip(*puzzle)))
    reverse_cols = [row[::-1] for row in transposed_puzzle]
    shifted = shift_rocks(reverse_cols)
    original_order = [row[::-1] for row in shifted]
    new_puzzle = list(map(list, zip(*original_order)))
    return new_puzzle


def tilt_west(puzzle: List[List[str]]):
    new_puzzle = shift_rocks(puzzle.copy())
    return new_puzzle


def tilt_east(puzzle: List[List[str]]):
    reverse_cols = [row[::-1] for row in puzzle]
    shifted = shift_rocks(reverse_cols)
    new_puzzle = [row[::-1] for row in shifted]
    return new_puzzle


def cycle(puzzle: List[List[str]]):
    north = tilt_north(puzzle)
    west = tilt_west(north)
    south = tilt_south(west)
    east = tilt_east(south)
    return east


def calculate_weight_north(puzzle: List[List[str]]) -> int:
    return sum(sum(1 for x in row if x == "O") * (len(puzzle) - idx) for idx, row in enumerate(puzzle))


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        puzzle = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            puzzle.append(list(stripped_line))

    num_cycles = 1000000000
    historical_puzzles = [puzzle]
    for _ in tqdm(range(num_cycles)):
        puzzle = cycle(puzzle)
        if puzzle in historical_puzzles:
            print("found_already")
            break
        historical_puzzles.append(puzzle)

    num_puzzles = len(historical_puzzles) - 1
    resets_to = historical_puzzles.index(puzzle)
    final_index = find_final_index(num_puzzles, resets_to, num_cycles)
    final_puzzle = historical_puzzles[final_index]

    return calculate_weight_north(final_puzzle)


def find_final_index(num_puzzles, resets_to, total_length):
    steps_in_loop = total_length - resets_to
    length_loop = num_puzzles - resets_to + 1
    steps_after_start_loop = steps_in_loop % length_loop
    final_index = resets_to + steps_after_start_loop
    return final_index


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
