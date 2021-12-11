from statistics import median

from utils import read_input_file


bracket_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


incorrect_bracket_score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


missing_bracket_score_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def is_closing_bracket(char):
    return char in [')', ']', '}', '>']


def matching_brackets(open: str, close: str) -> bool:
    if bracket_map[open] == close:
        return True


if __name__ == '__main__':
    lines = read_input_file(10)
    part1_score = 0
    part2_scores = []
    
    for line in lines:
        incomplete_line = True
        open_brackets = [line[0]]
        for i in range(1, len(line)):
            c = line[i]
            if is_closing_bracket(c):
                if matching_brackets(open_brackets[-1], c):
                    open_brackets.pop()
                else:
                    part1_score += incorrect_bracket_score_map[c]
                    incomplete_line = False
                    break
            else:
                open_brackets.append(c)
        
        if incomplete_line:
            missing_brackets = []
            while len(open_brackets) > 0:
                missing_brackets.append(bracket_map[open_brackets.pop()])

            line_score = 0
            for bracket in missing_brackets:
                line_score *= 5
                line_score += missing_bracket_score_map[bracket]
            part2_scores.append(line_score)

    print('part1 result:', part1_score)
    print('part2 result:', median(part2_scores))