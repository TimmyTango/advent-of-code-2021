from typing import List


def read_input_file(day: int) -> List[str]:
    with open(f'input/day{day}.txt', 'r') as file:
        return file.read().splitlines()
