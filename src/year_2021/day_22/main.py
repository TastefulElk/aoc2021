from collections import defaultdict
from src.utility.file import read_lines


def parse_instruction(line):
    action, coords = line.split(" ")
    x, y, z = coords.split(",")

    ret = {
        "action": action,
    }

    for values, label in zip([x, y, z], ["x", "y", "z"]):
        start, end = values.split("=")[1].split("..")
        floor = int(start)
        ceil = int(end)

        ret[label] = (floor, ceil)

    return ret


def parse_instructions(lines):
    return [parse_instruction(line) for line in lines]


def is_valid_instruction(instruction):
    """
    check if instruction overlap -50..50,-50..50,-50..50 area
    """
    x, y, z = instruction["x"], instruction["y"], instruction["z"]
    valid = True
    if (x[0] < -50 and x[1] < -50) or (x[0] > 50 and x[1] > 50):
        valid = False

    if (y[0] < -50 and y[1] < -50) or (y[0] > 50 and y[1] > 50):
        valid = False

    if (z[0] < -50 and z[1] < -50) or (z[0] > 50 and z[1] > 50):
        valid = False

    return valid


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    instructions = parse_instructions(input_data)

    cubes = defaultdict(lambda: 0)
    for instruction in instructions:
        if not is_valid_instruction(instruction):
            continue

        for x in range(max(-50, instruction["x"][0]), min(instruction["x"][1] + 1, 51)):
            for y in range(max(-50, instruction["y"][0]), min(instruction["y"][1] + 1, 51)):
                for z in range(max(-50, instruction["z"][0]), min(instruction["z"][1] + 1, 51)):
                    value = 1 if instruction["action"] == "on" else 0
                    cubes[(x, y, z)] = value

    return sum(1 if x == 1 else 0 for x in cubes.values())


def count_cubes(x, y, z):
    return (x[1] + 1 - x[0]) * (y[1] + 1 - y[0]) * (z[1] + 1 - z[0])


def count_cubes_in_cubes(cubes):
    if len(cubes) == 0:
        return 0

    current, *remaining_cubes = cubes
    overlaps = get_overlaps(current, remaining_cubes)
    return count_cubes(current["x"], current["y"], current["z"]) + count_cubes_in_cubes(remaining_cubes) - count_cubes_in_cubes(overlaps)


def get_overlap(cube_a, cube_b):
    x_overlap_range = range(max(cube_a["x"][0], cube_b["x"][0]), min(
        cube_a["x"][-1], cube_b["x"][-1]) + 1)
    if len(x_overlap_range) == 0:
        return None
    x_overlap = ((x_overlap_range[0], x_overlap_range[-1]))

    y_overlap_range = range(max(cube_a["y"][0], cube_b["y"][0]), min(
        cube_a["y"][-1], cube_b["y"][-1]) + 1)
    if len(y_overlap_range) == 0:
        return None
    y_overlap = (y_overlap_range[0], y_overlap_range[-1])

    z_overlap_range = range(max(cube_a["z"][0], cube_b["z"][0]), min(
        cube_a["z"][-1], cube_b["z"][-1]) + 1)
    if len(z_overlap_range) == 0:
        return None
    z_overlap = ((z_overlap_range[0], z_overlap_range[-1]))

    return {"x": x_overlap, "y": y_overlap, "z": z_overlap}


def get_overlaps(cube, other_cubes):
    overlaps = []
    for other_cube in other_cubes:
        overlap = get_overlap(cube, other_cube)
        if overlap is not None:
            overlaps.append(overlap)

    return overlaps


def execute_instructions(instructions: list):
    """
    instead of turning off cubes, just count how many we turn on for each instruction but and
    remove the count of overlapping cubes in the remaining instructions
    """

    if len(instructions) == 0:
        return 0

    instruction, *remaining_instructions = instructions
    if instruction["action"] == "off":
        return execute_instructions(remaining_instructions)

    overlaps = get_overlaps(instruction, remaining_instructions)

    return (
        count_cubes(instruction["x"], instruction["y"], instruction["z"]) -
        count_cubes_in_cubes(overlaps) +
        execute_instructions(remaining_instructions)
    )


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    instructions = parse_instructions(input_data)

    return execute_instructions(instructions)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_22/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
