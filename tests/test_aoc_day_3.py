from aoc_day_3 import main_day_3, find_number_position_range_within_string, find_symbol_position_within_string, \
    NumberCoordinates, SymbolCoordinates, is_number_valid


def test_find_number_position_range_within_string():
    calculated = find_number_position_range_within_string(0, "467..114..")
    assert len(calculated) == 2
    assert calculated[0].number == 467
    assert calculated[0].row == 0
    assert calculated[0].column_min == 0
    assert calculated[0].column_max == 2
    assert calculated[1].number == 114
    assert calculated[1].row == 0
    assert calculated[1].column_min == 5
    assert calculated[1].column_max == 7


def test_find_symbol_position_within_string():
    calculated = find_symbol_position_within_string(0, "617*......")
    assert len(calculated) == 1
    assert calculated[0].symbol == "*"
    assert calculated[0].row == 0
    assert calculated[0].column == 3


def test_is_number_valid():
    number_1 = NumberCoordinates(467, 0, 0, 2)
    number_2 = NumberCoordinates(114, 0, 5, 7)
    symbol = SymbolCoordinates("*", 0, 3)
    assert is_number_valid(number_1, symbol) is True
    assert is_number_valid(number_2, symbol) is False

def test_main_day_3():
    assert main_day_3("fixtures/test_input_part_3.txt") == 4361