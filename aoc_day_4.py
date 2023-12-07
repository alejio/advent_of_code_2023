from dataclasses import dataclass
from math import floor

import regex as re


@dataclass
class Scratchcard:
    winning_numbers: list[int]
    drawn_numbers: list[int]

    def count_set_of_drawn_numbers_that_were_winning(self) -> int:
        return len(set(self.winning_numbers).intersection(set(self.drawn_numbers)))

    def calculate_points_per_game(self) -> int:
        return floor(2**(self.count_set_of_drawn_numbers_that_were_winning()-1))


def load_and_parse_txt_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        list_of_lines = f.readlines()
        list_of_lines = [re.sub(r"Card\s+\d+: ", "", line) for line in list_of_lines]
        list_of_lines = [' '.join(line.split()) for line in list_of_lines]
        list_of_lines = [line.split("|") for line in list_of_lines]
        list_of_scratchcards = [Scratchcard(list(map(int, line[0].split())),
                                            list(map(int, line[1].split()))) for line in list_of_lines]
        return list_of_scratchcards


def main_day_4(input_file: str) -> int:
    list_of_scratchcards = load_and_parse_txt_lines(input_file)
    total_count = 0
    total_cards = [1] * len(list_of_scratchcards)
    for idx, scratchcard in enumerate(list_of_scratchcards):
        number_of_matches = scratchcard.count_set_of_drawn_numbers_that_were_winning()
        total_count += scratchcard.calculate_points_per_game()
        for n in range(number_of_matches):
            total_cards[idx + n + 1] += total_cards[idx]
    return total_count, sum(total_cards)


if __name__ == "__main__":
    print(main_day_4("data/input_day_4.txt"))