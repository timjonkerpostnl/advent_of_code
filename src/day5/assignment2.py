def get_seeds(stripped_line):
    seed_input = stripped_line.split(": ")[1].split(" ")
    seed_input = [int(s) for s in seed_input]
    seeds = []
    for seed_start, length in zip(seed_input[::2], seed_input[1::2]):
        seeds.append(range(seed_start, seed_start + length))
    return seeds


def find_minimum_location(maps, seed_ranges):
    input_ranges = seed_ranges
    for garden_map, lookup_dict in maps.items():
        new_ranges = create_ranges(input_ranges, lookup_dict)
        input_ranges = new_ranges

    minimum_location = min(new_range.start for new_range in input_ranges)
    return minimum_location


def create_ranges(input_ranges, lookup_dict):
    new_ranges = []
    while input_ranges:
        input_range = input_ranges.pop()
        found_interval = False
        for source, destination in lookup_dict.items():
            if input_range.stop <= source.start or input_range.start >= source.stop:
                # Not part of this source at all
                pass
            elif input_range.start >= source.start and input_range.stop <= source.stop:
                # Completely within
                destination_start = destination.start + input_range.start - source.start
                destination_stop = destination_start + input_range.stop - input_range.start
                new_ranges.append(range(destination_start, destination_stop))
                found_interval = True
                break
            elif input_range.start < source.start < input_range.stop <= source.stop:
                # Stop is within range of source but start is not
                input_ranges.append(range(input_range.start, source.start))
                input_ranges.append(range(source.start, input_range.stop))
                found_interval = True
                break
            elif source.start <= input_range.start < source.stop <= input_range.stop:
                # Start is within range of source but stop is not
                input_ranges.append(range(input_range.start, source.stop))
                input_ranges.append(range(source.stop, input_range.stop))
                found_interval = True
                break
            else:
                print(f"Debug {input_range.start >= source.start and input_range.stop <= source.stop}")
        if not found_interval:
            new_ranges.append(input_range)

    return new_ranges


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        map_name = None
        maps = {}
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if idx == 0:
                seeds = get_seeds(stripped_line)
            elif not any(char.isdigit() for char in stripped_line) and stripped_line != "":
                map_name = stripped_line
                maps[map_name] = {}
            elif stripped_line != "":
                destination_start, source_start, length = stripped_line.split(" ")
                destination_start, source_start, length = (
                    int(destination_start),
                    int(source_start),
                    int(length),
                )
                maps[map_name][range(source_start, source_start + length)] = range(
                    destination_start, destination_start + length
                )

        minimum_location = find_minimum_location(maps, seeds)

    return minimum_location


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
