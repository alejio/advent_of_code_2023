from dataclasses import dataclass
import regex as re


@dataclass
class Scratchcard:
    winning_numbers: list[int]
    drawn_numbers: list[int]


def load_and_parse_txt_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        list_of_lines = f.readlines()
        list_of_lines = [re.sub(r"Card \d+: ", "", line) for line in list_of_lines]
        list_of_lines = [' '.join(line.split()) for line in list_of_lines]
        list_of_lines = [line.split("|") for line in list_of_lines]
        list_of_scratchcards = [Scratchcard(list(map(int, line[0].split())),
                                            list(map(int, line[1].split()))) for line in list_of_lines]
        return list_of_scratchcards