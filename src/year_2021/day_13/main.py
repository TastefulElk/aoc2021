import re
from src.utility.file import read_lines


def get_grid_lines(input_data):
    return filter(lambda line: re.match("\d+,\d+", line) is not None, input_data)


def get_paper(input_data):
    return set(map(lambda line: tuple([int(x) for x in line.split(",")]), get_grid_lines(input_data)))


def parse_instruction(instruction):
    _, rel = instruction.split("along ")
    dimension, point = rel.split("=")
    return (dimension, int(point))


def get_fold_instructions(input_data):
    raw_instructions = filter(lambda line: re.match("fold along", line) is not None, input_data)
    instructions = map(parse_instruction, raw_instructions)
    return list(instructions)


def fold(paper: set[tuple], instruction: tuple[str, int]):
    paper_copy = paper.copy()
    dimension, point = instruction
    if dimension == "x":
        for x, y in paper:
            if x > point:
                paper_copy.remove((x, y))
                paper_copy.add((point - (x - point), y))

    elif dimension == "y":
        for x, y in paper:
            if y > point:
                paper_copy.remove((x, y))
                paper_copy.add((x, point - (y - point)))
    else:
        raise ValueError(f"Unknown dimension: {dimension}")

    return paper_copy


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    paper = get_paper(input_data)
    fold_instructions = get_fold_instructions(input_data)

    for instruction in fold_instructions[:1]:
        paper = fold(paper, instruction)

    return len(paper)


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    paper = get_paper(input_data)
    fold_instructions = get_fold_instructions(input_data)

    for instruction in fold_instructions:
        paper = fold(paper, instruction)

    xMax, _ = max(paper, key=lambda x: x[0])
    _, yMax = max(paper, key=lambda x: x[1])

    answer = ""
    for y in range(yMax + 1):
        answer += "\n" + "".join(["#" if (x, y) in paper else " " for x in range(xMax + 1)])

    return answer


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_13/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
