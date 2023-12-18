from shapely import Polygon
from tqdm import tqdm

def build_exterior(direction, exterior, position, steps):
    steps = int(steps)
    if direction == "R":
        position = (position[0] + steps, position[1])
    elif direction == "L":
        position = (position[0] - steps, position[1])
    elif direction == "U":
        position = (position[0], position[1] + steps)
    elif direction == "D":
        position = (position[0], position[1] - steps)
    exterior.append(position)
    return position


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        position = (0, 0)
        exterior = [position]
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            direction, steps, color = stripped_line.split(" ")
            position = build_exterior(direction, exterior, position, steps)

    polygon = Polygon(exterior)
    buffered = polygon.buffer(0.5, cap_style="square", join_style="mitre")
    # shapely.plotting.plot_polygon(polygon, color="b")
    # plt.show()

    return buffered.area


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
