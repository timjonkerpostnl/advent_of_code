def parse(filename):
    lines = open(filename).read()
    sections = lines.split("\n\n")
    seeds = [int(i) for i in sections[0].split(": ")[1].split()]
    maps = {}
    for sec in sections[1:]:
        sec = sec.split("\n")
        frm, to = sec[0].split()[0].split("-to-")
        maps[(frm, to)] = [[int(n) for n in m.split()] for m in sec[1:]]
    return seeds, maps


def find_min_location(source_name, source_start, source_length, maps):
    if source_name == "location":
        return source_start
    destination_name = next(d for s, d in maps.keys() if s == source_name)
    map_ranges = maps[(source_name, destination_name)]
    source_ranges = [(source_start, source_length)]

    minimum_location = float("inf")

    for map_destination_start, map_source_start, map_len in map_ranges:
        map_source_end = map_source_start + map_len
        new_source_ranges = []
        for source_start, source_length in source_ranges:
            source_end = source_start + source_length

            cuts = sorted([source_start, source_end, map_source_start, map_source_end])
            for start, end in zip(cuts[:-1], cuts[1:]):
                if start != end:  # length > 0
                    if source_start <= start and end <= source_end:  # inside source range
                        if map_source_start <= start and end <= map_source_end:  # inside map range
                            destination_start = map_destination_start + (start - map_source_start)
                            destination_length = end - start
                            minimum_location = min(
                                minimum_location,
                                find_min_location(
                                    destination_name,
                                    destination_start,
                                    destination_length,
                                    maps,
                                ),
                            )
                        else:  # not part of this range -> try other ranges or res
                            new_source_ranges.append((start, end - start))
                    else:
                        pass  # not part of src -> part of map -> ignore
                else:
                    pass  # empty range

        source_ranges = new_source_ranges

    # remaining source_ranges are mapped 1:1
    for source_start, source_length in source_ranges:
        minimum_location = min(
            minimum_location,
            find_min_location(destination_name, source_start, source_length, maps),
        )

    return minimum_location


def problem2(lines):
    seeds, maps = parse(lines)
    seeds = list(zip(seeds[::2], seeds[1::2]))

    minimum_location = float("inf")
    for seed_range_start, seed_range_length in seeds:
        num = find_min_location("seed", seed_range_start, seed_range_length, maps)
        minimum_location = min(num, minimum_location)
    print(minimum_location)
    return minimum_location


if __name__ == "__main__":
    min_loc = problem2("input.txt")
