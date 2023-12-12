from typing import List

import pytest

from src.day4.assignment1 import process_file, find_numbers, calculate_score


def test_find_numbers():
    winning_numbers, my_numbers = find_numbers("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert winning_numbers == {41, 48, 83, 86, 17}
    assert my_numbers == {83, 86, 6, 31, 17, 9, 48, 53}


@pytest.mark.parametrize(
    "winning_numbers, my_numbers, expected",
    [
        ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}, 8),
        ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}, 1),
        ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}, 0),
    ],
)
def test_calculate_score(winning_numbers, my_numbers, expected):
    assert calculate_score(winning_numbers, my_numbers) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 13
