import re
from typing import List, Tuple, Set


def find_numbers(stripped_line: str) -> Tuple[Set[int], Set[int]]:
    winning_numbers, my_numbers = stripped_line.split(": ")[1].split(" | ")
    winning_numbers = {int(x) for x in winning_numbers.split(" ") if len(x) > 0}
    my_numbers = {int(x) for x in my_numbers.split(" ") if len(x) > 0}
    return winning_numbers, my_numbers


def calculate_score(winning_numbers: Set[int], my_numbers: Set[int]) -> int:
    present_winning_numbers = winning_numbers.intersection(my_numbers)
    if len(present_winning_numbers) == 0:
        return 0
    elif len(present_winning_numbers) == 1:
        return 1
    else:
        return 2 ** (len(present_winning_numbers) - 1)


def process_file(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()

            winning_numbers, my_numbers = find_numbers(stripped_line)
            summed += calculate_score(winning_numbers, my_numbers)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
