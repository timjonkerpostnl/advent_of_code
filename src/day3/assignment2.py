import re
from typing import List


def find_gear_positions(input_string: str) -> List[int]:
    special_characters = r"\*"
    matches = [match.start() for match in re.finditer(special_characters, input_string)]

    return matches


def find_digit_sequences_with_positions(input_string):
    # Define the regex pattern for sequences of digits
    pattern = r"\d+"

    # Use re.finditer to find all matches in the input string along with their indices
    matches = [(int(match.group()), match.start(), match.end() - 1) for match in re.finditer(pattern, input_string)]

    return matches


def process_file(file_name: str) -> int:
    summed = 0
    special_character_positions = []
    digit_positions = []
    with open(file_name) as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            special_character_positions.append(find_gear_positions(stripped_line))
            digit_positions.append(find_digit_sequences_with_positions(stripped_line))

    for idx, positions in enumerate(special_character_positions):
        for position in positions:
            adjacent = []
            for digit_idx in range(max(0, idx - 1), min(len(digit_positions), idx + 2)):
                digit_row = digit_positions[digit_idx]
                found_in_row = []
                for num, start, end in digit_row:
                    if end >= position - 1 and start <= position + 1:
                        found_in_row.append((num, start, end))
                        adjacent.append(num)
                digit_positions[digit_idx] = [x for x in digit_row if x not in found_in_row]
            if len(adjacent) == 2:
                summed += adjacent[0] * adjacent[1]

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
