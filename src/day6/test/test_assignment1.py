from typing import List

import pytest

from src.day6.assignment1 import process_file, calculate_distance, ways_to_beat_record


@pytest.mark.parametrize(
    "race_duration, hold_time, expected",
    [
        (7, 0, 0),
        (7, 1, 6),
        (7, 2, 10),
        (7, 3, 12),
        (7, 4, 12),
        (7, 5, 10),
        (7, 6, 6),
        (7, 7, 0),
    ],
)
def test_calculate_distance(race_duration, hold_time, expected):
    assert calculate_distance(race_duration, hold_time) == expected


@pytest.mark.parametrize(
    "race_duration, record, expected",
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
    ],
)
def test_ways_to_beat_record(race_duration, record, expected):
    assert ways_to_beat_record(record, race_duration) == expected


def test_assignment1():
    assert process_file("input_test1.txt") == 288
