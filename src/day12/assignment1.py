import re
from typing import List


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")