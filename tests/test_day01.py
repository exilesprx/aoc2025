from solutions.day01 import solve


def test_example_file():
    file = "data/day01.example.txt"
    result = solve(file)
    assert result == 3


def test_input_file():
    file = "data/day01.txt"
    result = solve(file)
    assert result == 1
