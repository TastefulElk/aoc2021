from functools import reduce
from src.utility.file import read_lines


def is_low_point(x, y, height_map):
    lenX, lenY = len(height_map[0]), len(height_map)
    adjacent = get_adjacent(x, y, lenX, lenY)
    height = height_map[y][x]

    return all([height < height_map[adjY][adjX] for adjX, adjY in adjacent])


def get_adjacent(x: int, y: int, x_exclusive_end: int, y_exclusive_end: int):
    adjacent = []
    if x > 0:
        adjacent.append((x - 1, y))
    if x < x_exclusive_end - 1:
        adjacent.append((x + 1, y))
    if y > 0:
        adjacent.append((x, y - 1))
    if y < y_exclusive_end - 1:
        adjacent.append((x, y + 1))
    return adjacent


def find_low_points(height_map):
    low_points = []
    for y in range(len(height_map)):
        for x in range(len(height_map[y])):
            if is_low_point(x, y, height_map):
                low_points.append((x, y))
    return low_points


def get_height_map(inputFile):
    input_data = read_lines(inputFile)
    height_map = []
    for line in input_data:
        height_map.append([int(x) for x in line])

    return height_map


def get_basin(x, y, height_map, visited={}) -> dict:
    """
    recursively find how many adjacent numbers are lower than their adjacent numbers
    """
    visited_copy = visited.copy()

    visited_copy[(x, y)] = True
    height = height_map[y][x]
    lenX, lenY = len(height_map[0]), len(height_map)
    adjacent = get_adjacent(x, y, lenX, lenY)

    for adjX, adjY in adjacent:
        already_visited = visited_copy.get((adjX, adjY)) is True
        if already_visited:
            continue
        if height_map[adjY][adjX] != 9 and height_map[adjY][adjX] > height:
            visited_copy = get_basin(adjX, adjY, height_map, visited_copy)

    return visited_copy


def get_basin_size(x, y, height_map):
    return len(get_basin(x, y, height_map).values())


def solve_part_1(inputFile):
    height_map = get_height_map(inputFile)
    low_points = find_low_points(height_map)

    return sum([height_map[y][x] + 1 for x, y in low_points])


def solve_part_2(inputFile):
    height_map = get_height_map(inputFile)
    low_points = find_low_points(height_map)
    basin_sizes = [get_basin_size(x, y, height_map) for x, y in low_points]

    # return the product of the three largest basins multiplied
    return reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:])


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_09/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
