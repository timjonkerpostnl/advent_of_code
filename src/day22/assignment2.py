from typing import Tuple

from matplotlib import pyplot as plt
from tqdm import tqdm
from shapely import Polygon
import shapely.plotting

from src.day22.assignment1 import get_bricks, get_is_supported_by, transform_to_supports


def process_file(file_name: str) -> int:
    bricks = get_bricks(file_name)

    # Let bricks fall down
    is_supported_by_all = get_is_supported_by(bricks)

    # Transform to supports
    supports = transform_to_supports(bricks, is_supported_by_all)

    summed = 0
    for idx, brick in enumerate(bricks):
        if supports[brick]:
            fallen_bricks = {brick}
            for other in bricks[idx+1:]:
                if is_supported_by_all[other] and not is_supported_by_all[other].difference(fallen_bricks):
                    fallen_bricks.add(other)
            summed += len(fallen_bricks) - 1

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
