from aoc_day_4 import load_and_parse_txt_lines, Scratchcard, main_day_4


def test_load_and_parse_txt_lines():
    expected = Scratchcard([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
    full_output = load_and_parse_txt_lines("fixtures/test_fixture_day_4.txt")
    assert full_output[0] == expected


def test_count_set_of_drawn_numbers_that_were_winning():
    scratchcard = Scratchcard([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])
    assert scratchcard.count_set_of_drawn_numbers_that_were_winning() == 4


def test_main_day_4():
    assert main_day_4("fixtures/test_fixture_day_4.txt") == 13