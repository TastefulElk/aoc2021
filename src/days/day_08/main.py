from src.utility.file import read_lines


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)

    lines = [line.split('|') for line in input_data]
    output_count = 0
    for _, output in lines:
        output_count += sum(len(code) in [2, 3, 4, 7] for code in output.split(' '))

    return output_count


def get_value_with_length(list: list[str], length: int) -> list[str]:
    return [x for x in list if len(x) == length]


def format(input):
    return list(map(lambda w: ''.join(sorted(w)), input))


def is_discovered(code, code_mapping):
    return code in code_mapping.values()


def has_length(code, length):
    return len(code) == length


def fully_overlaps(code, overlaps_with, code_mapping):
    return all(char in code_mapping[overlaps_with] for char in code)


def partial_overlap(code, overlaps_with, code_mapping):
    return any(char not in code for char in code_mapping[overlaps_with])


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)

    code = []
    len_mapping = {2: 1, 3: 7, 4: 4, 7: 8}

    total = 0
    lines = [line.split('|') for line in input_data]
    for input, output in lines:
        input_codes = format(input.strip().split())
        output_codes = format(output.strip().split())

        code_mapping = {}

        # find unique length codes
        for code in input_codes:
            if len(code) in len_mapping:
                code_mapping[len_mapping[len(code)]] = code

        # Find 6: 0, 6 and 9 has 6 chars but only 6 doesn't fully overlap number 1
        for code in input_codes:
            if has_length(code, 6) and partial_overlap(code, 1, code_mapping):
                code_mapping[6] = code
                break

        # Find 0: 0, 6 and 9 has 6 chars but only 0 doesn't fully overlap number 4 and isn't discovered yet
        for code in input_codes:
            if has_length(code, 6) and partial_overlap(code, 4, code_mapping) and not is_discovered(code, code_mapping):
                code_mapping[0] = code
                break

        # Find 9: only one with len 6 that hasn't been discovered yet
        for code in input_codes:
            if has_length(code, 6) and not is_discovered(code, code_mapping):
                code_mapping[9] = code
                break

        # Find 5: len 5 and fully overlaps 6
        for code in input_codes:
            if has_length(code, 5) and fully_overlaps(code, 6, code_mapping):
                code_mapping[5] = code
                break

        # Find 3: len 5 and fully overlaps 9 and hasn't been discovered yet
        for code in input_codes:
            if has_length(code, 5) and fully_overlaps(code, 9, code_mapping) and not is_discovered(code, code_mapping):
                code_mapping[3] = code
                break

        # Find 2: len 5 and hasn't been discovered yet
        for code in input_codes:
            if has_length(code, 5) and not is_discovered(code, code_mapping):
                code_mapping[2] = code

        # Transform key-value to value-key
        code_table = ({value: key for key, value in code_mapping.items()})
        total += int(''.join(map(str, [code_table[code] for code in output_codes])))

    return total


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/day_08/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
