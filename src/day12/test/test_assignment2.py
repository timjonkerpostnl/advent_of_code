from typing import List

import pytest

from src.day12.assignment2 import process_file, fill_in_character


@pytest.mark.parametrize(
    "sequence, sequence_lengths, expected",
    [
        ("???.###", [1, 1, 3], 1),
        (".??..??...?##.", [1, 1, 3], 4),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        ("????.#...#...", [4, 1, 1], 1),
        ("????.######..#####.", [1, 6, 5], 4),
        ("?###????????", [3, 2, 1], 10),
    ],
)
def test_fill_in_character(sequence, sequence_lengths, expected):
    sequence += "."
    assert fill_in_character(sequence, tuple(sequence_lengths)) == expected


@pytest.mark.parametrize(
    "sequence, sequence_lengths, expected",
    [
        ("???.###", [1, 1, 3], 1),
        (".??..??...?##.", [1, 1, 3], 16384),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        ("????.#...#...", [4, 1, 1], 16),
        ("????.######..#####.", [1, 6, 5], 2500),
        ("?###????????", [3, 2, 1], 506250),
    ],
)
def test_fill_in_character_with_unfolding(sequence, sequence_lengths, expected):
    sequence = "?".join([sequence] * 5)
    sequence_lengths *= 5
    sequence += "."
    assert fill_in_character(sequence, tuple(sequence_lengths)) == expected


def test_assignment2():
    assert process_file("input_test1.txt") == 467835
