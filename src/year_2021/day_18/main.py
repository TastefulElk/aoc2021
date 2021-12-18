# heavily inspired by https://github.com/shnako/advent-of-code-2021/blob/main/day18/solution_list.py

from math import floor, ceil
from src.utility.file import read_lines


def explode(elements, opening_bracket_index):
    left_number = elements[opening_bracket_index + 1]
    right_number = elements[opening_bracket_index + 2]

    for i in range(opening_bracket_index - 1, 0, -1):
        if isinstance(elements[i], int):
            elements[i] += left_number
            break

    for i in range(opening_bracket_index + 4, len(elements)):
        if isinstance(elements[i], int):
            elements[i] += right_number
            break

    return elements[:opening_bracket_index] + [0] + elements[opening_bracket_index + 4:]


def try_explode(elements):
    open_brackets = 0
    for i in range(len(elements)):
        if open_brackets == 4 and elements[i] == '[':
            elements = explode(elements, i)
            return True, elements
        elif elements[i] == '[':
            open_brackets += 1
        elif elements[i] == ']':
            open_brackets -= 1

    return False, elements


def split(elements: list):
    for i in range(len(elements)):
        if isinstance(elements[i], int) and elements[i] >= 10:
            elements[i:i + 1] = ['[', floor(elements[i] / 2), ceil(elements[i] / 2), ']']
            return True, elements
    return False, elements


def reduce_number(elements: list):
    while True:
        did_explode, elements = try_explode(elements)
        if did_explode:
            continue

        did_split, elements = split(elements)
        if not did_split:
            break

    return elements


def add(a, b):
    c = ["["] + a + b + ["]"]
    return reduce_number(c)


def calculate_magnitude(elements, index=0):
    if isinstance(elements[index], int):
        return elements[index], index

    left_sum, index = calculate_magnitude(elements, index + 1)
    right_sum, index = calculate_magnitude(elements, index + 1)

    return 3 * left_sum + 2 * right_sum, index + 1


def parse_line(line):
    elements = filter(lambda element: element != ',', line)
    elements = list(map(lambda element: int(element) if element.isdigit() else element, elements))
    return elements


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    elements = list(map(parse_line, input_data))

    sum = elements[0]
    for element in elements[1:]:
        sum = add(sum, element)

    magnitude, _ = calculate_magnitude(sum)
    return magnitude


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    lines = list(map(parse_line, input_data))

    highest_magnitude = 0

    for a in lines:
        for b in lines:
            if a == b:
                continue

            magnitude, _ = calculate_magnitude(add(a, b))
            highest_magnitude = max(highest_magnitude, magnitude)

    return highest_magnitude


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_18/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
