from typing import List


def read_input_file() -> List[int]:
    with open('input/day6.txt') as file:
        line = file.readline()
        return [int(n) for n in line.split(',')]


def advance_tracker(tracker: List[int]):
    new_tracker = tracker.copy()
    reset_count = 0  # number of fish that are reset, 0 -> 6 (also number of new fish)
    for i in range(len(new_tracker)):
        if i == 0:
            reset_count = new_tracker[0]
            new_tracker[8] += reset_count
            new_tracker[6] += reset_count
            new_tracker[0] = 0
        elif i in [6, 8]:
            new_tracker[i-1] = new_tracker[i] - reset_count
            new_tracker[i] = reset_count
        else:
            new_tracker[i-1] += new_tracker[i]
            new_tracker[i] = 0

    return new_tracker


def get_sum_after_n_days(tracker: List[int], days: int):
    for _ in range(days):
        tracker = advance_tracker(tracker)
    
    return sum(tracker)


if __name__ == '__main__':
    initial_state = read_input_file()

    # each index is the number of days left
    # each element is the number of fish in that category
    # fish_tracker[5] = 6 means there are 6 fish with 5 days left
    fish_tracker = [0] * 9
    for n in initial_state:
        fish_tracker[n] += 1

    print('part1 result:', get_sum_after_n_days(fish_tracker, 80))
    print('part2 result:', get_sum_after_n_days(fish_tracker, 256))
