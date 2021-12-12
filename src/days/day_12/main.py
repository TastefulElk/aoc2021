from collections import defaultdict
from src.utility.file import read_lines


def traverse(current: str, paths: dict[str, list[str]], allow_visit_small_cave_twice: bool, visited=None, valid_count=0):
    if visited is None:
        visited = defaultdict(int)

    for path in paths[current]:
        visited_copy = visited.copy()
        if path == "start":
            continue

        if path == "end":
            valid_count += 1
            continue

        visited_small_caves = list(filter(lambda x: x.islower(), visited_copy.keys()))
        any_small_cave_visited_twice = any(visited_copy[v] > 1 for v in visited_small_caves)
        not_visited = path not in visited_copy

        if not_visited or path.isupper() or (allow_visit_small_cave_twice and not any_small_cave_visited_twice):
            visited_copy[path] += 1
            valid_count = traverse(path, paths, allow_visit_small_cave_twice, visited_copy, valid_count)

    return valid_count


def get_paths(input_data):
    paths = defaultdict(list[str])
    for line in input_data:
        a, b = line.split('-')
        paths[a].append(b)
        paths[b].append(a)

    return paths


def solve_part_1(inputFile):
    input_data = read_lines(inputFile)
    paths = get_paths(input_data)
    valid_paths = traverse("start", paths, allow_visit_small_cave_twice=False)

    return valid_paths


def solve_part_2(inputFile):
    input_data = read_lines(inputFile)
    paths = get_paths(input_data)
    valid_paths = traverse("start", paths, allow_visit_small_cave_twice=True)

    return valid_paths


def solve(part=1, example=False):
    fileName = "input.txt" if not example else "example.txt"
    filePath = f"src/days/day_12/{fileName}"

    if part == 1:
        return solve_part_1(filePath)
    elif part == 2:
        return solve_part_2(filePath)
    else:
        raise ValueError(f'There is no part {part}')
