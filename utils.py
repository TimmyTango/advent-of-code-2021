from typing import List


def read_input_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.readlines()
