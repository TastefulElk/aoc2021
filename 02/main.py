def read_lines_from_file(filename):
    with open(filename, "r") as f:
        return f.readlines()

def solve_part_1(input_data: list):
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

def solve_part_2(input_data: list):
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

input_data = read_lines_from_file("02/input.txt")
input_data_example = read_lines_from_file("02/example.txt")

answer_part_1_example = solve_part_1(input_data_example)
answer_part_1 = solve_part_1(input_data)
print("Part 1: {}".format(answer_part_1))
print("Part 1 example: {}".format(answer_part_1_example))

answer_part_2_example = solve_part_2(input_data_example)
answer_part_2 = solve_part_2(input_data)
print("Part 2: {}".format(answer_part_2))
print("Part 2 example: {}".format(answer_part_2_example))