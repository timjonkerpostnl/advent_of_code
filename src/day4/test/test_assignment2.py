from typing import List

import pytest

from src.day4.assignment2 import process_file


def test_assignment2():
    assert process_file("input_test1.txt") == 30
