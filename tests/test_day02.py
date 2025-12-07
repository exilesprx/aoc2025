from solutions.day02 import part1, part2


def test_example_file_part_1():
    file = "data/day02.example.txt"
    result = part1(file)
    assert result == 1227775554


def test_example_file_part_2():
    file = "data/day02.example.txt"
    result = part2(file)
    assert result == 0

