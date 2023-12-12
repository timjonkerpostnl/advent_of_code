import re
from collections import defaultdict
from typing import List

from src.day4.assignment1 import find_numbers


def process_file(file_name: str) -> int:
    num_cards = defaultdict(int)
    lines = 0
    with open(file_name) as f:
        for idx, line in enumerate(f):
            lines += 1
            stripped_line = line.strip()
            winning_numbers, my_numbers = find_numbers(stripped_line)
            present_winning_numbers = winning_numbers.intersection(my_numbers)
            wins = len(present_winning_numbers)
            num_cards[idx + 1] += 1
            for i in range(wins):
                num_cards[idx + 2 + i] += num_cards[idx + 1]

    summed = sum(x for i, x in enumerate(num_cards.values()) if i <= lines)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
