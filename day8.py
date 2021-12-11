from typing import Dict, List

from utils import read_input_file


# segment_count_map[i] = n:
# maps i -> n, where i is the display number, and n is the number of segments required to draw it
# 0 requires 4 segments to display, so segment_count_map[0] = 4
segment_count_map = [
    6,  # 0
    2,  # 1
    5,  # 2
    5,  # 3
    4,  # 4
    5,  # 5
    6,  # 6
    3,  # 7
    7,  # 8
    6,  # 9
]

# segment_to_number_map[i] = [n]:
# maps i -> [n], where i is the number of segments, and n is the number that could be drawn
# if we have 4 segments, we know the number is either a 0 or 4
# this is the counterpart to the segment_count_map
segment_to_number_map = [
    [],            # 0
    [],            # 1
    [1],           # 2
    [7],           # 3
    [4],           # 4
    [2, 3, 5],     # 5
    [0, 6, 9],     # 6
    [8],           # 7
]

number_to_signal_map = [
    'abcefg',   # 0
    'cf',       # 1
    'acdeg',    # 2
    'acdfg',    # 3
    'bcdf',     # 4
    'abdfg',    # 5
    'abdefg',   # 6
    'acf',      # 7
    'abcdefg',  # 8
    'abcdfg',   # 9
]


def generate_blank_signal_map() -> Dict[str, List[str]]:
    return {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': [],
    }


def find_missing_chars_in_string(source: str, search_for: str):
    missing_chars = []
    for c in search_for:
        if c not in source:
            missing_chars.append(c)
    return missing_chars

#        0:      1:      2:      3:      4:
#       aaaa    ....    aaaa    aaaa    ....
#      b    c  .    c  .    c  .    c  b    c
#      b    c  .    c  .    c  .    c  b    c
#       ....    ....    dddd    dddd    dddd
#      e    f  .    f  e    .  .    f  .    f
#      e    f  .    f  e    .  .    f  .    f
#       gggg    ....    gggg    gggg    ....


#        5:      6:      7:      8:      9:
#       aaaa    aaaa    aaaa    aaaa    aaaa
#      b    .  b    .  .    c  b    c  b    c
#      b    .  b    .  .    c  b    c  b    c
#       dddd    dddd    ....    dddd    dddd
#      .    f  e    f  .    f  e    f  .    f
#      .    f  e    f  .    f  e    f  .    f
#       gggg    gggg    ....    gggg    gggg

# Notes:
# Finding 1 will give c & f
# If we know c & f and we find a 6 segment number, we know if it's a 6 if c&f are not present
# We can use that to figure out which value maps to c and which maps to f
# 
# 


if __name__ == '__main__':
    digits_with_unique_segments = 0

    lines = read_input_file(8)
    for line in lines[:1]:
        signal_map = generate_blank_signal_map()
        sorted_values = [[] for _ in range(8)]
        sorted_segment_codes = [[] for _ in range(8)]

        parts = line.split('|')

        signal_pattern = parts[0].strip()
        signals = signal_pattern.split(' ')

        output_value = parts[1].strip()
        segment_codes = output_value.split(' ')

        for signal in signals:
            sorted_signal = ''.join(sorted(signal))
            sorted_values[len(signal)].append(sorted_signal)

        for segment_code in segment_codes:
            sorted_code = ''.join(sorted(segment_code))
            sorted_values[len(segment_code)].append(sorted_code)
            sorted_segment_codes[len(segment_code)].append(sorted_code)

        for i, signals in enumerate(sorted_values):
            print(f'{i}: {signals}')

    print('part1 result:', digits_with_unique_segments)
