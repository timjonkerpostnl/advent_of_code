from collections.abc import Iterator
from functools import cache

from tqdm import tqdm


def parse_input(lines: Iterator[str]) -> Iterator[tuple[str, tuple[int, ...]]]:
    for line in lines:
        row, groups = line.split()
        yield row, tuple(map(int, groups.split(',')))


@cache
def count_arrangements(sequence: str, sequence_lengths: tuple[int, ...]) -> int:
    first = sequence_lengths[0]
    rest_length = sum(sequence_lengths[1:]) + len(sequence_lengths) - 1
    count = 0
    for first_position in range(len(sequence) - rest_length - first):
        prefix = '.' * first_position + '#' * first + '.'
        if is_possible_prefix(prefix, sequence):
            if len(sequence_lengths) == 1:
                if all(char != '#' for char in sequence[len(prefix):]):
                    count += 1
            else:
                count += count_arrangements(sequence[len(prefix):], sequence_lengths[1:])
    return count


def is_possible_prefix(prefix: str, row: str) -> bool:
    return all(char1 == char2 or char2 == '?' for char1, char2 in zip(prefix, row))


def main(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            sequence, sequence_lengths = stripped_line.split(" ")
            sequence = "?".join([sequence] * 5)
            sequence_lengths = ",".join([sequence_lengths] * 5)
            sequence += "."
            sequence_lengths = [int(x) for x in sequence_lengths.split(",")]
            summed += count_arrangements(sequence, tuple(sequence_lengths))

    return summed


if __name__ == '__main__':
    result = main("input.txt")
    print(result)
