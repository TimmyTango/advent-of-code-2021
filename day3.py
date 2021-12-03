from typing import List, Optional, Tuple
from math import ceil, floor
from enum import Enum

from utils import read_input_file


def get_enabled_bit_count_for_index(data: List[str], index: int) -> int:
    enabled_count = 0
    for datum in data:
        if datum[index] == '1':
            enabled_count += 1
    return enabled_count


def get_enabled_bit_counts(data: List[str]) -> List[int]:
    return [get_enabled_bit_count_for_index(data, i) for i in range(len(data[0]))]


def binary_str_to_int(bin_str: str) -> int:
    return int(''.join(bin_str), 2)

#
#   Part 1
#

def calculate_rates(counts: List[int], threshold: int) -> Tuple[int, int]:
    gamma_rate_values: List[str] = []
    epsilon_rate_values: List[str] = []

    for count in counts:
        if count > threshold:
            gamma_rate_values.append('1')
            epsilon_rate_values.append('0')
        else:
            gamma_rate_values.append('0')
            epsilon_rate_values.append('1')

    gamma_rate = binary_str_to_int(gamma_rate_values)
    epsilon_rate = binary_str_to_int(epsilon_rate_values)

    return gamma_rate, epsilon_rate

#
#   Part 2
#

class RatingType(Enum):
    OXYGEN = 1
    CO2 = 2


def filter_rating_part2(data: List[str], index: int, rating_type: RatingType) -> List[str]:
    count = get_enabled_bit_count_for_index(data, index)
    threshold = ceil(len(data)/2)

    if count > threshold:
        target = '1'
    elif count < threshold:
        target = '0'
    else:
        target = '1'

    if rating_type == RatingType.CO2:
        if target == '1':
            target = '0'
        else:
            target = '1'

    return list(filter(lambda d: d[index] == target, data))


def calculate_rating_part2(data: List[str], rating_type: RatingType) -> Optional[int]:
    for i in range(len(data[0])):
        data = filter_rating_part2(data, i, rating_type)
        if len(data) == 1:
            return binary_str_to_int(data[0])
    return None

# 
#   Main
# 

if __name__ == '__main__':
    data = read_input_file(3)
    threshold = floor(len(data)/2)
    enabled_counts = get_enabled_bit_counts(data)
    gamma_rate, epsilon_rate = calculate_rates(enabled_counts, threshold)
    print('gamma rate:', gamma_rate)
    print('epsilon rate:', epsilon_rate)
    print('part1 result:', gamma_rate * epsilon_rate)

    print('='*20)

    oxygen_rating = calculate_rating_part2(data, RatingType.OXYGEN)
    co2_rating = calculate_rating_part2(data, RatingType.CO2)
    print('oxygen rating:', oxygen_rating)
    print('co2 rating:', co2_rating)
    print('part2 result:', oxygen_rating * co2_rating)
