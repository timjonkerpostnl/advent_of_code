from collections import defaultdict
from typing import Dict

COLORS = ["red", "green", "blue"]


def store_in_dict(input_string: str) -> Dict[str, int]:
    color_counts = defaultdict(int)
    components = input_string.split(",")
    for component in components:
        count, color = component.strip().split(" ")
        count = int(count)
        color_counts[color] = count
    return color_counts


def extract_grabs(input_string: str) -> Dict[str, int]:
    grabs = input_string.split(":")[1].split(";")
    maxima = {c: 0 for c in COLORS}
    grab_results = [store_in_dict(grab) for grab in grabs]
    for grab_result in grab_results:
        for k, v in grab_result.items():
            maxima[k] = max(maxima[k], v)

    return maxima


def process_games(file_name: str) -> int:
    summed = 0
    cubes = {}
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            cubes[idx + 1] = extract_grabs(stripped_line)
            power = cubes[idx + 1]["red"] * cubes[idx + 1]["green"] * cubes[idx + 1]["blue"]
            summed += power
    return summed


if __name__ == "__main__":
    result = process_games("input.txt")
