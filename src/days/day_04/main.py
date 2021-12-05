from utility.file import read_lines


def get_sum_unmarked_numbers(board: list[list[int]], drawn_numbers: list[int]) -> int:
    sum_unmarked_numbers = 0
    for row in board:
        for number in row:
            if number not in drawn_numbers:
                sum_unmarked_numbers += number
    return sum_unmarked_numbers


def is_bingo_line(line: list[int], drawn_numbers: list[int]) -> bool:
    return True if all(x in drawn_numbers for x in line) else False


def has_bingo(board: list[list[int]], drawn_numbers: list[int]) -> bool:
    # check rows
    for row in board:
        if is_bingo_line(row, drawn_numbers):
            return True

    # transpose array and check columns
    transposed_board = list(map(list, zip(*board)))
    for column in transposed_board:
        if is_bingo_line(column, drawn_numbers):
            return True

    return False


def get_lotto_numbers(lines: list[str]) -> list[int]:
    return [int(x) for x in lines[0].split(',')]


def get_lotto_boards(lines: list[str]) -> list[list[int]]:
    boards = []
    board_iterator = 0
    for line in lines[2:]:
        if line == '':
            board_iterator += 1
            continue

        if board_iterator >= len(boards):
            boards.append([])
        boards[board_iterator].append([int(x) for x in line.split()])

    return boards


def calculate_board_score(board: list[list[int]], drawn_numbers: list[int]) -> int:
    winning_number = drawn_numbers[-1]
    sum_unmarked_numbers = get_sum_unmarked_numbers(board, drawn_numbers)

    return sum_unmarked_numbers * winning_number


def solve_part_1(filePath):
    input_data = read_lines(filePath)
    lotto_numbers = get_lotto_numbers(input_data)

    boards = get_lotto_boards(input_data)

    # find first winning board
    drawn_numbers: list[int] = []
    while(len(lotto_numbers) > 0):
        drawn_numbers.append(lotto_numbers.pop(0))

        for board in boards:
            if has_bingo(board, drawn_numbers):
                return calculate_board_score(board, drawn_numbers)


def solve_part_2(filePath):
    input_data = read_lines(filePath)
    lotto_numbers = get_lotto_numbers(input_data)

    boards = get_lotto_boards(input_data)

    # find last winning board
    drawn_numbers: list[int] = []
    while(len(lotto_numbers) > 0):
        drawn_numbers.append(lotto_numbers.pop(0))

        for board in list(boards):
            if has_bingo(board, drawn_numbers):
                if len(boards) == 1:
                    return calculate_board_score(board, drawn_numbers)
                boards.remove(board)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/day_04/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
