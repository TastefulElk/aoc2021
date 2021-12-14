from collections import defaultdict
from src.utility.file import read_lines


def simulate_polymer(steps, input_data):
    template = input_data[0]
    insertion_rules = {k: v for k, v in [x.split(" -> ") for x in input_data[2:]]}

    template_pairs = defaultdict(int)
    template_char_counts = defaultdict(int)

    for i, j in zip(template, template[1:]):
        template_pairs[i + j] = 1

    for a in template:
        template_char_counts[a] += 1

    for _ in range(steps):
        for pair, count in template_pairs.copy().items():
            if pair in insertion_rules:
                first_letter = pair[0]
                second_letter = pair[1]

                insert = insertion_rules[pair]

                template_char_counts[insert] += count
                template_pairs[first_letter + insert] += count
                template_pairs[insert + second_letter] += count
                template_pairs[pair] -= count

    return max(template_char_counts.values()) - min(template_char_counts.values())


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    return simulate_polymer(10, input_data)


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    return simulate_polymer(40, input_data)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_14/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
