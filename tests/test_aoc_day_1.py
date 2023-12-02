from aoc_day_1 import txt_loader, combine_first_and_last_digits_in_list, main_day_1, \
    replace_number_strings_with_digits
from aoc_day_1 import extract_digits


def test_txt_loader():
    lines_list = txt_loader('fixtures/test_input.txt')
    assert len(lines_list) == 3


def test_replace_number_strings_with_digits():
    number_strings = ["two1nine", "eightwothree", "abcone2threexyz",
                      "xtwone3four", "4nineeightseven2", "zoneight234",
                      "7pqrstsixteen"]
    expected_strings = ["219", "8wo3", "abc123xyz",
                        "x2ne34", "49eight72", "z1ight234", "7pqrst6teen"]
    for number_string, expected in zip(number_strings, expected_strings):
        assert replace_number_strings_with_digits(number_string) == expected


def test_extract_digits():
    number_strings = ["219", "8wo3", "abc123xyz",
                      "x2ne34", "49eight72", "z1ight234", "7pqrst6teen"]
    expected_strings = [[2, 1, 9], [8, 3], [1, 2, 3], [2, 3, 4], [4, 9, 7, 2], [1, 2, 3, 4], [7, 6]]
    for number_string, expected in zip(number_strings, expected_strings):
        assert extract_digits(number_string) == expected


def test_sum_first_and_last_digits_in_list():
    digits_list = [2, 8, 1, 2, 8, 9, 7]
    expected = 27
    calculated = combine_first_and_last_digits_in_list(digits_list)
    assert expected == calculated


def test_main_day_1_part_1():
    calculated = main_day_1("fixtures/test_input.txt")
    assert calculated == 110


def test_main_day_1_part_2():
    calculated = main_day_1("fixtures/test_input_part_2.txt", replace_number_strings=True)
    assert calculated == 281
