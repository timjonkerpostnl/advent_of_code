from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Set, Tuple, Dict

from shapely import Polygon
from tqdm import tqdm

@dataclass(unsafe_hash=True)
class Brick:
    brick_index: int
    x1: int = field(hash=False, compare=False, repr=False)
    y1: int = field(hash=False, compare=False, repr=False)
    z1: int = field(hash=False, compare=False, repr=False)
    x2: int = field(hash=False, compare=False, repr=False)
    y2: int = field(hash=False, compare=False, repr=False)
    z2: int = field(hash=False, compare=False, repr=False)

    def overlap(self, brick: Brick) -> bool:
        return (self.x2 >= brick.x1 and brick.x2 >= self.x1) and (self.y2 >= brick.y1 and brick.y2 >= self.y1)

    def is_supported_by(self, bricks: List[Brick]) -> Tuple[int, Set[Brick]]:
        has_overlap_with = {brick for brick in bricks if self.overlap(brick)}
        if has_overlap_with:
            maximum_height = max(brick.z2 for brick in has_overlap_with)
            return maximum_height + 1, {brick for brick in has_overlap_with if brick.z2 == maximum_height}
        else:
            return 1, set()


def get_bricks(file_name):
    with open(file_name) as f:
        bricks = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            stripped_line = stripped_line.replace("~", ",")
            brick = Brick(idx, *(int(x) for x in stripped_line.split(",")))
            bricks.append(brick)
    bricks = sorted(bricks, key=lambda x: x.z2)
    return bricks


def get_is_supported_by(bricks) -> Dict[Brick, Set[Brick]]:
    is_supported_by_all = {}
    for idx, brick in enumerate(bricks):
        maximum_height, supporting_bricks = brick.is_supported_by(bricks[:idx])
        falling_height = brick.z1 - maximum_height
        brick.z1 -= falling_height
        brick.z2 -= falling_height
        is_supported_by_all[brick] = supporting_bricks
    return is_supported_by_all


def transform_to_supports(bricks, is_supported_by_all):
    supports = {brick: [] for brick in bricks}
    for brick, is_supported_by in is_supported_by_all.items():
        for supporting_brick in is_supported_by:
            supports[supporting_brick].append(brick)
    return supports


def process_file(file_name: str) -> int:
    bricks = get_bricks(file_name)

    # Let bricks fall down
    is_supported_by_all = get_is_supported_by(bricks)

    # Transform to supports
    supports = transform_to_supports(bricks, is_supported_by_all)

    # Find which can be disintegrated
    can_be_disintegrated = set()
    for brick, bricks_supported in supports.items():
        if all(len(is_supported_by_all[supported_brick]) > 1 for supported_brick in bricks_supported):
            can_be_disintegrated.add(brick)

    return len(can_be_disintegrated)


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
