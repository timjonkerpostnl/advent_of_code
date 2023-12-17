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
    destination = (len(maze) - 1, len(maze[0]) - 1)
    lower_bound = nx.shortest_path_length(graph, (0, 0), destination)
    lower_bounds = {(0, 0): lower_bound}
    queue.put((lower_bound, 0, (0, 0), ("right", 0)))
    queue.put((lower_bound, 0, (0, 0), ("down", 0)))
    shortest_path = 9999999999
    minimum_travel_length = 4
    maximum_travel_length = 10
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
        _, length, node, (direction, direction_length) = queue.get()
        out_edges = graph.out_edges(node, data=True)
        for out_edge in out_edges:
            new_direction = out_edge[2]["direction"]
            if new_direction == opposite_direction[direction]:
                # We cannot turn 180 degrees
                continue
            if direction_length == maximum_travel_length and new_direction == direction:
                # We must turn 90 degrees
                continue
            new_node = None
            if new_direction != direction or direction_length == 0:
                if 0 < direction_length < minimum_travel_length:
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
                else:
                    # Set 4 steps in the same direction
                    new_length = length
                    new_length += out_edge[2]["weight"]
                    new_node = out_edge[1]
                    for _ in range(minimum_travel_length - 1):
                        out_edge = next(x for x in graph.out_edges(new_node, data=True) if x[2]["direction"] == new_direction)
                        new_length += out_edge[2]["weight"]
                        new_node = out_edge[1]
                    new_direction_length = minimum_travel_length
            else:
                new_length = length + out_edge[2]["weight"]
                new_node = out_edge[1]
                new_direction_length = direction_length + 1

            if new_length > shortest_path:
                # We already have a path that reached the end earlier
                continue
            if new_node == destination:
                if new_direction_length < minimum_travel_length:
                    # We cannot stop
                    continue
                # We reached the destination, save the shortest path length
                shortest_path = new_length
                print("Found a path")
            else:
                # We reached an intermediate node, check if this node is dominated
                previous_visit_to_node = shortest_arrivals[(new_node, new_direction)]
                if any(new_length >= previous_visit[0] and new_direction_length == previous_visit[1] for previous_visit
                       in previous_visit_to_node):
                    # The new visit is dominated by a previous visit
                    continue
                else:
                    # The new visit could potentially lead to the shortest path
                    previous_visit_to_node = [visit for visit in previous_visit_to_node if
                                              visit[0] < new_length or visit[1] < new_direction_length]
                    previous_visit_to_node.append((new_length, new_direction_length))
                    shortest_arrivals[(new_node, new_direction)] = previous_visit_to_node
                    if new_node in lower_bounds:
                        lower_bound = lower_bounds[new_node]
                    else:
                        # lower_bound = nx.shortest_path_length(graph, new_node, destination)
                        lower_bound = destination[0] - new_node[0] + destination[1] - new_node[1]
                        lower_bounds[new_node] = lower_bound
                    queue.put((new_length + lower_bound, new_length, new_node, (new_direction, new_direction_length)))

    print(f"Time: {datetime.datetime.now() - start}")
    return shortest_path


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
