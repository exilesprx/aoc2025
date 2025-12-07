import sys
from solutions.utils import read_comma_separated_input


def part1(file_path: str) -> int:
    lines = read_comma_separated_input(file_path)
    invalid_ids = []

    for line in lines:
        start, end = line.split("-")
        for i in range(int(start), int(end) + 1):
            num = str(i)
            parts = num[0 : len(num) // 2], num[len(num) // 2 :]
            if parts[0] == parts[1]:
                invalid_ids.append(i)

    return sum(invalid_ids)


def part2(file_path: str) -> int:
    return 2


def solve(file_path: str):
    return part1(file_path), part2(file_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        exit("Please provide the input file path as a command-line argument.")
    result = solve(sys.argv[1])
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")
