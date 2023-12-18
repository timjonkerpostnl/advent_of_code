import datetime
import re
from collections import defaultdict
from queue import PriorityQueue
from typing import List

import numpy as np
from tqdm import tqdm
import networkx as nx
from src.day17.assignment1 import build_graph


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        maze = []
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            maze.append([int(x) for x in stripped_line])

    graph = build_graph(maze)
    queue = PriorityQueue()
    queue.put((0, (0, 0), ("right", 0), [(0, 0)]))
    queue.put((0, (0, 0), ("down", 0), [(0, 0)]))
    destination = (len(maze) - 1, len(maze[0]) - 1)
    shortest_path = 9999999999
    minimum_travel_length = 4
    directions = ["right", "left", "up", "down"]
    shortest_arrivals = {(node, direction): [(9999999, 9999999)] for node in graph.nodes for direction in directions}
    opposite_direction = {
        "right": "left",
        "left": "right",
        "down": "up",
        "up": "down",
    }
    start = datetime.datetime.now()
    while not queue.empty():
        print(len(queue.queue))
        length, node, (direction, direction_length), path = queue.get()
        out_edges = graph.out_edges(node, data=True)
        for out_edge in out_edges:
            new_direction = out_edge[2]["direction"]
            if new_direction == opposite_direction[direction]:
                # We cannot turn 180 degrees
                continue
            if direction_length == 10 and new_direction == direction:
                # We must turn 90 degrees
                continue
            if direction != new_direction:
                if direction_length < minimum_travel_length:
                    # We must continue straight
                    continue
                elif (
                        node[0] < minimum_travel_length and new_direction == "up"
                        or node[1] < minimum_travel_length and new_direction == "left"
                        or node[0] > len(maze) - 1 - minimum_travel_length and new_direction == "down"
                        or node[1] > len(maze[0]) - 1 - minimum_travel_length and new_direction == "right"
                ):
                    # We cannot set 4 consecutive steps
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
                if new_direction_length < minimum_travel_length:
                    # We cannot stop
                    continue
                # We reached the destination, save the shortest path length
                shortest_path = new_length
            else:
                # We reached an intermediate node, check if this node is dominated
                previous_visit_to_node = shortest_arrivals[(new_node, new_direction)]
                if any(
                        new_length >= previous_visit[0] and (
                                new_direction_length == previous_visit[1] or
                                new_direction_length >= previous_visit[1] >= minimum_travel_length
                        )
                        for previous_visit in previous_visit_to_node
                ):
                    # The new visit is dominated by a previous visit
                    continue
                else:
                    # The new visit could potentially lead to the shortest path
                    previous_visit_to_node = [visit for visit in previous_visit_to_node if visit[0] < new_length or visit[1] < new_direction_length]
                    previous_visit_to_node.append((new_length, new_direction_length))
                    shortest_arrivals[(new_node, new_direction)] = previous_visit_to_node
                    new_path = path + [new_node]
                    queue.put((new_length, new_node, (new_direction, new_direction_length), new_path))

    print(f"Time: {datetime.datetime.now() - start}")
    return shortest_path

if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
