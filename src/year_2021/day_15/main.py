from collections import defaultdict, deque
from src.utility.file import read_lines
from math import inf


def get_adjacent(x, y, grid) -> list[tuple[int, int]]:
    adjacent = []
    if x > 0:
        adjacent.append((x - 1, y))
    if x < len(grid[0]) - 1:
        adjacent.append((x + 1, y))
    if y > 0:
        adjacent.append((x, y - 1))
    if y < len(grid) - 1:
        adjacent.append((x, y + 1))
    return adjacent


def get_lowest_cost_between(start, end, grid):
    costs = defaultdict(lambda: inf)
    costs[start] = 0
    queue = deque()
    queue.append(start)
    visited = set()

    while len(queue) > 0:
        x, y = queue.popleft()
        for adjX, adjY in get_adjacent(x, y, grid):
            cost = costs[(x, y)] + grid[adjY][adjX]
            if cost < costs[(adjX, adjY)]:
                costs[(adjX, adjY)] = cost
                visited.add((adjX, adjY))
                queue.append((adjX, adjY))

    return costs[end]


def get_grid(input_data, expanded=False):
    grid = []
    for line in input_data if not expanded else input_data * 5:
        row = []
        for num in line if not expanded else line * 5:
            row.append(int(num))
        grid.append(row)

    if not expanded:
        return grid

    original_grid_size = len(input_data)
    for y in range(original_grid_size):
        for x in range(original_grid_size):
            for i in range(5):
                for j in range(5):
                    grid[y + original_grid_size * j][x + original_grid_size * i] = (grid[y][x] - 1 + i + j) % 9 + 1

    return grid


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    grid = get_grid(input_data)

    return get_lowest_cost_between((0, 0), (len(grid[0]) - 1, len(grid) - 1), grid)


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    grid = get_grid(input_data, True)

    return get_lowest_cost_between((0, 0), (len(grid[0]) - 1, len(grid) - 1), grid)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_15/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
