from typing import List, Optional, TextIO, Tuple

class BingoCard:
    def __init__(self, numbers: List[int]):
        self.numbers: List[Tuple[int, bool]] = []
        self.has_bingo = False
        for n in numbers:
            self.numbers.append((n, False))

    def __str__(self):
        card = ''
        for i, n in enumerate(self.numbers):
            if i % 5 == 0:
                card += '\n'
            card += f'{n[0]:2d} '
        return card

    def mark_if_match(self, target: int):
        for i, n in enumerate(self.numbers):
            if n[0] == target:
                self.numbers[i] = (target, True)

    def check_for_bingo(self) -> bool:
        if self.check_rows():
            self.has_bingo = True
            return True
        if self.check_columns():
            self.has_bingo = True
            return True
        return False

    def check_rows(self) -> bool:
        for y in range(5):
            marked_spots = 0
            for x in range(5):
                n = self.numbers[y * 5 + x]
                if n[1]:
                    marked_spots += 1
            if marked_spots == 5:
                return True
        return False

    def check_columns(self) -> bool:
        for x in range(5):
            marked_spots = 0
            for y in range(5):
                n = self.numbers[y * 5 + x]
                if n[1]:
                    marked_spots += 1
            if marked_spots == 5:
                return True
        return False

    def get_score(self) -> int:
        return sum([n[0] for n in self.numbers if n[1] is False])


def read_pool(file: TextIO) -> List[int]:
    pool_str = file.readline().rstrip('\n').split(',')
    return [int(n) for n in pool_str]


def read_card(file: TextIO) -> Optional[BingoCard]:
    data: List[int] = []

    # eat blank line, return None if EOF
    line = file.readline()
    if line == '':
        return None

    for _ in range(5):
        numbers = file.readline().rstrip('\n').split()
        for n in numbers:
            if len(n) > 0:
                data.append(int(n))

    return BingoCard(data)


def read_input_file() -> Tuple[List[int], List[BingoCard]]:
    cards: List[BingoCard] = []

    with open('input/day4.txt') as file:
        pool = read_pool(file)

        while (card := read_card(file)) != None:
            cards.append(card)

    return pool, cards


if __name__ == '__main__':
    pool, cards = read_input_file()
    first_result = None
    last_result = None

    for n in pool:
        for card_index, card in enumerate(cards):
            if card.has_bingo:
                continue

            card.mark_if_match(n)
            if card.check_for_bingo():
                score = n * card.get_score()
                if first_result is None:
                    first_result = score
                last_result = score
                
    print('part1 result:', first_result)
    print('part2 result:', last_result)
