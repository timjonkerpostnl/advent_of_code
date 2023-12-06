import re
from collections import defaultdict
from typing import List

from src.day6.assignment1 import ways_to_beat_record

def process_file(file_name: str) -> int:
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()

    return wtbr


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)