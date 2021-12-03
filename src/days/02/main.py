from utility.file import read_lines


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    x = 0
    y = 0
    for line in input_data:
        direction, stepsStr = line.split(" ")
        steps = int(stepsStr)
        if direction == "forward":
            x += steps
        elif direction == "up":
            y -= steps
        elif direction == "down":
            y += steps
    return x * y


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    x = 0
    y = 0
    aim = 0
    for line in input_data:
        direction, stepsStr = line.split(" ")
        steps = int(stepsStr)
        if direction == "forward":
            x += steps
            y += steps * aim
        elif direction == "up":
            aim -= steps
        elif direction == "down":
            aim += steps
    return x * y


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/02/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
