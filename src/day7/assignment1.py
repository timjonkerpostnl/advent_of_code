import math
import re
from typing import List, Tuple, Set


def process_file(file_name: str) -> int:
    product = None
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()

    return product


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)