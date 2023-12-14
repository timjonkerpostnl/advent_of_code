from typing import List

import numpy as np
import pytest

from src.day14.assignment2 import (
    process_file, shift_rocks_row, tilt_north, cycle, calculate_weight_north, find_final_index
)

@pytest.mark.parametrize("row, expected", [
    ("OO.O.O..##", "OOOO....##"),
    ("...OO....O", "OOO......."),
])
def test_shift_rocks_row(row: str, expected:str):
    row = list(row)
    assert shift_rocks_row(row) == list(expected)


def test_tilt_north():
    expected = [
        ["O", "O", "O", "O", ".", "#", ".", "O", ".", "."],
        ["O", "O", ".", ".", "#", ".", ".", ".", ".", "#"],
        ["O", "O", ".", ".", "O", "#", "#", ".", ".", "O"],
        ["O", ".", ".", "#", ".", "O", "O", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
        [".", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        [".", ".", "O", ".", ".", "#", ".", "O", ".", "O"],
        [".", ".", "O", ".", ".", ".", ".", ".", ".", "."],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "."],
        ["#", ".", ".", ".", ".", "#", ".", ".", ".", "."],
    ]
    input = [
        ["O", ".", ".", ".", ".", "#", ".", ".", ".", ".", ],
        ["O", ".", "O", "O", "#", ".", ".", ".", ".", "#", ],
        [".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ],
        ["O", "O", ".", "#", "O", ".", ".", ".", ".", "O", ],
        [".", "O", ".", ".", ".", ".", ".", "O", "#", ".", ],
        ["O", ".", "#", ".", ".", "O", ".", "#", ".", "#", ],
        [".", ".", "O", ".", ".", "#", "O", ".", ".", "O", ],
        [".", ".", ".", ".", ".", ".", ".", "O", ".", ".", ],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", ".", ],
        ["#", "O", "O", ".", ".", "#", ".", ".", ".", ".", ],
    ]
    assert tilt_north(input) == expected

@pytest.mark.parametrize("cycles, expected", [
    (1, [
        ".....#....",
        "....#...O#",
        "...OO##...",
        ".OO#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#....",
        "......OOOO",
        "#...O###..",
        "#..OO#....",
    ]),
    (2, [
        ".....#....",
        "....#...O#",
        ".....##...",
        "..O#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#...O",
        ".......OOO",
        "#..OO###..",
        "#.OOO#...O",
    ]),
    (3, [
        ".....#....",
        "....#...O#",
        ".....##...",
        "..O#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#...O",
        ".......OOO",
        "#...O###.O",
        "#.OOO#...O",
    ])
])
def test_cycle(cycles, expected):
    input = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]
    input = [list(row) for row in input]
    expected = [list(row) for row in expected]
    for _ in range(0, cycles):
        input = cycle(input)
    assert input == expected


@pytest.mark.parametrize("input, expected", [
    ([
    "OOOO.#.O..",
    "OO..#....#",
    "OO..O##..O",
    "O..#.OO...",
    "........#.",
    "..#....#.#",
    "..O..#.O.O",
    "..O.......",
    "#....###..",
    "#....#....",
    ], 136),
    ([
        ".....#....",
        "....#...O#",
        ".....##...",
        "..O#......",
        ".....OOO#.",
        ".O#...O#.#",
        "....O#...O",
        ".......OOO",
        "#...O###.O",
        "#.OOO#...O",
    ], 69)
])
def test_calculate_weight_north(input, expected):
    input = [list(row) for row in input]
    assert calculate_weight_north(input) == expected

@pytest.mark.parametrize("num_puzzles, resets_to, total_length, expected", [
    (10, 3, 13, 5),
    (10, 3, 15, 7),
    (10, 3, 23, 7),
    (10, 3, 34, 10),
    (10, 3, 35, 3),
])
def test_find_final_index(num_puzzles, resets_to, total_length, expected):
    assert find_final_index(num_puzzles, resets_to, total_length) == expected

def test_assignment1():
    assert process_file("input_test1.txt") == 64
