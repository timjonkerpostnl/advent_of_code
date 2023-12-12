import math
import re
from typing import List, Tuple, Set, Dict
from collections import Counter


def convert_hand(hand: str, translate_dict: Dict[str, int]) -> List[int]:
    int_hand = []
    for card in hand:
        if not card.isdigit():
            int_hand.append(translate_dict[card])
        else:
            int_hand.append(int(card))
    return int_hand


def get_strength(hand: List[int]) -> int:
    count_dict = Counter(hand)
    occurences = sorted(list(count_dict.values()), reverse=True)
    if occurences[0] == 5:
        return 7
    elif occurences[0] == 4:
        return 6
    elif occurences[0] == 3 and occurences[1] == 2:
        return 5
    elif occurences[0] == 3:
        return 4
    elif occurences[0] == 2 and occurences[1] == 2:
        return 3
    elif occurences[0] == 2:
        return 2
    else:
        return 1


def get_overall_strength(hand: List[int]) -> tuple[int, ...]:
    strength = get_strength(hand)
    return (strength,) + tuple(hand)


def calculate_sum(card_bids):
    card_bids_sorted = sorted(card_bids, key=lambda x: x[0])
    summed = sum((rank + 1) * bid for rank, (_, bid) in enumerate(card_bids_sorted))
    return summed


def process_file(file_name: str) -> int:
    translate_dict = {
        "T": 10,
        "J": 11,
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
