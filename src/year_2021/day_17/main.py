from src.utility.file import read_lines


def parse_target_area(input):
    a = input.split(": ")[1]
    x, y = a.split(", ")

    x1, x2 = [int(x) for x in x[2:].split("..")]
    y1, y2 = [int(y) for y in y[2:].split("..")]

    return {
        "x1": x1,
        "x2": x2,
        "y1": y1,
        "y2": y2
    }


def get_most_distant_position_for_velocity(x):
    return (x * (x + 1)) // 2


def position_after_step(x, y, xv, yv):
    x += xv
    y += yv
    return (x, y)


def is_within_target_area(x, y, target_area):
    return x >= target_area["x1"] and x <= target_area["x2"] and y >= target_area["y1"] and y <= target_area["y2"]


def is_overshot_target_area(x, y, target_area):
    return x > target_area["x2"] or y < target_area["y1"]


def passes_through_target_area(x: int, y: int, xv: int, yv: int, target_area):
    x, y = position_after_step(x, y, xv, yv)
    xv = xv - 1 if xv > 0 else 0
    yv = yv - 1

    if is_within_target_area(x, y, target_area):
        return True

    if is_overshot_target_area(x, y, target_area):
        return False

    return passes_through_target_area(x, y, xv, yv, target_area)


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    target_area = parse_target_area(input_data[0])

    # lowest possible x velocity is where x will ever be leftmost target area X
    lowest_xv = 1
    while True:
        if get_most_distant_position_for_velocity(lowest_xv) >= target_area["x1"]:
            break
        lowest_xv += 1

    highpoint = 0
    for yv in range(0, 250):
        if passes_through_target_area(0, 0, lowest_xv, yv, target_area):
            highpoint = get_most_distant_position_for_velocity(yv)

    return highpoint


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    target_area = parse_target_area(input_data[0])

    # lowest possible x velocity is where x will ever be leftmost target area X
    lowest_xv = 1
    while True:
        if get_most_distant_position_for_velocity(lowest_xv) >= target_area["x1"]:
            break
        lowest_xv += 1
    max_xv = target_area["x2"]

    hits = 0
    for xv in range(lowest_xv, max_xv + 1):
        for yv in range(target_area["y1"], 250):
            if passes_through_target_area(0, 0, xv, yv, target_area):
                hits = hits + 1

    return hits


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_17/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
