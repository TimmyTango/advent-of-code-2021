import math
import statistics
from typing import List

from utils import read_input_as_int_list


def calculate_part1_fuel(positions: List[int], target: int) -> int:
    distances = [abs(n - target) for n in positions]
    return sum(distances)


def calculate_part2_fuel(positions: List[int], target: int) -> int:
    distances = [abs(n - target) for n in positions]
    # (n * n + n) / 2 is equal to n + n-1 + n-2...
    distances = [(n * n + n) / 2 for n in distances]
    return int(sum(distances))


if __name__ == '__main__':
    data = read_input_as_int_list(7)
    median = round(statistics.median(data))
    print('part1 result:', calculate_part1_fuel(data, median))

    # Result for part 2 could be either the floor or ceiling of the mean
    # Calculate both and take the most efficient result
    mean = statistics.mean(data)
    mean_floor = math.floor(mean)
    mean_ceil = math.ceil(mean)
    mean_floor_result = calculate_part2_fuel(data, mean_floor)
    mean_ceil_result = calculate_part2_fuel(data, mean_ceil)
    print('part2 mean_low_result:', mean_floor_result)
    print('part2 mean_high_result:', mean_ceil_result)
    print('part2 result:', min(mean_floor_result, mean_ceil_result))
