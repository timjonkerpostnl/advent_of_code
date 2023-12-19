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


def filter_condition(category: str, operator_str: str, threshold: int, item: Dict[str, int]) -> str:
    operator_mapping = {
        "<": operator.lt,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        ">=": operator.ge,
    }
    actual_operator = operator_mapping[operator_str]
    return actual_operator(item[category], threshold)


def sort_value(item: Dict[str, int], condition_list: List[Dict[str, Any]]) -> str:
    for condition in condition_list:
        if filter_condition(condition["category"], condition["operator"], condition["value"], item):
            return condition["result"]


def sort_all(item: Dict[str, int], workflows: Dict[str, List[Dict[str, Any]]]) -> Dict[str, int]:
    workflow_name = "in"
    while workflow_name != "R" and workflow_name != "A":
        condition_list = workflows[workflow_name]
        workflow_name = sort_value(item, condition_list)
    if workflow_name == "A":
        return item


def process_file(file_name: str) -> int:
    with open(file_name) as f:
        accepted_items = []
        work_flows = {}
        for idx, line in tqdm(enumerate(f)):
            stripped_line = line.strip()
            if stripped_line == "":
                continue
            elif stripped_line[0] != "{":
                get_workflows(stripped_line, work_flows)
            elif stripped_line[0] == "{":
                item_definition = stripped_line[1:].strip("}")
                categories = item_definition.split(",")
                item = {}
                for category in categories:
                    category_name, value = category.split("=")
                    item[category_name] = int(value)
                if sort_all(item, work_flows):
                    accepted_items.append(item)

    final_result = sum(sum(item.values()) for item in accepted_items)

    return final_result


if __name__ == "__main__":
    result = process_file("input.txt")
    print(result)
