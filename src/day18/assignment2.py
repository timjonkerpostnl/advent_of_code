from typing import Tuple

from matplotlib import pyplot as plt
from tqdm import tqdm
from shapely import Polygon
import shapely.plotting

from src.day18.assignment1 import build_exterior


def transform_instructions(color: str) -> Tuple[int, str]:
    steps = int(color[1:6], 16)
    if color[-1] == "0":
        direction = "R"
    elif color[-1] == "1":
        direction = "D"
    elif color[-1] == "2":
        direction = "L"
    elif color[-1] == "3":
        direction = "U"
    else:
        raise ValueError("Invalid")
    return steps, direction


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        position = (0, 0)
        exterior = [position]
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            direction, steps, color = stripped_line.split(" ")
            steps, direction = transform_instructions(color[1: -1])
            position = build_exterior(direction, exterior, position, steps)

    polygon = Polygon(exterior)
    buffered = polygon.buffer(0.5, cap_style="square", join_style="mitre")
    shapely.plotting.plot_polygon(polygon, color="b")
    plt.show()

    return buffered.area


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
