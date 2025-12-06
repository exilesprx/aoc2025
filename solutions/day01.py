import sys
from solutions.utils import read_input
from typing import Tuple


def part1(file_path: str, starting_point: int = 50) -> int:
    data = read_input(file_path)
    password = 0

    for line in data:
        parts = [line[0], line[1:]]
        direction = parts[0]
        distance = int(parts[1]) % 100  # remove full turns and get the remainder

        if direction == "L":
            starting_point -= distance
            if starting_point < 0:
                starting_point += 100
        elif direction == "R":
            starting_point += distance
            if starting_point > 99:
                starting_point -= 100
        else:
            raise ValueError(f"Invalid direction: {direction}")

        if starting_point == 0:
            password += 1

    return password


def part2(file_path: str, starting_point: int = 50) -> int:
    data = read_input(file_path)
    password = 0
    started_at_zero = starting_point == 0

    for line in data:
        parts = [line[0], line[1:]]
        direction = parts[0]
        distance = int(parts[1]) % 100  # remove full turns and get the remainder
        full_turns = int(parts[1]) // 100  # add times pointed at 0 for full turns

        if direction == "L":
            starting_point -= distance
            if starting_point < 0:
                starting_point += 100
                password += 0 if started_at_zero or starting_point == 0 else 1
        elif direction == "R":
            starting_point += distance
            if starting_point > 99:
                starting_point -= 100
                password += 0 if started_at_zero or starting_point == 0 else 1
        else:
            raise ValueError(f"Invalid direction: {direction}")

        if starting_point == 0:
            password += full_turns + 1
            started_at_zero = True
        else:
            password += full_turns
            started_at_zero = False

    return password


def solve(file_path: str, starting_point: int = 50) -> Tuple[int, int]:
    return part1(file_path, starting_point), part2(file_path, starting_point)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        exit("Please provide the input file path as a command-line argument.")
    result = solve(sys.argv[1])
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")
