from dataclasses import dataclass
from typing import List


@dataclass
class Octopus:
    energy: int = 0
    has_flashed: bool = False


class OctopiGrid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.octopi: List[List[Octopus]] = []
        for y in range(height):
            self.octopi.append([])
            for x in range(width):
                self.octopi[y].append(Octopus())

    def __str__(self) -> str:
        s = ''
        for y in range(self.height):
            for x in range(self.width):
                s += str(self.octopi[y][x].energy)
            s += '\n'
        return s

    def step(self) -> int:
        for y in range(self.height):
            for x in range(self.width):
                energy = self.increment_energy(x, y)

        for y in range(self.height):
            for x in range(self.width):
                if self.should_flash(x, y):
                    self.flash(x, y)

        flashes = 0

        for y in range(self.height):
            for x in range(self.width):
                octopus = self.octopi[y][x]
                if octopus.has_flashed:
                    flashes += 1
                    octopus.has_flashed = False
                    octopus.energy = 0

        return flashes

    def should_flash(self, x: int, y: int) -> bool:
        octopus = self.octopi[y][x]
        return not octopus.has_flashed and octopus.energy >= 10

    def within_bounds(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def increment_energy(self, x: int, y: int, allow_flash: bool = False, step: int = 1):
        if self.within_bounds(x, y):
            octopus = self.octopi[y][x]
            if not octopus.has_flashed:
                octopus.energy += step
                if allow_flash and octopus.energy >= 10:
                    self.flash(x, y)

    def flash(self, x: int, y: int):
        self.octopi[y][x].has_flashed = True
        
        directions = (
            (-1, -1),  # Top left
            ( 0, -1),  # Top
            ( 1, -1),  # Top Right
            (-1,  0),  # Left
            ( 1,  0),  # Right
            (-1,  1),  # Bottom Left
            ( 0,  1),  # Bottom
            ( 1,  1),  # Bottom Right
        )
        for dx, dy in directions:
            self.increment_energy(x + dx, y + dy, allow_flash=True)


def read_input_file() -> OctopiGrid:
    with open('input/day11.txt') as file:
        w = 10
        h = 10
        grid = OctopiGrid(w, h)
        for y in range(h):
            line = file.readline()
            for x in range(w):
                grid.octopi[y][x].energy = int(line[x])

    return grid


if __name__ == '__main__':
    grid = read_input_file()

    syncd_flash_step = -1
    flashes = 0
    for i in range(100):
        new_flashes = grid.step()
        flashes += new_flashes
        if new_flashes == 100:
            syncd_flash_step = i + 1
    
    print('part1 result:', flashes)

    i = 100
    while syncd_flash_step < 0:
        new_flashes = grid.step()
        if new_flashes == 100:
            syncd_flash_step = i + 1
        i += 1

    print('part2 result:', syncd_flash_step)


