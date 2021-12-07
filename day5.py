from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_string(cls, point_str: str) -> 'Point':
        coords = [int(n) for n in point_str.split(',')]
        return cls(coords[0], coords[1])


@dataclass
class Line:
    p1: Point
    p2: Point


class Grid:
    width: int
    height: int
    points: List[Point]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.points = [0] * (width * height)

    def plot_line(self, 
    line: Line, include_diagonal: bool) -> None:
        x1 = line.p1.x
        x2 = line.p2.x
        y1 = line.p1.y
        y2 = line.p2.y

        if y1 == y2:
            step = 1 if x2 > x1 else -1
            for i in range(x1, x2 + step, step):
                point_index = y1 * self.width + i
                self.points[point_index] += 1
        elif x1 == x2:
            step = 1 if y2 > y1 else -1
            for i in range(y1, y2 + step, step):
                point_index = i * self.width + x1
                self.points[point_index] += 1
        elif include_diagonal:
            # assumes 45 degree angle
            xstep = 1 if x2 > x1 else -1
            ystep = 1 if y2 > y1 else -1
            x = x1
            y = y1
            length = max([x1, x2]) - min([x1, x2]) + 1
            for i in range(length):
                point_index = y * self.width + x
                self.points[point_index] += 1
                x += xstep
                y += ystep

    def count_points_over_target(self, target: int) -> int:
        count = 0
        for n in self.points:
            if n > target:
                count += 1
        return count

    def __str__(self) -> str:
        s = ''
        for i, n in enumerate(self.points):
            if n == 0:
                s += '.'
            else:
                s += str(n)
            
            if (i + 1) % self.width == 0:
                s += '\n'
        return s


def read_input_file(include_diagonal: bool) -> Grid:
    lines: List[Line] = []
    x_max: int = 0
    y_max: int = 0

    with open('input/day5.txt') as file:
        for line in file:
            if line == '\n': continue  # skip blank lines

            point_strings = [p.strip() for p in line.split('->')]
            p1 = Point.from_string(point_strings[0])
            p2 = Point.from_string(point_strings[1])

            x_max = max([x_max, p1.x, p2.x])
            y_max = max([y_max, p1.y, p2.y])
            lines.append(Line(p1, p2))
    
    grid = Grid(x_max + 1, y_max + 1)
    for line in lines:
        grid.plot_line(line, include_diagonal)

    return grid


if __name__ == '__main__':
    # reads input file twice, but that's okay
    grid1 = read_input_file(include_diagonal=False)
    print('part1 result:', grid1.count_points_over_target(1))

    grid2 = read_input_file(include_diagonal=True)
    print('part2 result:', grid2.count_points_over_target(1))
