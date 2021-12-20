from collections import defaultdict
from src.utility.file import read_lines


def get_pixel_group(x, y):
    ret = []
    for y_shift in [-1, 0, 1]:
        for x_shift in [-1, 0, 1]:
            ret.append((x + x_shift, y + y_shift))

    return ret


def enhance(input_image: defaultdict, algorithm, default) -> defaultdict:
    output_image = defaultdict(lambda: default)

    keys = input_image.keys()
    lowest_y = min(y for _, y in keys)
    lowest_x = min(x for x, _ in keys)
    highest_y = max(y for _, y in keys)
    highest_x = max(x for x, _ in keys)

    for y in range(lowest_y - 1, highest_y + 2):
        for x in range(lowest_x - 1, highest_x + 2):
            pixel_group = get_pixel_group(x, y)

            binary_string = ""
            for (px, py) in pixel_group:
                binary_string += "1" if input_image[(px, py)] == "#" else "0"
            pixel_sum = int(binary_string, 2)
            output_image[(x, y)] = algorithm[pixel_sum]

    return output_image


def parse_image(input):
    raw_input_image = [list(x) for x in [y for y in input]]

    input_image = defaultdict(lambda: ".")
    for y in range(len(raw_input_image)):
        for x in range(len(raw_input_image[y])):
            input_image[(x, y)] = raw_input_image[y][x]

    return input_image


def count_active_pixels(input_image):
    return sum(1 for x in input_image.values() if x == "#")


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    algorithm = input_data[0]

    input_image = parse_image(input_data[2:])
    output_image = enhance(input_image, algorithm, algorithm[0])
    output_image = enhance(output_image, algorithm, algorithm[-1])

    return count_active_pixels(output_image)


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    algorithm = input_data[0]

    input_image = parse_image(input_data[2:])

    output_image = input_image
    should_flip_default = algorithm[0] == "."

    for i in range(50):
        output_image = enhance(output_image.copy(), algorithm, algorithm[0 if should_flip_default or i % 2 == 0 else -1])

    return count_active_pixels(output_image)


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/year_2021/day_20/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
