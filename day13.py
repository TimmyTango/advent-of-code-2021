from typing import List, Set, Tuple


Point = Tuple[int, int]


def read_input_file() -> Tuple[List[Point], List[str]]:
    points = []
    instructions = []

    with open('input/day13.txt') as file:
        reading_points = True
        for line in file:
            if line == '\n':
                reading_points = False
                continue

            line = line.rstrip('\n')

            if reading_points:
                x, y = line.split(',')
                x = int(x)
                y = int(y)
                points.append((x, y))
            else:
                instructions.append(line)

    return points, instructions


def fold_y(points: List[Point], n: int) -> List[Point]:
    new_points: Set[Point] = set()
    for point in points:
        x, y = point
        if y > n:
            new_points.add((x, n * 2 - y))
        else:
            new_points.add((x, y))
    return list(new_points)


def fold_x(points: List[Point], n: int) -> List[Point]:
    new_points: Set[Point] = set()
    for point in points:
        x, y = point
        if x > n:
            new_points.add((n * 2 - x, y))
        else:
            new_points.add((x, y))
    return list(new_points)


def perform_instruction(points: List[Point], instruction: str) -> List[Point]:
    instruction = instruction.lstrip('fold along ')
    coord, n = instruction.split('=')
    n = int(n)

    if coord == 'x':
        return fold_x(points, n)
    else:
        return fold_y(points, n)


def print_points(points: List[Point]):
    width = 0
    height = 0
    for point in points:
        x, y = point
        width = max(x, width)
        height = max(y, height)

    width += 1
    height += 1

    s = bytearray(b' ' * (width * height))

    for point in points:
        x, y = point
        s[y * width + x] = ord('#')

    for i in range(height):
        begin = i * width
        end = i * width + width
        print(s[begin:end].decode())


if __name__ == '__main__':
    points, instructions = read_input_file()

    first_instruction = instructions[0]
    points = perform_instruction(points, first_instruction)
    print('part1 result:', len(points))

    for i in range(1, len(instructions)):
        points = perform_instruction(points, instructions[i])

    print('part2 result:')
    print_points(points)

