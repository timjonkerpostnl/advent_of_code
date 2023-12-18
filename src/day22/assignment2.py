from typing import Tuple

from matplotlib import pyplot as plt
from tqdm import tqdm
from shapely import Polygon
import shapely.plotting

from src.day18.assignment1 import build_exterior


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()

    return 0


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
