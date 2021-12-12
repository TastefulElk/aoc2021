from functools import reduce
from src.utility.file import read_lines


PAIRS = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']'
}
OPENING_CHARS = PAIRS.keys()


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    error_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    total_score = 0
    for line in input_data:
        close_queue = []
        for char in line:
            if char in OPENING_CHARS:
                closer = PAIRS[char]
                # char is opening, adding closer to queue
                close_queue.append(closer)
                continue
            else:
                if close_queue[-1] == char:
                    close_queue.pop()
                else:
                    total_score += error_score[char]
                    break

    return total_score


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)

    error_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    scores = []
    for line in input_data:
        close_queue = []
        for char in line:
            if char in OPENING_CHARS:
                closer = PAIRS[char]
                # char is opening, adding closer to queue
                close_queue.append(closer)
                continue
            else:
                # char is closer, checking if next in queue
                if close_queue[-1] == char:
                    # char is closing and next is in queue - remove from queue
                    close_queue.pop()
                else:
                    # char is closing but not expected next - corrupt line
                    close_queue = []
                    break

        line_score = reduce(lambda x, y: x * 5 + error_score[y], close_queue[::-1], 0)
        if (line_score > 0):
            scores.append(line_score)

    # return "middle" score
    return sorted(scores)[len(scores) // 2]


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_10/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
