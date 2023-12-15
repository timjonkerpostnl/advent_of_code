import re
from collections import defaultdict
from typing import List

import numpy as np
from tqdm import tqdm

from src.day15.assignment1 import calculate_hash


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            commands = stripped_line.split(",")
            boxes = defaultdict(list)
            for command in commands:
                match = re.search(r'[^-=]+', command)
                label = match.group() if match else ""
                box = calculate_hash(label)
                if "-" in command:
                    # Remove label from box
                    boxes[box] = [x for x in boxes[box] if x[0] != label]
                elif "=" in command:
                    # Add label with a focal length to the box
                    focal_length = int(command.split("=")[1])
                    index_lens = next((idx for idx, (current_label, _) in enumerate(boxes[box]) if label == current_label), len(boxes[box]))
                    if index_lens == len(boxes[box]):
                        boxes[box].append((label, focal_length))
                    else:
                        boxes[box][index_lens] = (label, focal_length)

            for box, content in boxes.items():
                summed += sum((box + 1) * (position + 1) * focal_length for position, (_, focal_length) in enumerate(content))

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
