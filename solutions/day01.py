import sys
from solutions.utils import read_input


def solve(file_path: str, starting_point: int = 50) -> int:
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


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        exit("Please provide the input file path as a command-line argument.")
    solve(sys.argv[1])
