import math
import re
from typing import List, Tuple, Set, Dict
from collections import Counter

from src.day9.assignment1 import get_difference_sequence


def extrapolate_backward(sequences: List[List[int]]):
    value_to_append = 0
    for sequence in sequences[::-1]:
        value_to_append = sequence[0] - value_to_append
    return value_to_append


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            sequences = [[int(x) for x in stripped_line.split(" ")]]
            while not all(x == 0 for x in sequences[-1]):
                sequences.append(get_difference_sequence(sequences[-1]))
            summed += extrapolate_backward(sequences)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
