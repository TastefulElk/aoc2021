import argparse
import importlib


def main():
    print("🎄 Advent of Code 2021 🎄")
    parser = argparse.ArgumentParser(description="AoC2021 runner")
    parser.add_argument("-d", "--day", required=True, type=int, help="Day to run")
    parser.add_argument("-p", "--part", required=True, type=int, help="Part to run")
    parser.add_argument("-e", "--example", action='store_true', help="Use example input")

    args = parser.parse_args()
    if (args.day < 1 or args.day > 25):
        print("Day must be between 1 and 25")
        return

    if (args.part < 1 or args.part > 2):
        print("Part must be between 1 and 2")
        return

    solution = importlib.import_module("days.day_{:02d}.main".format(args.day))
    answer = solution.solve(args.part, args.example)
    print("Answer: {}".format(answer))


if __name__ == "__main__":
    main()
