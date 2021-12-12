from functools import cache
from src.utility.file import read_lines


def get_best_fuel_cost(initial_positions: list[int], fuel_cost_func=None):
    best_fuel_cost = None

    for pos in range(max(initial_positions)):
        fuel_cost = 0
        for initial_position in initial_positions:
            distance = abs(initial_position - pos)
            fuel_cost += fuel_cost_func(distance) if fuel_cost_func is not None else distance

        if best_fuel_cost is None or fuel_cost < best_fuel_cost:
            best_fuel_cost = fuel_cost

    return best_fuel_cost


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    initial_positions = [int(x) for x in input_data[0].split(',')]

    return get_best_fuel_cost(initial_positions)


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    initial_positions = [int(x) for x in input_data[0].split(',')]

    @cache
    def get_fuel_cost(distance):
        return sum(range(distance + 1))

    return get_best_fuel_cost(initial_positions, get_fuel_cost)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_07/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
