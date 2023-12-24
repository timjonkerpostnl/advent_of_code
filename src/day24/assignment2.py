import sympy as sym
from src.day24.assignment1 import get_lines


def process_file(file_name: str, dimensions: int) -> int:
    lines = get_lines(file_name, dimensions)

    lines = lines[:3]
    a = [line[0] for line in lines]
    b = [line[1] for line in lines]

    equations = []
    variable_names = ["t0", "t1", "t2", "r0", "r1", "r2", "v0", "v1", "v2"]

    # Create SymPy symbols for the variables
    variables = sym.symbols(variable_names)
    for line_idx, line in enumerate(lines):
        for d in range(dimensions):
            r = variables[variable_names.index(f"r{d}")]
            v = variables[variable_names.index(f"v{d}")]
            t = variables[variable_names.index(f"t{line_idx}")]
            equations.append(
                sym.Eq(
                    r + v * t,
                    a[line_idx][d] + b[line_idx][d] * t
                )
            )

    s = sym.solve(equations, variables)[0]

    initial_coordinate = sum(round(p) for p in s[dimensions:2 * dimensions])

    return initial_coordinate


if __name__ == "__main__":
    result = process_file("input.txt", 3)
    print(result)
