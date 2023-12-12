import math
import re
from typing import List, Tuple, Set, Dict
from collections import Counter, defaultdict


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
                    "L": "".join([d for d in left if d.isalpha() or d.isdigit()]),
                    "R": "".join([d for d in right if d.isalpha() or d.isdigit()]),
                }
    return input_sequence, connections


def process_file(file_name: str) -> int:
    instructions, connections = get_connections(file_name)
    steps = 0
    positions = [node for node in connections if node[-1] == "A"]
    steps_to_final = {start_pos_num: 0 for start_pos_num, position in enumerate(positions)}
    while not all(step > 0 for step in steps_to_final.values()):
        instruction = instructions[steps % len(instructions)]
        steps += 1
        positions = [connections[position][instruction] for position in positions]
        for start_pos_num, position in enumerate(positions):
            if position[-1] == "Z" and steps_to_final[start_pos_num] == 0:
                steps_to_final[start_pos_num] = steps

    return math.lcm(*steps_to_final.values())


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
