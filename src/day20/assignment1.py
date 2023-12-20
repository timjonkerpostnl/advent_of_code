from __future__ import annotations
from abc import abstractmethod, ABC
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict

import networkx as nx
from shapely import Polygon
from tqdm import tqdm


class Pulse(Enum):
    high = "high"
    low = "low"


@dataclass(unsafe_hash=True)
class Module(ABC):
    name: str
    outgoing: List[Module] = field(hash=False, repr=False, compare=False)

    @abstractmethod
    def process_input(self, pulse: Pulse, from_module: Module) -> Optional[Pulse]:
        pass


@dataclass(unsafe_hash=True)
class FlipFlop(Module):
    status: str = field(default="off", repr=False, compare=False, hash=False)

    def process_input(self, pulse: Pulse, from_module: Module) -> Optional[Pulse]:
        if pulse == pulse.high:
            return None
        if self.status == "off":
            self.status = "on"
            return pulse.high
        else:
            self.status = "off"
            return pulse.low

@dataclass(unsafe_hash=True)
class Conjunction(Module):
    memory: Dict[Module, Pulse] = field(hash=False, repr=False, compare=False)

    def process_input(self, pulse: Pulse, from_module: Module) -> Optional[Pulse]:
        self.memory[from_module] = pulse
        if all(remembered_pulse == pulse.high for remembered_pulse in self.memory.values()):
            return pulse.low
        return pulse.high


@dataclass(unsafe_hash=True)
class Button(Module):

    def process_input(self, pulse: Pulse, from_module: Module) -> Optional[Pulse]:
        return pulse.low


@dataclass(unsafe_hash=True)
class Output(Module):
    received: List[Pulse] = field(hash=False, repr=False, compare=False)

    def process_input(self, pulse: Pulse, from_module: Module) -> Optional[Pulse]:
        self.received.append(pulse)
        return None


@dataclass(unsafe_hash=True)
class Broadcast(Module):

    def process_input(self, pulse: Pulse, from_module: Module) -> Optional[Pulse]:
        return pulse


def create_modules(file_name):
    with open(file_name) as f:
        button_module = Button("button", [])
        modules = {"button": button_module, "output": Output("output", [], [])}
        destination_module = {button_module: ["broadcaster"]}
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            module_name, destination = stripped_line.split(" -> ")
            if module_name[0] == "%":
                module = FlipFlop(module_name[1:], [])
            elif module_name[0] == "&":
                module = Conjunction(module_name[1:], [], {})
            elif module_name == "broadcaster":
                module = Broadcast(module_name, [])

            modules[module.name] = module
            destination_module[module] = destination.split(", ")

        for module, destination_names in destination_module.items():
            for destination in destination_names:
                if destination not in modules:
                    modules[destination] = Output(destination, [], [])
                module.outgoing.append(modules[destination])

            module.outgoing = [modules[destination] for destination in destination_names]
            for outgoing_module in module.outgoing:
                if isinstance(outgoing_module, Conjunction):
                    outgoing_module.memory[module] = Pulse.low
    return modules


def process_file(file_name: str) -> int:
    modules = create_modules(file_name)

    low_pulses_send = 0
    high_pulses_send = 0

    for _ in range(1000):
        pulses_to_process = [(modules["button"], Pulse.low)]
        while pulses_to_process:
            current_module, outgoing_pulse = pulses_to_process.pop(0)
            for destination in current_module.outgoing:
                if outgoing_pulse == Pulse.low:
                    low_pulses_send += 1
                else:
                    high_pulses_send += 1
                new_outgoing_pulse = destination.process_input(outgoing_pulse, current_module)
                if new_outgoing_pulse is not None:
                    pulses_to_process.append((destination, new_outgoing_pulse))

    return low_pulses_send * high_pulses_send


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
