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
        list_of_lines = [re.sub(r"Card \d+: ", "", line) for line in list_of_lines]
        list_of_lines = [' '.join(line.split()) for line in list_of_lines]
        list_of_lines = [line.split("|") for line in list_of_lines]
        list_of_scratchcards = [Scratchcard(list(map(int, line[0].split())),
                                            list(map(int, line[1].split()))) for line in list_of_lines]
        return list_of_scratchcards


def main_day_4(input_file: str) -> int:
    list_of_scratchcards = load_and_parse_txt_lines(input_file)
    total_count = 0
    for scratchcard in list_of_scratchcards:
        total_count += scratchcard.calculate_points_per_game()
    return total_count