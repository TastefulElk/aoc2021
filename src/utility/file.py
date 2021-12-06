def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def read_lines_as_numbers(filename: str) -> list[str]:
    return [int(line) for line in read_lines(filename)]

