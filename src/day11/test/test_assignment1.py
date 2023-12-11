from typing import List

import pytest

from src.day11.assignment1 import process_file, build_universe


def test_build_universe():
    expected = [
        [".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ],
        [".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ],
        ["#", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ],
    ]
    result = build_universe("input_test1.txt")
    assert result == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 374
