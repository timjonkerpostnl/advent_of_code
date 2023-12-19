from dataclasses import dataclass
from typing import List, Dict, Any
import operator
from shapely import Polygon
from tqdm import tqdm


def get_workflows(stripped_line, work_flows):
    name, workflow_definition = stripped_line.split("{")
    workflow_definition = workflow_definition[:-1]
    steps = workflow_definition.split(",")
    work_flows[name] = []
    for step in steps:
        if ":" in step:
            condition, result = step.split(":")
            if "<" in condition:
                category, value = condition.split("<")
                operator_str = "<"
            elif ">" in condition:
                category, value = condition.split(">")
                operator_str = ">"
            else:
                raise NotImplemented(f"Not implemented for {condition}")
            value = int(value)
        else:
            result = step
            value = -1
            category = "x"
            operator_str = ">"
        work_flows[name].append({"category": category, "operator": operator_str, "value": value, "result": result})


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        work_flows = {}
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            if stripped_line == "":
                continue
            elif stripped_line[0] != "{":
                get_workflows(stripped_line, work_flows)

    found_potential_item = []

    for workflow_name, condition_list in work_flows.items():
        condition_indices = [idx for idx, condition in enumerate(condition_list) if condition["result"] == "A"]
        for condition_index in condition_indices:
            potential_item = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
            current_workflow_name = workflow_name
            current_condition_index = condition_index
            previous_workflow_name = None
            while previous_workflow_name != "in":
                # The condition at condition_index must be true
                current_condition_list = work_flows[current_workflow_name]
                condition_info = current_condition_list[current_condition_index]
                if condition_info["operator"] == ">":
                    potential_item[condition_info["category"]][0] = max(
                        potential_item[condition_info["category"]][0], condition_info["value"] + 1
                    )
                elif condition_info["operator"] == "<":
                    potential_item[condition_info["category"]][1] = min(
                        potential_item[condition_info["category"]][1], condition_info["value"] - 1
                    )

                # All preceding conditions from this workflow must be false
                for idx in range(current_condition_index):
                    condition_info = current_condition_list[idx]
                    if condition_info["operator"] == ">":
                        potential_item[condition_info["category"]][1] = min(
                            potential_item[condition_info["category"]][1], condition_info["value"]
                        )
                    elif condition_info["operator"] == "<":
                        potential_item[condition_info["category"]][0] = max(
                            potential_item[condition_info["category"]][0], condition_info["value"]
                        )

                previous_workflow_name = current_workflow_name
                # Find out how to arrive in this workflow
                new_search = [(idx, workflow_name_new)
                              for workflow_name_new, cond_list in work_flows.items()
                              for idx, condition in enumerate(cond_list)
                              if condition["result"] == current_workflow_name]
                if len(new_search) == 1:
                    current_condition_index = new_search[0][0]
                    current_workflow_name = new_search[0][1]
                elif len(new_search) > 1:
                    raise NotImplemented("Did not expect more ways leading to here")
                elif current_workflow_name == "in":
                    found_potential_item.append(potential_item)
                else:
                    raise NotImplemented("Workflow cannot be reached")

    summed = 0
    for potential_item in found_potential_item:
        summed += (potential_item["x"][1] + 1 - potential_item["x"][0]) * (potential_item["m"][1] + 1 - potential_item["m"][0]) *(potential_item["a"][1] + 1 - potential_item["a"][0]) * (potential_item["s"][1] + 1 - potential_item["s"][0])

    return summed


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
