from solutions.day01 import part1, part2, solve


def test_example_file_part_1():
    file = "data/day01.example.txt"
    result = part1(file)
    assert result == 3


def test_example_file_part_2():
    file = "data/day01.example2.txt"
    result = part2(file)
    assert result == 6
