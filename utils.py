from typing import List


def read_input_file(day: int) -> List[str]:
    with open(f'input/day{day}.txt', 'r') as file:
        return file.read().splitlines()

def read_input_as_int_list(day: int) -> List[int]:
    with open(f'input/day{day}.txt', 'r') as file:
        line = file.readline()
        return [int(n) for n in line.split(',')]
