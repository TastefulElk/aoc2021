from typing import Tuple
from utility.file import read_lines


def parse_input(input) -> list[Tuple[list[int], list[int]]]:
    # example line: 123,456 -> 321,654
    lines = []
    for line in input:
        cords = line.split('->')

        # split by ',' and parse as int
        start = [int(x) for x in cords[0].split(',')]
        end = [int(x) for x in cords[1].split(',')]
        lines.append((start, end))

    return lines


def plot_lines(lines, includeDiagonal) -> list[Tuple[int, int]]:
    plotted_lines = []
    for line in lines:
        xStart, yStart = line[0]
        xEnd, yEnd = line[1]

        plotted_line = []

        # diagonal
        if xStart != xEnd and yStart != yEnd:
            if not includeDiagonal:
                continue

            xRange = range(min(xStart, xEnd), max(xStart, xEnd) + 1)
            yRange = range(min(yStart, yEnd), max(yStart, yEnd) + 1)

            if xStart > xEnd:
                xRange = list(reversed(xRange))
            if yStart > yEnd:
                yRange = list(reversed(yRange))

            for x in list(zip(xRange, yRange)):
                plotted_line.append(x)

        # vertical
        elif xStart == xEnd:
            for y in range(min(yStart, yEnd), max(yStart, yEnd) + 1):
                plotted_line.append((xStart, y))

        # horizontal
        elif yStart == yEnd:
            for x in range(min(xStart, xEnd), max(xStart, xEnd) + 1):
                plotted_line.append((x, yStart))

        plotted_lines.append(plotted_line)

    return plotted_lines


def get_count_of_overlapping_points(plotted_lines):
    visited_points_count = {}
    for line in plotted_lines:
        for x, y in line:
            visited_points_count[(x, y)] = visited_points_count.get((x, y), 0) + 1

    return sum([1 for x in visited_points_count.values() if x > 1])


def solve_part_2(file_path):
    input = read_lines(file_path)
    parsed_input = parse_input(input)
    plotted_lines = plot_lines(parsed_input, includeDiagonal=True)
    return get_count_of_overlapping_points(plotted_lines)


def solve_part_1(file_path):
    input = read_lines(file_path)
    parsed_input = parse_input(input)
    plotted_lines = plot_lines(parsed_input, includeDiagonal=False)
    return get_count_of_overlapping_points(plotted_lines)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/day_05/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
