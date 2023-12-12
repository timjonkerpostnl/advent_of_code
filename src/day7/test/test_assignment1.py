from typing import List

import pytest

from src.day7.assignment1 import (
    process_file,
    convert_hand,
    get_strength,
    get_overall_strength,
)


@pytest.mark.parametrize("hand, expected", [("32T3K", [3, 2, 10, 3, 13]), ("QQQJA", [12, 12, 12, 11, 14])])
def test_convert_hand(hand, expected):
    translate_dict = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    assert convert_hand(hand, translate_dict) == expected


@pytest.mark.parametrize(
    "hand, expected",
    [
        ([3, 2, 10, 3, 13], 2),
        ([12, 12, 12, 11, 14], 4),
        ([3, 3, 3, 3, 2], 6),
        ([2, 15, 15, 15, 15], 6),
        ([7, 7, 7, 8, 8], 5),
        ([7, 7, 8, 8, 8], 5),
    ],
)
def test_get_strength(hand, expected):
    assert get_strength(hand) == expected


@pytest.mark.parametrize(
    "hand, expected",
    [
        ([3, 2, 10, 3, 13], (2, 3, 2, 10, 3, 13)),
        ([12, 12, 12, 11, 14], (4, 12, 12, 12, 11, 14)),
        ([3, 3, 3, 3, 2], (6, 3, 3, 3, 3, 2)),
        ([2, 15, 15, 15, 15], (6, 2, 15, 15, 15, 15)),
        ([7, 7, 7, 8, 8], (5, 7, 7, 7, 8, 8)),
        ([7, 7, 8, 8, 8], (5, 7, 7, 8, 8, 8)),
    ],
)
def test_get_overall_strength(hand, expected):
    assert get_overall_strength(hand) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 6440
