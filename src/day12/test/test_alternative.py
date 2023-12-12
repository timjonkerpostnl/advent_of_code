import pytest

from src.day12.alternative import count_arrangements


@pytest.mark.parametrize(
    "sequence, sequence_lengths, expected",
    [
        # ("???.###", [1, 1, 3], 1),
        # (".??..??...?##.", [1, 1, 3], 16384),
        # ("?#?#?#?#?#?#?#?", [1, 3, 1, 6], 1),
        # ("????.#...#...", [4, 1, 1], 16),
        # ("????.######..#####.", [1, 6, 5], 2500),
        ("?###????????", [3, 2, 1], 506250),
    ],
)
def test_count_arrangements(sequence, sequence_lengths, expected):
    sequence = "?".join([sequence] * 5)
    sequence_lengths *= 5
    sequence += "."
    assert count_arrangements(sequence, tuple(sequence_lengths)) == expected
