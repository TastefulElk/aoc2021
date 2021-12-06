from src.utility.file import read_lines


def calculate_fish_count(input: str, days: int):
    initial_fishes = [int(x) for x in input.split(',')]

    fish_dict = {}
    for fish in initial_fishes:
        if fish in fish_dict:
            fish_dict[fish] += 1
        else:
            fish_dict[fish] = 1

    for _ in range(days):
        new_fish_count = {}
        for timer in range(9):
            new_fish_count[timer - 1] = fish_dict.get(timer, 0)

        new_fish_count[8] = new_fish_count.get(-1, 0)
        new_fish_count[6] = new_fish_count.get(6, 0) + new_fish_count.get(-1, 0)
        new_fish_count[-1] = 0
        fish_dict = new_fish_count.copy()

    return sum(fish_dict.values())


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    return calculate_fish_count(input_data[0], 80)


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    return calculate_fish_count(input_data[0], 256)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/day_06/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
