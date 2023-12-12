import re

TRANSLATION = {
    "one": "1",
    "1": "1",
    "two": "2",
    "2": "2",
    "three": "3",
    "3": "3",
    "four": "4",
    "4": "4",
    "five": "5",
    "5": "5",
    "six": "6",
    "6": "6",
    "seven": "7",
    "7": "7",
    "eight": "8",
    "8": "8",
    "nine": "9",
    "9": "9",
}


def find_first_and_last_digit(input_string: str):
    pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")

    matches = [match.group(1) for match in pattern.finditer(input_string)]
    return TRANSLATION[matches[0]], TRANSLATION[matches[-1]]


summed = 0
with open("input.txt") as f:
    for idx, line in enumerate(f):
        # if idx > 100:
        #     break
        stripped_line = line.strip()
        first_digit, last_digt = find_first_and_last_digit(stripped_line)
        number = first_digit + last_digt
        # print(f"String {stripped_line} produced {number}")
        summed += int(number)
