from shapely import Polygon
from tqdm import tqdm

def process_file(file_name: str) -> int:
    with open(file_name) as f:
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()

    return 0


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
