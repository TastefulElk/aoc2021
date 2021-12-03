from utility.file import read_lines


def binary_array_to_decimal(binary_array):
    return int(''.join(map(str, binary_array)), 2)


def get_most_common_bit_at_pos(matrix, pos):
    ones = 0
    zeroes = 0

    for line in matrix:

        if line[pos] == "1":
            ones += 1
        else:
            zeroes += 1

    return "1" if ones >= zeroes else "0"


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    bits = [0] * len(input_data[0])

    for line in input_data:
        for index, char in enumerate(line):
            if char == "1":
                bits[index] += 1

    gamma = [0] * len(bits)
    epsilon = [0] * len(bits)

    for index, bit in enumerate(bits):
        if bit > len(input_data) / 2:
            gamma[index] = 1
        else:
            epsilon[index] = 1

    return binary_array_to_decimal(gamma) * binary_array_to_decimal(epsilon)


def filter_by(filter_func, data):
    return list(filter(filter_func, data))


def calculate_rate(matrix: list[list[str]], keep_most_common: bool):
    lines_to_keep = matrix.copy()
    sequence_length = len(matrix[0])

    iterator = 0
    while len(lines_to_keep) > 1 and iterator < sequence_length:
        most_common_bit = get_most_common_bit_at_pos(lines_to_keep, iterator)

        filterKeepMostCommon = (lambda line: line[iterator] == most_common_bit)
        filterKeepLeastCommon = (lambda line: line[iterator] != most_common_bit)
        filter_ = filterKeepMostCommon if keep_most_common else filterKeepLeastCommon

        lines_to_keep = filter_by(filter_, lines_to_keep)
        iterator += 1

    return lines_to_keep[0]


def calculate_oxygen_rate(matrix):
    return calculate_rate(matrix, True)


def calculate_co2_rate(matrix):
    return calculate_rate(matrix, False)


def solve_part_2(inputFile):
    matrix = read_lines(inputFile)

    oxygen_rate = calculate_oxygen_rate(matrix.copy())
    co2_rate = calculate_co2_rate(matrix.copy())

    return binary_array_to_decimal(oxygen_rate) * binary_array_to_decimal(co2_rate)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/03/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
