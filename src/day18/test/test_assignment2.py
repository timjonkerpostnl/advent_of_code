from typing import List

import numpy as np
import pytest

from src.day18.assignment2 import (
    process_file, transform_instructions
)

@pytest.mark.parametrize("color, direction, steps", [
    ("#70c710", "R", 461937),
    ("#0dc571", "D", 56407),
    ("#5713f0", "R", 356671),
    ("#d2c081", "D", 863240),
    ("#59c680", "R", 367720),
    ("#411b91", "D", 266681),
    ("#8ceee2", "L", 577262),
    ("#caa173", "U", 829975),
    ("#1b58a2", "L", 112010),
    ("#caa171", "D", 829975),
    ("#7807d2", "L", 491645),
    ("#a77fa3", "U", 686074),
    ("#015232", "L", 5411),
    ("#7a21e3", "U", 500254),
])
def test_transform_instructions(color, direction, steps):
    assert transform_instructions(color) == (steps, direction)


def test_assignment1():
    assert process_file("input_test1.txt") == 952408144115
