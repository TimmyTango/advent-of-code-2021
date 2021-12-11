from dataclasses import dataclass
from typing import List, Set, Tuple
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def index_to_coords(index: int, width: int) -> Tuple[int, int]:
    x = index % width
    y = index // width
    return x, y


def coords_to_index(x: int, y: int, width: int) -> int:
    return y * width + x


@dataclass
class Grid:
    values: List[int]
    width: int
    height: int

    def get_low_points(self) -> List[int]:
        indices = self.find_low_points()
        return [self.values[i] for i in indices]

    def find_low_points(self) -> Set[int]:
        low_point_indices: Set[int] = set()

        for i in range(len(self.values)):
            if self.is_low_point(i):
                low_point_indices.add(i)

        return low_point_indices
    
    def is_low_point(self, index: int) -> bool:
        for direction in Direction:
            if self.neighbor_is_lower_or_equal(index, direction):
                return False
        return True

    def neighbor_is_lower_or_equal(self, index: int, direction: Direction) -> bool:
        x, y = index_to_coords(index, self.width)
        value = self.values[index]
        
        if direction == Direction.UP and self.point_is_lower_or_equal(x, y - 1, value):
            return True
        elif direction == Direction.DOWN and self.point_is_lower_or_equal(x, y + 1, value):
            return True
        elif direction == Direction.LEFT and self.point_is_lower_or_equal(x - 1, y, value):
            return True
        elif direction == Direction.RIGHT and self.point_is_lower_or_equal(x + 1, y, value):
            return True

        return False

    def point_is_lower_or_equal(self, x: int, y: int, value: int) -> bool:
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.values[coords_to_index(x, y, self.width)] <= value
        return False

    def get_basin_indices(self, low_point_index: int) -> Set[int]:
        unprocessed_basin_indices = {low_point_index}
        processed_basin_indices = set()

        while len(unprocessed_basin_indices) > 0:
            self.process_basin(unprocessed_basin_indices, processed_basin_indices)
        
        return processed_basin_indices

    def process_basin(self, unprocessed_basin_indices: Set[int], processed_basin_indices: Set[int]) -> None:
        if len(unprocessed_basin_indices) == 0: return

        index = unprocessed_basin_indices.pop()
        x, y = index_to_coords(index, self.width)
        
        # Up
        if self.index_is_basin(x, y - 1, unprocessed_basin_indices, processed_basin_indices):
            other_index = coords_to_index(x, y - 1, self.width)
            unprocessed_basin_indices.add(other_index)

        # Down
        if self.index_is_basin(x, y + 1, unprocessed_basin_indices, processed_basin_indices):
            other_index = coords_to_index(x, y + 1, self.width)
            unprocessed_basin_indices.add(other_index)

        # Left
        if self.index_is_basin(x - 1, y, unprocessed_basin_indices, processed_basin_indices):
            other_index = coords_to_index(x - 1, y, self.width)
            unprocessed_basin_indices.add(other_index)

        # Right
        if self.index_is_basin(x + 1, y, unprocessed_basin_indices, processed_basin_indices):
            other_index = coords_to_index(x + 1, y, self.width)
            unprocessed_basin_indices.add(other_index)

        processed_basin_indices.add(index)

    def index_is_basin(self, x: int, y: int, unprocessed_basin_indices: Set[int], processed_basin_indices: Set[int]) -> bool:
        index = coords_to_index(x, y, self.width)
        if index not in unprocessed_basin_indices and index not in processed_basin_indices:
            return self.point_is_lower_or_equal(x, y, 8)
        return False


def read_input_file() -> Grid:
    with open('input/day9.txt') as file:
        width = 0
        height = 0
        values = []
        for line in file:
            if len(line) <= 1:
                break
            line = line.rstrip('\n')
            height += 1
            width = len(line)
            line_values = [int(c) for c in line]
            values.extend(line_values)
        
    return Grid(values, width, height)


if __name__ == '__main__':
    grid = read_input_file()
    low_point_indices = grid.find_low_points()
    low_points = [grid.values[i] for i in low_point_indices]
    risk_level = sum(low_points) + len(low_points)
    print('part1 result:', risk_level)

    basin_sizes = []
    for low_point_index in low_point_indices:
        basin_sizes.append(len(grid.get_basin_indices(low_point_index)))
    basin_sizes = sorted(basin_sizes, reverse=True)
    print('part2 result:', basin_sizes[0] * basin_sizes[1] * basin_sizes[2])