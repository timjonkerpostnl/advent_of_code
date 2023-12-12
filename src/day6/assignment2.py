import re
from collections import defaultdict
from typing import List

from src.day6.assignment1 import ways_to_beat_record


def read_values(splits):
    return int(splits[1].replace(" ", ""))


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            splits = stripped_line.split(":")
            if splits[0] == "Time":
                time = read_values(splits)
            if splits[0] == "Distance":
                distance = read_values(splits)

        wtbr = ways_to_beat_record(distance, time)

    return wtbr


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
