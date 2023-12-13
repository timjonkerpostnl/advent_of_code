import re
from typing import List

import numpy as np
from tqdm import tqdm

from src.day13.assignment1 import find_horizontal_reflection


def find_vertical_reflection(puzzle: np.ndarray) -> int:
    for option in range(1, puzzle.shape[1]):
        cols_left = option
        cols_right = puzzle.shape[1] - option
        num_to_check = min(cols_left, cols_right)
        left = puzzle[:, option - num_to_check : option]
        right = puzzle[:, option : option + num_to_check][:, ::-1]
        mask = left != right
        if len(np.where(mask)[0]) == 1:
            return option


def find_reflection_count(puzzle: np.ndarray) -> int:
    vertical_reflection = find_vertical_reflection(puzzle)
    if vertical_reflection is None:
        horizontal_reflection = find_horizontal_reflection(puzzle)
        return 100 * horizontal_reflection
    else:
        return vertical_reflection


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        puzzle = None
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            translated_line = [1 if x == "#" else 0 for x in stripped_line]
            if puzzle is None:
                puzzle = np.array([translated_line])
            elif translated_line:
                puzzle = np.append(puzzle, [translated_line], axis=0)
            else:
                summed += find_reflection_count(puzzle)
                puzzle = None

        summed += find_reflection_count(puzzle)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
