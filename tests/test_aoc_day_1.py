from aoc_day_1 import txt_loader, combine_first_and_last_digits_in_list, main_day_1
from aoc_day_1 import extract_digits


def test_txt_loader():
    lines_list = txt_loader('fixtures/test_input.txt')
    assert len(lines_list) == 3


def test_extract_digits():
    number_strings = ["219", "8wo3", "abc123xyz",
                      "x2ne34", "49eight72", "z1ight234", "7pqrst6teen"]
    expected_strings = [[2, 1, 9], [8, 3], [1, 2, 3], [2, 3, 4], [4, 9, 7, 2], [1, 2, 3, 4], [7, 6]]
    for number_string, expected in zip(number_strings, expected_strings):
        assert extract_digits(number_string) == expected


def test_extract_digits_include_number_strings():
    number_strings = ["219", "8wo3", "abc123xyz",
                      "x2ne34", "49eight72", "z1ight234", "7pqrst6teen"]
    expected_strings = [[2, 1, 9], [8, 3], [1, 2, 3], [2, 3, 4], [4, 9, 8, 7, 2], [1, 2, 3, 4], [7, 6]]
    for number_string, expected in zip(number_strings, expected_strings):
        assert extract_digits(number_string, include_number_strings=True) == expected


def test_extract_digits_include_number_strings_oneight():
    number_string = "oneight"
    expected = [1, 8]
    assert extract_digits(number_string, include_number_strings=True) == expected


def test_sum_first_and_last_digits_in_list():
    digits_list = [2, 8, 1, 2, 8, 9, 7]
    expected = 27
    calculated = combine_first_and_last_digits_in_list(digits_list)
    assert expected == calculated


def test_main_day_1_part_1():
    calculated = main_day_1("fixtures/test_input.txt")
    assert calculated == 110


def test_main_day_1_part_2():
    calculated = main_day_1("fixtures/test_input_part_2.txt", include_number_strings=True)
    assert calculated == 281
