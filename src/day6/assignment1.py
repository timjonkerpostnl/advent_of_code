import math
import re
from typing import List, Tuple, Set


def calculate_distance(race_duration: int, hold_time: int):
    assert race_duration >= hold_time
    speed = hold_time
    available_travel_time = race_duration - hold_time
    return speed * available_travel_time


def ways_to_beat_record(record: int, race_duration: int):
    d = race_duration**2 - 4 * record
    x1 = (-race_duration + math.sqrt(d)) / -2
    x2 = (-race_duration - math.sqrt(d)) / -2

    x1 = int(math.ceil(x1))
    x2 = int(x2)

    dx1 = calculate_distance(race_duration, x1)
    dx2 = calculate_distance(race_duration, x2)
    if dx1 > record and dx2 > record:
        return x2 - x1 + 1
    elif dx1 == record ^ dx2 == record:
        return x2 - x1
    elif dx1 == record and dx2 == record:
        return max(x2 - x1 - 1, 0)
    else:
        raise NotImplemented("Did not expect this")


def process_file(file_name: str) -> int:
    product = None
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            splits = stripped_line.split(":")
            if splits[0] == "Time":
                time = read_values(splits)
            if splits[0] == "Distance":
                distance = read_values(splits)

        for t, d in zip(time, distance):
            wtbr = ways_to_beat_record(d, t)
            if product is None:
                product = wtbr
            else:
                product *= wtbr

    return product


def read_values(splits):
    return [int(x.strip()) for x in splits[1].split(" ") if len(x) > 0]


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
