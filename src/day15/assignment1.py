import re
from typing import List

import numpy as np
from tqdm import tqdm


def calculate_hash(command):
    value = 0
    for x in command:
        value += ord(x)
        value *= 17
        value %= 256
    return value


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            commands = stripped_line.split(",")
            for command in commands:
                value = calculate_hash(command)
                summed += value

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
