from functools import cache

from tqdm import tqdm


def is_possible_prefix(prefix: str, row: str) -> bool:
    return all(char1 == char2 or char2 == "?" for char1, char2 in zip(prefix, row))


@cache
def count_arrangements(sequence: str, sequence_lengths: tuple[int, ...]) -> int:
    # Remove all leading . so that we start with either a # or an ?
    sequence = sequence.lstrip(".")
    damage_length = sequence_lengths[0]
    length_required_after_last_damage = sum(sequence_lengths[1:]) + len(sequence_lengths) - 1
    position_first_damage = sequence.find("#")
    if position_first_damage == -1:
        position_first_damage = 999999
    count = 0
    for first_damage_position in range(
        min(
            len(sequence) - length_required_after_last_damage - damage_length,
            position_first_damage + 1,
        )
    ):
        # Each sequence consists of a few . the damage length # and a .
        # Goal is to find how many . start the sequence
        prefix = "." * first_damage_position + "#" * damage_length + "."
        if is_possible_prefix(prefix, sequence):
            if len(sequence_lengths) == 1:
                if all(char != "#" for char in sequence[len(prefix) :]):
                    count += 1
            else:
                count += count_arrangements(sequence[len(prefix) :], sequence_lengths[1:])
    return count


def main(file_name: str) -> int:
    summed = 0
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            sequence, sequence_lengths = stripped_line.split(" ")
            sequence = "?".join([sequence] * 5)
            sequence_lengths = ",".join([sequence_lengths] * 5)
            # Always end the sequence with a .
            sequence += "."
            sequence_lengths = [int(x) for x in sequence_lengths.split(",")]
            summed += count_arrangements(sequence, tuple(sequence_lengths))

    return summed


if __name__ == "__main__":
    result = main("input.txt")
    print(result)
