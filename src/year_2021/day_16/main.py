from collections import deque
from enum import Enum
from functools import reduce
from src.utility.file import read_lines


class OperatorType(Enum):
    SUM = 1
    PRODUCT = 2,
    MIN = 3,
    LITERAL = 4
    MAX = 5,
    GREATER_THAN = 6
    LESS_THAN = 7
    EQUALS = 8


type_map = {
    0: OperatorType.SUM,
    1: OperatorType.PRODUCT,
    2: OperatorType.MIN,
    3: OperatorType.MAX,
    4: OperatorType.LITERAL,
    5: OperatorType.GREATER_THAN,
    6: OperatorType.LESS_THAN,
    7: OperatorType.EQUALS
}

translation_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def read_next_bits(packet, length):
    return ''.join([packet.popleft() for _ in range(length)])


def get_package_version(packet):
    version_bin = read_next_bits(packet, 3)
    version = int(version_bin, 2)
    return version


def get_package_type(packet):
    type_id = int(read_next_bits(packet, 3), 2)
    return type_map[type_id]


def read_packet_header(packet):
    version = get_package_version(packet)
    type = get_package_type(packet)
    return version, type


def hex_to_binary(hex_string):
    binary_string = ""
    for char in hex_string:
        binary_string += translation_table[char]
    return binary_string


def read_literal_packet(packet) -> int:
    number_bits = ""
    while True:
        last_group = read_next_bits(packet, 1) == "0"
        val = read_next_bits(packet, 4)
        number_bits += val
        if last_group:
            value = int(number_bits, 2)
            return value


def calculate(operator, values):
    if operator == OperatorType.SUM:
        return sum(values)

    if operator == OperatorType.PRODUCT:
        return reduce(lambda x, y: x * y, values)

    if operator == OperatorType.MIN:
        return min(values)

    if operator == OperatorType.MAX:
        return max(values)

    assert len(values) == 2
    if operator == OperatorType.GREATER_THAN:
        return values[0] > values[1]

    if operator == OperatorType.LESS_THAN:
        return values[0] < values[1]

    if operator == OperatorType.EQUALS:
        return values[0] == values[1]

    raise ValueError(f"Unknown operator {operator}")


def process_packet(packet):
    _, type = read_packet_header(packet)
    if type == OperatorType.LITERAL:
        return read_literal_packet(packet)

    values = []
    length_mode = read_next_bits(packet, 1)
    length = int(read_next_bits(packet, 15) if length_mode == "0" else read_next_bits(packet, 11), 2)

    if length_mode == "0":
        stop_line = len(packet) - length
        while(len(packet) > stop_line):
            values.append(process_packet(packet))
    else:
        for _ in range(length):
            values.append(process_packet(packet))

    return calculate(type, values)


def get_version_sum(packet):
    version_sum = 0
    while(len(packet) > 0 and any(x != '0' for x in packet)):
        package_version, package_type = read_packet_header(packet)
        version_sum += package_version
        if package_type == OperatorType.LITERAL:
            read_literal_packet(packet)
        else:
            length_mode = read_next_bits(packet, 1)
            _ = read_next_bits(packet, 15) if length_mode == "0" else read_next_bits(packet, 11)

    return version_sum


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    bin_string = hex_to_binary(input_data[0])
    packet = deque([x for x in bin_string])
    version_sum = get_version_sum(packet)
    return version_sum


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    bin_string = hex_to_binary(input_data[0])
    packet = deque([x for x in bin_string])
    expression_value = process_packet(packet)
    return expression_value


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_16/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
