import re
from typing import List, Tuple, Set


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        map_name = None
        maps = {}
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if idx == 0:
                seeds = get_seeds(stripped_line)
            elif not any(char.isdigit() for char in stripped_line) and stripped_line != "":
                map_name = stripped_line
                maps[map_name] = {}
            elif stripped_line != "":
                destination_start, source_start, length = stripped_line.split(" ")
                destination_start, source_start, length = (
                    int(destination_start),
                    int(source_start),
                    int(length),
                )
                maps[map_name][(source_start, source_start + length)] = destination_start

        minimum_location = find_minimum_location(maps, seeds)

    return minimum_location


def find_minimum_location(maps, seeds):
    locations = []
    for seed in seeds:
        lookup_num = seed
        for garden_map, lookup_dict in maps.items():
            for (source_start, source_end), destination_start in lookup_dict.items():
                if source_start <= lookup_num < source_end:
                    lookup_num = destination_start + lookup_num - source_start
                    break

        locations.append(lookup_num)
    minimum_location = min(locations)
    return minimum_location


def get_seeds(stripped_line):
    seeds = stripped_line.split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds]
    return seeds


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
