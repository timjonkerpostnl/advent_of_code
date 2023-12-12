from typing import List

import pytest

from src.day12.assignment1 import (
    process_file,
    sequence_correct,
    sequence_potentially_correct,
    fill_in_character,
)


@pytest.mark.parametrize(
    "sequence, sequence_lengths",
    [
        ("#.#.###", [1, 1, 3]),
        (".#...#....###.", [1, 1, 3]),
        (".#.###.#.######", [1, 3, 1, 6]),
        ("####.#...#...", [4, 1, 1]),
        ("#....######..#####.", [1, 6, 5]),
        (".###.##....#", [3, 2, 1]),
    ],
)
def test_sequence_correct(sequence, sequence_lengths):
    assert sequence_correct(sequence, sequence_lengths)


@pytest.mark.parametrize(
    "sequence, sequence_lengths, expected",
    [
        ("#.#.###", [1, 1, 3], True),
        ("???.###", [1, 1, 3], True),
        ("#??.###", [1, 1, 3], True),
        ("##?.###", [1, 1, 3], False),
        (".#...#....###.", [1, 1, 3], True),
        (".#.###.#.######", [1, 3, 1, 6], True),
        ("####.#...#...", [4, 1, 1], True),
        ("#....######..#####.", [1, 6, 5], True),
        (".###.##....#", [3, 2, 1], True),
    ],
)
def test_sequence_potentially_correct(sequence, sequence_lengths, expected):
    assert sequence_potentially_correct(sequence, sequence_lengths) == expected


@pytest.mark.parametrize(
    "sequence, sequence_lengths, expected",
    [
        # ("???.###", [1, 1, 3], 1),
        # (".??..??...?##.", [1, 1, 3], 4),
        ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        # ("????.#...#...", [4, 1, 1], 1),
        # ("????.######..#####.", [1, 6, 5], 4),
        # ("?###????????", [3, 2, 1], 10),
    ],
)
def test_fill_in_character(sequence, sequence_lengths, expected):
    unknown_positions = [i for i, char in enumerate(sequence) if char == "?"]
    found_valid = 0

    assert fill_in_character(unknown_positions, sequence, sequence_lengths, found_valid) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 4361
