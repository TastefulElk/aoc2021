from src.utility.file import read_lines


def get_adjacent(x, y, grid):
    adjacent = []
    if y > 0:
        adjacent.append((x, y - 1))
    if y < len(grid) - 1:
        adjacent.append((x, y + 1))
    if x > 0:
        adjacent.append((x - 1, y))
    if x < len(grid[y]) - 1:
        adjacent.append((x + 1, y))

    if y > 0 and x > 0:
        adjacent.append((x - 1, y - 1))
    if y > 0 and x < len(grid[y]) - 1:
        adjacent.append((x + 1, y - 1))
    if y < len(grid) - 1 and x > 0:
        adjacent.append((x - 1, y + 1))
    if y < len(grid) - 1 and x < len(grid[y]) - 1:
        adjacent.append((x + 1, y + 1))

    return adjacent


def flash(x, y, grid, flashed):
    if (x, y) in flashed:
        return grid

    grid[y][x] = 0
    flashed[(x, y)] = True

    adjacent = get_adjacent(x, y, grid)
    for x, y in adjacent:
        if (x, y) in flashed:
            continue

        grid[y][x] = grid[y][x] + 1
        if grid[y][x] > 9:
            grid = flash(x, y, grid, flashed)

    return grid


def generate_grid(lines: list[str]) -> list[list[int]]:
    grid = []
    for line in lines:
        grid.append([int(x) for x in line])
    return grid


def simulate_step(grid):
    """
    Simulate a step and return a map of which points flashed during the step.
    Mutates the grid in place.
    """
    flashed = {}

    should_flash = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = grid[y][x] + 1
            if grid[y][x] > 9:
                should_flash.append((x, y))

    flashed = {}
    for x, y in should_flash:
        grid = flash(x, y, grid, flashed)

    return flashed


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    grid = generate_grid(input_data)

    total_flashes = 0
    for _ in range(100):
        flashed = simulate_step(grid)
        total_flashes += len(flashed.keys())

    return total_flashes


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    grid = generate_grid(input_data)

    ALL_COUNT = len(grid) * len(grid[0])
    step = 1
    while True:
        flashed = simulate_step(grid)
        if len(flashed.keys()) == ALL_COUNT:
            return step
        step += 1


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_11/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
