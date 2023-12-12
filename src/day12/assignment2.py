import re
from typing import List

from tqdm import tqdm

from src.day12.assignment1 import fill_in_character


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            sequence, sequence_lengths = stripped_line.split(" ")
            sequence = "?".join([sequence] * 5)
            sequence_lengths = ",".join([sequence_lengths] * 5)
            sequence_lengths = [int(x) for x in sequence_lengths.split(",")]
            unknown_positions = [i for i, char in enumerate(sequence) if char == '?']

            found_valid_sequences = fill_in_character(unknown_positions, sequence, sequence_lengths, 0)
            summed += found_valid_sequences

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
