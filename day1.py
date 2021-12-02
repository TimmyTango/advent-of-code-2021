from typing import List

from utils import read_input_file

def next_element_is_larger(input: List[int]) -> bool:
    for i in range(len(input)-1):
        yield input[i+1] > input[i]
    return False

def get_increase_count(input: List[int]) -> int:
    return sum(next_element_is_larger(input))

def group_inputs(input: List[int]) -> List[int]:
    output = []
    for i in range(0, len(input) - 2):
        output.append(sum(input[i:i+3]))
    return output

if __name__ == '__main__':
    data = list(map(lambda s: int(s), read_input_file('input/day1.txt')))
    part1_result = get_increase_count(data)
    print('part1 result:', part1_result)
    assert part1_result == 1316
    
    part2_result = get_increase_count(group_inputs(data))
    print('part2 result:', part2_result)
    assert part2_result == 1344
