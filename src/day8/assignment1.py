import math
import re
from typing import List, Tuple, Set, Dict
from collections import Counter


def get_connections(file_name: str) -> Tuple[str, Dict[str, Dict[str, str]]]:
    connections = {}
    input_sequence = ""
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if idx == 0:
                input_sequence = [instruction for instruction in stripped_line]
            elif "=" in line:
                node, directions = line.split(" = ")
                left, right = directions[1:-1].split(", ")
                connections[node] = {
                    "L": "".join([d for d in left if d.isalpha()]),
                    "R": "".join([d for d in right if d.isalpha()]),
                }
    return input_sequence, connections


def process_file(file_name: str) -> int:
    instructions, connections = get_connections(file_name)
    steps = 0
    position = "AAA"
    while position != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        steps += 1
        position = connections[position][instruction]

    return steps


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
