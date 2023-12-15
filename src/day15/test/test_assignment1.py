from typing import List

import numpy as np
import pytest

from src.day15.assignment1 import process_file, calculate_hash


@pytest.mark.parametrize("command, expected", [
    ("HASH", 52),
    ("rn=1", 30),
    ("cm-", 253),
    ("qp=3", 97),
    ("cm=2", 47),
    ("qp-", 14),
    ("pc=4", 180),
    ("ot=9", 9),
    ("ab=5", 197),
    ("pc-", 48),
    ("pc=6", 214),
    ("ot=7", 231),
])
def test_calculate_hash(command, expected):
    assert calculate_hash(command) == expected

def test_assignment1():
    assert process_file("input_test1.txt") == 1320
