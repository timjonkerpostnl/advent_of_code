from typing import List

import pytest

from src.day3.assignment1 import (
    process_file,
    find_special_character_positions,
    find_digit_sequences_with_positions,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        ("617*......", [3]),
        ("617*...%..", [3, 7]),
    ],
)
def test_find_special_characters(input: str, expected: List[int]):
    assert find_special_character_positions(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("617*......", [(617, 0, 2)]),
        ("617*...%.7865.", [(617, 0, 2), (7865, 9, 12)]),
    ],
)
def test_find_digit_sequences_with_positions(input: str, expected: List[int]):
    assert find_digit_sequences_with_positions(input) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 4361
