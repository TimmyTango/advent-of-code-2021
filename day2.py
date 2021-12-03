from typing import Tuple

from utils import read_input_file


class Ship:
    def __init__(self, position: int, depth: int, aim: int):
        self.position = position
        self.depth = depth
        self.aim = aim

    def __str__(self) -> str:
        return f'{self.position * self.depth}'

    def forward(self, unit: int) -> None:
        pass

    def down(self, unit: int) -> None:
        pass
    
    def up(self, unit: int) -> None:
        pass


class Part1Ship(Ship):
    def forward(self, unit: int) -> None:
        self.position += unit

    def down(self, unit: int) -> None:
        self.depth += unit
    
    def up(self, unit: int) -> None:
        self.depth -= unit


class Part2Ship(Ship):
    def forward(self, unit: int) -> None:
        self.position += unit
        self.depth += self.aim * unit

    def down(self, unit: int) -> None:
        self.aim += unit
    
    def up(self, unit: int) -> None:
        self.aim -= unit


def parse_instruction(instruction: str) -> Tuple[str, int]:
    command, unit = instruction.split(' ')
    return command, int(unit)


def interperet_command(ship: Ship, command: str, unit: int) -> None:
    if command == 'forward':
        ship.forward(unit)
    elif command == 'down':
        ship.down(unit)
    elif command == 'up':
        ship.up(unit)
    else:
        raise ValueError(f'Invalid command: {command}')


if __name__ == '__main__':
    input_data = read_input_file(2)
    part1_ship = Part1Ship(0, 0, 0)
    part2_ship = Part2Ship(0, 0, 0)

    for inst in input_data:
        command, unit = parse_instruction(inst)
        interperet_command(part1_ship, command, unit)
        interperet_command(part2_ship, command, unit)
    
    print('part1 result:', part1_ship)
    assert str(part1_ship) == '1813801'

    print('part2 result:', part2_ship)
    assert str(part2_ship) == '1960569556'
