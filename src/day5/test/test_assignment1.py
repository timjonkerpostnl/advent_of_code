from typing import List

import pytest

from src.day5.assignment1 import process_file


def test_assignment1():
    assert process_file("input_test1.txt") == 35
