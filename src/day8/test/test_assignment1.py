from typing import List

import pytest

from src.day8.assignment1 import process_file, get_connections


def test_get_connections():
    assert get_connections("input_test1b.txt") == (
        ["L", "L", "R"],
        {
            "AAA": {"L": "BBB", "R": "BBB"},
            "BBB": {"L": "AAA", "R": "ZZZ"},
            "ZZZ": {"L": "ZZZ", "R": "ZZZ"},
        },
    )


def test_assignment1():
    assert process_file("input_test1a.txt") == 2
    assert process_file("input_test1b.txt") == 6
