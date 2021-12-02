def parse_input_as_numbers_list(filename):
    with open(filename) as f:
        return [int(x) for x in f]

def count_increases(readings):
    totalIncreases = 0
    for index, reading in enumerate(readings):
        if index == 0:
            continue
        if reading > readings[index - 1]:
            totalIncreases = totalIncreases + 1

    return totalIncreases

def solve_part_1(inputFile):
    readings = parse_input_as_numbers_list(inputFile)
    return count_increases(readings)

def solve_part_2(inputFile):
    readings = parse_input_as_numbers_list(inputFile)
    group_sums = []
    for index, reading in enumerate(readings):
        # break if we've seen the last complete group of 3
        if index + 2 > len(readings) - 1:
            break
        
        # get the sum of the full group
        group_sums.append(reading + readings[index + 1] + readings[index + 2])

    total_increases = count_increases(group_sums)
    return total_increases

def solve(part = 1, example = False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/01/{fileName}"
    
    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
