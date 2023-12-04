from dataclasses import dataclass

import regex as re

@dataclass
class NumberCoordinates:
    number: int
    row: int
    column_min: int
    column_max: int

@dataclass
class SymbolCoordinates:
    symbol: str
    row: int
    column: int


def find_number_position_range_within_string(row_number: int, row_content: str) -> list[NumberCoordinates]:
    number_matches = re.finditer(r"\d+", row_content)
    return [NumberCoordinates(int(number_match.group(0)),
                              row_number,
                              number_match.start(0), number_match.end(0) - 1) for number_match in number_matches]


def find_symbol_position_within_string(row_number: int, row_content: str) -> list[SymbolCoordinates]:
    # write regex to match all non-alphanumeric characters except for the dot
    symbol_matches = re.finditer(r"[^\w.]", row_content)
    return [SymbolCoordinates(symbol_match.group(0),
                              row_number,
                              symbol_match.start(0)) for symbol_match in symbol_matches]


def is_number_valid(number: NumberCoordinates, symbol: SymbolCoordinates) -> bool:
    on_same_row_flag = abs(symbol.row - number.row) <= 1
    overlapping_columns_flag = (abs(symbol.column - number.column_min) <= 1 or
                                abs(symbol.column - number.column_max) <= 1)
    return on_same_row_flag and overlapping_columns_flag


def main_day_3(input_file: str) -> int:
    return 0

if __name__ == "__main__":
    main_day_3("data/input_day_3.txt")