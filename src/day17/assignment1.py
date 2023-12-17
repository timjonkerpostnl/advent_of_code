import re
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import networkx as nx
from queue import PriorityQueue


def build_graph(maze) -> nx.DiGraph:
    graph = nx.DiGraph()
    for row_idx, row in enumerate(maze):
        for column_idx, weight in enumerate(row):
            if column_idx < len(row) - 1:
                # We may move right
                graph.add_edge((row_idx, column_idx), (row_idx, column_idx + 1), weight=maze[row_idx][column_idx + 1],
                               direction="right")
            if column_idx > 0:
                # We may move left
                graph.add_edge((row_idx, column_idx), (row_idx, column_idx - 1), weight=maze[row_idx][column_idx - 1],
                               direction="left")
            if row_idx < len(maze) - 1:
                # We may move down
                graph.add_edge((row_idx, column_idx), (row_idx + 1, column_idx), weight=maze[row_idx + 1][column_idx],
                               direction="down")
            if row_idx > 0:
                # We may move up
                graph.add_edge((row_idx, column_idx), (row_idx - 1, column_idx), weight=maze[row_idx - 1][column_idx],
                               direction="up")
    # nx.draw(graph, pos={n: (n[0], len(maze[0]) - n[1]) for n in graph.nodes}, with_labels=True)
    # plt.show()
    return graph


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        maze = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            maze.append([int(x) for x in stripped_line])

    graph = build_graph(maze)
    queue = PriorityQueue()
    queue.put((0, (0, 0), ("right", 0)))
    destination = (len(maze) - 1, len(maze[0]) - 1)
    shortest_path = 9999999999
    directions = ["right", "left", "up", "down"]
    shortest_arrivals = {(node, direction): [(9999999, 9999999)] for node in graph.nodes for direction in directions}
    opposite_direction = {
        "right": "left",
        "left": "right",
        "down": "up",
        "up": "down",
    }
    while not queue.empty():
        length, node, (direction, direction_length) = queue.get()
        out_edges = graph.out_edges(node, data=True)
        for out_edge in out_edges:
            new_direction = out_edge[2]["direction"]
            if new_direction == opposite_direction[direction]:
                # We cannot turn 180 degrees
                continue
            if direction_length == 3 and new_direction == direction:
                # We must turn 90 degrees
                continue

            new_length = length + out_edge[2]["weight"]
            new_node = out_edge[1]
            if new_direction == direction:
                new_direction_length = direction_length + 1
            else:
                new_direction_length = 1

            if new_length > shortest_path:
                # We already have a path that reached the end earlier
                continue
            if new_node == destination:
                # We reached the destination, save the shortest path length
                shortest_path = new_length
            else:
                # We reached an intermediate node, check if this node is dominated
                previous_visit_to_node = shortest_arrivals[(new_node, new_direction)]
                if any(new_length >= previous_visit[0] and new_direction_length >= previous_visit[1] for previous_visit in previous_visit_to_node):
                    # The new visit is dominated by a previous visit
                    continue
                else:
                    # The new visit could potentially lead to the shortest path
                    previous_visit_to_node = [visit for visit in previous_visit_to_node if visit[0] < new_length or visit[1] < new_direction_length]
                    previous_visit_to_node.append((new_length, new_direction_length))
                    shortest_arrivals[(new_node, new_direction)] = previous_visit_to_node
                    queue.put((new_length, new_node, (new_direction, new_direction_length)))

    return shortest_path


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
