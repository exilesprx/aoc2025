from typing import List


def read_input(file_path: str) -> List[str]:
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
