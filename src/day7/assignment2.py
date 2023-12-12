import math
import re
from typing import List, Tuple, Set, Dict
from collections import Counter

from src.day7.assignment1 import convert_hand, get_strength, calculate_sum


def build_new_hand(hand: List[int]) -> List[int]:
    count_dict = Counter(hand)
    sorted_count_desc = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    if 1 in hand and len(count_dict) > 1:
        if sorted_count_desc[0][0] != 1:
            # There is another card that occurs more frequently that is not a joker
            card_to_replace = sorted_count_desc[0][0]
        else:
            # The joker occurs most frequently
            card_to_replace = sorted_count_desc[1][0]
        new_hand = [card_to_replace if x == 1 else x for x in hand]
        return new_hand
    return hand


def get_overall_strength(hand: List[int]) -> tuple[int, ...]:
    new_hand = build_new_hand(hand)
    strength = get_strength(new_hand)
    return (strength,) + tuple(hand)


def process_file(file_name: str) -> int:
    translate_dict = {
        "T": 10,
        "J": 1,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    card_bids = []
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            hand, bid = stripped_line.split(" ")
            int_hand = convert_hand(hand, translate_dict)
            card_bids.append((get_overall_strength(int_hand), int(bid)))

    summed = calculate_sum(card_bids)

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
