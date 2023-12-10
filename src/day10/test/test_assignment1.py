from typing import List

import pytest

from src.day10.assignment1 import process_file


def test_assignment1():
    assert process_file("input_test1.txt") == 4
    assert process_file("input_test2.txt") == 8
