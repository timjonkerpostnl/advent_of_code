from typing import List

import pytest

from src.day7.assignment2 import process_file, build_new_hand


@pytest.mark.parametrize(
    "hand, expected",
    [
        ([3, 2, 10, 3, 13], [3, 2, 10, 3, 13]),
        ([10, 5, 5, 1, 1], [10, 5, 5, 5, 5]),
        ([14, 14, 6, 7, 7], [14, 14, 6, 7, 7]),
        ([14, 10, 1, 1, 10], [14, 10, 10, 10, 10]),
        ([13, 13, 13, 1, 14], [13, 13, 13, 13, 14]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ],
)
def test_build_new_hand(hand, expected):
    assert build_new_hand(hand) == expected


def test_assignment2():
    assert process_file("input_test1.txt") == 5905
