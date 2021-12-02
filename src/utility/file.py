def read_lines(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

def read_lines_as_numbers(filename):
    return [int(line) for line in read_lines(filename)]
