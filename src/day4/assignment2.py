import re
from typing import List

from src.day4.assignment1 import find_numbers


def process_cards(num_cards, wins_per_card):
    for card, wins in wins_per_card.items():
        for i in range(wins):
            num_cards[card + 1 + i] += num_cards[card]
    return num_cards


def process_file(file_name: str) -> int:
    wins_per_card = {}
    num_cards = {}
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            winning_numbers, my_numbers = find_numbers(stripped_line)
            present_winning_numbers = winning_numbers.intersection(my_numbers)
            wins_per_card[idx+1] = len(present_winning_numbers)
            num_cards[idx + 1] = 1

    num_cards = process_cards(num_cards, wins_per_card)

    summed = sum(num_cards.values())

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)