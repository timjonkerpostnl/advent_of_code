import math
from typing import Tuple

import networkx as nx
from matplotlib import pyplot as plt
from tqdm import tqdm
from shapely import Polygon
import shapely.plotting

from src.day20.assignment1 import create_modules, Pulse, FlipFlop, Conjunction, Module



def process_file(file_name: str) -> int:
    modules = create_modules(file_name)

    graph = nx.DiGraph()
    for module in modules.values():
        for destination in module.outgoing:
            graph.add_edge(module, destination)

    # graph_with_colors(graph)

    disjunct_graph = graph.copy()
    disjunct_graph.remove_nodes_from([modules["button"], modules["broadcaster"], modules["vm"], modules["lm"], modules["jd"], modules["fv"], modules["zg"], modules["rx"]])
    # graph_with_colors(disjunct_graph)

    button_hits = []
    for component in nx.weakly_connected_components(disjunct_graph):
        subgraph = nx.subgraph(disjunct_graph, component).copy()
        for destination in modules["broadcaster"].outgoing:
            if destination in subgraph.nodes:
                subgraph.add_edge(modules["broadcaster"], destination)
        subgraph.add_edge(modules["button"], modules["broadcaster"])
        # graph_with_colors(subgraph)
        sink = next(node for node in subgraph.nodes if isinstance(node, Conjunction))
        button_hits.append(get_button_hits(modules, sink))

    starts = [x[0] for x in button_hits]
    # ? I dont understand why starts doesnt matter
    periodicities = [[p - q for p, q in zip(x[1:], x[:-1])][0] for x in button_hits]

    return math.lcm(*periodicities)


def get_button_hits(modules, sink: Module):
    result = []
    for button_hits in tqdm(range(100000)):
        pulses_to_process = [(modules["button"], Pulse.low)]
        modules["rx"].received = []
        while pulses_to_process:
            current_module, outgoing_pulse = pulses_to_process.pop(0)
            if current_module == sink and outgoing_pulse == Pulse.low:
                result.append(button_hits)
                if len(result) == 2:
                    return result
            for destination in current_module.outgoing:
                new_outgoing_pulse = destination.process_input(outgoing_pulse, current_module)
                if new_outgoing_pulse is not None:
                    pulses_to_process.append((destination, new_outgoing_pulse))


def graph_with_colors(graph):
    node_colors = []
    labels = {}
    for node in graph:
        if isinstance(node, FlipFlop):
            node_colors.append("b")
        elif isinstance(node, Conjunction):
            node_colors.append("r")
        else:
            node_colors.append("g")
        labels[node] = node.name
    pos = nx.spring_layout(graph, seed=3113794652)  # positions for all nodes
    nx.draw(graph, pos, node_color=node_colors)
    nx.draw_networkx_labels(graph, pos, labels)
    plt.show()
    return labels, node_colors


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
