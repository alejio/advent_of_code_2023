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


def load_input_file(input_file: str) -> list[str]:
    with open(input_file, "r") as file:
        return [line.strip() for line in file.readlines()]


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


def get_gear_numbers(symbol: SymbolCoordinates, list_of_valid_numbers) -> list:
    gear_count = 0
    adjacent_numbers = []
    for number in list_of_valid_numbers:
        if is_number_valid(number, symbol):
            gear_count += 1
            adjacent_numbers.append(number.number)
    if gear_count == 2:
        return adjacent_numbers
    else:
        return [0, 0]


def calculate_gear_ratio(adjacent_numbers: list) -> int:
    return adjacent_numbers[0] * adjacent_numbers[1]


def main_day_3(input_file: str) -> tuple[int]:
    data = load_input_file(input_file)
    number_coordinates = []
    symbol_coordinates = []
    for row in range(len(data)):
        number_coordinates += find_number_position_range_within_string(row, data[row])
        symbol_coordinates += find_symbol_position_within_string(row, data[row])
    sum_of_valid_numbers = 0
    valid_numbers = []
    for nc in number_coordinates:
        for sc in symbol_coordinates:
            if is_number_valid(nc, sc):
                sum_of_valid_numbers += nc.number
                valid_numbers.append(nc)
                break
    sum_of_gear_ratios = 0
    for sc in symbol_coordinates:
        gear_numbers = get_gear_numbers(sc, valid_numbers)
        sum_of_gear_ratios += calculate_gear_ratio(gear_numbers)
    return sum_of_valid_numbers, sum_of_gear_ratios


if __name__ == "__main__":
    print(main_day_3("data/input_day_3.txt"))