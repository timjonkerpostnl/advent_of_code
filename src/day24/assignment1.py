from itertools import combinations
from typing import Tuple

import numpy as np
from shapely import Polygon
from tqdm import tqdm


def get_lines(file_name, dimensions: int):
    with open(file_name) as f:
        lines = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            intercept, direction = stripped_line.split(" @ ")
            intercept = [int(x) for x in intercept.split(", ")][:dimensions]
            direction = [int(x) for x in direction.split(", ")][:dimensions]
            lines.append((intercept, direction))
    return lines


def process_file(file_name: str, dimensions: int, size: Tuple[int, int]) -> int:
    summed = 0
    lines = get_lines(file_name, dimensions)
    for line1, line2 in combinations(lines, 2):
        ratios = np.array(line1[1]) / np.array(line2[1])
        if np.all(np.isclose(ratios, ratios[0])):
            if line1[0] != line2[0]:
                # Lines are parallel
                continue
            else:
                # Lines are equal
                print("Does this happen?")

        a = np.array([
            [p, -q] for p, q in zip(line1[1], line2[1])
        ])
        b = np.array([
            [q - p] for p, q in zip(line1[0], line2[0])
        ])

        # Solve for the variables t and s
        solution = np.linalg.lstsq(a, b, rcond=None)[0]

        # Calculate the intersection point
        intersection_point = [
            (line1[0][x] + line1[1][x] * solution[0][0]) for x in range(dimensions)
        ]

        if all(size[0] <= ip <= size[1] for ip in intersection_point) and all(s[0] >= 0 for s in solution):
            summed += 1

    return summed


if __name__ == "__main__":
    result = process_file("input.txt", 2, (200000000000000, 400000000000000))
    print(result)
